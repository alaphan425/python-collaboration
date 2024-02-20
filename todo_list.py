goAgain = True
allTasks = []
completedTasks = []

while goAgain == True:
    print("Would you like to make any changes to your tasks?")
    actionGo = ("y/n\n")
    if actionGo == "n":
        goAgain = False
        break
    else:
        print("Would you like to add tasks, mark tasks as completed, or delete tasks?")
        actionType = input("add/mark/delete\n")
        if actionType == "add":
            newTask = input("What is the task you would like to add?")
            allTasks.append(newTask)