#!/bin/bash

install_xcode_tools() {
    if type xcode-select >&- && xpath=$( xcode-select --print-path ) && test -d "${xpath}" && test -x "${xpath}" ; then
        echo "XCode tools are already installed."
    else
        echo "XCode tools are not installed. Installing."
        xcode-select --install
    fi
}

install_homebrew() {
    echo "Checking for Homebrew installation."
    which -s brew
    if [[ $? != 0 ]] ; then
        echo "Homebrew was not found. Inst alling."
        ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
    else
        echo "Homebrew was found. Updating."
        brew update
    fi
}

brew_install () {       
    if brew ls --versions $1 > /dev/null; then
        echo "$1 was found."
    else
        echo "$1 was not found. Installing."
        brew install $1
    fi
}

install_xcode_tools
install_homebrew
brew_install python3

cd ~/Documents
git clone git@github.com:MJVL/Chroma-Folder.git
cd Chroma-Folder
chmod +x src/fileicon
pip3 install pyqt5 pyshortcuts
pyshortcut chroma-folder-gui.py -n Chroma\ Folder -i src/icon.icns -d
mv ~/Desktop/Chroma\ Folder.app ~/Applications/Chroma\ Folder.app
