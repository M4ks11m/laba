import customtkinter as ctk
from base_DB import Base_DB
from book import *
from takenBook import *
from person import Person

class persWindowSpace(ctk.CTkToplevel):

    s = Base_DB()
    
    

    def __init__(self, parent):

        super().__init__(parent)
        def closing():
            if (self.dateEntry.get() != '' and self.nameEntry.get() != '' and self.numEntry.get() != '' ):
                pers = Person(self.dateEntry.get(), self.nameEntry.get(), self.numEntry.get() )
                parent.pers_arr.append(pers)
                parent.userbox.insert(len(parent.pers_arr)-1, pers.name)
                persWindowSpace.destroy(self)
            else:
                self.btn_close.configure(text="Заполните \n все \n Поля")
                self.btn_close.place(x=100, y=200)
            
            

        self.geometry('300x350')
        self.title('Добавление')
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

        self.nameEntry = ctk.CTkEntry(self.main_frame, 200, 10, 10,)
        self.nameEntry.place(x=70, y=22)
        self.nameEntry.insert(ctk.END, f"")

        self.dateEntry = ctk.CTkEntry(self.main_frame, 200, 10, 10,)
        self.dateEntry.place(x=70, y=47)
        self.dateEntry.insert(ctk.END, f"")

        self.numEntry = ctk.CTkEntry(self.main_frame, 200, 10, 10,)
        self.numEntry.place(x=70, y=72)
        self.numEntry.insert(ctk.END, f"")

        self.btn_close = ctk.CTkButton(self.main_frame, 100, 50, text='Сохранить', command=closing, corner_radius=0)
        self.btn_close.place(x=100, y=200)