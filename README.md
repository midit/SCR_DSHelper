
_![Logo](https://i.imgur.com/0fbw1nv.jpg)

# SCR DSHelper

![](https://img.shields.io/github/repo-size/midit/SCR_DSHelper)
![](https://img.shields.io/github/last-commit/midit/SCR_DSHelper/main)
![](https://img.shields.io/github/issues/midit/SCR_DSHelper)
![](https://img.shields.io/github/issues-closed/midit/SCR_DSHelper)

The script is designed to facilitate the **task of the dispatcher** and calculate the **earned points** and **other statistics** in Stepford Country Railway.
## Features

- **Auto Safe-trip:** The script reads the number of the dispatching train operated by the dispatcher, determines its route, and inserts the message `Safe trip to ${Destination}, ${Train_hedcode}` into the clipboard.

- **Active Train info:** Information about the active train in the dispatcher's control, its headcode and route

- **List of dispatched trains:** Stores headcodes of dispatched trains

- **Dispatch stats:** Displays the number of dispatched trains and the time of the dispatcher's shift

- **Exp counter:** Displays the number of points and experience earned
## Requirements
- Windows 11 (Windows 10 should also work)
- FHD screen resolution (1920x1080)
- Windows scaling set to 100%
- SCR in English language
## Installation

1. Navigate to https://python.org/downloads and click `Download Python 3.12.0` or higher
2. Open the downloaded file
3. Check `Add Python 3.12 to PATH`
4. Click `Install Now`
5. Navigate to https://github.com/midit/SCR_DSHelper/releases
6. Under `Assets` click `Source code (zip)`
7. Unzip the file where you want (e.g. on the Desktop)
8. Open the unzipped folder
9. Create a new folder called `Tesseract-OCR` in there
10. Navigate to https://digi.bib.uni-mannheim.de/tesseract/tesseract-ocr-w64-setup-v5.3.0.20221214.exe and open the downloaded file
11. Go through the installer as instructed, but change the `Destination Folder` to folder you created in step 10 (e.g. `Desktop > scr_dshelper > Tesseract-OCR`)
12. Hit `Win + R`
13. Type `cmd` in there and hit OK
14. Paste this into the command prompt
```python
py -m pip install opencv_python requests PyDirectInput Flask numpy pytesseract Pillow pywin32
```
*The command installs required modules for DSHelper to work.*

15. After the installing finishes, you may get a warning message, but you can safely ignore it.
16. Close the command prompt and now you can start DSHelper.
## Usage/Examples

#### How to launch script at Windows:
1. Go to the `scr_dshelper` folder and run
2. Hit `Win + R` and type `cmd`
3. Enter `python main.py`
Next you will see DSHelper window:

![](https://i.imgur.com/MLw6gBP.png)

**Always on top:** the program`s window stays at the top of the screen.  
**Disable title bar:** hides the title bar  
**Reset statistics:** set actual statistics and timer to 0.  
**SC:** indicator that shows if train headcode have found


### Video How to Use:
• • • • soon • • • • 

## Authors

- [@delovebit](https://www.github.com/midit)





## License

[GNU General Public License v3.0](https://github.com/midit/SCR_DSHelper/blob/main/LICENSE)

*This is one of my first open-source scripts, please help if you can in improving my scripts and let me know if there are any problems.*_
