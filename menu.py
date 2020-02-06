from tkinter import*
from tkinter import messagebox
import webbrowser
from tkinter import filedialog


def new():
    t1.delete(0.0,END)

def about():
    messagebox.showinfo("Info","This a python notepad made by Yassa")

url = 'http://www.google.ca'
def f1doc():
    webbrowser.open_new(url)


def drive():
    url ="https://drive.google.com/drive/u/0/my-drive"
    webbrowser.open_new(url)



def saveas():
    name=filedialog.asksaveasfile(mode='w',defaultextension='.txt')
    text2save=str(t1.get(0.0,END))
    name.write(text2save)
    name.close
def clear():
    answer=messagebox.askyesno("Clear","Are you sure to clear")
    if answer==True:
        t1.delete(0.0,END)
def openf():
    global name
    name = filedialog.askopenfilename(initialdir="C:/Users/Admin/Documents/",
                           filetypes = (("Text File","*.txt"),("Python File","*.py"),("All Files","*.*")),
                           title = "Choose a file.")
    t1.delete(0.0,END)
    try:
        
        with open(name,'r') as file:
            t1.insert(END,file.read())
    except:
        print("No file exist")

    

              
    
    
                                        
                  

    
    
       
    


screen=Tk()
menubar=Menu(screen)
screen.geometry('500x500')
##screen.resizable(False,False)
filemenu = Menu (menubar,tearoff=0)



filemenu.add_command(label="New",command = new,background='medium spring green',foreground='black',activebackground='#004c99', activeforeground='white')
filemenu.add_command(label="Open",command=openf,background='medium spring green',foreground='black',activebackground='#004c99', activeforeground='white')
filemenu.add_command(label="Save As",command=saveas,background='medium spring green',foreground='black',activebackground='#004c99', activeforeground='white')
filemenu.add_command(label="Clear",command=clear,background='medium spring green',foreground='black',activebackground='#004c99', activeforeground='white')


filemenu.add_command(label="Exit",command=screen.destroy,background='medium spring green',foreground='black',activebackground='#004c99', activeforeground='white')

menubar.add_cascade(label="File",menu=filemenu)
screen.config(menu=menubar)





filemenu = Menu (filemenu,tearoff=0)
filemenu.add_command(label="About",command=about,background='cyan',foreground='black',activebackground='#004c99', activeforeground='white')
filemenu.add_command(label="Google",command=f1doc,background='cyan',foreground='black',activebackground='#004c99', activeforeground='white')
filemenu.add_command(label="Google Drive",command=drive,background='cyan',foreground='black',activebackground='#004c99', activeforeground='white')




menubar.add_cascade(label="Help",menu=filemenu)
screen.config(menu=menubar)
t1=Text(screen,height =500, width=500 )
t1.pack()






screen.mainloop()





































