class node:
	def __init__(self, data):
		self.data = data
		self.next = None

class singlylinkedlist:
	def __init__(self):
		self.head = None
		self.tail = None

	def __len__(self):
		ptr = self.head
		leng = 0
		while(ptr):
			leng += 1
			ptr = ptr.next
		return leng

	def display(self):
		ptr = self.head
		lst_to_str = ''
		while ptr:
			lst_to_str += str(ptr.data) + ' '

			ptr = ptr.next
		print(lst_to_str)

	def push_back(self, data):
		newNode = node(data)
		if not self.head:
			self.head = newNode
			self.tail = newNode
		else:
			self.tail.next = newNode
			self.tail = newNode

	def insert(self, data, position):
		if position > len(self):
			print("ERROR: position is too large")
			return False
		elif position == len(self):
			temp = node(data)
			self.tail.next = temp
			self.tail = temp
			return True

		ptr = self.head
		pos = 0
		while pos < position - 1:
			ptr = ptr.next
			pos += 1

		#ptr is now at the correct position
		temp = node(data)
		temp.next = ptr.next
		ptr.next = temp

		return True



lst = singlylinkedlist()
lst.push_back(2)
lst.push_back(5)
lst.push_back(7)

print(len(lst))
lst.display()

lst.insert(3,1)
lst.display()


lst.insert(4,4)
lst.display()