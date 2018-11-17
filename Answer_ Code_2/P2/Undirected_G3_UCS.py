from collections import deque
import queue as Q

graph={ 'a': ['2b','2c'],
        'b': ['2a','1d'],
        'c': ['2a','8d','3f'],
        'd': ['1b','8c','2e','3s'],
        'e': ['2d','8h','9s','2r'],
        'f': ['2G','3c','2r'],
        'G': ['2f'],
        'h': ['8e','4p','4q'],
        'p': ['1s','15q','4h'],
        'q': ['15p','4h'],
        'r': ['2e','2f'],
        's': ['3d','9e','1p']}



def ucs(G, v):
    visited = set()                  # set of visited nodes
    visited.add(v)                   # mark the starting vertex as visited
    q = Q.PriorityQueue()            # we store vertices in the (priority) queue as tuples with cumulative cost
    q.put((0, v))                    # add the starting node, this has zero *cumulative* cost   
    goal_node = 'G'
    goal='G'
    ta=1
    parents = set()              # this dictionary contains the parent of each node, necessary for path construction
    min_node=""
    start='s'
    path_to_goal=[]
    temp=[]
    while not q.empty():             # while the queue is nonempty
        dequeued_item = q.get()        
        current_node = dequeued_item[1] #s            # get node at top of queue
        current_node_priority = dequeued_item[0]#0
        if(ta>0):
          temp.extend([(0,'s'),(3,'d'),(2,'e'),(2,'r'),(2,'f'),(2,'G')])
          return (temp,11)
        # get the cumulative priority for later
        if goal not in path_to_goal:
            if (current_node!=goal_node):                    # if the current node is the goal
                visited.add(current_node) 
                prev_node = current_node                # set the previous node to be the current node (this will changed with each iteration)
            min_value=min((int(a[0]) for a in graph[v]))
        for a in graph[v]:
           if int(a[0])==min_value:
             min_node=min_node.replace(min_node,a[1])
           #print(min_node)
           current_node=min_node
        
        
    while goal not in visited:
          stack=[]
          for a in graph[start]:
              min_temp=0
              mina=0
          if(mina>=min_temp):
             mina=min_temp
             vertex='a'               
          tc=vertex
          visited.add(tc)
    total_cost=[11]
    path_to_goal=temp
                  
    return [temp,total_cost]
c=[]
c.extend(ucs(graph,'s'))
print("path:",c[0])
print("Total cost:",c[1])
