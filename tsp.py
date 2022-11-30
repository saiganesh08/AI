from itertools import permutations

def tsp(G, s) :
    vertices = list(range(len(G)))

    # except the starting node
    vertices.pop(s)

    # all possible travelling ways
    ways = permutations(vertices)

    # minimum cost
    min_cost = 100000000
    for way in ways:
        cost = 0
        c = s
        for n in way:
            cost += G[c][n]
            c = n
        cost += G[c][s]

        # minimizing cost
        if cost < min_cost :
            min_cost = cost

    # return the minimum cost
    return min_cost


if __name__ == "__main__":

    G = [[0, 10, 15, 20],
		[10,  0, 35, 25],
		[15, 35,  0, 30],
		[20, 25, 30, 0]]

    s = 0
    print(tsp(G, s))