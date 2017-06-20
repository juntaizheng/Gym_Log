from tkinter import *
import tkinter
from tkinter import ttk
import gym_writer

root = Tk()
root.title("Gym Log")
#root.grid_propagate(False) 
 
# Add a grid
mainframe = Frame(root)
mainframe.configure(background="DodgerBlue3")
mainframe.grid(column=0,row=0, sticky=(N,W,E,S) )
mainframe.columnconfigure(0, weight = 1)
mainframe.rowconfigure(0, weight = 1)

#initialize a database with bench, deadlift, and squats if not created before
gym_writer.initialize()
 
# Create a Tkinter variable
tkvar = StringVar(root)

# on change dropdown value or logging new exercise, refreshes the values on the home window
def refresh(*args):
    recent_query = gym_writer.table_recent(tkvar.get().lower().replace(" ", "_"))
    max_query = gym_writer.table_max(tkvar.get().lower().replace(" ", "_"))
    if recent_query is not None:
        L1.config(text=recent_query[0])
        L2.config(text=str(recent_query[1]) + ' lb')
        L3.config(text=recent_query[2])
        L4.config(text=recent_query[3])
        L5.config(text=max_query[0])
        L6.config(text=str(max_query[1]) + ' lb')
        L7.config(text=max_query[2])
        L8.config(text=max_query[3])
    else:
        L1.config(text='---')
        L2.config(text='---')
        L3.config(text='---')
        L4.config(text='---')
        L5.config(text='---')
        L6.config(text='---')
        L7.config(text='---')
        L8.config(text='---')

dayMenu = ""
# for creating a new window for logging
def new_log_window():
    wind = Toplevel()
    wind.geometry('300x300')
    wind.configure(background = "DodgerBlue3")
    Label(wind, text="Exercise Name", background="DodgerBlue3").grid(row = 0, column = 0)
    temp = StringVar(wind)
    temp.set(tkvar.get())
    popupMenu = ttk.OptionMenu(wind, temp, temp.get(), *sorted(choices))
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
    yearMenu.configure(width=5)
    
    #dropdown for month selection
    month = {'--', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12'}
    Label(wind, text="Month", background="DodgerBlue3").grid(row = 0, column = 2)
    monthTemp = StringVar(wind)
    monthTemp.set('--')
    monthMenu = ttk.OptionMenu(wind, monthTemp, monthTemp.get(), *sorted(month))
    monthMenu["menu"].configure(background="snow")
    monthMenu.grid(row = 1, column = 2, padx = 2, pady = 2)
    monthMenu.configure(width=3)

    #dropdown for day selection
    day = {'--', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', 
    '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31'}
    Label(wind, text="Day", background="DodgerBlue3").grid(row = 0, column = 3)
    dayTemp = StringVar(wind)
    dayTemp.set('--')
    global dayMenu
    dayMenu = ttk.OptionMenu(wind, dayTemp, dayTemp.get(), *sorted(day))
    dayMenu["menu"].configure(background="snow")
    dayMenu.grid(row = 1, column = 3, padx = 2, pady = 2)
    dayMenu.configure(width=3)

    Label(wind, text="Weight (lb)", background="DodgerBlue3").grid(row = 4, column = 0)
    weight = StringVar()
    E2 = Entry(wind, textvariable=weight)
    E2.grid(row = 5, column = 0, columnspan = 2) 

    Label(wind, text="Sets", background="DodgerBlue3").grid(row = 6, column = 0)
    sets = StringVar()
    E3 = Entry(wind, textvariable=sets)
    E3.grid(row= 7, column = 0, columnspan= 2)

    Label(wind, text="Reps", background="DodgerBlue3").grid(row = 8, column = 0)
    reps = StringVar()
    E4 = Entry(wind, textvariable=reps)
    E4.grid(row= 9, column= 0, columnspan= 2)

    def log():
        #logs the current exercise
        gym_writer.log_ex((yearTemp.get() + '-' + monthTemp.get() + '-' + dayTemp.get(),
            E2.get(), E3.get(), E4.get()), temp.get().lower())
        #refreshes the overall values if needed
        refresh()
        wind.destroy()

    con = Button(wind, text="Confirm", command=log, background="snow", state='disabled')
    con.grid(row=10, column=0, padx = 2, pady = 2)
    canc = Button(wind, text="Cancel", command=wind.destroy, background="snow")
    canc.grid(row=10, column=1, padx = 2, pady = 2)

    def disable(*args):
        #disables confirm button if a date, weight, set, or rep input is invalid
        if yearTemp.get() == '----' or monthTemp.get() == '--' or dayTemp.get() == '--' or not E2.get().isdigit() or not E3.get().isdigit() or not E4.get().isdigit():
            con.config(state='disabled')
        else:
            con.config(state='normal')

    def day_update(*args):
        #updates the day selection available with a selected month
        global dayMenu
        dayTemp.set('')
        days = set()
        dayMenu['menu'].delete(0, 'end')
        if monthTemp.get() == '02' and yearTemp.get().isdigit() and int(yearTemp.get()) % 4 == 0:
            #leap year
            days = {'--', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', 
            '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29'};
        elif monthTemp.get() == '01' or monthTemp.get() == '03' or monthTemp.get() == '05' or monthTemp.get() == '07' or monthTemp.get() == '08' or monthTemp.get() == '10' or monthTemp.get() == '12':
            days = {'--', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', 
            '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31'}
        elif monthTemp.get() == '02':
            days = {'--', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', 
            '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28'}
        else:
            days = {'--', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', 
            '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30'}

        dayMenu = ttk.OptionMenu(wind, dayTemp, '--', *sorted(days))

        dayMenu["menu"].configure(background="snow")
        dayMenu.grid(row = 1, column = 3, padx = 2, pady = 2)
        dayMenu.configure(width=3)

    #tracks change in date dropdown menu to enable/disable confirm button
    yearTemp.trace('w', disable)
    monthTemp.trace('w', disable)
    yearTemp.trace('w', day_update)
    monthTemp.trace('w', day_update)
    dayTemp.trace('w', disable)

    #tracks change in weight, sets, and reps entries to enable/disable confirm button
    weight.trace('w', disable)
    sets.trace('w', disable)
    reps.trace('w', disable)

# for creating a new window for new exercise
#todo: update home dropdown page once exercise is logged
def new_ex_window():
    wind = Toplevel()
    wind.geometry('150x100')
    wind.configure(background = "DodgerBlue3")
    Label(wind, text="Exercise Name", background="DodgerBlue3").grid(row = 0, column = 0, sticky=W+E+N+S, columnspan = 1)
    ex = StringVar()
    E1 = ttk.Entry(wind, textvariable=ex)
    E1.grid(row=1, column=0, columnspan=2)
    def create_ex():
        #function for creating a new exercise; rejection if exercise already exists
        if gym_writer.create_exercise(E1.get()):
            wind.destroy()
        else:
            pop = Toplevel()
            pop.geometry('150x100')
            pop.configure(background = "DodgerBlue3")
            Label(pop, text="Error! Exercise already exists.", background="DodgerBlue3").grid(row = 0, column = 0, sticky=W+E+N+S, columnspan = 2)
            ret = ttk.Button(pop, text="OK", command=pop.destroy)#, background="snow")
            ret.grid(row = 1, column = 0, sticky=W+E+N+S, columnspan = 2)
    con = ttk.Button(wind, text="Confirm", command=create_ex, state='disabled')#, background="snow")
    con.grid(row=2, column=0, padx = 5, pady = 5)
    canc = ttk.Button(wind, text="Cancel", command=wind.destroy)#, background="snow")
    canc.grid(row=2, column=1, padx = 5, pady = 5)

    def disable(*args):
        #disables confirm button if entry is empty or whitespace
        if E1.get() == '' or E1.get().isspace():
            con.config(state='disabled')
        else:
            con.config(state='normal')

    ex.trace('w', disable)


# Dictionary with options
choices = gym_writer.get_exercises()
tkvar.set(sorted(choices)[0]) # set the default option
 
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
tkvar.trace('w', refresh)


 
root.mainloop()
 




