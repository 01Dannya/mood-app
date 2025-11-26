# class Task():


# 	def __init__(self, taskName: str, taskDesc: str):
# 		self.taskName = taskName 
# 		self.taskDesc = taskDesc 

# 	def updateTaskName(self, newTaskName: str):
# 		self.taskName = newTaskName

# 	def updateTaskDesc(self, newTaskDesc):
# 		self.taskDesc = str(newTaskDesc)


# 	def printTask(self):
# 		print(self.taskName + ": " + self.taskDesc)

# 	def __str__(self):

# 		return self.taskName + ": " + self.taskDesc

class Task():

    def __init__(self, taskName: str, taskDesc: str, priority: str = "Medium"):
        self.taskName = taskName 
        self.taskDesc = taskDesc 
        self.priority = priority  # Added priority here

    def updateTaskName(self, newTaskName: str):
        self.taskName = newTaskName

    def updateTaskDesc(self, newTaskDesc):
        self.taskDesc = str(newTaskDesc)
        
    def updatePriority(self, newPriority: str): #function to set priority
        self.priority = newPriority


    #Changed formatting for priority
    def printTask(self):
        print(f"{self.taskName}: {self.taskDesc} [{self.priority}]")

    def __str__(self):
        return f"{self.taskName}: {self.taskDesc} [{self.priority}]"
    	
