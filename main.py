import tkinter as tk
import subprocess
import sys
import os
r = tk.Tk()
r.title('Counting Seconds')
def ImgClassifier():
    os.system('python readimage.py')
def VidClassifier():
    os.system('python readvideo.py')
button = tk.Button(r, text='Image', width=25, command=ImgClassifier)
btn2 = tk.Button(r, text='Video', width=25, command=VidClassifier)
button.pack()
btn2.pack()
r.mainloop()
"""
print("1. Classify From Image file")
print("2. Classify from Video file")
c=int(input("Enter Choice"))

if c == 1:
    subprocess.call(" python readimage.py 1", shell=True)
elif c == 2:
    subprocess.call(" python readvideo.py 1", shell=True)
else:
    print("Please enter the correct option")
"""
