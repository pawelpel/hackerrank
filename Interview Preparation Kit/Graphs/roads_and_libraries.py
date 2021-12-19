# https://www.hackerrank.com/challenges/torque-and-development/


def roadsAndLibraries(n, c_lib, c_road, cities):
    if c_lib <= c_road:
        return n * c_lib
    
    city_connections = {i: {i} for i in range(1, n+1)}
    
    for c1, c2 in cities:
        city_connections[c1].add(c2)
        city_connections[c2].add(c1)
    
    final_groups = []
    
    visited = set()
    for city in range(1, n+1):
        if city in visited:
            continue
        visited.add(city)
        group = set()    
        stack = [city_connections[city],]
        while stack:
            connected_cities = stack.pop()
            group.update(connected_cities)
            for connected in connected_cities:
                if connected in visited:
                    continue
                visited.add(connected)
                stack.append(city_connections[connected])
        
        final_groups.append(group)
        
    total = 0
    for g in final_groups:
        count = len(g)
        total += c_lib + ((count-1) * c_road)
    
    return total


assert roadsAndLibraries(3, 2, 1, [[1, 2], [3, 1], [2, 3]]) == 4
    