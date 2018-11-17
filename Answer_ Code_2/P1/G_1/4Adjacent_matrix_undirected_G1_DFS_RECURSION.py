#Adjacent_matrix_undirected_G1_DFS
matrix=[
            [0,1,1,0,0,0,0,0,0,0,0,0],[1,0,0,1,0,0,0,0,0,0,0,0],
            [1,0,0,1,0,1,0,0,0,0,0,0],[0,1,1,1,1,0,0,0,0,0,0,1],
            [0,0,0,1,0,0,0,1,0,0,1,1],[0,0,1,0,0,0,1,0,0,0,1,0],
            [0,0,0,0,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,0,0,1,1,0,0],
            [0,0,0,0,0,0,0,1,0,1,0,1],[0,0,0,0,0,0,0,1,1,0,0,0],
            [0,0,0,0,1,1,0,0,0,0,0,0],[0,0,0,1,1,0,0,0,1,0,0,0]]
dic ={'0':'a','1':'b','2':'c','3':'d','4':'e','5':'f','6':'G','7':'h','8':'p','9':'q','10':'r','11':'s'}
dicp ={'a':'0','b':'1','c':'2','d':'3','e':'4','f':'5','G':'6','h':'7','p':'8','q':'9','r':'10','s':'11'}

w=12
def replacement(ls):
    counter=0
    ts=[]
    for i in ls:
        if (i>0):
           ts.extend(dic.get(str(counter)))
        counter=counter+1        
    return ts               
#recursions
def dfssearchingr(matrix,visited,stack,nodes,goal,path):
    
    if nodes<0:
        return (path,visited)
    if  not stack:
        return (path,visited)
    
    vertex= stack.pop()
    if vertex not in path:
           path.extend(vertex) 
           visited.extend(vertex)
    temp=replacement(matrix[int(dicp.get(vertex))])
    stack.extend(list(set(temp)-set(visited)))
    if goal in path:
        return (path,visited)
   
    return dfssearchingr(matrix,visited,stack,nodes-1,goal,path)

p=[]
p.extend(dfssearchingr(matrix,[],[dic.get(str(11))],w,dic.get(str(6)),[]))
print("path :",p[0])
print("visited nodes:",p[1])
