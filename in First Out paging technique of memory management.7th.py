#Construct a C program to simulate the First in First Out paging technique of memory management
from queue import Queue

def pageFaults(pages, n, capacity):
 
 s = set()

 indexes = Queue()

 page_faults = 0
 for i in range(n):
  

  if (len(s) < capacity):
   
   if (pages[i] not in s):
    s.add(pages[i])

    page_faults += 1

    indexes.put(pages[i])

  else:
   
   if (pages[i] not in s):
    
    val = indexes.queue[0]

    indexes.get()

    s.remove(val)


    s.add(pages[i])

    indexes.put(pages[i])

    page_faults += 1

 return page_faults

if _name_ == '_main_':
 pages = [7, 0, 1, 2, 0, 3, 0,
    4, 2, 3, 0, 3, 2]
 n = len(pages)
 capacity =int(input("enter n:"))
 print(pageFaults(pages, n, capacity))
