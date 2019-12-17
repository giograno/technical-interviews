class TreeNode:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def visit(self):
        print(self.value)

    def __str__(self):
        return '(' + str(self.left) + ':L ' + "V:" + str(self.value) + " R:" + str(self.right) + ')'


def initiate_array_to_binary(array):
    return array_to_binary(array, 0, len(array) - 1)


def array_to_binary(array, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    root = TreeNode(array[mid])
    root.left = array_to_binary(array, start, mid - 1)
    root.right = array_to_binary(array, mid + 1, end)
    return root


def example_tree():
    testArray = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 15, 18, 22, 43, 144, 515, 4123]
    return initiate_array_to_binary(testArray)



