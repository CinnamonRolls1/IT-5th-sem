
def input_graph(G,E,V) :

	for i in E :
		G[i[0]].append(i[1])


def get_V(E) :

	V = []
	for i in E :
		if i[0] not in V :
			V.append(i[0])

		if i[1] not in V :
			V.append(i[1])

	return V

def input_E(num_edges) :

	E = []
	for i in range(num_edges) :

		e = list(map(int,input().split(',')))
		E.append(e)

	return E



#E =input_E(5)

E = [[0,2],[2,4],[1,0],[2,1],[1,3]]
print("Edge List:",E)
V = get_V(E)
print("Nodes: ",V)
G = [[] for i in range(len(V))]
input_graph(G,E,V)
print("Adjacency list:")
for i in range(len(G)):
	print(i, G[i])


def check_deadlock(G,probe) :

	b=False
	if probe[0] == probe[2] :
		print("Deadlock detected at:",probe)
		return True


	for i in G[probe[2]] :
		new_probe = [probe[0],probe[2],i]

		print("New probe:",new_probe)

		b= b or check_deadlock(G, new_probe)


	return (b or False)


print(check_deadlock(G,[0,0,2]))