import math
INFINITY = math.inf  # float("inf")

class myqueue(list):
    def __init__(self, a=[]):
        list.__init__(self, a)

    def dequeue(self):
        return self.pop(0)

    def enqueue(self, x):
        self.append(x)


class Vertex:
    def __init__(self, data):
        self.data = data

    def __repr__(self):  # voor afdrukken
        return str(self.data)

    def __lt__(self, other):  # voor sorteren
        return self.data < other.data

def vertices(G):
    return sorted(G)

def edges(G):
    return [(u, v) for u in vertices(G) for v in G[u]]



def clear(G):
    for v in vertices(G):
        k = [e for e in vars(v) if e != 'data']
        for e in k:
            delattr(v, e)


def BFS(G, s):

    V = vertices(G)
    s.predecessor = None
    s.distance = 0
    for v in V:
        if v != s:
            v.distance = INFINITY  # v krijgt het attribuut 'distance'
    q = myqueue()
    q.enqueue(s)
    #    print("q:", q)
    while q:
        u = q.dequeue()
        for v in G[u]:
            if v.distance == INFINITY:  # v is nog niet bezocht
                v.distance = u.distance + 1
                v.predecessor = u  # v krijgt het attribuut 'predecessor'
                q.enqueue(v)



def show_tree_info(G):
    print('tree:', end=' ')
    for v in vertices(G):
        print('(' + str(v), end='')
        if hasattr(v, 'distance'):
            print(',d:' + str(v.distance), end='')
        if hasattr(v, 'predecessor'):
            print(',p:' + str(v.predecessor), end='')
        print(')', end=' ')
    print()





def show_sorted_tree_info(G):
    print('sorted tree:')
    V = vertices(G)
    #    V = [v for v in V if hasattr(v,'distance') and hasattr(v,'predecessor')]
    V.sort(key=lambda x: (x.distance, x.predecessor))
    d = 0
    for v in V:
        if v.distance > d:
            print()
            d += 1
        print('(' + str(v) + ',d:' + str(v.distance) + ',p:'
              + str(v.predecessor), end='')
        print(')', end=' ')
    print()





def path_BFS(G, u, v):
    BFS(G, u)
    a = []
    if hasattr(v, 'predecessor'):
        current = v
        while current:
            a.append(current)
            current = current.predecessor
        a.reverse()
    return a





class myqueue(list):
    def __init__(self, a=[]):
        list.__init__(self, a)

    def dequeue(self):
        return self.pop(0)

    def enqueue(self, x):
        self.append(x)


class Vertex:
    def __init__(self, data):
        self.data = data

    def __repr__(self):  # voor afdrukken
        return str(self.data)

    def __lt__(self, other):  # voor sorteren
        return self.data < other.data


def vertices(G):
    return sorted(G)


def edges(G):
    return [(u, v) for u in vertices(G) for v in G[u]]





def clear(G):
    for v in vertices(G):
        k = [e for e in vars(v) if e != 'data']
        for e in k:
            delattr(v, e)


def BFS(G, s):
    V = vertices(G)
    s.predecessor = None
    s.distance = 0
    for v in V:
        if v != s:
            v.distance = INFINITY  # v krijgt het attribuut 'distance'
    q = myqueue()
    q.enqueue(s)
    #    print("q:", q)
    while q:
        u = q.dequeue()
        for v in G[u]:
            if v.distance == INFINITY:  # v is nog niet bezocht
                v.distance = u.distance + 1
                v.predecessor = u  # v krijgt het attribuut 'predecessor'
                q.enqueue(v)


def show_tree_info(G):
    print('tree:', end=' ')
    for v in vertices(G):
        print('(' + str(v), end='')
        if hasattr(v, 'distance'):
            print(',d:' + str(v.distance), end='')
        if hasattr(v, 'predecessor'):
            print(',p:' + str(v.predecessor), end='')
        print(')', end=' ')
    print()





def show_sorted_tree_info(G):
    print('sorted tree:')
    V = vertices(G)
    #    V = [v for v in V if hasattr(v,'distance') and hasattr(v,'predecessor')]
    V.sort(key=lambda x: (x.distance, x.predecessor))
    d = 0
    for v in V:
        if v.distance > d:
            print()
            d += 1
        print('(' + str(v) + ',d:' + str(v.distance) + ',p:'
              + str(v.predecessor), end='')
        print(')', end=' ')
    print()

def path_BFS(G, u, v):
    BFS(G, u)
    a = []
    if hasattr(v, 'predecessor'):
        current = v
        while current:
            a.append(current)
            current = current.predecessor
        a.reverse()
    return a

# opdracht 1
def isConnected(G):
    V = vertices(G)
    s = V[0]
    s.predecessor = None
    s.distance = 0
    for v in V:
        if v != s:
            v.distance = INFINITY  # v krijgt het attribuut 'distance'
    q = myqueue()
    q.enqueue(s)
    #    print("q:", q)
    while q:
        u = q.dequeue()
        for v in G[u]:
            if v.distance is INFINITY:  # v is nog niet bezocht
                v.distance = u.distance + 1
                v.predecessor = u  # v krijgt het attribuut 'predecessor'
                q.enqueue(v)

    for v in V:
        if v.distance == INFINITY:
            return False
    return True

# opdracht 2

def checkForCycles(G, s):
    V = vertices(G)
    s.predecessor = None
    s.distance = 0
    for v in V:
        if v != s:
            v.distance = INFINITY  # v krijgt het attribuut 'distance'
    q = myqueue()
    q.enqueue(s)
    #    print("q:", q)
    while q:
        u = q.dequeue()
        for v in G[u]:
            if v.distance is INFINITY:  # v is nog niet bezocht
                v.distance = u.distance + 1
                v.predecessor = u  # v krijgt het attribuut 'predecessor'
                q.enqueue(v)
            else:
                if v != u.predecessor:

                    return False
    return True

def noCycles(G):
    V = vertices(G)
    BFS(G, V[0])
    for v in range(0, len(G)):
        if checkForCycles(G, V[v]) is False:
            return False

    return True

# opdracht 3
def getBridges(G):
    bridges = []
    for i in edges(G):
        G[i[1]].remove(i[0]) # verwijder de connectie
        G[i[0]].remove(i[1])
        BFS(G, i[0]) # check G specifiek vanaf punt 1
        for v in vertices(G):
            if v == i[1] and v.distance is INFINITY: # check of punt 2 nog verbonden is met punt 1
                bridges.append(i)
        G[i[1]].append(i[0]) # zet de connectie terug
        G[i[0]].append(i[1])
    return bridges

#opdracht 4
def isStronglyConnected(G):
    V = vertices(G)
    # check de normale graaf

    BFS(G, V[0])
    for v in vertices(G):
        if v.distance is INFINITY:
            return False

    # reverse de graaf (praktische het pijltje omdraaien)
    for e in edges(G):
        G[e[0]].remove(e[1])
        G[e[1]].append(e[0])

    # check reverse graaf
    BFS(G, V[0])
    for v in vertices(G):
        if v.distance == INFINITY:
            return False

    return True


# opdracht 5a
def isEulerGraph(G):
    for v in vertices(G):
        degree = len(G[v])
        if (degree % 2) is not 0:
            return False
    return True


# opdracht 5b
def getEulerCircuit(G, s):
    path = [s]
    edgesList = edges(G)
    bridgeList = getBridges(G)
    allBridges = True
    next = None;

    while edgesList:
        for t in G[s]: # kies een buur t
            if (s, t) not in bridgeList: # waarbij de edge (s,t) geen brug is
                next = t
                allBridges = False

                break #niet onodig loopen
        if allBridges: # (tenzij het niet anders kan)
            next = G[s][0]

        allBridges = True
        # verwijder de edge
        G[s].remove(next)
        G[next].remove(s)
        bridgeList = getBridges(G) # fancier maken?
        edgesList = edges(G) # fancier maken?
        path.append(next)
        s = next

    return path

print("<================================>")
v = [Vertex(i) for i in range(8)]


print("<================================>")
print("begin opdracht 1 is connected:")
G = {v[0]: [v[4], v[5]],
     v[1]: [v[4], v[5], v[6]],
     v[2]: [v[4], v[5], v[6]],
     v[3]: [v[7]],
     v[4]: [v[0], v[1], v[2], v[5]],
     v[5]: [v[0], v[1], v[2], v[4]],
     v[6]: [v[1], v[2]],
     v[7]: [v[3]]
}

print(isConnected(G))  # <- False
clear(G)

G = {v[0]: [v[4], v[5]],
     v[1]: [v[4], v[5], v[6]],
     v[2]: [v[4], v[5], v[6]],
     v[4]: [v[0], v[1], v[2], v[5]],
     v[5]: [v[0], v[1], v[2], v[4]],
     v[6]: [v[1], v[2]],
}

print(isConnected(G))  # <- True
clear(G)
print("<================================>")
print("begin opdracht 2 no cycles:")
G = {v[0]: [v[4], v[5]],
     v[1]: [v[4], v[5], v[6]],
     v[2]: [v[4], v[5], v[6]],
     v[4]: [v[0], v[1], v[2], v[5]],
     v[5]: [v[0], v[1], v[2], v[4]],
     v[6]: [v[1], v[2]],
}

print(noCycles(G))  # <- False
clear(G)

G = {v[0]: [v[4], v[5]],
     v[1]: [v[4], v[6]],
     v[2]: [v[5]],
     v[3]: [v[7]],
     v[4]: [v[0], v[1]],
     v[5]: [v[0], v[2]],
     v[6]: [v[1]],
     v[7]: [v[3]]
}

print(noCycles(G))  # <- True
clear(G)


print("<================================>")
print("begin opdracht 3 get bridges:")
G = {v[0]: [v[1], v[3]],
     v[1]: [v[0], v[2]],
     v[2]: [v[1], v[3], v[4]],
     v[3]: [v[0], v[2]],
     v[4]: [v[2], v[5], v[6]],
     v[5]: [v[4], v[6]],
     v[6]: [v[4], v[5], v[7]],
     v[7]: [v[6]]
}
print(getBridges(G))  # <- [(2, 4), (4, 2), (6, 7), (7, 6)]
clear(G)

print("<================================>")
print("begin opdracht 4 is strongly connected:")
G = {v[0]: [v[1]],
     v[1]: [v[2]],
     v[2]: [v[0]]
}
print(isStronglyConnected(G))  # True

G = {v[0]: [v[1]],
     v[1]: [],
     v[2]: [v[0], v[1]]
}
print(isStronglyConnected(G))  # False
clear(G)

print("<================================>")
print("begin opdracht 5a is een Euler-graaf:")
G = {v[0]: [v[1], v[2]],
     v[1]: [v[2], v[0]],
     v[2]: [v[0], v[1]]
}
print(isEulerGraph(G))  # True

G = {v[0]: [v[1]],
     v[1]: [],
     v[2]: [v[0], v[1]]
}
print(isEulerGraph(G))  # False
clear(G)

print("<================================>")
print("begin opdracht 5b print Euler circuit:")
G = {v[0]: [v[1], v[2]],
     v[1]: [v[0], v[3]],
     v[2]: [v[0], v[3]],
     v[3]: [v[1], v[2], v[4], v[6]],
     v[4]: [v[3], v[5], v[6], v[7]],
     v[5]: [v[4], v[6]],
     v[6]: [v[3], v[4], v[5], v[7]],
     v[7]: [v[4], v[6]]
}
V = vertices(G)
print(getEulerCircuit(G, V[0]))  # [0,1,3,4,5,6,4,7,6,3,2,0]
clear(G)
