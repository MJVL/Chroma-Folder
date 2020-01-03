import subprocess
import sys


def main():
    if not (sys.version_info > (3, 0)):
        print("Please install Python 3 to continue.")
        exit(1)
    subprocess.call("chmod +x ./src/fileicon", shell=True)
    subprocess.call("pip3 install pyqt5", shell=True)


if __name__ == "__main__":
    main()