#python 3.7.9

#This program experiments with graphical libraries networkx and matplotlib to generate a gui type image of networked content.
#This program is experimental and led to a series of images of networked graphs

import networkx as nx
import matplotlib.pyplot as plt
#edge list of connected nodes
edgelist= [(1,'Lol',),('Lol',3),(3,4),(3,5),(3,"New Node")]
#simple un-directed graph, not 1 to 2 ect DiGraph(), MultiGraph(), MultiDigraph()
TestGraph = nx.DiGraph()
"""#1 node, second node
TestGraph.add_edge(1, 2)
#weight is the longer it takes to get from 2 to 3, strength of connection
TestGraph.add_edge(2, 3, weight = 0.1)
#line from node a to b
TestGraph.add_edge("A", "B")
#line from b to b, back on itself
TestGraph.add_edge("B", "B")
#add node without connecting to anything, 
TestGraph.add_node("C")
#can pass things to node
TestGraph.add_node(print)
https://www.youtube.com/watch?v=VetBkjcm9Go&t=744s"""
#add edges from
TestGraph.add_edges_from(edgelist)

pos = nx.planar_layout(TestGraph)

#text variable for below sentence
text= ("of me")

#edge labels. To iterate through the edges of graph, you can use TestGraph.edges {n1} is node 1
"""To iterate through the edges of graph, you can use G.edges.

G.edges returns a list of (node1, node2), where node1 and node2 are two nodes of the edge.
G.edges(data=True) returns a list of (node1, node2, ddict), where ddict is edge attribute dict.
G.edges(data=attr) returns a list of (node1, node2, ddict[attr])
https://stackoverflow.com/questions/47094949/labeling-edges-in-networkx
"""
edge_labels = dict([((n1, n2), f'{n1} is connected to {n2} because {text}')
                    for n1, n2 in TestGraph.edges])
#edge_labels = nx.get_edge_attributes(TestGraph,text)

#fancy stuff
#formatted_edge_labels = {(elem[0],elem[1]):edge_labels[elem] for elem in edge_labels} # use this to modify the tuple keyed dict if it has > 2 elements, else ignore

#draw the graph, with labels to see the names of the nodes, other options
#draw_planar, random, spectral, spring, shell, circular
nx.draw_planar(TestGraph, with_labels=True, bbox=dict())

# Add labels to the connections
nx.draw_networkx_edge_labels(TestGraph, pos,
                             edge_labels = edge_labels, font_color='red')
#junk: =nx.planar_layout(TestGraph) : edge_labels = 


#show
plt.show()
