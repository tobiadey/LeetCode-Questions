def preOrder(root):
    #Write your code here
    '''
    Traverse binary search tree- prints in ascending order
    '''

    if root:
        print(root.info, end=' ')
        preOrder(root.left)
        preOrder(root.right)

def postOrder(root):
    #Write your code here

    if root:
        preOrder(root.left)
        preOrder(root.right)
        print(root.info, end=' ')

def inOrder(root):
    #Write your code here

    if root:
        preOrder(root.left)
        print(root.info, end=' ')
        preOrder(root.right)
    