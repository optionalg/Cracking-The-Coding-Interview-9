'''
Cracking the Coding Interview 2.5
add_list_reverse
linked list represent numbers, but in reverse order.
implement a way to add two numbers and return the sum
in the correct manner.
'''


class Node:
	def __init__(self, val):
		self.val = val;
		self.next = None;

class LinkedList:
	def __init__(self, item):
		self.head = Node(item)

	def add_node_to_linked_list(self, item):
		cur = self.head

		while cur.next is not None:
			cur = cur.next
		cur.next = Node(item)

	def get_head(self):
		return self.head

	def __str__(self):
		nodes = []
		cur = self.head

		while cur.next is not None:
			nodes.append(cur.val)
			cur = cur.next
		nodes.append(cur.val)

		return "All nodes: {}".format(nodes)


def add(ll_a, ll_b):
	val1 = ll_a.get_head() #.head vs .get_head()
	val2 = ll_b.get_head()
	carry = 0
	last_carry = 0

	while (val1 is not None):
		value = ((val1.val + val2.val) % 10) + carry
		carry = (val1.val + val2.val) // 10
		val1.val = value
		last_digit_1 = val1.val
		last_digit_2 = val2.val
		val1 = val1.next #.next vs .get_next()
		val2 = val2.next

	if last_digit_1 + last_digit_2 >= 10:
		last_carry = 1

	mul = 1
	val1 = ll_a.get_head()
	answer = 0
	while (val1 is not None):
		answer += mul * val1.val
		mul *= 10
		val1 = val1.next

	if (last_carry == 1):
		answer += 1 * mul
		
	return answer


l1 = LinkedList(9)
l1.add_node_to_linked_list(9)
l1.add_node_to_linked_list(9)

l2 = LinkedList(9)
l2.add_node_to_linked_list(9)
l2.add_node_to_linked_list(9)

print (add(l1, l2))

