#!/bin/bash

install_gem() {
    echo "Checking for gem $1 installation."
    if ! gem spec $1 > /dev/null 2>&1; then
        echo "Gem $1 was not found. Installing"
        sudo gem install $1
    else
        echo "Gem $1 was found."
    fi
}

install_xcode_tools() {
    echo "Checking for XCode tools installation."
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
        echo "Homebrew was not found. Installing."
        ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
    else
        echo "Homebrew was found. Updating."
        brew update
    fi
}

brew_install() {
    echo "Checking for formula $1 installation."       
    if brew ls --versions $1 > /dev/null; then
        echo "$1 is found."
    else
        echo "$1 was not found. Installing."
        brew install $1
    fi
    sudo chown -R $(whoami) /usr/local/share/man/man6
}

chroma_install() {
    echo "Cloning Chroma Folder repository."
    cd ~/Documents
    git clone https://github.com/MJVL/Chroma-Folder.git
    cd Chroma-Folder
    echo ""
    echo "Setting permissions."
    chmod +x src/fileicon
    echo ""
    echo "Installing pip packages."
    pip3 install pyqt5 pyshortcuts
    echo ""
    pyshortcut chroma-folder-gui.py -n Chroma\ Folder -i src/icon.icns -d
    echo "Bundling the Application."
    mv ~/Desktop/Chroma\ Folder.app /Applications/Chroma\ Folder.app
    chmod -R 755 /Applications/Chroma\ Folder.app
    echo ""
}

clear
echo "Starting Chroma Folder installation..."
echo ""
install_gem figlet
install_gem lolcat
echo ""
install_xcode_tools
echo ""
install_homebrew
echo ""
brew_install figlet
brew_install python3
echo ""
chroma_install

figlet Chroma Folder | lolcat --animate
echo ""
echo "Installation complete. Chroma Folder can now be found in your Applications."