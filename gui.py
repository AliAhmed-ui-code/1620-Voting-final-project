from tkinter import *
from logic import submit_logic

class Gui:

    def __init__(self, window)-> None:
        """
        This function creates all the widgets on the GUI
        :param window: This is the window that is created in main
        """
        self.window = window
        # Title
        self.frame_one = Frame(self.window)
        self.title_name = Label(self.frame_one, text='VOTING APPLICATION', font=("Times New Roman", 20))
        self.title_name.pack(padx=30)
        self.frame_one.pack(anchor='w')

        # ID Label and ID entry Box
        self.frame_two = Frame(self.window)
        self.ID_Label = Label(self.frame_two, text='ID', font=("Times New Roman", 15))
        self.ID_entry = Entry(self.frame_two, width=30)
        self.ID_Label.pack(side='left', padx=5)
        self.ID_entry.pack(side='left', padx=10)
        self.frame_two.pack(anchor='w')

        # Radio Buttons
        self.frame_three = Frame(self.window)
        self.radio_answer = IntVar()
        self.radio_answer.set(0)
        self.radio_Candidate1 = Radiobutton(self.frame_three, text='Jane', font=("Times New Roman", 15), variable=self.radio_answer, value=1)
        self.radio_Candidate2 = Radiobutton(self.frame_three, text='John', font=("Times New Roman", 15), variable=self.radio_answer, value=2)
        self.radio_Candidate1.pack(side='left', padx=45)
        self.radio_Candidate2.pack(side='left', padx=70)
        self.frame_three.pack(anchor='w')

        # Submit Vote Button
        self.frame_four = Frame(self.window)
        self.button_save = Button(self.frame_four, text='SUBMIT VOTE', command=self.submit)
        self.button_save.pack()
        self.frame_four.pack()

    def submit(self)-> None:
        """
        This function is called when pushing the gui button Submit
        :return: Sends the values to the logic file and creates the clear_fields function used in logic
        """
        # Source for passing a function as an argument: https://www.geeksforgeeks.org/passing-function-as-an-argument-in-python/
        def clear_fields():
            self.ID_entry.delete(0, END)
            self.radio_answer.set(0)

        # Call the logic function
        ID = self.ID_entry.get()
        radio_answer = self.radio_answer.get()
        submit_logic(ID, radio_answer, clear_fields)
