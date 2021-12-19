# https://www.hackerrank.com/challenges/find-the-nearest-clone/

def findShortest(graph_nodes, graph_from, graph_to, ids, val):
    connections = {i: set() for i in range(1, graph_nodes+1)}
    colors = {i: ids[i-1] for i in range(1, graph_nodes+1)}

    for i in range(len(graph_from)):
        connections[graph_from[i]].add(graph_to[i])
        connections[graph_to[i]].add(graph_from[i])
    
    starting_nodes = {n for n, c in colors.items() if c == val}
    
    all_paths = []
    
    for n in starting_nodes:          
        visited = {n,}
        stack = [(connections[n], 1)] 
        paths_len = []                
        while stack:
            st, level = stack.pop()
            for s in st:
                if s in visited:
                    continue
                visited.add(s)
                if colors[s] == val:
                    paths_len.append(level)
                else:
                    stack.append((connections[s], level+1))
        
        all_paths.extend(paths_len)
    
    if all_paths:
        return min(all_paths)
    return -1


assert findShortest(5, [1,2,2,3], [2,3,4,5], [1,2,3,1,3], 3) == 1
assert findShortest(5, [1,2,2,3], [2,3,4,5], [1,2,3,1,3], 1) == 2
assert findShortest(5, [1,2,2,3], [2,3,4,5], [1,2,3,1,3], 2) == -1
