from gui import *
import csv

def main()-> None:
    """
    This function creates the gui window and the file voted!
    :return: Sends the window to gui file
    """
    window = Tk()
    window.title('Voting')
    window.geometry('350x230')
    window.resizable(False, False)
    #Creates VOTED.CSV
    Gui(window)
    window.mainloop()
if __name__ == '__main__':
    main()
