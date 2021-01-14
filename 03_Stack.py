# implement stack using list
stack =[]
def Push_element():
    push =input("Element you want to insert: ")
    stack.append(push)
    print(stack)
def Pop_element():
    if stack is None:
        print("stack is empty!!!")
    else:
        pop = stack.pop()
        print("Removed element: ",pop)
        print(stack)
while True:
    inp = int(input("Which operation you want to perform..\n1. Push\n2.Pop\n3.Exit\n"))
    if inp==1:
        Push_element()
    elif inp==2:
        Pop_element()
    else:
        break




