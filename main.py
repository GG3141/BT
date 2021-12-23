import binaryTree as bt

root = bt.BTree.BNode(12)
root.insert(5)
root.insert(8)
root.insert(9)
root.insert(6)

#			12
#	    /\
#	   /  \
#	  7    8
#	 /		  \
#	6		     9

root.printTree()
print(root.findval(7))