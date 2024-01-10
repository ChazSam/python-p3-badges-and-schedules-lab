def badge_maker(name):
    return f"Hello, my name is {name}." 

def batch_badge_creator(names):
    lst = []
    for i in names:
        lst.append(f"Hello, my name is {i}." )     
    return lst

def assign_rooms(names):
    lst = []
    for i, name in enumerate(names, start=1):
        lst.append(f"Hello, {name}! You'll be assigned to room {i}!")
    return lst

def printer(names):
    for j in names:
        print(f"Hello, my name is {j}.")
    assignment = assign_rooms(names)
    for m in assignment:
        print(m) 
