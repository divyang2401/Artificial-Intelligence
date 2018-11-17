graph={ 'a': set(['b','c']),
        'b': set(['a','d']),
        'c': set(['a','d','f']),
        'd': set(['b','c','e','s']),
        'e': set(['d','h','s','r']),
        'f': set(['G','c','r']),
        'G': set(['f']),
        'h': set(['e','p','q']),
        'p': set(['s','q','h']),
        'q': set(['p','h']),
        'r': set(['e','f']),
        's': set(['d','e','p'])}

dictp ={'a':5,'b':7,'c':4,'d':7,'e':5,'f':2,'G':0,'h':11,'p':14,'q':12,'r':3,'s':100}
dictq={"a:b":2,"a:c":2,"b:d":1,"c:d":8,"c:f":3,"f:G":2,"f:r":2,"r:e":2,
       "e:d":2,"e:s":9,"e:h":8,"d:s":3,"s:p":1,"p:h":4,"p:q":15,"q:h":4}

def fvalue(parent,child):
    t=str(parent)+":"+str(child)
    p=str(child)+":"+str(parent)
    try:
        if(dictq[t]>=0):
            cost=dictq[t]
    except:
        if(dictq[p]>=0):
           cost=dictq[p]
    return cost

def dfssearchings(graph,dictp,dictq, start,goal):
    path=[]
    visited=[]
    visited.extend(start)
    stack=[start]
    path_cost=0
    mina=0
    minc=""
    cost=0
    while stack:
        vertex= stack.pop()
        if (vertex==goal):
            path.extend(goal)
            print("path is:",path)
            #print(cost)
            #print(visited)
            print("Visited", visited)
            print("Search Node Expansion is:", path)
            
            return path
        if vertex not in path:        
           path.extend(vertex)
           temp=list(set(graph[vertex])-set(path))
           #print(temp)
           parent=vertex
           try:
               mina=fvalue(parent,temp[0])+dictp[temp[0]]    
           except Exception as e:
               print(e)
           for x in temp:
              visited.extend(x)
              t=fvalue(parent,x)
              w=t+dictp[x]
              if(w<=mina):
                  mina=w
                  minc=x
           #print(minc)
           #print(mina)
           #pathcost=pathcost+mina
           cost=cost+mina
           stack.extend(minc)
    
           
dfssearchings(graph,dictp,dictq, 's','G')

