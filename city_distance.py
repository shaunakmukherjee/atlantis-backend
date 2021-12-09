from math import sqrt
from collections import defaultdict


"""
 Inspired by Djkistra's shortest path algorithm, 
 this program takes in the cities along with their distances ('edges') 
 and delivers the shortest path from any vertex.
"""



# first we need to define the key coordinates - i.e. have a 'anchor' for each city to better traverse them
def key_coordinates(coordinates):
    count=0
    for coordinate in coordinates:
        count+=1
        coordinate.append(count)
    return coordinates

# simple metric to calculate distance via coordinate geometry
def distances_cities(x1, y1, x2, y2):
    distance = sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2))
    return distance

# creating the graph
def create_graph(c):
    coordinates = key_coordinates(c)
    graph = defaultdict(list)
    distances = {}
    for current in coordinates:
        for next in coordinates:
            if next == current:
                continue
            else:
                flight_dis = distances_cities(current[0], current[1],
                                                 next[0], next[1])
                graph[current[2]].append(next[2])
                distances[current[2], next[2]] = flight_dis
    return coordinates, distances

# the main logic behind the modified Djikstra algorithm

def shortest_flight_path(cities, edges, start):
    next_city = 0
    unvisited = []
    visited = []
    total_distance = 0
    current_city = start
    for city in cities:
        if city[2] == start:
            visited.append(start) #adding the cities if not visited
        else:
            unvisited.append(city[2])
    while unvisited: 
        for index, next_city in enumerate(unvisited): #between consecutive cities while traversing, we have to figure out the current distance 
            if index == 0: # this condition arises for the first city
                current_distance = edges[start, next_city]
                current_city = next_city
            elif edges[start, next_city] < current_distance: #keeps track of the shortest path at every interval, checking whether the distance is shorter or not
                current_distance = edges[start, next_city]
                current_city = next_city
        total_distance += current_distance
        unvisited.remove(current_city) #remove it from the 'unvisited' list because now its marked visited
        visited.append(current_city)
    return visited, total_distance

def driver_code():
    coordinates= [[0.0 for j in range(2)] for i in range(4)]
    print("\nNOTE: North (N) and East (E) are deemed positive, hence any (W) or (S) are automatically converted to negative values \n")
    character='A'
    for i in range(4):
        print("Please enter the co-ordinates for City {}! ".format(character))
        for j in range(2):
            k, dir = input().split(" ")
            if dir == 'N' or dir == 'E':
                coordinates[i][j] = float(k)
            else:
                coordinates[i][j]= -float(k)
        character=chr(ord(character)+1)
    
    print (coordinates)
    
    #coordinates = [[ 51.5074, 0.1278], [60.8566, 2.3522],
              #[55.2311, 2.1222], [64.0010, 0.1002]]
    cities, distances = create_graph(coordinates)
    #since we are told to start from A, i.e. '1', we shall do that
    shortest_path, shortest_distance = shortest_flight_path(cities, distances, 1)
    print('--------------------------------------')
    print("The shortest path to all citys from A is:", shortest_path)
    print("The shortest distance covered is:", shortest_distance)

driver_code()