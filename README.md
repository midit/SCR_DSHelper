
_![Logo](https://i.imgur.com/0fbw1nv.jpg)

# SCR DSHelper

![](https://img.shields.io/github/repo-size/midit/SCR_DSHelper)
![](https://img.shields.io/github/last-commit/midit/SCR_DSHelper/main)
![](https://img.shields.io/github/issues/midit/SCR_DSHelper)
![](https://img.shields.io/github/issues-closed/midit/SCR_DSHelper)

## Description
SCR DS Helper is a Python application designed to assist with the SCR dispatching process by providing real-time updates and useful functionalities like screenshot analysis and train tracking.

## Features

- **Auto Safe-trip:** The script reads the number of the dispatching train operated by the dispatcher, determines its route, and inserts the message `Safe trip to ${Destination}, ${Train_hedcode}` into the clipboard.

- **Active Train info:** Information about the active train in the dispatcher's control, its headcode and route

- **List of dispatched trains:** Stores headcodes of dispatched trains

- **Dispatch stats:** Displays the number of dispatched trains and the time of the dispatcher's shift

- **Exp counter:** Displays the number of points and experience earned
## Requirements
- Python 3.x
- [Tesseract OCR](https://github.com/tesseract-ocr/tesseract)
- Windows 11 (Windows 10 should also work)
- FHD screen resolution (1920x1080)
- Windows scaling set to 100%
- SCR in English language

### Setup

1. **Clone the repository**:
    ```bash
    git clone https://github.com/midit/SCR_DSHelper.git
    cd SCR_DSHelper
    ```

2. **Set up the virtual environment and install dependencies**:
    ```bash
    setup_and_run.bat
    ```

## Usage

1. **Run the application**:
    ```bash
    python main.py
    ```

2. **Next you will see DSHelper window**:

    ![](https://i.imgur.com/MLw6gBP.png)

    **Always on top:** the program`s window stays at the top of the screen.  
    **Disable title bar:** hides the title bar  
    **Reset statistics:** set actual statistics and timer to 0.  
    **SC:** indicator that shows if train headcode have found


## Video How to Use:
• • • • maybe later • • • • 

## Project Structure

- `main.py`: Main script of the application.
- `requirements.txt`: List of dependencies.
- `setup_and_run.bat`: Setup script.
- `README.md`: Project documentation.
- `logo.ico`, `logo.png`, `logo.svg`: Project logos.
- `sounds/`: Directory containing sound files.
- `screenshots/`: Directory containing screenshot files.

## License

This project is licensed under the [GNU General Public License v3.0](https://github.com/midit/SCR_DSHelper/blob/main/LICENSE)

## Acknowledgements

- [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter)
- [Tesseract OCR](https://github.com/tesseract-ocr/tesseract)
- [Pygame](https://www.pygame.org/news)

## Contact

For any questions or suggestions, feel free to open an issue or contact [me](https://www.github.com/midit).