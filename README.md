# C-Eng-C
## Setting up virtual environment ##

#### Mac OS / Linux ####
source venv/Lib/activate

pip3 install -r requirements.txt

#### Windows ####
venv/Lib/activate.bat

pip3 install -r requirements.txt


## Building the executable ##
pyinstaller --onefile -y main.spec

The executable will be created in dist/main.exe
