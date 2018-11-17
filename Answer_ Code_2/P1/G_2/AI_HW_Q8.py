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

#Stack
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
