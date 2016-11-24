class Node:
	def __init__(self, val, left = None, right = None):
		self.val = val
		self.left = left
		self.right = right


class BST:
	def __init__(self, val):
		self.root = Node(val)


	def insert(self, item):
		
		if self.root.val is None:
			self.root.val = item
		else:
			self._insert(self.root, item)

	def _insert(self, cur, item):
		if cur.val >= item:
			if cur.left is not None:
				self._insert(cur.left, item)
			else:
				cur.left = Node(item)
		else:
			if cur.right is not None:
				self._insert(cur.right, item)
			else:
				cur.right = Node(item)

	def getHeight(self, node):
		if node is None:
			return 0
		return max(self.getHeight(node.left), self.getHeight(node.right))+1

	def is_balanced(self):
		if self.checkHeight(self.root) == -1:
			return False
		else:
			return True

	def checkHeight(self, node):
		if node is None:
			return 0

		# if left subtree is balanced
		leftHeight = self.checkHeight(node.left)
		if leftHeight == -1:
			return -1
		# if right subtree is balanced
		rightHeight = self.checkHeight(node.right)
		if rightHeight == -1:
			return -1

		# if current node is balanced
		heightDiff = leftHeight - rightHeight
		if abs(heightDiff) > 1:
			return -1
		else:
			return max(leftHeight, rightHeight) + 1


bst = BST(6)

bst.insert(7)
bst.insert(8)
bst.insert(5)
bst.insert(4)
bst.insert(3)

print bst.getHeight(bst.root)

print bst.is_balanced()


