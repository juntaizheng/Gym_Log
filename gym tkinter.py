from tkinter import *
import tkinter
from tkinter import ttk
import gym_writer

# for creating a new window for new exercise
def new_ex_window():
	wind = Toplevel()
	wind.geometry('150x100')
	wind.configure(background = "DodgerBlue3")
	Label(wind, text="Exercise Name", background="DodgerBlue3").grid(row = 0, column = 0, sticky=W+E+N+S, columnspan = 2)
	E1 = ttk.Entry(wind)
	E1.grid(row=1, column=0, columnspan=2)
	con = ttk.Button(wind, text="Confirm", command=wind.destroy)#, background="snow")
	con.grid(row=2, column=0, padx = 5, pady = 5)
	canc = ttk.Button(wind, text="Cancel", command=wind.destroy)#, background="snow")
	canc.grid(row=2, column=1, padx = 5, pady = 5)

# for creating a new window for logging
def new_log_window():
	wind = Toplevel()
	wind.geometry('300x300')
	wind.configure(background = "DodgerBlue3")
	Label(wind, text="Exercise Name", background="DodgerBlue3").grid(row = 0, column = 0)
	temp = StringVar(wind)
	temp.set(tkvar.get())
	popupMenu = ttk.OptionMenu(wind, temp, temp.get(), *choices)
	popupMenu["menu"].configure(background="snow")
	Label(wind, text="Choose an exercise", background="DodgerBlue3").grid(row = 0, column = 0)
	popupMenu.grid(row = 1, column = 0)

	#dropdown for year selections
	year = {'----', '2017', '2018', '2019', '2020'}
	Label(wind, text="Year", background="DodgerBlue3").grid(row = 0, column = 1)
	yearTemp = StringVar(wind)
	yearTemp.set('----')
	yearMenu = ttk.OptionMenu(wind, yearTemp, yearTemp.get(), *sorted(year))
	yearMenu["menu"].configure(background="snow")
	yearMenu.grid(row = 1, column = 1)

	#dropdown for month selection
	month = {'--', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12'}
	Label(wind, text="Month", background="DodgerBlue3").grid(row = 0, column = 2)
	monthTemp = StringVar(wind)
	monthTemp.set('--')
	monthMenu = ttk.OptionMenu(wind, monthTemp, monthTemp.get(), *sorted(month))
	monthMenu["menu"].configure(background="snow")
	monthMenu.grid(row = 1, column = 2, padx = 2, pady = 2)

	#dropdown for day selection
	#to implement: change inputs dependent on month selection
	day = {'--', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', 
	'16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31'}
	Label(wind, text="Day", background="DodgerBlue3").grid(row = 0, column = 3)
	dayTemp = StringVar(wind)
	dayTemp.set('--')
	dayMenu = ttk.OptionMenu(wind, dayTemp, dayTemp.get(), *sorted(day))
	dayMenu["menu"].configure(background="snow")
	dayMenu.grid(row = 1, column = 3, padx = 2, pady = 2)

	Label(wind, text="Weight (lb)", background="DodgerBlue3").grid(row = 4, column = 0)
	E2 = Entry(wind)
	E2.grid(row = 5, column = 0, columnspan = 2)

	Label(wind, text="Sets", background="DodgerBlue3").grid(row = 6, column = 0)
	E3 = Entry(wind)
	E3.grid(row= 7, column = 0, columnspan= 2)

	Label(wind, text="Reps", background="DodgerBlue3").grid(row = 8, column = 0)
	E4 = Entry(wind)
	E4.grid(row= 9, column= 0, columnspan= 2)

	con = Button(wind, text="Confirm", command=wind.destroy, background="snow")
	con.grid(row=10, column=0, padx = 2, pady = 2)
	canc = Button(wind, text="Cancel", command=wind.destroy, background="snow")
	canc.grid(row=10, column=1, padx = 2, pady = 2)

# on change dropdown value
def change_dropdown(*args):
    print( tkvar.get() )


root = Tk()
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
choices = {'Bench','Squat','Deadlift'}
tkvar.set('Bench') # set the default option
 
popupMenu = ttk.OptionMenu(mainframe, tkvar, tkvar.get(), *sorted(choices))
popupMenu["menu"].configure(background="snow")
Label(mainframe, text="Choose an exercise", background="DodgerBlue3").grid(row = 0, column = 0)
popupMenu.grid(row = 1, column = 0)

B1 = ttk.Button(mainframe, text='Create new exercise', command=new_ex_window)#, background="snow")
B1.grid(row = 6, column = 0)

B2 = ttk.Button(mainframe, text='Log exercise', command=new_log_window)#, background="snow")
B2.grid(row = 4, column = 0)

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

# link function to change dropdown
tkvar.trace('w', change_dropdown)
 
root.mainloop()
 




