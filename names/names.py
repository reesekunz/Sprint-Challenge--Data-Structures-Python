
import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()


class BinarySearchTree:
    def __init__(self, value):
        self.value = value  # root node
        self.left = None
        self.right = None

    def insert(self, value):
        if self.value is None:
            self.value = value  # error handling
            # Go left
        elif value < self.value:
            if self.left is None:
                self.left = BinarySearchTree(value)
            else:
                self.left.insert(value)
        elif value < self.value:
            if self.right is None:
                self.right = BinarySearchTree(value)
            else:
                self.right.insert(value)
        elif self.value is value:
            return self.value

    def contains(self, target):
        if self.value == target:
            return True  # Base case - if root node is the same as the target
        elif target < self.value:
            if self.left is not None:
                return self.left.contains(target) if self.left is not None else False
        else:
            return self.right.contains(target) if self.right is not None else False


duplicates = []
for name_1 in names_1:
    bstree = BinarySearchTree(name_1[0])
    bstree.insert(name_1)
    for name_2 in names_2:
        if name_1 == name_2:
            duplicates.append(name_1)

end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish with no restrictions on techniques or data
# structures?
