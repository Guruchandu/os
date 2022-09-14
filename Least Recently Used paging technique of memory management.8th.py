#. Construct a C program to simulate the Least Recently Used paging technique of memory management.
N=int(input("Enter n value = "))
processList = [ 7, 0, 1, 2, 0, 3, 0,
                4, 2, 3, 0, 3, 2]
s = []
 
pageFaults = 0
 
for i in processList:
 
    if i not in s:
 
        if(len(s) == N):
            s.remove(s[0])
            s.append(i)
 
        else:
            s.append(i)
 
        pageFaults +=1

    else:
         
        s.remove(i)
        s.append(i)
     
print("no.of pagefaults = ","{}".format(pageFaults))

