# Question

This question basically asks us to find a connection that is not part of a cycle.
If you break such connection, the graph breaks into 2 components since there is no cycle
to have another path between the 2 nodes the edge was connecting.
The edge is also known as a bridge.

# Solution

We'll use a modified version of the Tarjan's algorithm that works on undirected graphs.
It will help us with finding out the bridges in a graph.

DFS is a discovery algorithm. It discovers nodes one after the other.
Lets add a label as when the node was discovered. First node will be labelled 0, second 1, and so on.
The labels are also called time of insertion/discovery.

Now, an edge going out of a node(not the parent) could have 2 cases:
1) The node it goes to has not yet been discovered.
2) The node it goes to has already been discovered.

For case 1:
We simply recursively call DFS on that node.

For case 2:
We look for its label and min it with the current node's ORIGINAL label (emphasis on orignal).
"label[curr_node] = min(label[curr_node], label[neighbour])"


# Lets take an example

Let say we have the below graph as input and we wanna find out its critical edges. We know the only critical edge it has is the one going out of the triangle.
Lets assume the the node marked S is the source.

![Graph](images/IMG_0255.png?raw=true "Graph")

We discover the node and mark its disovery time as 0 and label it as 0 as well initially.

![Graph1](images/IMG_0246.png?raw=true "Graph1")


Then, we move onto the next node. Since it has not been disovered yet too, we label it 1 with disovery time 1. Denoted as 1/1.
Similary, we go to the next node as 2/2.


![Graph2](images/IMG_0247.png?raw=true "Graph2")


Then we move onto the last node 3/3
![Graph](images/IMG_0248.png?raw=true "Graph")



Since, 3/3 has no neighbours (other than the caller node of course), it backtracks to 2/2.
Now, 2 evaluates the edege 2-3. 
The low link value of 3 (the node who backtracked) is higher than its low link value. This must mean that 3 did not run into any nodes discovered before it (node 2). So the edge 2-3 must be critical being the only link to the node labelled 3. We mark it critical.

![Graph](images/IMG_0249.png?raw=true "Graph")


![Graph](images/IMG_0250.png?raw=true "Graph")



Now, node 2 looks at node 1 as it is also its neighbour. Although, it has been disovered already so no need to call dfs on it.
But it will min its low link value with itself.

lowlink(node2) = min( lowlink(2), lowlink(node0) )
lowlink(node2) = min( 2, 0 )
lowlink(node2) = 0
So, node 2 will update its lowlink value as 0.

![Graph](images/IMG_0251.png?raw=true "Graph")


The graph look like this at this point.
![Graph](images/IMG_0252.png?raw=true "Graph")



Node 1 mins its lowlink value with node 2. Because node 2's lowlink is lower than or equal to (in this case equal to) to its own low link, then there must another way to reach node 2 from node 1 other than the direct link. We do not mark edge 1-2 critical.
![Graph](images/IMG_0253.png?raw=true "Graph")


Similary, edge 0-1 is not critical either.
![Graph](images/IMG_0254.png?raw=true "Graph")


The algorithm finishes up having found only one critical edge (edge 2 - 3) as expected.

