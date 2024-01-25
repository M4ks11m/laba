import customtkinter as ctk
from base_DB import Base_DB
from book import *
from takenBook import *
from book import Book

class bookWindowSpace(ctk.CTkToplevel):

    s = Base_DB()
    
    

    def __init__(self, parent):

        super().__init__(parent)
        def closing():
            if (len(self.nameEntry.get()) != 0 and self.authorsEntry.get() != '' and self.codeEntry.get() != '' and
                            self.dateEntry.get() != '' and self.placeEntry.get() != '' and self.pubEntry.get() != '' and
                            self.sumEntry.get() != '' and self.realEntry.get() != ''):
                pers = Book(self.nameEntry.get(), self.authorsEntry.get(), self.codeEntry.get(),
                            self.dateEntry.get(), self.placeEntry.get(), self.pubEntry.get(),
                            self.sumEntry.get(), self.realEntry.get() )
                parent.book_arr.append(pers)
                parent.bookbox.insert(len(parent.book_arr)-1, pers.name)
                bookWindowSpace.destroy(self)
            else:
                self.btn_close.configure(text="Заполните \n все \n Поля")
                self.btn_close.place(x=100, y=300)
            
            

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
		                                  text=("Автор:"))
        
        self.numLabel.place(x=20, y=75)

        self.numLabel = ctk.CTkLabel(self.main_frame, 20, 10, 10,
		                                  text=("Код:"))
        
        self.numLabel.place(x=20, y=100)

        self.numLabel = ctk.CTkLabel(self.main_frame, 20, 10, 10,
		                                  text=("Место Изд.:"))
        
        self.numLabel.place(x=20, y=125)

        self.numLabel = ctk.CTkLabel(self.main_frame, 20, 10, 10,
		                                  text=("Издатель:"))
        
        self.numLabel.place(x=20, y=150)

        self.numLabel = ctk.CTkLabel(self.main_frame, 20, 10, 10,
		                                  text=("Общ.кол-во:"))
        
        self.numLabel.place(x=20, y=175)

        self.numLabel = ctk.CTkLabel(self.main_frame, 20, 10, 10,
		                                  text=("Кол-во:"))
        
        self.numLabel.place(x=20, y=200)


        self.nameEntry = ctk.CTkEntry(self.main_frame, 150, 10, 10,)
        self.nameEntry.place(x=120, y=22)
        self.nameEntry.insert(ctk.END, "")

        self.dateEntry = ctk.CTkEntry(self.main_frame, 150, 10, 10,)
        self.dateEntry.place(x=120, y=47)
        self.dateEntry.insert(ctk.END, "")

        self.authorsEntry = ctk.CTkEntry(self.main_frame, 150, 10, 10,)
        self.authorsEntry.place(x=120, y=72)
        self.authorsEntry.insert(ctk.END, f"")

        self.codeEntry = ctk.CTkEntry(self.main_frame, 150, 10, 10,)
        self.codeEntry.place(x=120, y=97)
        self.codeEntry.insert(ctk.END, f"")
        
        self.placeEntry = ctk.CTkEntry(self.main_frame, 150, 10, 10,)
        self.placeEntry.place(x=120, y=122)
        self.placeEntry.insert(ctk.END, f"")

        self.pubEntry = ctk.CTkEntry(self.main_frame, 150, 10, 10,)
        self.pubEntry.place(x=120, y=147)
        self.pubEntry.insert(ctk.END, f"")

        self.sumEntry = ctk.CTkEntry(self.main_frame, 150, 10, 10,)
        self.sumEntry.place(x=120, y=172)
        self.sumEntry.insert(ctk.END, f"")

        self.realEntry = ctk.CTkEntry(self.main_frame, 150, 10, 10,)
        self.realEntry.place(x=120, y=197)
        self.realEntry.insert(ctk.END, f"")

        self.btn_close = ctk.CTkButton(self.main_frame, 100, 50, text='Сохранить', command=closing, corner_radius=0)
        self.btn_close.place(x=100, y=300)