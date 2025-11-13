from task import Task
from taskList import TaskList

def main():

	task1 = Task("Shopping", "Milk, Eggs, Chicken")
	task2 = Task("Laundry", "Whites, Colors")


	taskList = TaskList([])
	taskList.printList()
	taskList.addTask(task1)
	taskList.addTask(task2)
	taskList.printList()

if __name__ == "__main__":
	main()




