from tkinter import*
from tkinter import ttk
import random
import tkinter.messagebox
from datetime import datetime
from typing_extensions import Self
import logTicketDatabase
import datetime
import time
from datetime import datetime, timedelta
#Creating frontend design
class TicketingSystem:
    def _init(self,root):
        self.root = root
        self.root.title("Ticket Log Support System")
        self.root.geometry("1350x800+0+0")
        
        MainFrame = Frame(self.root)
        MainFrame.grid()
        TopFrame = Frame(MainFrame, bd=10, width=1000, height=450, relief=RIDGE)
        TopFrame.pack(side=TOP)

if _name_=='_main_':
    root = Tk()
    application = TicketingSystem (root)
    root.mainloop()