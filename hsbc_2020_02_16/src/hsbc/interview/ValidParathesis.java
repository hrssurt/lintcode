package hsbc.interview;

import java.lang.*;
import java.util.Stack;

/*
	use a stack, when encounter open parenthesis, push to stack, when encounter close parenthesis, pop from stack. 
		
	If the popped parenthesis is different type from encountered the close parenthesis,  return False

	At the end the program return True as the above loop does not return False.

	Run time: O(n), space complexity: O(n), when n is the length of the input string.

	Run time is O(n) because we only need to loop trough the string once.
	Space is O(n) as we need store previously visited parenthesis, and in the worst case it is O(n)


*/



public class ValidParathesis {
	public Boolean ValidParathesis(String s) {
		Stack<Character> stack = new Stack<Character>();

		for (Character c: s.toCharArray()) {
			if ("[{(".contains(String.valueOf(c))) {
				stack.push(c);
			} else if ("]})".contains(String.valueOf(c))) {
				Character top = stack.pop();
				if (!is_valid(top, c)) {
					return false;
				} 
			}
		}
		return true;

	}

	public Boolean is_valid(Character c1, Character c2) {
		return (c1 == '(' && c2 == ')') || (c1 == '{' && c2 == '}') || (c1 == '[' && c2 == ']');
	}

}