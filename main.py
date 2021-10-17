import subprocess
print("1. Classify From Image file")
print("2. Classify from Video file")
c=int(input("Enter Choice"))
if c == 1:
    subprocess.call(" python readimage.py 1", shell=True)
elif c == 2:
    subprocess.call(" python readvideo.py 1", shell=True)
else:
    print("Please enter the correct option")