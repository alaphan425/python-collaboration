goAgain = True
allTasks = []
completedTasks = []

while goAgain == True:
        print("Would you like to view all tasks, add tasks, mark tasks as completed, or delete tasks?")
        yesorno = input("y/n: ")
        if yesorno == "n":
            goAgain = False
            break
        elif yesorno == "y":
            actionType = input("Valid responses: view/add/mark/delete\n")
            if actionType == "add":
                newTask = input("What is the task you would like to add?")
                allTasks.append(newTask)
            elif actionType == "mark":
                if len(allTasks) == 0:
                    print("There are no tasks to mark as completed.")
                else:
                    print(allTasks)
                    n = int(input("Which number task in the list would you like to mark as completed\n"))
                    completedTasks.append(allTasks[n-1])
            elif actionType == "delete":
                if len (allTasks) == 0:
                    print("There are no tasks to delete.")
                else:
                    print(allTasks)
                    k = int(input("Which number task in the list would you like to delete?"))
                    deletedTask = allTasks[k-1]
                    if deletedTask in completedTasks:
                        completedTasks.remove(deletedTask)
                        allTasks.pop(k-1)
            elif actionType == "view" and len(allTasks) == 0:
                print("There are currently no tasks to view")
            elif actionType == "view" and len(allTasks) != 0:
                [allTasks]
            else:
                print("Please enter a valid response")
        else:
            print("Please enter a valid response.")
                