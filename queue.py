#@using list
queue=[]
#insert eneque
queue.append(5)
queue.append(-1)
queue.append("a")
queue.append("name")
#dequeue
a=queue.pop(0)
b=queue.pop(0)
print(queue)
# access
print(queue[0])
#isempty
print(len(queue)==0)

#@using queue
from queue import Queue as qu
q= qu( maxsize=3)
print(q.full)# to find the space
#insert eneque
q.put("hi")
q.put(2)
#dequeue
a=q.get()
print(a)
# front
print(q.queue[0]
#isempty
print(q.empty())
      # using collection for double ended queue
