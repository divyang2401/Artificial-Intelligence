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

def dfssearchings(graph,dictp, start,goal):
    path=[]
    visited=[]
    visited.extend(start)
    stack=[start]
    path_cost=0
    mina=0
    minc=""
    while stack:
        vertex= stack.pop()
        if (vertex==goal):
            path.extend(goal)
            print("path is:",path)
            print("Search state expand is ",path)
            #print("visited is:(with comaprison is happened)", visited)
            return path
        if vertex not in path:        
           path.extend(vertex)
           temp=list(set(graph[vertex])-set(visited))
           try:
              mina= dictp[temp[0]]
           except Exception as e:
               print (str(e))
           for x in temp:
              visited.extend(x)
              if(dictp[x]<=mina):
                  mina=dictp[x]
                  minc=x
           #print(minc)
           #print(mina)
           #pathcost=pathcost+mina
           stack.extend(minc)
            
           
dfssearchings(graph,dictp, 's','G')
