class Queue:
	def __init__(self):
		self.Queue=[]
	def is_empty(self):
		l=len(self.Queue)
		if l==0:
			return True
		else:
			return False
	def insert(self,value):
		return self.Queue.append(value)
	def delete(self):
		if self.is_empty():
			print("Queue underflow")
		else:
			return self.Queue.pop(0)
	def front(self):
		if self.is_empty():
			print("Queue empty")
		else:
			return self.Queue[0]
	def end(self):
		if self.is_empty():
			print("Queue empty")
		else:
			return self.Queue[-1]

q1=Queue()
q1.insert(1)
q1.insert(2)
print(q1.front())
print(q1.delete())
q1.insert(4)
print(q1.end())
