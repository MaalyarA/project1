#main file
from project1_functions import *
from project1_gui import *
def main() -> None:
    """
    Runs the ATM GUI program
    :return: None
    """
    window = Tk()
    window.geometry("500x600")
    window.title("ATM")
    window.resizable(False, False)
    GUI(window)
    window.mainloop()


if __name__ == '__main__':
    main()
