from collections import deque
graph={ 'a': set([]),
        'b': set(['a']),
        'c': set(['a']),
        'd': set(['b','c','e']),
        'e': set(['h','r']),
        'f': set(['G']),
        'G': set([]),
        'h': set(['p','q']),
        'p': set(['q']),
        'q': set([]),
        'r': set(['f']),
        's': set(['d','e','p'])}

#  BFS: Queue 
def bfssearchings(graph, start,goal):
    visited= []
    path=[]
    queue=deque([start])
    
    while queue:
        vertex= queue.popleft()
        
        if vertex not in path:        
           path.extend(vertex)
           visited.extend(vertex)
           queue.extend(list(set(graph[vertex])))
        if goal in path:
            return (path,visited)
        checker=1
        for a in graph:
            for b in graph[a]:
                if b in path:
                    checker=(checker)*(1)
                else:
                     checker=(checker)*(0)
            if(checker>0):
                if a not in visited:
                    visited.extend(a)
    return (path,visited)
p=[]
p.extend(bfssearchings(graph,'s','G'))
print("path :",p[0])
print("visited nodes:",p[1])
