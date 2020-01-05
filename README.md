# Chroma-Folder

Tool that allows easy color changes of Mac folder icons.

## CLI Usage

```
usage: chroma-folder-cli.py [-h] [-l LOAD] [-s SAVE] [-p PATH] [-c]

optional arguments:
  -h, --help            show this help message and exit
  -l LOAD, --load LOAD  The file to load the config from
  -s SAVE, --save SAVE  The file to save the config to
  -p PATH, --path PATH  The path to change folder icons in
  -c, --clean           Strip all custom icons from folders before applying
                        new ones
```

## GUI Installation

```Bash
cd ~/Documents
git clone git@github.com:MJVL/Chroma-Folder.git
cd Chroma-Folder
chmod +x src/fileicon
pip3 install pyqt5 pyshortcuts
pyshortcut chroma-folder-gui.py -n Chroma\ Folder -i src/icon.icns -d
mv ~/Desktop/Chroma\ Folder.app ~/Applications/Chroma\ Folder.app
```

These commands are run assuming you already have Python 3 and XCode Command Line Tools installed. For a full setup that installs XCode, Homebrew, and Python 3, run `install.sh`.