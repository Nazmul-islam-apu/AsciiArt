from tkinter import *
from tkinter import ttk
from PIL import Image, ImageDraw, ImageTk
from tkinter import filedialog
import math
import re
import os

root = Tk()
root.title("ASCII ART")
root.geometry("450x800")
root.resizable(width=True, height=True)
#variables

def open_image():
    fileName = filedialog.askopenfilename(title = "Open")
    img = Image.open(fileName)
    width, height = img.size
    ratio = 400/width
    img = img.resize((400,int(ratio*height)),Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    panel = Label(root,image=img)
    panel.image = img
    panel.grid(row=1,padx = 20, pady = 10)
    #create_btn = Button(root, text="Create ASCII ART", command=ascii_generator(fileName)).grid(row=2, padx=10, pady=10)
    ascii_generator(fileName)
    label = Label(root, text = "You will find the ASCII Art in the folder of original image. Enjoy it. Thanks").grid(row=2,column=0,padx=20,pady=20)


def ascii_generator(fileName):
    ascii_chars = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\\|()1{}[]?-_+~<>i!lI;:,\"^`'. "[::-1]
    ascii_array = list(ascii_chars)
    char_len = len(ascii_array)
    interval = char_len / 256
    char_width = 10
    char_height = 18

    def get_ascii(value):
        return ascii_array[math.floor(value * interval)]

    #text_file = open("output.txt", "w")
    img = Image.open(fileName)
    width, height = img.size
    scale = 400 / width
    img = img.resize((int(scale * width), int(scale * height * (char_width / char_height))), Image.NEAREST)
    width, height = img.size
    pixel = img.load()

    outputImage = Image.new("RGB", (char_width * width, char_height * height), color=(0, 0, 0))
    outputImage_bw = Image.new("RGB", (char_width * width, char_height * height), color=(0, 0, 0))
    d = ImageDraw.Draw(outputImage)
    d_bw = ImageDraw.Draw(outputImage_bw)

    for x in range(height):
        for y in range(width):
            R, G, B = pixel[y, x]
            h = int(R / 3 + G / 3 + B / 3)
            pixel[y, x] = (h, h, h)
            #text_file.write(get_ascii(h))
            d.text((y * char_width, x * char_height), get_ascii(h), fill=(R, G, B))
            d_bw.text((y * char_width, x * char_height), get_ascii(h))
        #text_file.write("\n")
    path = os.path.dirname(fileName)
    na = re.split('\W+',fileName)
    na.pop()
    name = path+"/"+na[-1]+"_ascii.png"
    outputImage.save(name)
    #outputImage_bw.save(name+"_bw.png")



btn = Button(root, text="Select Image", command=open_image, bg="skyblue").grid(row=0, column =0, padx = 10, pady=10)

root.mainloop()
