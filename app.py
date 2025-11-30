# from tkinter import *
# from task import Task
# from taskList import TaskList

# class TaskApp(Tk):

# 	def __init__(self):
# 		super().__init__() #initialize window
# 		self.title("Mood") #sets title to mood
# 		self.geometry("480x360")  #sets size

# 		#icon = PhotoImage(file='filelocation.png') #implement later
# 		#window.iconphoto(True,icon)

# 		self.tasks = TaskList([]) #setting up list data

# 		# -------input area (top)----------

# 		top = Frame(self) #creates frame widget

# 		top.pack(fill="x") #frame stretches all the way horizontally at the top

# 		Label(top, text="Task Name").grid(row = 0, column = 0) 
# 		#creates a label "Task Name" for top frame
# 		#places it at the top left

# 		self.name_var = StringVar() #stores text for task name

# 		Entry(top, textvariable = self.name_var).grid(row = 1, column = 0)
# 		#creates text input box inside top frame
# 		#uses our name_var variable to edit text
# 		#placed right below label

# 		# --------description area---------

# 		Label(top, text = "Description").grid(row = 0, column = 1)
# 		#creates a label in top with text "Description"
# 		#placed to the right of Task Name

# 		self.desc_var = StringVar()

# 		Entry(top, textvariable = self.desc_var).grid(row = 1, column = 1)
# 		#same variable creation and entry for description

# 		# --------column management--------

# 		top.columnconfigure(0, weight = 1)
# 		#column 0 should expand when theres more horizontal space with flexibility 1

# 		top.columnconfigure(1, weight = 1)

# 		# -----------buttons---------------

# 		btns = Frame(self)
# 		#frame for buttons

# 		btns.pack(fill="x")
# 		#place buttons frame below top frame, stretches horizontally

# 		Button(btns, text = "Add", command = self.add_task).pack(side = "left")
# 		#creates a button labeled "Add"
# 		#when clicked, self.add_task called
# 		#placed on left side of buttons frame

# 		Button(btns, text = "Delete", command = self.delete_selected).pack(side = "left")
# 		#delete button

# 		# --------task list---------------

# 		listfrm = Frame(self)
# 		listfrm.pack(fill = "both", expand = True)
# 		#list frame placed below button frame, stretched in both directions

# 		self.listbox = Listbox(listfrm)
# 		self.listbox.pack(side = "left", fill = "both", expand = True)
# 		#displays tasks into text rows

# 		scroll = Scrollbar(listfrm, orient = "vertical", command = self.listbox.yview)
# 		scroll.pack(side="right", fill = "y")
# 		self.listbox.config(yscrollcommand=scroll.set)
# 		#scrollbar

# 	def add_task(self):
# 		name = self.name_var.get()
# 		desc = self.desc_var.get()
# 		task = Task(name, desc)

# 		self.tasks.addTask(task)
# 		self.listbox.insert(END, str(task))

# 		self.name_var.set("")
# 		self.desc_var.set("")

# 	def delete_selected(self):
# 		selected = list(self.listbox.curselection())
# 		for index in reversed(selected):
# 			self.tasks.remove_task(index)
# 			self.listbox.delete(index)

# if __name__ == "__main__":
# 	app = TaskApp()
# 	app.mainloop()

from tkinter import *
from task import Task
from taskList import TaskList

class TaskApp(Tk):



    def __init__(self):
        super().__init__() #initialize window
        self.title("Mood - Task Manager") #sets title to mood
        self.geometry("520x450")  #sets size
    


        
        # Mood settings for organization
        self.moods = {
            "productive": {
                "priority_order": ["High", "Medium", "Low"],
                "message": "Let's tackle important tasks first!",
                "suggestions": ["Break big tasks into smaller steps", "Time block your schedule", "Take short breaks between tasks"]
            },
            "neutral": {
                "priority_order": ["Medium", "High", "Low"],
                "message": "Balance is key.",
                "suggestions": ["Mix urgent and easy tasks", "Stay hydrated", "Check your progress periodically"]
            },
            "lazy": {
                "priority_order": ["Low", "Medium", "High"],
                "message": "Be kind to yourself. Start with easy wins.",
                "suggestions": ["Choose 1-2 simple tasks to start", "Use the Pomodoro technique", "Reward yourself after completing tasks"]
            }
        }
        
        self.priority_colors = {
            "High": "#ff6b6b",    # Red
            "Medium": "#ffd93d",  # Yellow
            "Low": "#6bcf7f"      # Green
        }

        self.tasks = TaskList([]) #setting up list data
        self.current_mood = "neutral"

        # ======= MOOD SELECTION SECTION =======
        mood_frame = Frame(self, bg='#f0f8ff', relief='raised', bd=1)
        mood_frame.pack(fill="x", padx=10, pady=10)
        
        Label(mood_frame, text="How are you feeling today? :)", 
              font=('Arial', 12, 'bold'), bg='#f0f8ff').pack(pady=5)
        
        mood_btn_frame = Frame(mood_frame, bg='#f0f8ff')
        mood_btn_frame.pack(pady=5)
        
        # Mood buttons
        self.mood_var = StringVar(value="neutral")
        
        productive_btn = Radiobutton(mood_btn_frame, text="Productive 😀", 
                                   variable=self.mood_var, value="productive",
                                   command=self.update_mood, bg='#f0f8ff')
        productive_btn.pack(side="left", padx=10)
        
        neutral_btn = Radiobutton(mood_btn_frame, text="Neutral 😐", 
                                variable=self.mood_var, value="neutral",
                                command=self.update_mood, bg='#f0f8ff')
        neutral_btn.pack(side="left", padx=10)
        
        lazy_btn = Radiobutton(mood_btn_frame, text="Lazy 😓", 
                             variable=self.mood_var, value="lazy",
                             command=self.update_mood, bg='#f0f8ff')
        lazy_btn.pack(side="left", padx=10)
        
        # Mood message display
        self.mood_label = Label(mood_frame, text="Balance is key.", 
                               font=('Arial', 10, 'italic'), bg='#f0f8ff', wraplength=400)
        self.mood_label.pack(pady=5)

        # timer:
        self.timer_running = False
        self.is_work_time = True
        self.time_remaining = 25 * 60  
        self.work_duration = 25 * 60   
        self.break_duration = 5 * 60   

        timer_frame = Frame(self, bg='#e8f4fd', relief='raised', bd=2)
        timer_frame.pack(fill="x", padx=10, pady=10)

        Label(timer_frame, text="⏰ Focus Timer", 
              font=('Arial', 14, 'bold'), bg='#e8f4fd').pack(pady=5)

        # Timer display
        self.timer_label = Label(timer_frame, text="25:00", 
                                font=('Arial', 24, 'bold'), bg='#e8f4fd', fg='#2c3e50')
        self.timer_label.pack(pady=5)

        # Timer controls frame
        timer_controls = Frame(timer_frame, bg='#e8f4fd')
        timer_controls.pack(pady=5)

        self.timer_btn = Button(timer_controls, text="Start Focus", 
                               command=self.toggle_timer, bg='#27ae60', fg='black',
                               font=('Arial', 10, 'bold'))
        self.timer_btn.pack(side="left", padx=5)

        Button(timer_controls, text="Reset", 
               command=self.reset_timer, bg='#95a5a6', fg='black').pack(side="left", padx=5)

        
        time_settings = Frame(timer_frame, bg='#e8f4fd')
        time_settings.pack(pady=10)

        
        work_frame = Frame(time_settings, bg='#e8f4fd')
        work_frame.pack(side="left", padx=20)
        Label(work_frame, text="Work Time (min):", bg='#e8f4fd').pack()
        self.work_var = StringVar(value="25")
        Spinbox(work_frame, from_=5, to=120, increment=5, width=5,
                textvariable=self.work_var, command=self.update_work_time).pack()

        # Break time setting  
        break_frame = Frame(time_settings, bg='#e8f4fd')
        break_frame.pack(side="left", padx=20)
        Label(break_frame, text="Break Time (min):", bg='#e8f4fd').pack()
        self.break_var = StringVar(value="5")
        Spinbox(break_frame, from_=1, to=30, increment=1, width=5,
                textvariable=self.break_var, command=self.update_break_time).pack()

        # Timer mode indicator
        self.mode_label = Label(timer_frame, text="Focus Time 🎯", 
                               font=('Arial', 10, 'bold'), bg='#e8f4fd', fg='#27ae60')
        self.mode_label.pack(pady=5)
        # ======= TIMER SECTION ======= (ADD ENDING HERE)

        # -------input area (top)---------- (YOUR EXISTING CODE CONTINUES)
        top = Frame(self)





        # -------input area (top)----------

        top = Frame(self) #creates frame widget

        top.pack(fill="x", padx=10, pady=10) #frame stretches all the way horizontally at the top

        Label(top, text="Task Name").grid(row = 0, column = 0, sticky="w") 
        #creates a label "Task Name" for top frame
        #places it at the top left

        self.name_entry = Entry(top, width=20)
        #creates text input box inside top frame
        self.name_entry.grid(row = 1, column = 0, sticky="ew", padx=(0,5))
        #placed right below label
        self.name_entry.bind("<Return>", lambda e: self.add_task())

        # --------description area---------

        Label(top, text = "Description").grid(row = 0, column = 1, sticky="w")
        #creates a label in top with text "Description"
        #placed to the right of Task Name

        self.desc_entry = Entry(top, width=25)
        #same variable creation and entry for description
        self.desc_entry.grid(row = 1, column = 1, sticky="ew", padx=5)
        self.desc_entry.bind("<Return>", lambda e: self.add_task())

        # --------priority selection---------
        Label(top, text="Priority").grid(row=0, column=2, sticky="w")
        self.priority_var = StringVar(value="Medium")
        priority_options = ["High", "Medium", "Low"]
        self.priority_menu = OptionMenu(top, self.priority_var, *priority_options)
        self.priority_menu.grid(row=1, column=2, sticky="ew", padx=(5,0))

        # --------column management--------

        top.columnconfigure(0, weight = 1)
        #column 0 should expand when theres more horizontal space with flexibility 1

        top.columnconfigure(1, weight = 1)
        top.columnconfigure(2, weight = 1)

        # -----------buttons---------------

        btns = Frame(self)
        #frame for buttons

        btns.pack(fill="x", padx=10, pady=5)
        #place buttons frame below top frame, stretches horizontally

        Button(btns, text = "Add Task", command = self.add_task, bg='#4CAF50', fg='black').pack(side = "left", padx=5)
        #creates a button labeled "Add"
        #when clicked, self.add_task called
        #placed on left side of buttons frame

        Button(btns, text = "Delete Selected", command = self.delete_selected, bg='#f44336', fg='black').pack(side = "left", padx=5)
        #delete button

        Button(btns, text="Organize by Mood", command=self.organize_by_mood,
               bg='#2196F3', fg='black').pack(side="left", padx=5)
        

        Button(btns, text="Start Timer", command=self.toggle_timer,
       bg='#9b59b6', fg='black').pack(side="left", padx=5)

        # --------task list---------------

        listfrm = Frame(self)
        listfrm.pack(fill = "both", expand = True, padx=10, pady=5)
        #list frame placed below button frame, stretched in both directions

        self.listbox = Listbox(listfrm, font=('Arial', 11), selectmode=SINGLE)
        self.listbox.pack(side = "left", fill = "both", expand = True)
        #displays tasks into text rows

        scroll = Scrollbar(listfrm, orient = "vertical", command = self.listbox.yview)
        scroll.pack(side="right", fill = "y")
        self.listbox.config(yscrollcommand=scroll.set)
        #scrollbar
        
        self.task_count = Label(self, text="0 tasks")
        self.task_count.pack(side="bottom", pady=5)
        
        self.suggestion_label = Label(self, text="", font=('Arial', 9), fg='#666', wraplength=500)
        self.suggestion_label.pack(side="bottom", pady=2)

    def update_mood(self):
        """Update the interface based on selected mood"""
        self.current_mood = self.mood_var.get()
        mood_info = self.moods[self.current_mood]
        
        self.mood_label.config(text=mood_info["message"])
        
        import random
        suggestion = random.choice(mood_info["suggestions"])
        self.suggestion_label.config(text=f"💡 Tip: {suggestion}")

    def add_task(self, event=None):
        name = self.name_entry.get().strip()
        desc = self.desc_entry.get().strip()
        priority = self.priority_var.get() 
        
        if not name:
            return
            
        task = Task(name, desc, priority)
        self.tasks.addTask(task)
        
        self.listbox.insert(END, str(task))
        index = self.listbox.size() - 1
        self.listbox.itemconfig(index, {'bg': self.priority_colors[priority]})
        
        self.name_entry.delete(0, END)
        self.desc_entry.delete(0, END)
        self.name_entry.focus()
        self.update_counter()

    def organize_by_mood(self):
        """Reorganize tasks based on current mood without changing priorities"""
        if not self.tasks.taskList:
            return
            
        # Clear the listbox
        self.listbox.delete(0, END)
        
        # Sort tasks based on current mood's priority order
        mood_info = self.moods[self.current_mood]
        priority_order = mood_info["priority_order"]
        
        sorted_tasks = sorted(self.tasks.taskList, 
                            key=lambda task: (
                                priority_order.index(task.priority), 
                                task.taskName.lower() 
                            ))
        
        self.tasks.taskList = sorted_tasks
        for task in sorted_tasks:
            self.listbox.insert(END, str(task))
            index = self.listbox.size() - 1
            self.listbox.itemconfig(index, {'bg': self.priority_colors[task.priority]})
        
        self.update_counter()
        
        mood_name = self.current_mood.capitalize()
        self.suggestion_label.config(text=f"✅ Tasks organized for {mood_name} mode!")

    def delete_selected(self):
        selected = list(self.listbox.curselection())
        for index in reversed(selected):
            if 0 <= index < len(self.tasks.taskList):
                self.tasks.remove_task(index)
                self.listbox.delete(index)
        self.update_counter()

    def update_counter(self):
        count = len(self.tasks.taskList)
        self.task_count.config(text=f"{count} task{'s' if count != 1 else ''}")
    

    def toggle_timer(self):
        """Start or pause the timer"""
        if not self.timer_running:
            self.start_timer()
        else:
            self.pause_timer()

    def start_timer(self):
        """Start the timer"""
        self.timer_running = True
        self.timer_btn.config(text="Pause", bg='#e74c3c')
        self.update_timer()

    def pause_timer(self):
        """Pause the timer"""
        self.timer_running = False
        self.timer_btn.config(text="Resume", bg='#3498db')

    def reset_timer(self):
        """Reset timer to current duration"""
        self.timer_running = False
        if self.is_work_time:
            self.time_remaining = self.work_duration
            self.mode_label.config(text="Focus Time 🎯", fg='#27ae60')
        else:
            self.time_remaining = self.break_duration  
            self.mode_label.config(text="Break Time ☕", fg='#e67e22')
        
        self.timer_btn.config(text="Start Focus", bg='#27ae60')
        self.update_timer_display()

    def update_timer(self):
        """Update timer countdown"""
        if self.timer_running:
            if self.time_remaining > 0:
                self.time_remaining -= 1
                self.update_timer_display()
                self.after(1000, self.update_timer)  # Schedule next update in 1 second
            else:
                self.timer_complete()

    def update_timer_display(self):
        """Update the timer display label"""
        minutes = self.time_remaining // 60
        seconds = self.time_remaining % 60
        self.timer_label.config(text=f"{minutes:02d}:{seconds:02d}")

    def timer_complete(self):
        """Handle timer completion"""
        self.timer_running = False
        
        if self.is_work_time:
            # switch to break time
            self.is_work_time = False
            self.time_remaining = self.break_duration
            self.mode_label.config(text="Break Time ☕", fg='#e67e22')
            self.show_timer_alert("🎉 Focus Session Complete!", 
                                "Time for a break!\n\nTake a moment to:\n• Stretch\n• Drink water\n• Rest your eyes")
        else:
            # Switch to work time  
            self.is_work_time = True
            self.time_remaining = self.work_duration
            self.mode_label.config(text="Focus Time 🎯", fg='#27ae60')
            self.show_timer_alert("⏰ Break Time Over!", 
                                "Ready to focus again?\n\nLet's get back to work!")
        
        self.timer_btn.config(text="Start Focus", bg='#27ae60')
        self.update_timer_display()

    def show_timer_alert(self, title, message):
        """Show alert when timer completes"""
        alert_win = Toplevel(self)
        alert_win.title(title)
        alert_win.geometry("300x200")
        alert_win.attributes('-topmost', True)
        
        Label(alert_win, text=title, font=('Arial', 14, 'bold')).pack(pady=20)
        Label(alert_win, text=message, font=('Arial', 11), justify='left').pack(pady=10)
        
        Button(alert_win, text="OK", command=alert_win.destroy,
            bg='#3498db', fg='black', font=('Arial', 11)).pack(pady=10)

    def update_work_time(self):
        """Update work duration"""
        self.work_duration = int(self.work_var.get()) * 60
        if self.is_work_time and not self.timer_running:
            self.time_remaining = self.work_duration
            self.update_timer_display()

    def update_break_time(self):
        """Update break duration"""  
        self.break_duration = int(self.break_var.get()) * 60
        if not self.is_work_time and not self.timer_running:
            self.time_remaining = self.break_duration
            self.update_timer_display()




if __name__ == "__main__":
    app = TaskApp()
    app.mainloop()


