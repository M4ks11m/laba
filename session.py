import customtkinter as ctk
from base_DB import Base_DB

class session(ctk.CTkToplevel):

    s = Base_DB()

    def __init__(self, parent):
        super().__init__(parent)
        self.geometry('300x350')
        self.title('Результаты сессии')
        self.resizable(False, False)

        self.main_frame = ctk.CTkFrame(self, 350, 400, 10,bg_color='transparent')
        self.main_frame.place(x=0, y=0)

        self.nameLabel = ctk.CTkLabel(self.main_frame, 20, 10, 10,
		                                  text=(f"Выданные книги:{str(parent.backedbooks)}"))
        
        self.nameLabel.place(x=20, y=25)

        self.dateLabel = ctk.CTkLabel(self.main_frame, 20, 10, 10,
		                                  text=(f"Возвращенные книги: {str(parent.tBookToday)}"))
        
        self.dateLabel.place(x=20, y=50)
        