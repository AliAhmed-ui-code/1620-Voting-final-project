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
    with open("VOTED.csv", "a", newline="") as csvfile:
        writer = csv.writer(csvfile, delimiter='\t')
        writer.writerow(['ID NUMBER', 'CANDIDATE VOTED FOR'])
    Gui(window)
    window.mainloop()
if __name__ == '__main__':
    main()
