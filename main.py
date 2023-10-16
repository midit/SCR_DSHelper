from PIL import Image
import pytesseract
import os
import re
import datetime
import pygame
import keyboard
import pyperclip
import customtkinter
import pyautogui
import threading

customtkinter.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"

customtkinter.set_default_color_theme("green")  # Themes: "blue" (standard), "green", "dark-blue"

# Define the destinations dictionary
DESTINATIONS = {
    'A': 'Airport Central',
    'B': 'Benton',
    'C': 'Beechley',
    'D': 'Willowfield',
    'E': 'Edgemead',
    'F': 'Whitefield',
    'G': 'Greenslade',
    'H': 'Newry Harbour',
    'I': 'St Helens Bridge',
    'J': 'Farleigh',
    'K': 'Leighton West',
    'L': 'Llyn-by-the-Sea',
    'M': 'Morganstown',
    'N': 'Newry',
    'O': 'Connolly',
    'P': 'Port Benton',
    'Q': 'Esterfield',
    'R': 'Leighton Stepford Road',
    'S': 'Stepford Central',
    'T': 'Leighton City',
    'U': 'Stepford UFC',
    'V': 'Stepford Victoria',
    'W': 'Westwyvern',
    'X': 'Airport Terminal 2',
    'Y': 'Berrily',
    'Z': 'Airport Terminal 3'
}

activeTrainHeadcode = "None"
timeString = "0m 0s"


class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        # Configure window
        self.title("SCR DS Helper")

        self.geometry(f"{350}x{200}")

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        self.lastTrains = {}
        self.startTime = datetime.datetime.now()
        self.timeDispatching = "0m 0s"
        self.trainsDispatched = 0
        self.pointsEarned = 0
        self.expEarned = 0

        # Active train frame
        self.activeTrainFrame = customtkinter.CTkFrame(self)
        self.activeTrainFrame.pack(fill='both', side='left', expand='True')

        # Statistics frame
        self.playerStatisticsFrame = customtkinter.CTkFrame(self, fg_color="transparent")
        self.playerStatisticsFrame.pack()

        # Quick-config buttons frame
        self.quickButtonConfigFrame = customtkinter.CTkFrame(self, fg_color="transparent")
        self.quickButtonConfigFrame.pack()

        # Active train labels
        self.activeTrainLabel = customtkinter.CTkLabel(self.activeTrainFrame, text="Active train", anchor="nw",
                                                       justify="left")
        self.activeTrainLabel.pack()
        self.activeTrainHeadcodeLabel = customtkinter.CTkLabel(self.activeTrainFrame, text=activeTrainHeadcode,
                                                               anchor="nw", font=("Roboto Mono", 32, "bold"),
                                                               justify="left", text_color="cyan")
        self.activeTrainHeadcodeLabel.pack()
        self.trainDestination = find_destinations(activeTrainHeadcode)
        self.activeTrainDestination = customtkinter.CTkLabel(self.activeTrainFrame,
                                                             text=f"to {', '.join(self.trainDestination)}", anchor="nw",
                                                             font=("Roboto Mono", 16), justify="left",
                                                             text_color="lightgray")
        self.activeTrainDestination.pack()
        self.lastTrainsLabel = customtkinter.CTkLabel(self.activeTrainFrame, text=f"Last trains: ", anchor="nw",
                                                      justify="left")
        self.lastTrainsLabel.pack()
        self.lastTrainsList = customtkinter.CTkLabel(self.activeTrainFrame, text=self.get_last_train(),
                                                     text_color="lime")
        self.lastTrainsList.pack()

        self.playerStatisticsLabel = customtkinter.CTkLabel(self.playerStatisticsFrame,
                                                            text=f"Statistics: \n"
                                                                 f"Time dispatching: {timeString} \n "
                                                                 f"Trains dispatched: 4 \n "
                                                                 f"Points earned: 8 \n "
                                                                 f"Exp earned: 4",
                                                            justify="left")
        self.playerStatisticsLabel.pack()

        self.alwaysOnTopVar = customtkinter.BooleanVar(value=True)
        self.titleBarVar = customtkinter.BooleanVar(value=False)
        self.alwaysOnTopSwitch = customtkinter.CTkSwitch(self.quickButtonConfigFrame, switch_width=30, switch_height=20,
                                                         text=f"Always on top  ", font=("Roboto Mono", 10),
                                                         command=self.toggle_always_on_top,
                                                         variable=self.alwaysOnTopVar, onvalue=True, offvalue=False)
        self.alwaysOnTopSwitch.pack()
        self.titleBarSwitch = customtkinter.CTkSwitch(self.quickButtonConfigFrame, switch_width=30, switch_height=20,
                                                      text=f"Disable title bar", font=("Roboto Mono", 10),
                                                      command=self.toggle_title_bar, variable=self.titleBarVar,
                                                      onvalue=True, offvalue=False)
        self.titleBarSwitch.pack()
        self.resetStatisticsButton = customtkinter.CTkButton(self.quickButtonConfigFrame,
                                                             command=self.reset_statistics_button_event,
                                                             text="Reset statistics", font=("Roboto Mono", 10))
        self.resetStatisticsButton.pack()

        self.activeTrainScStatusLabel = customtkinter.CTkLabel(self, text="SC", text_color=self.toggle_sc_status(False))
        self.activeTrainScStatusLabel.pack()

        self.bind("<B1-Motion>", self.move_window)

    def reset_statistics_button_event(self):
        self.startTime = datetime.datetime.now()
        self.lastTrains = {}
        self.timeDispatching = "0m 0s"
        self.trainsDispatched = 0
        self.pointsEarned = 0
        self.expEarned = 0
        self.update_statistics()
        self.lastTrainsList.configure(text='')
        print("🔄️ Statistics reset")

    def toggle_always_on_top(self):
        app.attributes('-topmost', self.alwaysOnTopVar.get())
        print("Always on top: ", app.alwaysOnTopVar.get())

    def toggle_title_bar(self):
        self.overrideredirect(self.titleBarVar.get())
        print("Title bar: ", app.titleBarVar.get())

    @staticmethod
    def toggle_sc_status(status):
        if status:
            return "lime"
        else:
            return "#FF4040"

    def move_window(self, event):
        x, y = self.winfo_pointerxy()
        self.geometry(f"+{x}+{y}")

    def get_last_train(self):
        trains_list = '\n'.join(self.lastTrains.keys())
        return trains_list

    def update_active_train_headcode(self, new_headcode):
        self.activeTrainHeadcodeLabel.configure(text=new_headcode)
        self.trainDestination = find_destinations(new_headcode)
        self.activeTrainDestination.configure(text=f"to {', '.join(self.trainDestination)}")

    def update_statistics(self):
        self.timeDispatching = self.update_time_dispatching()
        self.trainsDispatched = len(self.lastTrains)
        self.pointsEarned = self.trainsDispatched * 5
        self.expEarned = self.trainsDispatched
        stats_text = (
            f"Statistics:\nTime dispatching: {self.timeDispatching}\n"
            f"Trains dispatched: {self.trainsDispatched}\n"
            f"Points earned: {self.pointsEarned}\n"
            f"Exp earned: {self.expEarned}"
        )
        self.playerStatisticsLabel.configure(text=stats_text)
        self.after(1000, self.update_statistics)

    def update_time_dispatching(self):
        current_time = datetime.datetime.now()
        elapsed_time = current_time - self.startTime
        minutes, seconds = divmod(elapsed_time.seconds, 60)
        time_string = f"{minutes}m {seconds}s"
        return time_string

    def update_last_trains(self, headcode):
        self.lastTrains[headcode] = True
        self.lastTrainsList.configure(text=self.get_last_train())


# Looking for newest screenshot in the folder
def find_screenshot():
    folder_path = 'screenshots'
    all_files = os.listdir(folder_path)
    image_files = [f for f in all_files if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
    image_files.sort(key=lambda x: os.path.getmtime(os.path.join(folder_path, x)), reverse=True)

    if image_files:
        newest_screenshot = os.path.join(folder_path, image_files[0])

        print("✅ Newest screenshot: ", newest_screenshot)
        return newest_screenshot
    else:
        print("❗No screenshot files found in the folder.")


# Cropping the screenshot and looking for the text
def find_text_on_image(size):
    path_to_image = find_screenshot()

    image = Image.open(path_to_image)
    cropped_image = image.crop(size)

    text_on_image = pytesseract.image_to_string(cropped_image)

    # print('❔Output:\n' + textOnImage)
    return text_on_image


def extract_headcode(text):
    pattern = r'\b[1-3|9][A-Z]\d{2}\b'
    match = re.search(pattern, text)
    if match:
        return match.group()
    return None


def find_destinations(headcode):
    destinations_list = []
    for letter in headcode[1]:
        if letter in DESTINATIONS:
            destinations_list.append(DESTINATIONS[letter])
    return destinations_list


def take_screenshot():
    destination_folder = 'screenshots'
    try:
        now = datetime.datetime.now()
        timestamp = now.strftime("%Y-%m-%d_%H-%M-%S")

        screenshot = pyautogui.screenshot()

        filename = f"{timestamp}.png"

        full_path = f"{destination_folder}/{filename}"
        screenshot.save(full_path)

        print(f"Screenshot saved as: {full_path}")
    except Exception as e:
        print(f"Error taking screenshot: {e}")


def play_sound(choose):
    if choose == 1:
        sound = pygame.mixer.Sound('sounds/success.wav')
        sound.play()
    elif choose == 2:
        sound = pygame.mixer.Sound('sounds/screenshot.mp3')
        sound.play()


def main():
    pygame.init()
    pygame.mixer.init()

    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

    while True:
        print("✅ Press Q to make screenshot and initiate the process...")
        keyboard.wait("q")
        take_screenshot()
        play_sound(2)

        not_full_screen = (1760, 468, 1904, 500)
        full_screen = (1738, 429, 1918, 698)

        text = find_text_on_image(full_screen)
        active_train_headcode = extract_headcode(text)

        if active_train_headcode is None:
            print("❗ Error: First unsuccessful try to find headcode. Trying again..")
            text = find_text_on_image(not_full_screen)
            active_train_headcode = extract_headcode(text)

        if active_train_headcode:
            dest_list = find_destinations(active_train_headcode)
            if dest_list:
                formatted_text = f"Safe trip to {', '.join(dest_list)}, {active_train_headcode}"
                pyperclip.copy(formatted_text)
                play_sound(1)
                app.update_last_trains(active_train_headcode)
                app.update_active_train_headcode(active_train_headcode)
                app.activeTrainScStatusLabel.configure(text_color=app.toggle_sc_status(True))
                print(f"🆔 Headcode: {active_train_headcode}\n"
                      f"🗺️  Destination: {', '.join(dest_list)}\n"
                      f"✅ Formatted text copied to clipboard.")
            else:
                print("Headcode:", active_train_headcode)
                print("No destinations found for the given headcode.")
                formatted_text = f"Safe trip to *"
                pyperclip.copy(formatted_text)
                app.activeTrainScStatusLabel.configure(text_color=app.toggle_sc_status(False))
                print("Backup text copied to clipboard.")
        else:
            print("No valid headcode found.")
            formatted_text = f"Safe trip to *"
            pyperclip.copy(formatted_text)
            app.activeTrainScStatusLabel.configure(text_color=app.toggle_sc_status(False))
            print("Backup text copied to clipboard.")


if __name__ == "__main__":
    app = App()
    app.update_statistics()
    app.resizable(width=False, height=False)
    app.attributes("-alpha", 0.9)
    app.attributes('-topmost', app.alwaysOnTopVar.get())
    main_thread = threading.Thread(target=main)
    main_thread.daemon = True  # This allows the thread to be terminated when the program exits
    main_thread.start()
    app.iconbitmap('logo.ico')
    app.mainloop()
