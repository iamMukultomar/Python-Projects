import pyautogui
import tkinter as tk

from tkinter import filedialog
import time

#creating an object for our dialog box 
obj=tk.Tk()

#setting length and height of dialog box
box=tk.Canvas(obj,width=200,height=200)
box.pack()


#function to take a screenshot
def screenshot():
    print('Screenshot will be taken after two seconds of pressing button so minimize the dialog box afteer pressing the button')
    time.sleep(2)
    ss=pyautogui.screenshot()
    file_path=filedialog.asksaveasfilename(defaultextension='.png')
    ss.save(file_path)

#adding button
b=tk.Button(text="Take A Screenshot",command=screenshot,bg='blue',fg='white',font=5)

box.create_window(100,100,window=b)
#popping the dialog box
obj.mainloop()