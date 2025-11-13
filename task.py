class Task():


	def __init__(self, taskName: str, taskDesc: str):
		self.taskName = taskName 
		self.taskDesc = taskDesc 

	def updateTaskName(self, newTaskName: str):
		self.taskName = newTaskName

	def updateTaskDesc(self, newTaskDesc):
		self.taskDesc = str(newTaskDesc)


	def printTask(self):
		print(self.taskName + ": " + self.taskDesc)

	def __str__(self):
		return self.taskName + ": " + self.taskDesc