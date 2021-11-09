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

## Running the executable ##
To allow the program to find the model, create a folder face_mask_detection and copy model3.h5 from
face_mask_detection/model3.h5 into that folder. This folder should be on the same level as the executable

