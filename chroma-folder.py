import subprocess
import os

print("Creating temp icns")
subprocess.call("cp data/default.icns data/temp.icns", shell=True)

print("Opening Preview")
os.system("open -Wna Preview data/temp.icns")
print("Closing Preview")

folders = [i[0].replace(" ", "\\ ") for i in os.walk(os.path.expanduser("~/Desktop"))]

print("Removing old icons")
[subprocess.call("fileicon remove %s" % f, shell=True) for f in folders]

[subprocess.call("fileicon set %s data/temp.icns " % f, shell=True) for f in folders]

print("Cleaning up temp icns")
subprocess.call("rm data/temp.icns", shell=True)