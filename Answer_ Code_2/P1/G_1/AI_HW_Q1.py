#1:DFS using recursion :G1
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

#  DFS: recursion
def dfssearchingr(graph,visited,stack,path,goal):
    if  not stack:
        return (path,visited)
    vertex= stack.pop()
    if vertex not in path:        
           path.extend(vertex)
           stack.extend(list(set(graph[vertex])-set(path)))
           visited.extend(vertex)
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
    return dfssearchingr(graph,visited,stack,path,goal)
p=[]
p.extend(dfssearchingr(graph,[],['s'],[],'G'))
print("path :",p[0])
print("visited nodes:",p[1])

