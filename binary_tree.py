class Vertex:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self, root):
        self.root = root

    def pre_order(self, start, path):
        if start is not None:
            path += f"{start.data} -> "
            path = self.pre_order(start=start.left, path=path)
            if start is self.root:
                path += "\n"
            path = self.pre_order(start=start.right, path=path)
        return path

    def pre_order_print(self, start):
        if start is None:
            return
        else:
            print(f"{start.data} -> ", end="")
            self.pre_order_print(start=start.left)
            if start is self.root:
                print()
            self.pre_order_print(start=start.right)

    def in_order_print(self, start):
        if start is None:
            return
        else:
            self.in_order_print(start=start.left)
            print(f"{start.data} -> ", end="")
            self.in_order_print(start=start.right)

    def post_order_print(self, start):
        if start is None:
            return
        else:
            self.post_order_print(start=start.left)
            self.post_order_print(start=start.right)
            print(f"{start.data} -> ", end="")


if __name__ == '__main__':
    tree = BinaryTree(root=Vertex("F"))
    tree.root.left = Vertex("B")
    tree.root.left.left = Vertex("A")
    tree.root.left.right = Vertex("D")
    tree.root.left.right.left = Vertex("C")
    tree.root.left.right.right = Vertex("E")
    tree.root.right = Vertex("G")
    tree.root.right.right = Vertex("I")
    tree.root.right.right.left = Vertex("H")
    # print(tree.pre_order(start=tree.root, path=""))
    # tree.pre_order_print(start=tree.root)
    print("In-order")
    tree.in_order_print(start=tree.root)
    print("\nPost-order")
    tree.post_order_print(start=tree.root)

