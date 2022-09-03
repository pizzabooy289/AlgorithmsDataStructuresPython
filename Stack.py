#python 3.5.2

class Stack:
     def __init__(self):
         self.items = []

     def isEmpty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)

     def pop(self):
         return self.items.pop()

     def peek(self):
         return self.items[len(self.items)-1]

     def size(self):
         return len(self.items)

                
s=Stack()

print('isEmpty:',s.isEmpty())
print('-'*20)
s.push(4)
print('push(4): s=',s.items)
s.push('dog')
print('push(dog): s=',s.items)
s.push(8.4)
print('push(8.4): s=',s.items)
print('s=',s.items)
print('-'*20)
print('peek:',s.peek())
print('-'*20)
s.push(True)
print('push(True): s=',s.items)
print('s=',s.items)
print('size:',s.size())
print('-'*20)
print('s=',s.items)
print('pop:',s.pop())
print('pop:',s.pop())
print('s=',s.items)
print('size:',s.size())


'''
OUTPUT:
isEmpty: True
--------------------
push(4): s= [4]
push(dog): s= [4, 'dog']
push(8.4): s= [4, 'dog', 8.4]
s= [4, 'dog', 8.4]
--------------------
peek: 8.4
--------------------
push(True): s= [4, 'dog', 8.4, True]
s= [4, 'dog', 8.4, True]
size: 4
--------------------
s= [4, 'dog', 8.4, True]
pop: True
pop: 8.4
s= [4, 'dog']
size: 2
'''
