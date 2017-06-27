import tkinter as tk
from tkinter import ttk
import gym_writer

def main(): 
    root = tk.Tk()
    if len(gym_writer.get_exercises()) == 0:
        gym_writer.initialize()
    root.title("Gym Log")
    app = home(root)
    root.mainloop()

class home:
    #main home page of application
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.frame.configure(background="DodgerBlue3")
        self.frame.grid(column=0,row=0, sticky='news')
        self.frame.columnconfigure(0, weight = 1)
        self.frame.rowconfigure(0, weight = 1)
        self.tkvar = tk.StringVar(master)
        self.choices = gym_writer.get_exercises()
        self.tkvar.set(sorted(self.choices)[0]) # set the default option
        self.popupMenu = ttk.OptionMenu(self.frame, self.tkvar, self.tkvar.get(), *sorted(self.choices))
        self.popupMenu["menu"].configure(background="snow")
        tk.Label(self.frame, text="Choose an exercise", background="DodgerBlue3").grid(row = 0, column = 0)
        self.popupMenu.grid(row = 1, column = 0)

        self.B1 = ttk.Button(self.frame, text='Create new exercise', command=self.new_ex_window)
        self.B1.grid(row = 6, column = 0)

        self.B2 = ttk.Button(self.frame, text='Log exercise', command=self.new_log_window)
        self.B2.grid(row = 4, column = 0)

        self.B0 = ttk.Button(self.frame, text='View log', command=self.new_view_window)
        self.B0.grid(row = 2, column = 0, pady = (10,0))

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

        self.refresh()

        # link function to change dropdown
        self.tkvar.trace('w', self.refresh)

    # on change dropdown value or logging new exercise, refreshes the values on the home window
    def refresh(self, *args):
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
        else:
            self.L1.config(text='---')
            self.L2.config(text='---')
            self.L3.config(text='---')
            self.L4.config(text='---')
            self.L5.config(text='---')
            self.L6.config(text='---')
            self.L7.config(text='---')
            self.L8.config(text='---')

    def new_log_window(self):
        return None
    def new_ex_window(self):
        return None
    def new_view_window(self):
        return None







if __name__ == '__main__':
    main()