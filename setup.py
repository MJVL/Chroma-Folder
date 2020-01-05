from setuptools import setup

APP = ['chroma-folder-gui.py']
DATA_FILES = ['src', 'data']
OPTIONS = {
    'iconfile': 'src/icon.icns',
    'argv_emulation': True
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    install_requires = [
           "pyqt5 >= 5.14.0",
           "sip >= 5.0.1"
    ],
    setup_requires=['py2app'],
)