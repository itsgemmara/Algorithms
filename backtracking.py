"""Print all paths from the root to leaf nodes of a binary tree
		  a
		/   \
	   /     \
	  b       c
	 / \     / \
	d   e   f   g
		   /     \
		  h       i
"""

from collections import deque


class Node:
	def __init__(self, data, left=None, right=None):
		self.data = data
		self.left = left
		self.right = right


class PrintAllPath:
	def __init__(self, nodes):
		self.nodes = nodes

	def is_leaf(self, node):
		if not node.right and not node.left:
			return True

	def create_path(self):
		stack = deque()
		stack.append((self.nodes, ''))
		while stack:
			node, _path = stack.popleft()
			if self.is_leaf(node):
				print(_path)
			if node.left:
				if _path:
					path = _path + f'-->{node.left.data}'
				if not _path:
					path = str(node.data) + '-->' + str(node.left.data)
				stack.appendleft((node.left, path))

			if node.right:
				if _path:
					path = _path + f'-->{node.right.data}'
				if not _path:
					path = str(node.data) + '-->' + str(node.right.data)
				stack.appendleft((node.right, path))


if __name__ == '__main__':
	root = Node('a')
	root.left = Node('b')
	root.right = Node('c')
	root.left.left = Node('d')
	root.left.right = Node('e')
	root.right.left = Node('f')
	root.right.right = Node('g')
	root.right.left.left = Node('h')
	root.right.right.right = Node('i')

	print_path = PrintAllPath(root)
	print_path.create_path()