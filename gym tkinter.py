from tkinter import *
import gym_writer

root = Tk()
root.configure(background="gold")
root.title("Gym Log")

 
# Add a grid
mainframe = Frame(root)
mainframe.configure(background="DodgerBlue3")
mainframe.grid(column=0,row=0, sticky=(N,W,E,S) )
mainframe.columnconfigure(0, weight = 1)
mainframe.rowconfigure(0, weight = 1)

"""mainframe.pack(pady = 50, padx = 50)"""
 
# Create a Tkinter variable
tkvar = StringVar(root)
 
# Dictionary with options
choices = { 'Bench','Squat','Deadlift' }
tkvar.set('Bench') # set the default option

# for creating a new window for new exercise
def new_window():
	wind = Toplevel()
	wind.geometry('300x100')
	Label(wind, text="Exercise Name").grid(row = 0, column = 0)
	E1 = Entry(wind, bd =5)
	E1.grid(row=2, column=0)
	con = Button(wind, text="Confirm", command=wind.destroy)
	con.grid(row=2, column=2)
	canc = Button(wind, text="Cancel", command=wind.destroy)
	canc.grid(row=2, column=3)
 
popupMenu = OptionMenu(mainframe, tkvar, *choices)
popupMenu["menu"].configure(background="snow")
Label(mainframe, text="Choose an exercise", background="DodgerBlue3").grid(row = 0, column = 0)
popupMenu.grid(row = 1, column = 0)

top = None
B1 = Button(mainframe, text='Create new exercise', command=new_window, background="snow")
B1.grid(row = 6, column = 0)

Label(mainframe, text="Last time exercised:", background="DodgerBlue3").grid(row = 0, column = 1)
L1 = Label(mainframe, text=gym_writer.table_recent('bench')[0], background="DodgerBlue3")
L1.grid(row = 1, column = 1)

Label(mainframe, text="Last time weight", background="DodgerBlue3").grid(row = 2, column = 1)
L2 = Label(mainframe, text=str(gym_writer.table_recent('bench')[1]) + ' lb', background="DodgerBlue3")
L2.grid(row = 3, column = 1)

Label(mainframe, text="Last time sets", background="DodgerBlue3").grid(row = 4, column = 1)
L3 = Label(mainframe, text=gym_writer.table_recent('bench')[2], background="DodgerBlue3")
L3.grid(row = 5, column = 1)

Label(mainframe, text="Last time reps", background="DodgerBlue3").grid(row = 6, column = 1)
L4 = Label(mainframe, text=gym_writer.table_recent('bench')[3], background="DodgerBlue3")
L4.grid(row = 7, column = 1)

Label(mainframe, text="Max weight date", background="DodgerBlue3").grid(row = 0, column = 2)
L5 = Label(mainframe, text=gym_writer.table_max('bench')[0], background="DodgerBlue3")
L5.grid(row = 1, column = 2)

Label(mainframe, text="Max weight", background="DodgerBlue3").grid(row = 2, column = 2)
L6 = Label(mainframe, text=str(gym_writer.table_max('bench')[1]) + ' lb', background="DodgerBlue3")
L6.grid(row = 3, column = 2)

Label(mainframe, text="Max weight sets", background="DodgerBlue3").grid(row = 4, column = 2)
L7 = Label(mainframe, text=gym_writer.table_max('bench')[2], background="DodgerBlue3")
L7.grid(row = 5, column = 2)

Label(mainframe, text="Max weight reps", background="DodgerBlue3").grid(row = 6, column = 2)
L8 = Label(mainframe, text=gym_writer.table_max('bench')[3], background="DodgerBlue3")
L8.grid(row = 7, column = 2)
 
# on change dropdown value
def change_dropdown(*args):
    print( tkvar.get() )



 
# link function to change dropdown
tkvar.trace('w', change_dropdown)
 
root.mainloop()