N = 1000
P = list(range(0,N+1))
S = [1 for _ in range(0,N+1)]

def find(u):
	if u == P[u]:
		return u
	P[u] = find(P[u])
	return P[u]

def union(u,v):
	u = find(u)
	v = find(v)
	if u != v:
		# merge smaller set into bigger set
		if S[u] < S[v]:
			P[u] = v
			S[v] += S[u]
		else:
			P[v] = u
			S[u] += S[v]
