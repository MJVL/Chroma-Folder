import subprocess
import os
import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-l", "--load", help="The file to load the config from")
    parser.add_argument("-s", "--save", help="The file to save the config to")
    parser.add_argument("-c", "--clean", help="Strip all custom icons from folders before applying new ones", action="store_true")
    args = parser.parse_args()
    
    if not args.load:
        print("Creating temp icns")
        subprocess.call("cp data/default.icns data/temp.icns", shell=True)

        print("Opening Preview")
        os.system("open -Wna Preview data/temp.icns")
        print("Closing Preview")

    folders = [i[0].replace(" ", "\\ ") for i in os.walk(os.path.expanduser("~/Desktop"))]

    if args.clean:
        print("Removing old icons")
        [subprocess.call("fileicon remove %s" % f, shell=True) for f in folders]

    print("Adding new icons")
    [subprocess.call("fileicon set %s data/%s.icns " % (f, "temp" if not args.load else args.load.split(".")[0]), shell=True) for f in folders]

    if args.save:
        print("Saving config: %s.icns" % args.save.split(".")[0])
        subprocess.call("cp data/temp.icns data/%s.icns" % args.save.split(".")[0], shell=True)

    if not args.load:
        print("Cleaning up temp icns")
        subprocess.call("rm data/temp.icns", shell=True)


if __name__ == "__main__":
    main()