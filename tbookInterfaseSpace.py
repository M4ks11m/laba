import customtkinter as ctk
from base_DB import Base_DB
from book import *
from takenBook import *
from takenBook import takenBook

class tbookWindowSpace(ctk.CTkToplevel):

    s = Base_DB()
    
    

    def __init__(self, parent):

        super().__init__(parent)
        def closing():
            i = 0
            for (index, elem) in enumerate(parent.book_arr):
                if parent.book_arr[index].name == self.bookEntry.get():
                    i = i+1
                else:
                    pass
            
            if i != 0:
                self.btn_close.configure (text ='Неверный \n ввод')
                self.btn_close.place(x=100, y=200)
                    
                     
            for (index, elem) in enumerate(parent.pers_arr):
                if parent.pers_arr[index].name == self.personEntry.get() and len(parent.pers_arr[index].books) != 0:
                    i = i+1
                else:
                    self.btn_close = ctk.CTkButton(self.main_frame, 100, 50, text='Неверный \n ввод', command=closing, corner_radius=0)
                    self.btn_close.place(x=100, y=200)
            if i > 1:
                self.btn_close.configure (text ='Неверный \n ввод')
                self.btn_close.place(x=100, y=200)

            if (self.bookEntry.get() != '' and self.personEntry.get() != '' and self.dataEntry.get() != '' and self.backEntry.get() != '' and self.backedEntry.get() != '' ):
                if ( self.backedEntry.get() == 'False' 
                     or self.backedEntry.get() == 'Нет' ):
                    pers = takenBook(self.bookEntry.get(), self.personEntry.get(), self.dataEntry.get(), self.backEntry.get(), self.backedEntry.get() )
                    parent.tBook_arr.append(pers)
                    parent.tBookbox.insert(len(parent.tBook_arr)-1, "Книга:{0} Вернули?:{2} \nФИO: {1}".format(self.bookEntry.get(), self.personEntry.get(), self.backedEntry.get()))
                    if(self.backedEntry.get() == 'False' or self.backedEntry.get() == 'Нет' ):
                        for (index, elem) in enumerate(parent.book_arr):
                                if parent.book_arr[index].name == self.bookEntry.get():
                                    parent.book_arr[index].realQuan = parent.book_arr[index].realQuan - 1
                        for (index, elem) in enumerate(parent.pers_arr):
                                if parent.pers_arr[index].name == self.personEntry.get():
                                    parent.pers_arr[index].books.append(f"{self.bookEntry.get()}")
                                    parent.backedbooks.append(f"{self.bookEntry.get()}")
                        if i > 1:
                            tbookWindowSpace.destroy(self)     
                else:
                    self.btn_close.configure(text="B поле вернули \n неодходимо ввести \n Нет")
                    self.btn_close.place(x=90, y=200)
            else:
                    self.btn_close.configure(text="Заполните \n все \n Поля")
                    self.btn_close.place(x=100, y=200)
            

        self.geometry('300x350')
        self.title('Добавление')
        self.resizable(False, False)

        self.main_frame = ctk.CTkFrame(self, 350, 400, 10,bg_color='transparent')
        self.main_frame.place(x=0, y=0)
        
        self.nameLabel = ctk.CTkLabel(self.main_frame, 20, 10, 10,
		                                  text=("Книга:"))
        
        self.nameLabel.place(x=20, y=25)

        self.dateLabel = ctk.CTkLabel(self.main_frame, 20, 10, 10,
		                                  text=("ФИО:"))
        
        self.dateLabel.place(x=20, y=50)

        self.numLabel = ctk.CTkLabel(self.main_frame, 20, 10, 10,
		                                  text=("Дата выдачи:"))
        
        self.numLabel.place(x=20, y=75)

        self.numLabel = ctk.CTkLabel(self.main_frame, 20, 10, 10,
		                                  text=("Дата возврата:"))
        
        self.numLabel.place(x=20, y=100)

        self.numLabel = ctk.CTkLabel(self.main_frame, 20, 10, 10,
		                                  text=("Вернули?:"))
        
        self.numLabel.place(x=20, y=125)

        self.bookEntry = ctk.CTkEntry(self.main_frame, 150, 10, 10,)
        self.bookEntry.place(x=120, y=22)
        self.bookEntry.insert(ctk.END, f"")

        self.personEntry = ctk.CTkEntry(self.main_frame, 150, 10, 10,)
        self.personEntry.place(x=120, y=47)
        self.personEntry.insert(ctk.END, f"")

        self.dataEntry = ctk.CTkEntry(self.main_frame, 150, 10, 10,)
        self.dataEntry.place(x=120, y=72)
        self.dataEntry.insert(ctk.END, f"")

        self.backEntry = ctk.CTkEntry(self.main_frame, 150, 10, 10,)
        self.backEntry.place(x=120, y=97)
        self.backEntry.insert(ctk.END, f"")

        self.backedEntry = ctk.CTkEntry(self.main_frame, 150, 10, 10,)
        self.backedEntry.place(x=120, y=122)
        self.backedEntry.insert(ctk.END, f"")


        self.btn_close = ctk.CTkButton(self.main_frame, 100, 50, text='Сохранить', command=closing, corner_radius=0)
        self.btn_close.place(x=100, y=200)