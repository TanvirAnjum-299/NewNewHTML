todolist=["Make your bed","Feed the pet","Take out the trash","Wash the dishes"]
count_of_todos=len(todolist)
print("You Have",count_of_todos,"task to finish today!")
completed_count=0
while len(todolist)>0:
    current_task=todolist[0]
    answer=input("Have you finished:"+current_task+"/(yes/no):")
    if answer=="yes":
        todolist.pop(0)
        completed_count=completed_count+1
        print("Great job!Chore Completed.")
    else:
        print("Okay,finish it and check again")
    print("Tasks remaining:",len(todolist))
    print("")
print("=====ALL TASKS COMPLETE!=====")
print("Great work finishing your entire checklist today!")