# Desafío 1: jerarquía de sistema de archivos
"""
Dado un árbol binario que representa un sistema de archivos, 
imprimir la estructura de forma jerárquica. 
Salida esperada:  
|-- Folder_A
|   |-- File_A1
|   |-- File_A2
|-- Folder_B
    |-- File_B1
"""

# Clase para el desafío
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Crear el sistema de archivos
root = TreeNode("Root")

root.left = TreeNode("Folder_A")
root.right = TreeNode("Folder_B")

root.left.left = TreeNode("File_A1")
root.left.right = TreeNode("File_A2")

root.right.left = TreeNode("File_B1")

def in_order_traversal(root, prefix="", is_root=True, is_last=False):

    # if my root is None, do not print anything
    if root is None:
        return

    # print my current node
    if is_root:
        print(root.value)
    else:
        print(prefix + "|-- " + root.value)

    # define the prefix for the children/leafs
    if is_root:
        child_prefix = ""
    elif is_last:
        child_prefix = prefix + "    "
    else:
        child_prefix = prefix + "|   "

    if root.left:
        in_order_traversal(
            root.left,
            child_prefix,
            False,
            root.right is None
        )

    if root.right:
        in_order_traversal(
            root.right,
            child_prefix,
            False,
            True
        )

in_order_traversal(root)


