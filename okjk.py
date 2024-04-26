# def BinaryTree(r):
#     return [r, [], []]
#
# def insertLeft(root,newBranch):
#     t = root.pop(1)
#     print(t)
#     if len(t) > 1:
#         root.insert(1,[newBranch,t,[]])
#     else:
#         root.insert(1,[newBranch, [], []])
#     return root
#
# def insertRight(root,newBranch):
#     t = root.pop(2)
#     if len(t) > 1:
#         root.insert(2,[newBranch,[],t])
#     else:
#         root.insert(2,[newBranch,[],[]])
#     return root
#
# def getRootVal(root):
#     return root[0]
#
# def setRootVal(root,newVal):
#     root[0] = newVal
#
# def getLeftChild(root):
#     return root[1]
#
# def getRightChild(root):
#     return root[2]
#
#
# r = BinaryTree(3)
# print(r)
# l = insertLeft(r,4)
# print(l)


class BinaryTree:
    def __init__(self, root):
        self.key = root
        self.left = None
        self.right = None

    def insertLeft(self, data):
        if self.left == None:
            self.left = BinaryTree(data)
        else:
            t = BinaryTree(data)
            t.left = self.left
            self.left = t

    def insertRight(self, data):
        if self.right == None:
            self.right = BinaryTree(data)
        else:
            t = BinaryTree(data)
            t.right = self.right
            self.right = t

    def getLeftChild(self):
        print(self.left)
        return self.left

    def getRightChild(self):
        return self.right

    def getRootValue(self):
        return self.key


root = BinaryTree("Book")

root.insertLeft("Chapter1")
root.insertRight("chapter2")
root.insertLeft("Chapter1")

print(root.getLeftChild().getRootValue())
a = 0//2
b = [3]
print(a)
b.append(8)
print(b)


