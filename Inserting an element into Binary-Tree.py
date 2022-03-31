# Aim:- Write Python Program for inserting an element into binary tree .


class Node():
	def __init__(self,key):
		self.key = key
		self.left = None
		self.right = None
		self.parent = None

class Tree():
	def __init__(self):
		self.root = None
	def add_node(self,key,node=None):
		
		if node is None:
			node = self.root
		if self.root is None:
			self.root = Node(key)
			print (key, "root")
		else:
			if key <= node.key :
				if node.left is None:
					node.left = Node(key)
					node.left.parent = node
					print (key, "left")
					return
				else:
					# return self.add_node(key,node = self.root.left)
					return self.add_node(key,node = node.left)
			else:
				if node.right is None:
					node.right = Node(key)
					node.right.parent = node
					print (key, "right")
					return
				else:
					# return self.add_node(key,node = self.root.right)
					return self.add_node(key,node = node.right)
t=Tree()
t.add_node(10)
t.add_node(13)
t.add_node(14)
t.add_node(8)
t.add_node(9)
t.add_node(7)
t.add_node(11)

'''
			   10
			  /    \
		        8      13
		       / \    /  \
		      7  9  11   14

'''