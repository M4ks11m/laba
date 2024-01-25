import customtkinter as ctk
from base_DB import Base_DB
from book import *
from takenBook import *

class bookWindow(ctk.CTkToplevel):

    s = Base_DB()
    ind = 0

    def __init__(self, parent, selected_option):

        book_arr = parent.book_arr

        super().__init__(parent)
        def closing():
            print(self.nameEntry.get())
            if (len(self.nameEntry.get()) != 0 and self.authorsEntry.get() != '' and self.codeEntry.get() != '' and
                            self.dateEntry.get() != '' and self.placeEntry.get() != '' and self.pubEntry.get() != '' and
                            self.sumEntry.get() != '' and self.realEntry.get() != ''):
                book_arr[self.ind].name = self.nameEntry.get()
                book_arr[self.ind].authors = self.authorsEntry.get()
                book_arr[self.ind].code = self.codeEntry.get()
                book_arr[self.ind].date = self.dateEntry.get()
                book_arr[self.ind].place = self.placeEntry.get()
                book_arr[self.ind].pubHouse = self.pubEntry.get()
                book_arr[self.ind].sumQuan = self.sumEntry.get()
                book_arr[self.ind].realQuan = self.realEntry.get()
                parent.book_arr[self.ind].name = self.nameEntry.get()
                parent.book_arr[self.ind].authors = self.authorsEntry.get()
                parent.book_arr[self.ind].code = self.codeEntry.get()
                parent.book_arr[self.ind].date = self.dateEntry.get()
                parent.book_arr[self.ind].place = self.placeEntry.get()
                parent.book_arr[self.ind].pubHouse = self.pubEntry.get()
                parent.book_arr[self.ind].sumQuan = self.sumEntry.get()
                parent.book_arr[self.ind].realQuan = self.realEntry.get()
                parent.bookbox.delete("all")
                for (index, elem) in enumerate(book_arr):
                    parent.bookbox.insert(index, elem.name)
            else:
                self.btn_close.configure(text="Заполните \n все \n Поля")
                self.btn_close.place(x=100, y=300)
               
                
        def deleting():
            parent.book_arr.pop(self.ind)
            parent.bookbox.delete("all")
            for (index, elem) in enumerate(book_arr):
                parent.bookbox.insert(index, elem.name)

        for (index, elem) in enumerate(book_arr):
            if elem.name == selected_option:
                self.ind = index
                person = book_arr[index]

        self.geometry('300x350')
        self.title('Редактирование')
        self.resizable(False, False)

        self.main_frame = ctk.CTkFrame(self, 350, 400, 10,bg_color='transparent')
        self.main_frame.place(x=0, y=0)
        
        self.nameLabel = ctk.CTkLabel(self.main_frame, 20, 10, 10,
		                                  text=("Название:"))
        
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
        self.nameEntry.insert(ctk.END, f"{person.name}")

        self.dateEntry = ctk.CTkEntry(self.main_frame, 150, 10, 10,)
        self.dateEntry.place(x=120, y=47)
        self.dateEntry.insert(ctk.END, f"{person.date}")

        self.authorsEntry = ctk.CTkEntry(self.main_frame, 150, 10, 10,)
        self.authorsEntry.place(x=120, y=72)
        self.authorsEntry.insert(ctk.END, f"{person.authors}")

        self.codeEntry = ctk.CTkEntry(self.main_frame, 150, 10, 10,)
        self.codeEntry.place(x=120, y=97)
        self.codeEntry.insert(ctk.END, f"{person.code}")
        
        self.placeEntry = ctk.CTkEntry(self.main_frame, 150, 10, 10,)
        self.placeEntry.place(x=120, y=122)
        self.placeEntry.insert(ctk.END, f"{person.place}")

        self.pubEntry = ctk.CTkEntry(self.main_frame, 150, 10, 10,)
        self.pubEntry.place(x=120, y=147)
        self.pubEntry.insert(ctk.END, f"{person.pubHouse}")

        self.sumEntry = ctk.CTkEntry(self.main_frame, 150, 10, 10,)
        self.sumEntry.place(x=120, y=172)
        self.sumEntry.insert(ctk.END, f"{person.sumQuan}")

        self.realEntry = ctk.CTkEntry(self.main_frame, 150, 10, 10,)
        self.realEntry.place(x=120, y=197)
        self.realEntry.insert(ctk.END, f"{person.realQuan}")

        self.btn_close = ctk.CTkButton(self.main_frame, 100, 50, text='Сохранить', command=closing, corner_radius=0)
        self.btn_close.place(x=100, y=300)
        self.btn_close1 = ctk.CTkButton(self.main_frame, 100, 50, text='Удалить', command=deleting, corner_radius=0)
        self.btn_close1.place(x=100, y=250)
        
        