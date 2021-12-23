if __name__ != "__main__":

	class BTree:
		class BNode:
			def __init__(self, data):
				self.left = None
				self.right = None
				self.data = data

			def insert(self, val):
				if self.data:
					if val < self.data:
						if self.left is None:
							self.left = BTree.BNode(val)
						else:
							self.left.insert(val)
					elif val > self.data:
						if self.right is None:
							self.right = BTree.BNode(val)
						else:
							self.right.insert(val)
				else:
					self.data = val

			def findval(self, lkpval):
				if lkpval < self.data:
						if self.left is None:
								return str(lkpval)+" Not Found"
						return self.left.findval(lkpval)
				elif lkpval > self.data:
						if self.right is None:
								return str(lkpval)+" Not Found"
						return self.right.findval(lkpval)
				else:
						print(str(self.data) + ' Is Found')

			def printTree(self):
					if self.left:
							self.left.printTree()
					print(self.data)
					if self.right:
							self.right.printTree()
