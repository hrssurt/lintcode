package hsbc.interview;

import java.lang.*;
import java.util.Arrays;

import hsbc.interview.*;
import org.omg.Messaging.SYNC_WITH_TRANSPORT;

import javax.swing.plaf.synth.SynthTextAreaUI;

import static org.junit.Assert.*;
public class Main {
	public void testQuestionOne() {
		ValidParathesis vp = new ValidParathesis();
		String s1 = "()";
		String s2 = "([])";
		String s3 = "([{}])";
		String s4 = "([(){}{}])";
		String s5 = "([{{}])";

		System.out.println("Question 1 ******************");
		System.out.printf("Input: %s, Valid: %s\n", s1, vp.ValidParathesis(s1));
		System.out.printf("Input: %s, Valid: %s\n", s2, vp.ValidParathesis(s2));

		System.out.printf("Input: %s, Valid: %s\n", s3, vp.ValidParathesis(s3));
		System.out.printf("Input: %s, Valid: %s\n", s4, vp.ValidParathesis(s4));
		System.out.printf("Input: %s, Valid: %s\n", s5, vp.ValidParathesis(s5));

		System.out.println();


	}

	public void testQuestionTwo() {
		Node root = new Node(1);
		root.leftChild = new Node(2);
		root.rightChild = new Node(3);
		root.leftChild.leftChild = new Node(4);
		root.leftChild.rightChild = new Node(5);
		root.rightChild.leftChild = new Node(6);
		root.rightChild.rightChild = new Node(7);


		System.out.println("Question 2***************");
		System.out.println("Before inverting.....");
		System.out.println(root.val);
		System.out.print(root.leftChild.val);
		System.out.print(root.rightChild.val);
		System.out.println();
		System.out.print(root.leftChild.leftChild.val);
		System.out.print(root.leftChild.rightChild.val);
		System.out.print(root.rightChild.leftChild.val);
		System.out.print(root.rightChild.rightChild.val);
		System.out.println();


		InvertBinaryTree ibt = new InvertBinaryTree();
		ibt.invertBinaryTree(root);
		System.out.println("After inverting.....");

		System.out.println(root.val);
		System.out.print(root.leftChild.val);
		System.out.print(root.rightChild.val);
		System.out.println();
		System.out.print(root.leftChild.leftChild.val);
		System.out.print(root.leftChild.rightChild.val);
		System.out.print(root.rightChild.leftChild.val);
		System.out.print(root.rightChild.rightChild.val);
		System.out.println();

	}

	public void testQuestionThree() {
		int target = 5;
		int[] test1 = {1,2,4};
		int[] test2 = {0,2, 4, 11, 4, -6};
		int[] test3 = {-2,2,-4, 4, 1, 0};

		TwoSum ts = new TwoSum();

		System.out.println("Question 3***************");
		try {
			System.out.println("Target is 5");
			System.out.println(Arrays.toString(test1));
			System.out.println(Arrays.toString(ts.twoSum(test1, target)));
			System.out.println(Arrays.toString(test2));
			System.out.println(Arrays.toString(ts.twoSum(test2, target)));
			System.out.println(Arrays.toString(test3));
			System.out.println(Arrays.toString(ts.twoSum(test3, target)));

		} catch (InvalidInputException e){
			System.out.println();
		}


	}

	public static void main(String argv[]) {
		System.out.println("Hello World");
		Main m = new Main();
		m.testQuestionOne();
		m.testQuestionTwo();
		m.testQuestionThree();

	}
}