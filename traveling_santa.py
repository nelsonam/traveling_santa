import networkx as nx

G=nx.Graph()
G.add_node(1)
G.add_node(2)
G.add_node(3)
G.add_node(4)
G.add_node(5)
G.add_node(6)
G.add_node(7)
G.add_weighted_edges_from([(1,7,15),(1,3,6),(1,5,7),(1,6,6),(1,2,4),(2,4,10),(3,5,10),(3,7,5),(3,6,5),(4,7,3),(4,5,15),(5,6,5)])

distances=[]
#go through each type of cycle we can have (1-7)
for i in range(1,8): #1-8 because range is not inclusive
    #cutoff is to make sure we get out to the ham. cycle
    for path in nx.all_simple_paths(G, source=i, target=i cutoff=len(G)):
        #we only want the longest ones
        if(len(path)==len(G)+1):
            distance=0
            #add up the weights for each edge
            for i in range(0,7):
                distance=distance+G[path[i]][path[i+1]]['weight']
            #add these to a list
            distances.append((distance,path))

#defaults
min_dist=distances[0];
min_path=[]

#find the min distance
for dist in distances:
    if(dist[0]<=min_dist):
        min_dist=dist[0]
        min_path=dist[1]

print(min_path)
print("has a distance of")
print(min_dist)
