#!C:\python27
#--- Day 9: All in a Single Night ---
#http://adventofcode.com/day/9
# Shortest Path Problem

import sys, re, numpy as np

def main(data):
    V, A = create_array(data)

    P, K = prim(V, A, 0)
            
    print np.sum(K)

def create_array(edges):
    string = ' '.join(lines)
    string = re.sub(' to ', ' ', string)
    string = re.sub(' = ', ' ', string)
    string = re.sub(' \d+', '', string)

    num_cities = len(set(string.split(' ')))

    key = []

    g = np.zeros((num_cities, num_cities), dtype = int)

    for edge in edges:
        v1, to, v2, equal, w = edge.split(' ')
        w = int(w)

        if v1 not in key:
            key.append(v1)
        if v2 not in key:
            key.append(v2)

        g[key.index(v1)][key.index(v2)] = w
        g[key.index(v2)][key.index(v1)] = w

    return np.arange(num_cities), g
   
def weight(A, u, v):
    return A[u][v]

def adjacent(A, u):
    L = []
    for x in range(len(A)):
        if A[u][x] > 0 and x <> u:
            L.insert(0,x)
    return L

def extractMin(Q):
    q = Q[0]
    Q.remove(Q[0])
    return q

def decreaseKey(Q, K):
    for i in range(len(Q)):
        for j in range(len(Q)):
            if K[Q[i]] < K[Q[j]]:
                s = Q[i]
                Q[i] = Q[j]
                Q[j] = s

def prim(V, A, r):
    u = 0
    v = 0

    # initialize and set each value of the array P (pi) to none
    # pi holds the parent of u, so P(v)=u means u is the parent of v
    P=np.ndarray(len(V), dtype = int)

    # initialize and set each value of the array K (key) to some large number (simulate infinity)
    K=np.ndarray(len(V), dtype = int)
    K.fill(999999)

    # initialize the min queue and fill it with all vertices in V
    Q=np.zeros(len(V))
    for u in range(len(Q)):
        Q[u] = V[u]

    # set the key of the root to 0
    K[r] = 0
    decreaseKey(Q, K)    # maintain the min queue

    # loop while the min queue is not empty
    while len(Q) > 0:
        u = extractMin(Q)    # pop the first vertex off the min queue

        # loop through the vertices adjacent to u
        Adj = adjacent(A, u)
        for v in Adj:
            w = weight(A, u, v)    # get the weight of the edge uv

            # proceed if v is in Q and the weight of uv is less than v's key
            if Q.count(v)>0 and w < K[v]:
                # set v's parent to u
                P[v] = u
                # v's key to the weight of uv
                K[v] = w
                decreaseKey(Q, K)    # maintain the min queue
    return P, K
    
if __name__ == '__main__':
    if len(sys.argv) != 2:
        print 'Usage: all_in_a_single_night.py <filename>'
    else:
        with open(sys.argv[1], 'r') as f:
            lines = [line.strip() for line in f.readlines()]
        main(lines)
