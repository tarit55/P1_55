class Stack:
	def __init__(self):
		self.Stack=[]
	def is_empty(self):
		l=len(self.Stack)
		if l==0:
			return True
		else:
			return False
	def push(self,value):
		return self.Stack.append(value)
	def pop(self):
		if self.is_empty():
			print("Stack underflow")
		else:
			return self.Stack.pop()
	def peek(self):
		if self.is_empty():
			print("Stack empty")
		else:
			return self.Stack[-1]

s1=Stack()
s1.push(10)
s1.push(100)
print(s1.peek())
print(s1.pop())