from tkinter import *

from PIL import Image, ImageTk

class Start:
    def __init__(self, parent):

        self.img_file = Image.open("333.png")
        self.img_file = self.img_file.resize((300,100))
        self.img_file = ImageTk.PhotoImage(self.img_file)

        self.b1 = Button(parent,image=self.img_file, border = 0, command = self.inst)
        self.b1.place(x=195,y=400)
   
    def inst(self):
      self.b1.destroy()
    name(window)


class name:
    def __init__(self, parent):
     
        bg_image2 = Image.open("Name22.png")
        bg_image2 = bg_image2.resize((700,600),Image.ANTIALIAS)
        bg_image2 = ImageTk.PhotoImage(bg_image2)
        image_label.configure(image = bg_image2)
        image_label.image=bg_image2

 
     
if __name__== "__main__":
    window = Tk()
    window.title("IQ Quiz")
    window.geometry("700x600")
    bg_image = Image.open("startpage1.png")
    bg_image = bg_image.resize((700,600),Image.ANTIALIAS)
    bg_image = ImageTk.PhotoImage(bg_image)
    image_label= Label(window, image=bg_image)
    image_label.place(x=0, y=0, relwidth=1, relheight=1)
    start_object = Start(window)

    window.mainloop()