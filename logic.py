# logic.py
from tkinter import messagebox
import csv

def submit_logic(ID:str, radio_answer:int, clear_fields) -> None:
    """
    This function contains all the logic for the code
    :param ID: This is the 8-digits ID entered by the user
    :param radio_answer: This is result of which radio_button is clicked
    :param clear_fields: This is the function used to clear all the entry boxes
    :return: The ID and Candidate voted for is sent to the voted.csv file if all values are valid
    """
    try:
        if radio_answer == 1:
            candidate = 'Jane'
        elif radio_answer == 2:
            candidate = 'John'
        else:
            raise TypeError
        if len(ID) != 8:
            raise ValueError
        with open("VOTED.csv", "r") as csvfile:
            reader = csv.reader(csvfile, delimiter='\t')
            for row in reader:
                if ID == row[0]:
                    messagebox.showerror("Error", "You have already voted.")
                    return
        with open("VOTED.csv", "a", newline="") as csvfile:
            writer = csv.writer(csvfile, delimiter='\t')
            writer.writerow([ID, candidate])
            messagebox.showinfo("Success", "Your vote has been submitted successfully!")

        clear_fields()
    except ValueError:
        messagebox.showerror("Invalid Input", "ID number must be an integer and only 8 characters long.")
        clear_fields()
    except TypeError:
        messagebox.showerror("Invalid Input", "Must choose a candidate.")
        clear_fields()
