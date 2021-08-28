class Node():
    def __init__(self):
        self.data = None
        self.link = None

node1 = Node()
node.data = "다현"
node.link = node1

node2 = Node()
node2.data = "정연"
node1.link = node2
node2.link = node1

node3 = Node()
node3.data = "쯔위"
node2.link = node3
node3.link = node1

current = node1
print(current.data, end=' ')
while current.link != node1:
    current = current.link
    print(current.data, end=' ')

# 새로운 노드 삽입
newNode = Node()
newNode.data = "지효"
newNode.link = node2.link
node2.link = newNode

# 노드 삭제
node2.link = node3.link
del(node3)
