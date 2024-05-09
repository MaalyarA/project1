#gui file
from tkinter import *
import csv
from project1_functions import *
#MAKE SURE TO ADD PRIVATE VARIABLESSSSSSS
class GUI:
    def __init__(self, window):
        self.__window = window
        self.__frame1 = Frame(self.__window)
        self.__frame2 = Frame(self.__window)
        self.__frame3 = Frame(self.__window)
        self.name_label = Label(self.__frame1, text='Name')
        self.name_entry = Entry(self.__frame1)