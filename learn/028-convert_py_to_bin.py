# ----------------------------------
# This script is used for learning
# Created by winadm
# Version 0.1
# Examples
# ...
# ----------------------------------
# we have to install some packages on server
# sudo apt install build-essential
# next we have to download actual version of pyinstaller
# wget https://github.com/pyinstaller/pyinstaller/archive/refs/tags/v5.7.0.tar.gz
# untar it and install it
# tar -xvf v5.7.0.tar.gz
# ./pyinstaller.py setup.py
# copy bin
# sudo cp pyinstaller /usr/bin/
# and check pyinstaller version by
# pyinstaller --version
# next write simple script, put it in some directory and make executable
cp 001-hello-world.py /home/admin7/converting/
chmod +x 001-hello-world.py
pyinstaller --onefile 001-hello-world.py
# look in dist folder and explore bin file properties. look carefully for file SIZE!
file 001-hello-world
# run new bin
file 001-hello-world
