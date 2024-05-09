#main file
from project1_functions import *
from project1_gui import *
def main():
    window = Tk()
    window.geometry("500x500")
    window.title("ATM")
    window.resizable(False, False)
    GUI(window)
    window.mainloop()


if __name__ == '__main__':
    main()