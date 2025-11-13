from task import Task

class TaskList():
	def __init__(self, taskList: list):
		self.taskList = taskList

	def addTask(self, task):
		self.taskList.append(task)

	def printList(self):
		
		for task in self.taskList:
			task.printTask()

	def remove_task(self, index: int):
		if 0 <= index < len(self.taskList):
			self.taskList.pop(index)

	def __iter__(self):
		return iter(self.taskList)