
class Node(object):

	def __init__(self, value):
		self.value = value 
		self.next = None
		self.previous = None


class SinglyLinkedList(object):

	def __init__(self):
		self.current_element = None

	def insert_element(self, value):
		new_element = Node(value)
		new_element.next = self.current_element
		self.current_element = new_element

	def print_list(self):
		printing_node = self.current_element
		while printing_node:
			print printing_node.value
			printing_node = printing_node.next

	def search(self, value):
		searching_node = self.current_element
		while searching_node:
			if value == searching_node.value:
				return True
			searching_node = searching_node.next 
		return False


class DoublyLinkedList(SinglyLinkedList):

	def insert_element(self, value):
		if self.current_element:
			self.current_element.previous = value
		super(DoublyLinkedList, self).insert_element(value)





test = SinglyLinkedList()
print ""
print "Linked list: "
for i in range(5):
	test.insert_element(i)

test.print_list()

print "Pick a number to search the list and see if it is there:"
for _ in range(5):
	test_me = int(raw_input(">> " ))
	print test.search(test_me)
print ""
print "Doubly Linked List:"
test2 = DoublyLinkedList()
for i in range(5):
	test2.insert_element(i)

test2.print_list()

print "Pick a number to search the list and see if it is there:"
for _ in range(5):
	test_me = int(raw_input(">> " ))
	print test2.search(test_me)