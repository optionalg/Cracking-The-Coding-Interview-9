'''
Given two BSTs (possibly with different sizes),
determine if one is a child of the other
'''

class Node:
	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None

class BST:
	def __init__(self, root):
		self.root = Node(root)

		self.inorder = []

	def add(self, item):
		if self.root is None:
			self.root = Node(item)
		else:
			self._add(self.root, item)

	def _add(self, cur, item):
		if cur.val >= item:
			if cur.left is not None:
				self._add(cur.left, item)
			else:
				cur.left = Node(item)
		else:
			if cur.right is not None:
				self._add(cur.right, item)
			else:
				cur.right = Node(item)

	def inorderTraversal(self, item):
		if self.root is None:
			return False
		elif self.root is item:
			return True
		else:
			self._inorderTraversal(self.root)

	def _inorderTraversal(self, cur):
		if cur.left is not None:
			self._inorderTraversal(cur.left)

		self.inorder.append(cur.val)
		
		if cur.right is not None:
			self._inorderTraversal(cur.right)

	def search(self, item):
		if self.root is None:
			return False
		else:
			self._search(self.root, item)

	def _search(self, cur, item):
		if cur.val == item:
			return True
		else:
			if cur.val >= item:
				if cur.left is None:
					return False
				else:
					self._search(cur.left, item)
			else:
				if cur.right is None:
					return False
				else:
					self._search(cur.right, item)


	def __str__(self):
		return "nodes: {}".format(self.inorder)
			

bst = BST(7)
bst.add(8)
bst.inorderTraversal(8)

bstB = BST(1)
bstB.add(4)
bstB.add(7)
bstB.add(8)
bstB.inorderTraversal(8)

print bst.search(8)
