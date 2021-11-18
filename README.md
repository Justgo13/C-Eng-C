# C-Eng-C
Project created during Carleton Engineering Programming Competition. 

<h3>Problem Statement:</h3>
Living through a pandemic for the past year and a half it’s safe to say we’re all sick of it, however, the appropriate health measures are still important to mitigate infection numbers and keep everyone safe. At Carleton one of the most important measures that allowed the campus to reopen was the COVID screeners placed at major entrances to every building. While this has allowed the university to reopen these screeners are put at risk every day being exposed to possibly infected individuals. Your challenge will be to accomplish the following:
To help increase safety across campus cameras have been placed at the doors to every major entrance. These cameras will use computer vision to unlock their corresponding door when they have confirmed the follow: An individual is wearing a mask, they have completed their screening form, and they are fully vaccinated. Your job will be to create a software that can do this.

<h3>Solution:</h3>
Our solution consists of imagining if every door to a carleton building had a webcam attached to it. Through computer vision and the webcam, a student would have to complete 3 tasks to open the door. 

1. Show their face wearing a mask. Our computer vision system can detect a face wearing a mask in a correct way. It will then allow you to continue to the next step
2. The student must show their vaccine QR code to the camera. Our code will scan the QR code. If this was implemented, it would be referenced to the Ontario Vaccine database to confirm it is valid
3. The student pass then can their carleton screening form to the camera. It will be detected and scanned to verify that it was completed on todays data. 

With all 3 of these steps being completed, the door will open.

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

