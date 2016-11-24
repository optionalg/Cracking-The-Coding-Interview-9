'''
Detect if there is a loop in a linked list
CTCI 2.8
http://www.geeksforgeeks.org/detect-and-remove-loop-in-a-linked-list/
'''

class Node:
	def __init__(self, val):
		self.val = val
		self.next = None

class LinkedList:
	def __init__(self, root):
		self.root = Node(root)

	def add(self, node):
		# Add give node to the end of linked list
		cur = self.root
		while cur.next is not None:
			cur = cur.next
		cur.next = Node(node)

	def findLoop(self):
		# Returns 1 if there is a loop, else returns 0
		slow_iter = self.root
		fast_iter = self.root

		while (slow_iter and fast_iter and fast_iter.next):
		
			slow_iter = slow_iter.next
			fast_iter = fast_iter.next.next
			# print "Slow :", slow_iter.val
			# print "Slow.next :", slow_iter.next.val

			# print "Fast :", fast_iter.val
			# print "Fast.next :", fast_iter.next.val

			if slow_iter is fast_iter:

				self.deleteLoop(slow_iter)

				return 1

		return 0

	def deleteLoop(self, nodeInLoop):
		cur = self.root
		while 1:
			pt = nodeInLoop
			while pt.next is not nodeInLoop and pt.next is not cur:
				pt = pt.next
				
			if cur is pt.next:
				break

			else:
				cur = cur.next

		pt.next = None

	def printll(self):
		if self.findLoop:
			print "There is a loop"
		else:
			nodes = []
			cur = self.root
			while cur.next is not None:
				nodes.append(cur.val)
				cur = cur.next
			nodes.append(cur.val)
			print nodes

if __name__ == '__main__':
	llist = LinkedList(50)
	llist.add(20)
	llist.add(15)
	llist.add(4)
	llist.add(10)
	llist.add(70)

	llist.root.next.next.next.next.next = llist.root.next.next.next

	
	print llist.findLoop()
