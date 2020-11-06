import PySimpleGUI as sg

sg.theme("darkgreen1")


def add_task(values):
    task = values['taskname']
    todolist.append(task)
    window.FindElement('taskname').Update(value="")
    window.FindElement('todolist').Update(values=todolist)
    window.FindElement('add_save').Update('Add')

def edit_tasks(values):
    edit_val = values['todolist'][0]
    window.FindElement('taskname').Update(value=edit_val)
    todolist.remove(edit_val)
    window.FindElement('add_save').Update('Save')

def edit_fav_tasks(values):
    edit_fav_val = values['todolist1'][0]
    window.FindElement('taskname').Update(value=edit_fav_val)
    todolist1.remove(edit_fav_val)
    window.FindElement('add_save').Update('save')
    
def delete_tasks(values):
    delete_val = values['todolist'][0]
    todolist.remove(delete_val)
    window.FindElement('todolist').Update(values=todolist)

def delete_fav_tasks(values):
    delete_fav_val = values['todolist1'][0]
    todolist1.remove(delete_fav_val)
    window.FindElement('todolist1').Update(values=todolist1)
    

def favourite_tasks(values):
     fav_task = values['todolist'][0]
     todolist1.append(fav_task)
     window.FindElement('todolist').Update(values=todolist)
     window.FindElement('todolist1').Update(values=todolist1)
     
def read_file():
    tasks = []
    with open("output.txt", "r") as fp:
        line = fp.readline()
        while line != '':
            tasks.append(line.strip("\n"))
            line = fp.readline()
    return tasks

def show_tasks():
    fav_tasks = []
    with open("input.txt", "r") as fp:
        line = fp.readline()
        while line != '':
            fav_tasks.append(line.strip("\n"))
            line = fp.readline()
    return fav_tasks

def save_tasks():
    with open("output.txt", "w") as fw:
        for x in todolist:
            fw.write(x+"\n")
    todolist.clear()

def save_fav_tasks():
    with open("input.txt", "w") as f:
        for i in todolist1:
            f.write(i+"\n")
    todolist1.clear()
    
def sort_fav_tasks():
        todolist1.sort()
        window.FindElement('todolist1').Update(todolist1)

    
todolist = read_file()
todolist1 = show_tasks()

layout = [
    [sg.Text("Enter the task", font=("Arial", 14)), sg.InputText("", font=("Arial", 14), size=(20,1), key="taskname"),
     sg.Button("Add", font=("Arial", 14), key="add_save"),
    sg.Text("YOUR FAVOURTES", font=("Arial", 14), size=(100,1), justification = 'r')],
    [sg.Listbox(values=[todolist][0], size=(40, 10), font=("Arial", 14), key='todolist'), sg.Button("Edit", font=("Arial", 14)),
     sg.Button("Delete", font=("Arial", 14)),sg.Button("your favourites", font=("Arial", 14)),sg.Button("save task"),
    sg.Button("save your favourite task"),sg.Button("sort your favourite tasks"),
      sg.Listbox(values=[todolist1][0], size=(40,10), font=("Arial", 14), key=('todolist1'))],
     
]

window = sg.Window("Week1", layout)
while True:
    event, values = window.Read()
    if event == 'Edit':
         if values['todolist']:
             edit_tasks(values)
         if values['todolist1']:
             edit_fav_tasks(values)
    elif event == 'Delete':
         if values['todolist']:
            delete_tasks(values)
         if values['todolist1']:
            delete_fav_tasks(values)
    elif event == 'add_save':
        add_task(values)
    elif event == 'your favourites':
        favourite_tasks(values)
    elif event == 'save task':
        save_tasks()
    elif event == 'save your favourite task':
        save_fav_tasks()
    elif event == 'sort your favourite tasks':
        sort_fav_tasks()
    else:
        break
      
  
window.Close()
