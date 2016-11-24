'''
Cracking the Coding Interview 2.4
'''



class Node:
	def __init__(self, val):
		self.val = val
		self.next = None

class LinkedList:
	def __init__(self, item):
		self.head = Node(item)

	def add(self, item):
		cur = self.head

		while cur.next is not None:
			cur = cur.next
		cur.next = Node(item)

	def __str__(self):
		nodes = []

		cur = self.head
		while cur.next is not None:
			nodes.append(cur.val)
			cur = cur.next
		nodes.append(cur.val)

		return "Here is the list of nodes, sorted around the pivot: {}".format(nodes)

def partition(llist, pivot):
	cur = llist.head
	pre = None
	post = None

	while cur is not None:
		if cur.val < pivot.val:
			if pre is None:
				pre = LinkedList(cur.val)
			else:
				pre.add(cur.val)	
		elif cur.val == pivot.val:
			cur = cur.next
			continue
		else:
			if post is None:
				post = LinkedList(cur.val)
			else:
				post.add(cur.val)

		cur = cur.next

	cur = pre.head
	while cur.next is not None:
		cur = cur.next
	cur.next = pivot
	cur.next.next = post.head

	print pre
	return pre


ll = LinkedList(6)
ll.add(3)
ll.add(8)
ll.add(1)
ll.add(5)
ll.add(9)

partition(ll, Node(5))

