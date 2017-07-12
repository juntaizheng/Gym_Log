import tkinter as tk
from tkinter import ttk
import gym_writer
import numpy as np
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
import matplotlib.pyplot as plt

def main():
    #main function for loading the program
    root = tk.Tk()
    if len(gym_writer.get_exercises()) == 0:
        gym_writer.initialize()
    root.title("Gym Log")
    app = Home(root)
    root.mainloop()

class Home:
    #main home page of application, combined as a controller
    def __init__(self, master):
        #function for initializing home window
        #param master: tk.Tk() instance
        self.master = master
        #setting up frame
        self.frame = tk.Frame(self.master)
        self.frame.configure(background="DodgerBlue3")
        self.frame.grid(column=0,row=0, sticky='news')
        self.frame.columnconfigure(0, weight = 1)
        self.frame.rowconfigure(0, weight = 1)
        #setting up variable to track current input
        self.tkvar = tk.StringVar(master)
        self.choices = gym_writer.get_exercises()
        self.tkvar.set(sorted(self.choices)[0]) # set the default option
        #setting up dropdown menu
        self.popupMenu = ttk.OptionMenu(self.frame, self.tkvar, self.tkvar.get(), *sorted(self.choices))
        self.popupMenu["menu"].configure(background="snow")
        tk.Label(self.frame, text="Choose an exercise", background="DodgerBlue3").grid(row = 0, column = 0)
        self.popupMenu.grid(row = 1, column = 0)

        #setting up buttons
        self.B1 = ttk.Button(self.frame, text='Create new exercise', command=self.new_ex_window)
        self.B1.grid(row = 6, column = 0)

        self.B2 = ttk.Button(self.frame, text='Log exercise', command=self.new_log_window)
        self.B2.grid(row = 4, column = 0)

        self.B0 = ttk.Button(self.frame, text='View log', command=self.new_view_window)
        self.B0.grid(row = 2, column = 0, pady = (10,0))

        #setting up labels for interesting statistics
        tk.Label(self.frame, text="Last time exercised", background="DodgerBlue3").grid(row = 0, column = 1)
        self.L1 = tk.Label(self.frame, background="DodgerBlue3")
        self.L1.grid(row = 1, column = 1)

        tk.Label(self.frame, text="Last time weight", background="DodgerBlue3").grid(row = 2, column = 1)
        self.L2 = tk.Label(self.frame, background="DodgerBlue3")
        self.L2.grid(row = 3, column = 1)

        tk.Label(self.frame, text="Last time sets", background="DodgerBlue3").grid(row = 4, column = 1)
        self.L3 = tk.Label(self.frame, background="DodgerBlue3")
        self.L3.grid(row = 5, column = 1)

        tk.Label(self.frame, text="Last time reps", background="DodgerBlue3").grid(row = 6, column = 1)
        self.L4 = tk.Label(self.frame, background="DodgerBlue3")
        self.L4.grid(row = 7, column = 1)

        tk.Label(self.frame, text="Max weight date", background="DodgerBlue3").grid(row = 0, column = 2)
        self.L5 = tk.Label(self.frame, background="DodgerBlue3")
        self.L5.grid(row = 1, column = 2)

        tk.Label(self.frame, text="Max weight", background="DodgerBlue3").grid(row = 2, column = 2)
        self.L6 = tk.Label(self.frame, background="DodgerBlue3")
        self.L6.grid(row = 3, column = 2)

        tk.Label(self.frame, text="Max weight sets", background="DodgerBlue3").grid(row = 4, column = 2)
        self.L7 = tk.Label(self.frame, background="DodgerBlue3")
        self.L7.grid(row = 5, column = 2)

        tk.Label(self.frame, text="Max weight reps", background="DodgerBlue3").grid(row = 6, column = 2)
        self.L8 = tk.Label(self.frame, background="DodgerBlue3")
        self.L8.grid(row = 7, column = 2)

        #initates values for loaded exercise
        self.refresh()

        # link function to change dropdown
        self.tkvar.trace('w', self.refresh)

    def refresh(self, *args):
        #on change dropdown value or logging new exercise, refreshes the values on the home window
        recent_query = gym_writer.table_recent(self.tkvar.get().lower().replace(" ", "_"))
        max_query = gym_writer.table_max(self.tkvar.get().lower().replace(" ", "_"))
        if recent_query is not None:
            self.L1.config(text=recent_query[0])
            self.L2.config(text=str(recent_query[1]) + ' lb')
            self.L3.config(text=recent_query[2])
            self.L4.config(text=recent_query[3])
            self.L5.config(text=max_query[0])
            self.L6.config(text=str(max_query[1]) + ' lb')
            self.L7.config(text=max_query[2])
            self.L8.config(text=max_query[3])
        #if no values have been initiated yet for the exercise
        else:
            self.L1.config(text='---')
            self.L2.config(text='---')
            self.L3.config(text='---')
            self.L4.config(text='---')
            self.L5.config(text='---')
            self.L6.config(text='---')
            self.L7.config(text='---')
            self.L8.config(text='---')

    #functions meant for creating new windows
    def new_log_window(self):
        self.newLogWindow = tk.Toplevel(self.master)
        self.app1 = Log_window(self.newLogWindow, self)
    def new_ex_window(self):
        self.newExWindow = tk.Toplevel(self.master)
        self.app2 = Ex_window(self.newExWindow, self)
    def new_view_window(self):
        self.newViewWindow = tk.Toplevel(self.master)
        self.app3 = View_window(self.newViewWindow, self)


class Log_window:
    #class for window that allows user to log exercises
    def __init__(self, master, controller):
        #function for initializing a log window
        #param master: tk.Toplevel instance based off the tk.Tk() instance
        #param controller: Home class, containing data to be used
        self.master = master
        self.controller = controller
        #setting up frame
        self.frame = tk.Frame(self.master)
        self.master.geometry('300x300')
        self.master.configure(background = "DodgerBlue3")
        #setting up widgets inculding labels and dropdown menu for exercise
        tk.Label(self.master, text="Exercise Name", background="DodgerBlue3").grid(row = 0, column = 0)
        tk.Label(self.master, text="Choose an exercise", background="DodgerBlue3").grid(row = 0, column = 0)
        self.temp = tk.StringVar(self.master)
        self.temp.set(controller.tkvar.get())
        self.popupMenu = ttk.OptionMenu(self.master, self.temp, self.temp.get(), *sorted(controller.choices))
        self.popupMenu["menu"].configure(background="snow")
        self.popupMenu.grid(row = 1, column = 0)

        #dropdown for year selections
        self.year = {'----', '2017', '2018', '2019', '2020'}
        tk.Label(self.master, text="Year", background="DodgerBlue3").grid(row = 0, column = 1)
        self.yearTemp = tk.StringVar(self.master)
        self.yearTemp.set('----')
        self.yearMenu = ttk.OptionMenu(self.master, self.yearTemp, self.yearTemp.get(), *sorted(self.year))
        self.yearMenu["menu"].configure(background="snow")
        self.yearMenu.grid(row = 1, column = 1)
        self.yearMenu.configure(width=5)
        
        #dropdown for month selection
        self.month = {'--', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12'}
        tk.Label(self.master, text="Month", background="DodgerBlue3").grid(row = 0, column = 2)
        self.monthTemp = tk.StringVar(self.master)
        self.monthTemp.set('--')
        self.monthMenu = ttk.OptionMenu(self.master, self.monthTemp, self.monthTemp.get(), *sorted(self.month))
        self.monthMenu["menu"].configure(background="snow")
        self.monthMenu.grid(row = 1, column = 2, padx = 2, pady = 2)
        self.monthMenu.configure(width=3)

        #dropdown for day selection
        self.day = {'--', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', 
        '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31'}
        tk.Label(self.frame, text="Day", background="DodgerBlue3").grid(row = 0, column = 3)
        self.dayTemp = tk.StringVar(self.master)
        self.dayTemp.set('--')
        self.dayMenu = ttk.OptionMenu(self.master, self.dayTemp, self.dayTemp.get(), *sorted(self.day))
        self.dayMenu["menu"].configure(background="snow")
        self.dayMenu.grid(row = 1, column = 3, padx = 2, pady = 2)
        self.dayMenu.configure(width=3)

        #labels and entries for inputting weight, sets and reps
        tk.Label(self.master, text="Weight (lb)", background="DodgerBlue3").grid(row = 4, column = 0)
        self.weight = tk.StringVar()
        self.E2 = tk.Entry(self.master, textvariable=self.weight)
        self.E2.grid(row = 5, column = 0, columnspan = 2) 

        tk.Label(self.master, text="Sets", background="DodgerBlue3").grid(row = 6, column = 0)
        self.sets = tk.StringVar()
        self.E3 = tk.Entry(self.master, textvariable=self.sets)
        self.E3.grid(row= 7, column = 0, columnspan= 2)

        tk.Label(self.master, text="Reps", background="DodgerBlue3").grid(row = 8, column = 0)
        self.reps = tk.StringVar()
        self.E4 = tk.Entry(self.master, textvariable=self.reps)
        self.E4.grid(row= 9, column= 0, columnspan= 2)

        #confirm and cancel buttons
        self.con = ttk.Button(self.master, text="Confirm", command=self.log, state='disabled')
        self.con.grid(row=10, column=0, padx = 2, pady = 2)
        self.canc = ttk.Button(self.master, text="Cancel", command=self.master.destroy)
        self.canc.grid(row=10, column=1, padx = 2, pady = 2)

        #tracks change in date dropdown menu to enable/disable confirm ttk.button
        self.yearTemp.trace('w',self.disable)
        self.monthTemp.trace('w', self.disable)
        self.yearTemp.trace('w', self.day_update)
        self.monthTemp.trace('w', self.day_update)
        self.dayTemp.trace('w', self.disable)

        #tracks change in weight, sets, and reps entries to enable/disable confirm ttk.button
        self.weight.trace('w', self.disable)
        self.sets.trace('w', self.disable)
        self.reps.trace('w', self.disable)

    def log(self):
        #logs the current exercise
        gym_writer.log_ex((self.yearTemp.get() + '-' + self.monthTemp.get() + '-' + self.dayTemp.get(),
            self.E2.get(), self.E3.get(), self.E4.get()), self.temp.get().lower())
        #refreshes the overall values
        self.controller.refresh()
        self.master.destroy()

    def disable(self, *args):
        #disables confirm ttk.button if a date, weight, set, or rep input is invalid
        if self.yearTemp.get() == '----' or self.monthTemp.get() == '--' or self.dayTemp.get() == '--' or not self.E2.get().isdigit() or not self.E3.get().isdigit() or not self.E4.get().isdigit():
            self.con.config(state='disabled')
        else:
            self.con.config(state='normal')

    def day_update(self, *args):
        #updates the day selection available with a selected self.month
        self.dayTemp.set('')
        self.days = set()
        self.dayMenu['menu'].delete(0, 'end')
        if self.monthTemp.get() == '02' and self.yearTemp.get().isdigit() and int(self.yearTemp.get()) % 4 == 0:
            #accounts for leap year
            self.days = {'--', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', 
            '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29'};
        elif self.monthTemp.get() == '01' or self.monthTemp.get() == '03' or self.monthTemp.get() == '05' or self.monthTemp.get() == '07' or self.monthTemp.get() == '08' or self.monthTemp.get() == '10' or self.monthTemp.get() == '12':
            #months with 31 days
            self.days = {'--', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', 
            '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31'}
        elif self.monthTemp.get() == '02':
            #non-leap year February
            self.days = {'--', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', 
            '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28'}
        else:
            #months with 30 days
            self.days = {'--', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', 
            '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30'}

        #refreshes the day dropdown menu
        self.dayMenu = ttk.OptionMenu(self.master, self.dayTemp, '--', *sorted(self.days))
        self.dayMenu["menu"].configure(background="snow")
        self.dayMenu.grid(row = 1, column = 3, padx = 2, pady = 2)
        self.dayMenu.configure(width=3)


class View_window:
    #class for view window
    def __init__(self, master, controller):
        #function for initializiing viewing window
        #param master: tk.Toplevel instance based off the tk.Tk() instance
        #param controller: Home class, containing data to be used
        self.master = master
        self.controller = controller
        #setting up frame
        self.frame = tk.Frame(self.master)
        self.master.configure(background = "DodgerBlue3")
        #setting up treeview for viewing data in a table
        self.tree = ttk.Treeview(self.master)
        self.tree.grid(sticky = 'news', rowspan=5)
        self.master.treeview = self.tree
        self.master.grid_rowconfigure(0, weight = 1)
        self.master.grid_columnconfigure(0, weight = 1)
        self.tree['columns'] = ('Weight', 'Sets', 'Reps')
        self.tree.heading("#0", text='Date', anchor='w')
        self.tree.column("#0", anchor="w")
        self.tree.heading('Weight', text='Weight (lb)')
        self.tree.column('Weight', anchor='center', width=100)
        self.tree.heading('Sets', text='Sets')
        self.tree.column('Sets', anchor='center', width=100)
        self.tree.heading('Reps', text='Reps')
        self.tree.column('Reps', anchor='center', width=100)
        #setting up scrollbar for treeview
        self.treeScroll = ttk.Scrollbar(self.master)
        self.treeScroll.configure(command=self.tree.yview)
        self.treeScroll.grid(row=0, column=1, rowspan=5, sticky = 'news',)
        self.tree.configure(yscrollcommand=self.treeScroll.set)
        #defaults to viewing most recent exercises
        for exercise in gym_writer.get_dworkouts(self.controller.tkvar.get()):
            self.master.treeview.insert('', 'end', text=exercise[0], values=(exercise[1],
                                 exercise[2], exercise[3]))
        self.order =tk.Label(self.master, text="Ordered by: \nmost recent" , background="DodgerBlue3")
        self.order.grid(row = 0, column = 2, sticky = 'news')

        #buttons for ordering the view and testing adding and removing exercises
        self.b0 = ttk.Button(self.master, text='Order by most recent', command=self.mrecent)
        self.b0.grid(row = 1, column = 2, sticky = 'news')
        self.b1 = ttk.Button(self.master, text='Order by least recent', command=self.lrecent)
        self.b1.grid(row = 2, column = 2, sticky = 'news')
        self.b2 = ttk.Button(self.master, text='Order by greatest weight', command=self.heavy)
        self.b2.grid(row = 3, column = 2, sticky = 'news')
        self.b3 = ttk.Button(self.master, text='Order by least weight', command=self.light)
        self.b3.grid(row = 4, column = 2, sticky = 'news')
        self.b4 = ttk.Button(self.master, text='test clear', command=self.test_clear)
        self.b4.grid(row = 6, column = 2, sticky = 'news')
        self.b5 = ttk.Button(self.master, text='test populate', command=self.test_populate)
        self.b5.grid(row = 7, column = 2, sticky = 'news')

        #using matplotlib to plot a graph of the data points
        self.create_figure()

    def test_clear(self):
        #test method meant to clear current table
        gym_writer.clear_table(self.controller.tkvar.get())
        self.create_figure()

        self.tree.delete(*self.tree.get_children())
        #may be unecessary below this line, test without
        for exercise in gym_writer.get_dworkouts(self.controller.tkvar.get()):
            self.master.treeview.insert('', 'end', text=exercise[0], values=(exercise[1],
                                 exercise[2], exercise[3]))
        self.order = tk.Label(self.master, text="Ordered by: \nmost recent" , background="DodgerBlue3")
        self.order.grid(row = 0, column = 2, sticky = 'news')

    def test_populate(self):
        #test method meant to populate current table
        gym_writer.populate(self.controller.tkvar.get(), 5)
        self.create_figure()

        self.tree.delete(*self.tree.get_children())
        for exercise in gym_writer.get_dworkouts(self.controller.tkvar.get()):
            self.master.treeview.insert('', 'end', text=exercise[0], values=(exercise[1],
                                 exercise[2], exercise[3]))
        self.order =tk.Label(self.master, text="Ordered by: \nmost recent" , background="DodgerBlue3")
        self.order.grid(row = 0, column = 2, sticky = 'news')


    def mrecent(self):
        #for ordering table by most recent workouts
        self.tree.delete(*self.tree.get_children())
        for exercise in gym_writer.get_dworkouts(self.controller.tkvar.get()):
           self.master.treeview.insert('', 'end', text=exercise[0], values=(exercise[1],
                            exercise[2], exercise[3]))
        self.order.configure(text = "Ordered by: \nmost recent")

    def lrecent(self):
        #for ordering table by least recent workouts
        self.tree.delete(*self.tree.get_children())
        for exercise in gym_writer.get_dworkouts(self.controller.tkvar.get()):
            self.master.treeview.insert('', 0, text=exercise[0], values=(exercise[1],
                             exercise[2], exercise[3]))
        self.order.configure(text = "Ordered by: \nleast recent")

    def heavy(self):
       #for ordering table by greatest weight
        self.tree.delete(*self.tree.get_children())
        for exercise in gym_writer.get_wworkouts(self.controller.tkvar.get()):
           self.master.treeview.insert('', 'end', text=exercise[0], values=(exercise[1],
                             exercise[2], exercise[3]))
        self.order.configure(text = "Ordered by: \nhighest weight")

    def light(self):
        #for ordering table by least weight
        self.tree.delete(*self.tree.get_children())
        for exercise in gym_writer.get_wworkouts(self.controller.tkvar.get()):
            self.master.treeview.insert('', 0, text=exercise[0], values=(exercise[1],
                             exercise[2], exercise[3]))
        self.order.configure(text = "Ordered by: \nlowest weight")

    def create_figure(self):
        #todo: create y axis ticks for interesting points corresponding with the x axis
        #for creating the matplotlib figure graph
        f = Figure(figsize=(5, 4), dpi=100)
        a = f.add_subplot(111)
        t = np.arange(0.0, len(gym_writer.get_wworkouts(self.controller.tkvar.get())))
        s = []
        labels = []
        temp = []
        counter = 0
        #two counters keeping track of min and max weights on graph
        max = (0, 0)
        min = (999999, 0)
        for exercise in gym_writer.get_dworkouts(self.controller.tkvar.get()):
            s.insert(0, exercise[1])
            if exercise[1] > max[0]:
                labels.insert(0, exercise[0])
                labels[len(labels)-1-max[1]] = ''
                max = (exercise[1], counter)
            elif exercise[1] < min[0]:
                labels.insert(0, exercise[0])
                labels[len(labels)-1-min[1]] = ''
                min = (exercise[1], counter)
            else:
                labels.insert(0, '')
            temp.append(counter)
            counter += 1
        
        a.plot(t, np.array(s))
        a.set_xticks(temp)
        a.set_xticklabels(labels)#, rotation='vertical')

        #a tk.DrawingArea
        self.canvas = FigureCanvasTkAgg(f, master=self.master)
        self.canvas.show()
        self.canvas.get_tk_widget().grid(row=5,column=0)
        #create new frame since toolbar automatically packs itself instead of using a grid
        self.toolbarFrame = tk.Frame(self.master)
        self.toolbarFrame.grid(row=6,column=0, sticky='news')
        toolbar = NavigationToolbar2TkAgg(self.canvas, self.toolbarFrame)
        toolbar.update()
        toolbar.pack(side=tk.LEFT, expand=1)
        self.canvas._tkcanvas.grid(row=5,column=0)
    
        
class Ex_window:
    #class for creating a new window for creating a new exercise
    def __init__(self, master, controller):
        #function for initializing an exercise creation window
        #param master: tk.Toplevel instance based off the tk.Tk() instance
        #param controller: Home class, containing data to be used
        self.master = master
        self.controller = controller
        self.frame = tk.Frame(self.master)
        self.master.configure(background = "DodgerBlue3")
        tk.Label(self.master, text="Exercise Name", background="DodgerBlue3").grid(row = 0, column = 0, sticky='news', columnspan = 1, padx = 10, pady = 10)
        self.ex = tk.StringVar()
        self.E1 = ttk.Entry(self.master, textvariable=self.ex)
        self.E1.grid(row=1, column=0, columnspan=2)
        self.exercises = gym_writer.getTables()

        #setting up confirm (disabled by default) and cancel buttons
        self.con = ttk.Button(self.master, text="Confirm", command=self.create_ex, state='disabled')
        self.con.grid(row=2, column=0, padx = 10, pady = 10)
        self.canc = ttk.Button(self.master, text="Cancel", command=self.master.destroy)
        self.canc.grid(row=2, column=1, padx = 10, pady = 10)

        #set up confirm button to be traced with changes to the exercise entry
        self.ex.trace('w', self.disable)

    def disable(self, *args):  
    #disables confirm button if entry is empty or whitespace
        if self.E1.get() == '' or self.E1.get().isspace() or self.E1.get().isdigit():
            #checks for whitespace only, empty, or a number (breaks sqlite)
            self.con.config(state='disabled')
        else:
            self.con.config(state='normal')

    def create_ex(self):
    #function for creating a new exercise; rejection if exercise already exists
        if self.E1.get().lower().replace(" ", "_") in self.exercises:
            #creates popup for invalid, duplicated exercise
            pop = tk.Toplevel()
            pop.configure(background = "DodgerBlue3")
            tk.Label(pop, text="Error! Exercise already exists.", background="DodgerBlue3").grid(row = 0, column = 0, sticky='news', columnspan = 2, padx = 10, pady = 10)
            ret = ttk.Button(pop, text="OK", command=pop.destroy)
            ret.grid(row = 1, column = 0, sticky='news', columnspan = 2, padx = 10, pady = 10)
        else:
            gym_writer.create_exercise(self.E1.get())
            #refreshing of home page exercises to include new exercise
            self.controller.tkvar.set(self.ex.get())
            self.controller.popupMenu['menu'].delete(0, 'end')
            self.controller.choices = gym_writer.get_exercises()
            self.controller.popupMenu = ttk.OptionMenu(self.controller.frame, self.controller.tkvar, self.controller.tkvar.get(), *sorted(self.controller.choices))
            self.controller.popupMenu.grid(row = 1, column = 0)
            self.controller.popupMenu["menu"].configure(background="snow")
            self.controller.refresh()
            self.master.destroy()

        


#run the program!
if __name__ == '__main__':
    main()