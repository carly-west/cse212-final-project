
call_queue = []

caller_1 = "Nancy"
caller_2 = "Mary"
caller_3 = "Jackson"

call_queue.append(caller_1)
call_queue.append(caller_2)
call_queue.append(caller_3)


'''Solution'''
while call_queue:
    print(call_queue.pop(0))
