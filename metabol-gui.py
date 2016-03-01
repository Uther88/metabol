# Графический интерфейс программы Metabol

import tkinter
from tkinter.constants import *

# Main class
class App(tkinter.Frame):
    def __init__(self, master=None):
        tkinter.Frame.__init__(self, master)
        self.pack(fill=BOTH)
        self.create_widgets()
    def create_widgets(self):
        self.weight = tkinter.IntVar()
        self.height = tkinter.IntVar()
        self.age = tkinter.IntVar()
        self.gender = tkinter.IntVar()
        
        self.label = tkinter.Label(self, text='Ваш вес:')
        self.label.pack()
        self.entry = tkinter.Entry(self, textvariable=self.weight,width=5)
        self.entry.pack()
        
        self.label = tkinter.Label(self, text='Ваш рост:')
        self.label.pack()
        self.entry = tkinter.Entry(self, textvariable=self.height,width=5)
        self.entry.pack()

        self.label = tkinter.Label(self, text='Ваш возраст:')
        self.label.pack()
        self.entry = tkinter.Entry(self, textvariable=self.age,width=5)
        self.entry.pack()

        self.label = tkinter.Label(self, text='Ваш пол:')
        self.label.pack()
        self.radiobutton1 = tkinter.Radiobutton(self, variable=self.gender,text="Мужской", value='1')
        self.radiobutton2 = tkinter.Radiobutton(self, variable=self.gender,text="Женский",value='2')
        self.radiobutton1.pack()
        self.radiobutton2.pack()
        
        self.button_ok = tkinter.Button(self, text='Расчитать', command=self.press_button_ok)
        self.button_ok.pack(pady=10)
        
        

        self.f = tkinter.Frame(self.master)
        self.f.pack(fill=BOTH)
        self.f.v = tkinter.IntVar()
        self.f.c = tkinter.IntVar()
        self.f.c2 = tkinter.IntVar()

        self.f.label= tkinter.Label(self.f, text="Скорость метаболизма:")
        self.f.label.pack()
        self.f.l = tkinter.Entry(self.f, textvariable=self.f.v,bd='1',width=5,state="readonly")
        self.f.l.pack()

        self.f.label= tkinter.Label(self.f, text="Количество калорий")
        self.f.label.pack()
        self.f.label= tkinter.Label(self.f, text="От:")
        self.f.label.pack(side=LEFT,padx=5)
        self.f.l = tkinter.Entry(self.f, textvariable=self.f.c,bd='1',width=5,state="readonly")
        self.f.l.pack(side=LEFT,padx=5)

        
        self.f.l = tkinter.Entry(self.f, textvariable=self.f.c2,bd='1',width=5,state="readonly")
        self.f.l.pack(side=RIGHT,padx=5)

        self.f.label= tkinter.Label(self.f, text="До:")
        self.f.label.pack(side=RIGHT,padx=5)
        

        self.button_quit = tkinter.Button(text='Выйти', command=self.master.destroy)
        self.button_quit.pack(side=BOTTOM,pady=15)
        
# Actions
    def press_button_ok(self):       
        if self.gender.get() == 1:
            self.f.v.set(int((self.weight.get()*13.75)+(self.height.get()*5)-(self.age.get()*6.76)+66.47))
        elif self.gender.get() == 2:
            self.f.v.set(int((self.weight.get()*9.56)+(self.height.get()*1.85)-(self.age.get()*4.68)+655.1))

        self.f.c.set(int(self.f.v.get() * 1.2))
        self.f.c2.set(int(self.f.v.get() * 1.9))

# Launch app      
if __name__ == '__main__':
    root = App()
    root.master.title('Metabol')
    root.master.minsize(170,380)
    root.master.maxsize(170,380)
