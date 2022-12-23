


from tkinter import *
import tkinter
from tkinter import messagebox
from PIL import Image, ImageTk
from numpy import place
from tkinter import Canvas
import cv2
from tensorflow.keras.models import load_model
import matplotlib.pyplot as plt
from tensorflow.keras.utils import load_img, img_to_array
from tkinter import filedialog
import pytesseract as tess
tess.pytesseract.tesseract_cmd = r'D:\\ProjectAI\\tesseract.exe'
import numpy as np

    


def giao_dien():
    present = Tk()
    present.title("PROJECT:PHAT HIEN NHAC CU")
    present.geometry("1000x800")
     #đưa ra giữa màn hình
    present.update_idletasks()
    width = present.winfo_width()
    frm_width = present.winfo_rootx() - present.winfo_x()
    win_width = width + 2 * frm_width
    height = present.winfo_height()
    titlebar_height = present.winfo_rooty() - present.winfo_y()
    win_height = height + titlebar_height + frm_width
    x = present.winfo_screenwidth() // 2 - win_width // 2
    y = present.winfo_screenheight() // 2 - win_height // 2
    present.geometry('{}x{}+{}+{}'.format(width, height, x, y))
    
    return

def cua_so(): 
   
    window = Tk()
    window.title("GIỚI THIỆU ĐỀ TÀI ")
    window.geometry("1000x800") 
   
    window.update_idletasks()
    width = window.winfo_width()
    frm_width = window.winfo_rootx() - window.winfo_x()
    win_width = width + 2 * frm_width
    height = window.winfo_height()
    titlebar_height = window.winfo_rooty() - window.winfo_y()
    win_height = height + titlebar_height + frm_width
    x = window.winfo_screenwidth() // 2 - win_width // 2
    y = window.winfo_screenheight() // 2 - win_height // 2
    window.geometry('{}x{}+{}+{}'.format(width, height, x, y))
    rec = Canvas(window, bg= "lightcyan",height= 1000, width= 1000).place(x= 0, y= 0)
  
    
    lbl1 = tkinter.Label(window,text= "---PHÁT HIỆN NHẠC CỤ DÂN TỘC---",fg="black",bg="lightcyan",font= ("times",27)).place(x= 40, y= 20)
    
   
    panel3 = Label(window)
    panel3.place(x=430,y=100)
    
  
    def mo_anh():
        filename = filedialog.askopenfilename()
        img = Image.open(filename)
        x =int(img.size[0])
        y =int(img.size[1])
        img2 =img.resize((x,y))
        imgtk= ImageTk.PhotoImage(img)
        panel3.config(image=imgtk, width= 500, height= 600)
        panel3.img=imgtk
        def nhandien():
            model = load_model('nhaccu.h5')
            img5 = load_img(filename,target_size=(150,150))
            plt.imshow(img5)
            img5=img_to_array(img5)
            img5=img5.astype('float32')
            img5=img5/255
            img5=np.expand_dims(img5,axis=0)
            result=model.predict(img5)
            class_nhaccu=['Dan Tranh',
 'Dan bau',
 'Sáo trúc',
 'Đàn Nhị',
 'Đàn nguyệt',
 'Đàn tam thập lục',
 'Đàn tì bà',
 'Đàn Đáy']
            a= int(np.argmax(model.predict(img5),axis=1))
            print("Đây là nhạc cụ:", class_nhaccu[a])
            lable2= Label(text=class_nhaccu[a], bg="black",fg='white',font= 'arial 20').place(x=600,y=730)
            
        btn1= Button(window, text= "Nhận Diện",font=("Arial",18,"bold"),bg="lavenderblush",fg= "red",command=nhandien).place(x=60, y= 300)
        
      
    
 

    btn = Button(window, text= "Chọn ảnh",font=("Arial",18,"bold"),bg="lavenderblush",fg= "red",command=mo_anh).place(x=60, y= 200)
    
    
    


    
    
    
    
    
    window.mainloop()
    return

cua_so()