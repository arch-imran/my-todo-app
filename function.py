FILEPATH = "todos.txt"

def get_todos(filepath=FILEPATH):
    with open(filepath,'r') as local_file:
        todos_local = local_file.readlines()
    return todos_local


def write_todos(todos,filepath=FILEPATH):
    with open(filepath,'w') as local_file:
        local_file.writelines(todos)

if __name__=="__main__":
    print(get_todos())
