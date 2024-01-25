import customtkinter as ctk
from base_DB import Base_DB
from book import *
from takenBook import *


class persWindow(ctk.CTkToplevel):

    s = Base_DB()
    
    ind = 0

    def __init__(self, parent, selected_option):

        pers_arr = parent.pers_arr

        super().__init__(parent)
        def closing():
            if (self.dateEntry.get() != '' and self.nameEntry.get() != '' and self.numEntry.get() != '' ):
                pers_arr[self.ind].date= self.dateEntry.get()
                pers_arr[self.ind].name= self.nameEntry.get()
                pers_arr[self.ind].number= self.numEntry.get()
                parent.pers_arr[self.ind].date= self.dateEntry.get()
                parent.pers_arr[self.ind].name= self.nameEntry.get()
                parent.pers_arr[self.ind].number= self.numEntry.get() 
                print(f"{self.ind}")
                parent.userbox.delete("all")
                for (index, elem) in enumerate(parent.pers_arr):
                    parent.userbox.insert(index, elem.name)
                persWindow.destroy(self)
            else:
                self.btn_close.configure(text="Заполните \n все \n Поля")
                self.btn_close.place(x=100, y=200)
            
        def deleting():
              parent.pers_arr.pop(self.ind)
              parent.userbox.delete("all")
              for (index, elem) in enumerate(parent.pers_arr):
                parent.userbox.insert(index, elem.name)


        for (index, elem) in enumerate(pers_arr):
            if elem.name == selected_option:
                self.ind = index
                person = pers_arr[index]

        self.geometry('300x350')
        self.title('Редактирование')
        self.resizable(False, False)

        self.main_frame = ctk.CTkFrame(self, 350, 400, 10,bg_color='transparent')
        self.main_frame.place(x=0, y=0)
        
        self.nameLabel = ctk.CTkLabel(self.main_frame, 20, 10, 10,
		                                  text=("ФИО:"))
        
        self.nameLabel.place(x=20, y=25)

        self.dateLabel = ctk.CTkLabel(self.main_frame, 20, 10, 10,
		                                  text=("Дата:"))
        
        self.dateLabel.place(x=20, y=50)

        self.numLabel = ctk.CTkLabel(self.main_frame, 20, 10, 10,
		                                  text=("Номер:"))
        
        self.numLabel.place(x=20, y=75)
        self.booksLabel = ctk.CTkLabel(self.main_frame, 20, 10, 10,
		                                  text=(f"Книги:{str(person.books)}"))
        
        self.booksLabel.place(x=20, y=125)

        self.nameEntry = ctk.CTkEntry(self.main_frame, 200, 10, 10,)
        self.nameEntry.place(x=70, y=22)
        self.nameEntry.insert(ctk.END, f"{person.name}")

        self.dateEntry = ctk.CTkEntry(self.main_frame, 200, 10, 10,)
        self.dateEntry.place(x=70, y=47)
        self.dateEntry.insert(ctk.END, f"{person.date}")

        self.numEntry = ctk.CTkEntry(self.main_frame, 200, 10, 10,)
        self.numEntry.place(x=70, y=72)
        self.numEntry.insert(ctk.END, f"{person.number}")

        self.btn_close = ctk.CTkButton(self.main_frame, 100, 50, text='Сохранить', command=closing, corner_radius=0)
        self.btn_close.place(x=100, y=200)
        self.btn_close1 = ctk.CTkButton(self.main_frame, 100, 50, text='Удалить', command=deleting, corner_radius=0)
        self.btn_close1.place(x=100, y=250)
        
        
    
