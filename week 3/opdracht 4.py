# -------------------------------------------#
#--------------Methode 1---------------------$
# -------------------------------------------#


def fileToDict(fileName):
    wordDict = dict()
    with open(fileName) as f:
        for line in f:
            for word in line.split():
                if word in wordDict:
                    wordDict[word] += 1
                else:
                    wordDict[word] = 1
        f.close()
    return wordDict

def dictToFile(wordDict):
    with open("wordDict.txt", "w") as f:
        for word, count in wordDict.items():
            f.write(word + " - " + str(count) + "\n")

        f.close()

dictToFile(fileToDict("words.txt"))

# -------------------------------------------#
#--------------Methode 2---------------------$
# -------------------------------------------#
class myqueue(list):
    def __init__(self,a=[]):
        list.__init__(self,a)

    def dequeue(self):
        return self.pop(0)

    def enqueue(self,x):
        self.append(x)

class Node():
   def __init__(self):
       # Note that using dictionary for children (as in this implementation) would not allow lexicographic sorting mentioned in the next section (Sorting),
       # because ordinary dictionary would not preserve the order of the keys
       self.children = {}  # mapping from character ==> Node
       self.value = None

def find(node, key):
    for char in key:
        if char in node.children:
            node = node.children[char]
        else:
            return None
    return node.value

def insert(root, string, value):
    node = root
    index_last_char = None
    for index_char, char in enumerate(string):
        if char in node.children:
            node = node.children[char]
        else:
            index_last_char = index_char
            break

    # append new nodes for the remaining characters, if any
    if index_last_char is not None:
        for char in string[index_last_char:]:
            node.children[char] = Node()
            node = node.children[char]
        node.isWord = True
    # store value in the terminal node
    node.value = value

def fileToTrie(trie, fileName):
    wordDict = dict()
    with open(fileName) as f:
        for line in f:
            for word in line.split():
                if find(trie, word):
                    insert(tree, word, (find(trie, word) + 1) )
                else:
                    insert(tree, word, 1)
        f.close()
    return wordDict

def TrieTofile(node, curstr = "", first = True):
    if first:
        open("wordTrie.txt", 'w').close()
    if len(node.children) > 0:
        for letter, child in node.children.items():
            tmpcurstr = curstr + letter
            if child.value:
                with open("wordTrie.txt", "a") as f:
                    f.write(tmpcurstr + " - " + str(child.value) + "\n")
                    f.close()
                print(tmpcurstr, child.value)
            TrieTofile(child, tmpcurstr, False)
    return

tree = Node()

fileToTrie(tree, "words.txt")
TrieTofile(tree)