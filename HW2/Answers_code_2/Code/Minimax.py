import math
import string
graph=[3,10,2,9,10,7,5,9,2,5,6,4,2,7,9,1]
t=string.ascii_uppercase[:26]
path=[]
deapth=math.log(len(graph),2)

def IsPowerOfTwo(x):
    return (x != 0) and ((x & (x - 1)) == 0);

def min_value(a,b):
    return min(a,b)

def max_value(a,b):
    return max(a,b)
def pathrr():
    return t
r=['A','B','C','D','G']
def minimax(graph,current_level,deapth,maxTurn,minTurn,index):
     path.extend(t[index])
     if(current_level==deapth):
        return graph[index]
     elif(maxTurn):
         maxTurn=False
         minTurn=True
         
         return max_value(minimax(graph,current_level+1,deapth,maxTurn,minTurn,index*2),minimax(graph,current_level+1,deapth,maxTurn,minTurn,index*2+1))
     elif(minTurn):
         maxTurn=True
         minTurn=False
         return min_value(minimax(graph,current_level+1,deapth,maxTurn,minTurn,index*2),minimax(graph,current_level+1,deapth,maxTurn,minTurn,index*2+1))

    


print(minimax(graph,0, deapth, True,False,0))
print("path is:")
for i in range(0,5):
    print(t[(2*i+1)-1])
