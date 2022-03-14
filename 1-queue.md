#Queue Data Structure

##Introduction
What are Queues? They are a type of data structure that uses the idea of "First in, first out" when adding and removing data from the queue. A quick example of the "FIFO" method is when a group of people get into a line for something.


###What is First in, first out?

Let's say there is one person in line for cottton candy at a State Fair. Then another person gets in line behind them. The vendor then yells out, "NEXT PERSON PLEASE!" Who would be the next person to buy their cotton candy? Definitley the first person in line! This is how the "First in, first out" method works with queues, the next person in line is the one to be removed, or the one at the "front of the line". The data will always be flowing one way, almost like a stream. 

###When to use a Queue?

The main factor when deciding whether your program should us a queue, is to ask yourself, "Do I want my data structure to remove items in the order that they are added?" If the answer is no, it may be best to use a different data structure, but if the answer is yes, then queues would work great! Queues also allow duplicate values, so if the data structure you are looking for shouldn't allow that, it might be best to look for a different data structure option.

##Queue Operations

###Initializing the Queue
This will create a new queue. 
```
my_queue = []
```


###Appending values
This operation is also known by the name of "enqueue", and it adds the value to the end of the queue.

This will have an **O(1)** performance.
```
my_queue.append(value)
```

###Removing values
Because of the "FIFO" rule, it is only possible to remove from the front of the queue.
There are two possible ways of implementing this. These will both be an **O(n)** performance.
```
del my_queue[0] #The "0" is referencing index 0
#OR
my_queue.pop(0)
```

###Finding size of queue
This operation will return the size of the queue. It has an **O(1)** performance.
```
queue_length = len(my_queue)
```

##Code Example
When you use a keyboard to type, there is the expectation for the letters to appear on the screen in the order that you typed them. But what if there is a delay or buffer of when the key is pressed, to when it appears on the screen? Having jumbled up letters appear on the screen would be no fun! Here is an example of using a queue to receive input, and then print the input in the order that it was added.

```
# Initiate queue
keys_pressed = []

# As long as the user would like to continue typing, remain True
continue_typing = True
while continue_typing:
    # Receive letter input
    letter = input("Please type a letter: ")

    #Append it to back of queue
    keys_pressed.append(letter)

    # Check to see if user would like to continue typing
    user_continue = input("Would you like to continue typing? (Y/N) ").lower()

    # If the user would like to continue typing, continue the loop
    if user_continue == "y":
        pass

    # If the user would like to finish typing, exit the loop
    elif user_continue == "n":
        continue_typing = False

    # Check for invalid input
    else:
        print("Input Error")

# Starting at the beginning of the queue, print the key pressed as it is being removed
while keys_pressed:
    print(keys_pressed.pop(0))
```

##Problem for you to solve


###Definitions
