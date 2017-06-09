from tkinter import *
import gym_writer

root = Tk()
root.title("Gym Log")
 
# Add a grid
mainframe = Frame(root)
mainframe.grid(column=0,row=0, sticky=(N,W,E,S) )
mainframe.columnconfigure(0, weight = 1)
mainframe.rowconfigure(0, weight = 1)
"""mainframe.pack(pady = 50, padx = 50)"""
 
# Create a Tkinter variable
tkvar = StringVar(root)
 
# Dictionary with options
choices = { 'Bench','Squat','Deadlift' }
tkvar.set('Bench') # set the default option

# for creating a new window
def new_window():
	wind = Toplevel()
	button = Button(wind, text="Dismiss", command=wind.destroy)
	button.pack()
 
popupMenu = OptionMenu(mainframe, tkvar, *choices)
Label(mainframe, text="Choose an exercise").grid(row = 0, column = 0)
popupMenu.grid(row = 1, column = 0)

top = None
B1 = Button(mainframe, text='Create new exercise', command=lambda: new_window())
B1.grid(row = 6, column = 0)

Label(mainframe, text="Last time exercised:").grid(row = 0, column = 1)
L1 = Label(mainframe, text="Last time exercised placeholder")
L1.grid(row = 1, column = 1)

Label(mainframe, text="Last time weight").grid(row = 2, column = 1)
L2 = Label(mainframe, text="Last time weight placeholder")
L2.grid(row = 3, column = 1)

Label(mainframe, text="Last time sets").grid(row = 4, column = 1)
L3 = Label(mainframe, text="Last time sets placeholder")
L3.grid(row = 5, column = 1)

Label(mainframe, text="Last time reps").grid(row = 6, column = 1)
L4 = Label(mainframe, text="Last time reps placeholder")
L4.grid(row = 7, column = 1)

Label(mainframe, text="Max weight date").grid(row = 0, column = 2)
L5 = Label(mainframe, text="Max weight date placeholder")
L5.grid(row = 1, column = 2)

Label(mainframe, text="Max weight").grid(row = 2, column = 2)
L6 = Label(mainframe, text="Max weight placeholder")
L6.grid(row = 3, column = 2)

Label(mainframe, text="Max weight sets").grid(row = 4, column = 2)
L7 = Label(mainframe, text="Max weight sets placeholder")
L7.grid(row = 5, column = 2)

Label(mainframe, text="Max weight reps").grid(row = 6, column = 2)
L8 = Label(mainframe, text="Max weight reps placeholder")
L8.grid(row = 7, column = 2)
 
# on change dropdown value
def change_dropdown(*args):
    print( tkvar.get() )



 
# link function to change dropdown
tkvar.trace('w', change_dropdown)
 
root.mainloop()