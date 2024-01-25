import customtkinter as ctk
import threading
import time
from tkinter import IntVar
from PIL import Image
import ctk_listbox as list
from base_DB import Base_DB
import persInterfase
import persInterfaseSpace
import bookInterface
import tbookInterface
import bookInterfaseSpace
import tbookInterfaseSpace
import session

class App(ctk.CTk):
    s = Base_DB()
    pers_arr = s.person_arr
    book_arr = s.book_arr
    tBook_arr = [s.tBook1]
    sessionTBook_arr = [s.tBook1]
    backedbooks = []
    tBookToday = []
    def __init__(self):

        def open_window(selected_option):
            logWindow = persInterfase.persWindow(self,selected_option)
            logWindow.grab_set()
        def addPerson():
            logWindow = persInterfaseSpace.persWindowSpace(self)
            logWindow.grab_set()
        def open_bookwindow(selected_option):
            logWindow = bookInterface.bookWindow(self,selected_option)
            logWindow.grab_set()
        def addBook():
            logWindow = bookInterfaseSpace.bookWindowSpace(self)
            logWindow.grab_set()
        def open_tbookwindow(selected_option):
            logWindow = tbookInterface.tbookWindow(self,selected_option)
            logWindow.grab_set()
        def addtBook():
            logWindow = tbookInterfaseSpace.tbookWindowSpace(self)
            logWindow.grab_set()
        
            #self.userbox.delete(self.userbox.curselection())
            
        super().__init__()

        def findByName():
            newArr = []
            newArr2 = []
            i = 0
            if self.nameEntry.get() != "":
                for (index, elem) in enumerate(self.book_arr):
                    if self.book_arr[index].name[:len(self.nameEntry.get())] == self.nameEntry.get():
                        newArr.append(self.book_arr[index])
                        i = i+1
                self.bookbox.delete("all")
                for (index, elem) in enumerate(newArr):
                    self.bookbox.insert(index, elem.name)
                for (index, elem) in enumerate(self.tBook_arr):
                    if self.tBook_arr[index].book[:len(self.nameEntry.get())] == self.nameEntry.get():
                        newArr2.append(self.tBook_arr[index])
                        i = i+1
                self.tBookbox.delete("all")
                for (index, elem) in enumerate(newArr2):
                    self.tBookbox.insert(index, "Книга:{0} Вернули?:{2} \nФИO: {1}".format(elem.book, elem.person, elem.backed))
            else :
                self.bookbox.delete("all")
                for (index, elem) in enumerate(self.book_arr):
                    self.bookbox.insert(index, elem.name)
                self.tBookbox.delete("all")
                for (index, elem) in enumerate(self.tBook_arr):
                    self.tBookbox.insert(index, "Книга:{0} Вернули?:{2} \nФИO: {1}".format(elem.book, elem.person, elem.backed))
            
        def findByCode():
            newArr = []
            newArr2 = []
            i = 0
            codeArr=[]
            for (index, elem) in enumerate(self.tBook_arr):
                for (index1, elem1) in enumerate(self.book_arr):
                    if elem.book == elem1.name:
                        codeArr.append(self.book_arr[index1].code)

            if self.codesortEntry.get() != "":
                for (index, elem) in enumerate(self.book_arr):
                    if self.book_arr[index].code[:len(self.codesortEntry.get())] == self.codesortEntry.get():
                        newArr.append(self.book_arr[index])
                        i = i+1
                self.bookbox.delete("all")
                for (index, elem) in enumerate(newArr):
                    self.bookbox.insert(index, elem.name)

                for (index, elem) in enumerate(self.tBook_arr):
                    if codeArr[index][:len(self.codesortEntry.get())] == self.codesortEntry.get():
                        newArr2.append(self.tBook_arr[index])
                        i = i+1
                self.tBookbox.delete("all")
                for (index, elem) in enumerate(newArr2):
                    self.tBookbox.insert(index, "Книга:{0} Вернули?:{2} \nФИO: {1}".format(elem.book, elem.person, elem.backed))
            else :
                self.bookbox.delete("all")
                for (index, elem) in enumerate(self.book_arr):
                    self.bookbox.insert(index, elem.name)
                self.tBookbox.delete("all")
                for (index, elem) in enumerate(self.tBook_arr):
                    self.tBookbox.insert(index, "Книга:{0} Вернули?:{2} \nФИO: {1}".format(elem.book, elem.person, elem.backed))

        def openSession():
            logWindow = session.session(self)
            logWindow.grab_set()


        self.geometry("770x750")
        self.title("Library Project")
        self.resizable(False, False)

        
        # W O R K S P A C E
        
        self.userlistframe = ctk.CTkFrame(self, 250, 600, 10, bg_color='transparent')
        self.userlistframe.place(x=10, y=25)
        self.takenlistframe = ctk.CTkFrame(self, 250, 600, 10, bg_color='transparent')
        self.takenlistframe.place(x=260, y=25)
        self.booklistframe = ctk.CTkFrame(self, 250, 600, 10, bg_color='transparent')
        self.booklistframe.place(x=510, y=25)
        self.findlistframe = ctk.CTkFrame(self, 650, 100, 10, bg_color='transparent')
        self.findlistframe.place(x=50, y=625)
        ##self.text = ctk.CTkTextbox(self.wicket, 351, 61)
        ##self.text.place(x=10, y=300)
        
        # Поиск

        self.namesortLabel = ctk.CTkLabel(self.findlistframe, 20, 10, 10,
		                                  text=("поиск по названию:"))
        self.namesortLabel.place(x=10, y=10)
        self.nameEntry = ctk.CTkEntry(self.findlistframe,150, 10, 10)
        self.nameEntry.place(x=150, y=8)
        self.nameSortBtn = ctk.CTkButton(self.findlistframe, 30, 10, text='Найти', command=findByName, corner_radius=0)
        self.nameSortBtn.place(x=300, y=8)

        self.codesortLabel = ctk.CTkLabel(self.findlistframe, 20, 10, 10,
		                                  text=("поиск по коду:"))
        self.codesortLabel.place(x=10, y=35)
        self.codesortEntry = ctk.CTkEntry(self.findlistframe,150, 10, 10)
        self.codesortEntry.place(x=150, y=33)
        self.codesortBtn = ctk.CTkButton(self.findlistframe, 30, 10, text='Найти', command=findByCode, corner_radius=0)
        self.codesortBtn.place(x=300, y=33)
        self.sessionBtn = ctk.CTkButton(self.findlistframe, 30, 10, text='Результаты сессии', command=openSession, corner_radius=0)
        self.sessionBtn.place(x=500, y=33)
        
        

        # Списки
        self.userbox = list.CTkListbox(self.userlistframe,height=550,text_color=	'#000000',font =('font', 10), command=open_window)
        self.userbox.pack(fill="both", expand=True, padx=10, pady=10)
        self.btn_pesrAdd = ctk.CTkButton(self.userlistframe, 100, 50, text='Добавить', command=addPerson, corner_radius=0)
        self.btn_pesrAdd.place(x=75, y=500)
        self.bookbox = list.CTkListbox(self.booklistframe,height=550,text_color=	'#000000',font =('font', 10), command=open_bookwindow)
        self.bookbox.pack(fill="both", expand=True, padx=10, pady=10)
        self.btn_bookAdd = ctk.CTkButton(self.booklistframe, 100, 50, text='Добавить', command=addBook, corner_radius=0)
        self.btn_bookAdd.place(x=75, y=500)
        self.tBookbox = list.CTkListbox(self.takenlistframe,height=550,text_color=	'#000000',font =('font', 10), command=open_tbookwindow)
        self.tBookbox.pack(fill="both", expand=True, padx=10, pady=10)
        self.btn_bookAdd = ctk.CTkButton(self.takenlistframe, 100, 50, text='Добавить', command=addtBook, corner_radius=0)
        self.btn_bookAdd.place(x=75, y=500)

        
        for (index, elem) in enumerate(self.pers_arr):
            self.userbox.insert(index, elem.name)

        for (index, elem) in enumerate(self.book_arr):
            self.bookbox.insert(index, elem.name)

        for (index, elem) in enumerate(self.tBook_arr):
            self.tBookbox.insert(index, "Книга:{0} Вернули?:{2} \nФИO: {1}".format(elem.book, elem.person, elem.backed))

        

        