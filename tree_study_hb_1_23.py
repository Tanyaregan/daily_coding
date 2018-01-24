class Node(object):
    """A binary tree node"""

    def __init__(self, data, left_kid=None, right_kid=None):
        self.data = data
        self.left_kid = left_kid
        self.right_kid = right_kid

    @classmethod
    def create_sample_BST(cls):
        """Create and return a sample BST.

                        F
                      /   \
                    /       \
                  /           \
                 B             G
               /   \             \
              A     D             I
                  /   \         /
                 C     E       H

        """

        a = cls("A")
        c = cls("C")
        e = cls("E")
        h = cls("H")
        d = cls("D", left_kid=c, right_kid=e)
        i = cls("I", left_kid=h)
        b = cls("B", left_kid=a, right_kid=d)
        g = cls("G", right_kid=i)
        f = cls("F", left_kid=b, right_kid=g)
        return f



    def print_preorder(self):
        """Print the nodes in the tree rooted at self, using pre-order
           traversal.

           Example use: printing out a file structure.

           >>> tree = Node.create_sample_BST()
           >>> tree.print_preorder()
           F B A D C E G I H

        """

        print self.data,

        if self.left_kid:
            self.left_kid.print_preorder()

        if self.right_kid:
            self.right_kid.print_preorder()

    def print_inorder(self):
        """Print the nodes in the tree rooted at self, using in-order
           traversal.

           Example use: printing out BST nodes in order.

           >>> tree = Node.create_sample_BST()
           >>> tree.print_inorder()
           A B C D E F G H I

        """

        if self.left_kid:
            self.left_kid.print_inorder()

        print self.data,

        if self.right_kid:
            self.right_kid.print_inorder()

    def print_postorder(self):
        """Print the nodes in the tree rooted at self, using post-order
           traversal.

           Example use: rm -rf some-directory/

           >>> tree = Node.create_sample_BST()
           >>> tree.print_postorder()
           A C E D B H I G F

        """

        if self.left_kid:
            self.left_kid.print_postorder()

        if self.right_kid:
            self.right_kid.print_postorder()

        print self.data,

    def check_height(self):
        """Checks to see if the tree is balanced.
        balanced = height of any 2 sub trees never differs by more than one
        returns TRUE or FALSE.

            tree = Node.create_sample_BST()
            tree.check_order()
            4
            """

        # start heights at zero
        # figure out the height of the trees, compare the heights

        def check_height(Node):
            """Helper function for check balance.

            >>> tree = Node.create_sample_BST()
            >>> tree.check_order()
            4

            """
            left_height = right_height = 0

            if self.left_kid:
                self.left_kid.check_height()
            if self.right_kid:
                self.right_kid.check_height()

        if abs(left_height - right_height) > 1:
            return 'FALSE'

        if self.left_kid and not self.right_kid.check_balance():
            return 'FALSE'

        if self.right_kid and not self.right_kid.check_balance():
            return 'FALSE'

        return 'TRUE'









