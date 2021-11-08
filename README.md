# C-Eng-C

## Installing pytesseract ##

https://nanonets.com/blog/ocr-with-tesseract/#installingtesseract


## Setting up virtual environment ##

#### Mac OS / Linux ####
source venv/Scripts/activate

pip3 install -r requirements.txt

#### Windows ####
venv/Scripts/activate.bat

pip3 install -r requirements.txt


## Building the executable ##
pyinstaller --onefile -y main.spec

The executable will be created in dist/main.exe
