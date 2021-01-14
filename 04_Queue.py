# Queue implementation using list
# Add the element called enqueue and delete the element called dequeue

queue =[]
def add_element():
    ele = input("Element you want to add: ")
    queue.append(ele)
    print(ele, "will be added....")
def remove_element():
    if not queue:        # not queue means there is no element in a queue...
        print("Queue is empty....!")
    else:
        a= queue.pop(0)
        print("Removed element: ",a)
def display():
    print(queue)

while True:

    inp = int(input("Choose betwwen these:\n1.Add element\n2.Remove element\n3.Display\n4.Exit\n"))
    if inp==1:
        add_element()
    elif inp==2:
        remove_element()
    elif inp==3:
        display()
    else:
        break
