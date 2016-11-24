class Stack:
	def __init__(self):
		self.items = []

	def push(self, item):
		self.items.append(item)

	def pop(self):
		return self.items.pop()

	def getStacklen(self):
		return len(self.items)

	def isEmpty(self):
		return self.getStacklen() == 0

	def __str__(self):
		return "Stack: {}".format(self.items)

class Queue:
	def __init__(self):
		self.s1 = Stack()
		self.s2 = Stack()

	def enqueue(self, item):
		self.s1.push(item)
		# print self.s1

	def dequeue(self):
		if self.s2.isEmpty():
			while self.s1.isEmpty() is False:
				self.s2.push(self.s1.pop())

		return self.s2.pop()

	def __str__(self):
		return "Queue1: {}, Queue2: {}".format(self.s1, self.s2)


q = Queue()

q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)

q.dequeue()

q.dequeue()

print q
