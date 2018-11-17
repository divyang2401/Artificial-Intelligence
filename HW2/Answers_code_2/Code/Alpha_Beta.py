import sys
import math
import string
graph=[3,10,2,9,10,7,5,9,2,5,6,4,2,7,9,1]
deapth=math.log(len(graph),2)
n=2#branching factor
t=string.ascii_uppercase[:26]
path=[]
def min_value(a,b):
    return min(a,b)

def max_value(a,b):
    return max(a,b)

def minimax(graph,current_level,deapth,maxTurn,minTurn,index,alpha,beta):
    i=0
    if(current_level==deapth):
         return graph[index]
    elif(maxTurn):
        maxTurn=False
        minTurn=True
        final=(-sys.maxsize-1)
        while (i<n): 
            v= minimax(graph,current_level+1,deapth,maxTurn,minTurn,index*2+i,alpha,beta)
            #print(v)
            i=i+1
            final=max_value(final,v)
            alpha=max_value(alpha,final)
            if(beta<=alpha):
                break
                
    elif(minTurn):
        maxTurn=True
        minTurn=False
        final=sys.maxsize
        while (i<n): 
            v= minimax(graph,current_level+1,deapth,maxTurn,minTurn,index*2+i,alpha,beta)
            #print(v)
            i=i+1
            final=min_value(final,v)
            beta=min_value(beta,final)
            if(beta<=alpha):
                break
    print("alpha is:{} and beta is:{}".format(alpha,beta))
    return final
    
print("final value is: {}".format(minimax(graph,0, deapth, True,False,0,(-sys.maxsize-1),sys.maxsize)))
print("path is:")
for i in range(0,5):
    print(t[(2*i+1)-1])

