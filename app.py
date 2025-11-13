from tkinter import *
from task import Task
from taskList import TaskList

class TaskApp(Tk):

	def __init__(self):
		super().__init__() #initialize window
		self.title("Mood") #sets title to mood
		self.geometry("480x360")  #sets size

		#icon = PhotoImage(file='filelocation.png') #implement later
		#window.iconphoto(True,icon)

		self.tasks = TaskList([]) #setting up list data

		# -------input area (top)----------

		top = Frame(self) #creates frame widget

		top.pack(fill="x") #frame stretches all the way horizontally at the top

		Label(top, text="Task Name").grid(row = 0, column = 0) 
		#creates a label "Task Name" for top frame
		#places it at the top left

		self.name_var = StringVar() #stores text for task name

		Entry(top, textvariable = self.name_var).grid(row = 1, column = 0)
		#creates text input box inside top frame
		#uses our name_var variable to edit text
		#placed right below label

		# --------description area---------

		Label(top, text = "Description").grid(row = 0, column = 1)
		#creates a label in top with text "Description"
		#placed to the right of Task Name

		self.desc_var = StringVar()

		Entry(top, textvariable = self.desc_var).grid(row = 1, column = 1)
		#same variable creation and entry for description

		# --------column management--------

		top.columnconfigure(0, weight = 1)
		#column 0 should expand when theres more horizontal space with flexibility 1

		top.columnconfigure(1, weight = 1)

		# -----------buttons---------------

		btns = Frame(self)
		#frame for buttons

		btns.pack(fill="x")
		#place buttons frame below top frame, stretches horizontally

		Button(btns, text = "Add", command = self.add_task).pack(side = "left")
		#creates a button labeled "Add"
		#when clicked, self.add_task called
		#placed on left side of buttons frame

		Button(btns, text = "Delete", command = self.delete_selected).pack(side = "left")
		#delete button

		# --------task list---------------

		listfrm = Frame(self)
		listfrm.pack(fill = "both", expand = True)
		#list frame placed below button frame, stretched in both directions

		self.listbox = Listbox(listfrm)
		self.listbox.pack(side = "left", fill = "both", expand = True)
		#displays tasks into text rows

		scroll = Scrollbar(listfrm, orient = "vertical", command = self.listbox.yview)
		scroll.pack(side="right", fill = "y")
		self.listbox.config(yscrollcommand=scroll.set)
		#scrollbar

	def add_task(self):
		name = self.name_var.get()
		desc = self.desc_var.get()
		task = Task(name, desc)

		self.tasks.addTask(task)
		self.listbox.insert(END, str(task))

		self.name_var.set("")
		self.desc_var.set("")

	def delete_selected(self):
		selected = list(self.listbox.curselection())
		for index in reversed(selected):
			self.tasks.remove_task(index)
			self.listbox.delete(index)

if __name__ == "__main__":
	app = TaskApp()
	app.mainloop()


