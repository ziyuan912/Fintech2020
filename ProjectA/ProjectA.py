def numEdges(a, b, c, d, e, f, g):
	return (a + b + c + d + f + g) + (a * e) + (b * e) + (c * e) + (c * f) + (d * f) + (e * g)

def numPaths(a, b, c, d, e, f, g):
	return g * (a * e + b * e + c * e) + c * f + d * f

nodes = [0 for i in range(7)]

for i in range(7):
	nodes[i] = int(input())

numedge = numEdges(nodes[0], nodes[1], nodes[2], nodes[3], nodes[4], nodes[5], nodes[6])
numpath = numPaths(nodes[0], nodes[1], nodes[2], nodes[3], nodes[4], nodes[5], nodes[6])

print('num edges:', numedge)
print('num paths:', numpath)