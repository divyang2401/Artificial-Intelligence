# A1 with stack as list: DFS

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

#stack

def dfssearchings(graph, start,goal):
    path=[]
    visited=[]
    stack=[start]
    while stack:
        vertex= stack.pop()
        
        if vertex not in path:        
           path.extend(vertex)
           stack.extend(list(set(graph[vertex])-set(path)))
           visited.extend(vertex)
        checker=1
        if goal in path:
            return (path,visited)
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
p.extend(dfssearchings(graph,'s','G'))
print("path:",p[0])
print("visited:",p[1])
