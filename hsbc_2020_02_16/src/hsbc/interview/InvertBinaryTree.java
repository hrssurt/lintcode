package hsbc.interview;
import hsbc.interview.Node;

/*

Tree is a recursive data structure so using recursion is usually a good choice
base case: node is null, in this case do nothing
otherwise: swap the left child and right child, and call recursion on them

run time: O(n), as for each node, as we visit each node exactly once. N is the number of nodes in the tree.

space complexity: O(n). Because when we use recursion, for each function call, we will add one entry in the call stack. In this case we will make exactly n function calls, 
and not until we reach the leaf node than we can pop stuff from the call stack. 

In the worst case, when tree is extremely unbalanced, we have n entries in the call stack.  So the space complexity is exactly O(n), same as run time.
*/



public class InvertBinaryTree {
	public void invertBinaryTree(Node root) {
		if (root == null) {
			return;
		} else {
			// swap
			Node temp = root.leftChild;
			root.leftChild = root.rightChild;
			root.rightChild = temp;

			invertBinaryTree(root.leftChild);	// recursion
			invertBinaryTree(root.rightChild);   // recursion
		}
	}
}