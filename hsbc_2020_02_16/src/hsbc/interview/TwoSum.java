package hsbc.interview;

import java.util.HashMap;
import hsbc.interview.InvalidInputException;
import java.lang.*;

/*
Since we are required to return the indicies, sorting is not a very good option

loop through array, use a dictionary(Hashmap) to record the previous integers and their indices

	key:  previous saw numbers
	value:  the indices for previous saw values

If target – current_num in dictionary, then that means there is a previous value that adds current value to the required target.

The conner case we should check is if the input array is null or less than two elements.



run time: O(n), we are visiting each number exactly once.

Space complexity: O(n), we are storing every number and their indices.

where n is the number of integers in the array

*/


public class TwoSum {

	public int[] twoSum(int[] array, int target) throws InvalidInputException {

		// abnormal input check
		if (array == null || array.length <= 1) {
			throw new InvalidInputException("input is null or does not have enough elements");
		}


		HashMap<Integer,Integer> map = new HashMap<Integer, Integer>();
		for (int i = 0; i < array.length; i++) {
			if (map.get(target - array[i]) != null) {		// we found a pair
				return new int[] {map.get(target-array[i]).intValue(), i};
			}
			map.put(array[i], i);
		}

		// if control goes here, means we have not found a soln:
		// since we are guranteed to have one soln, we should raise exception
		throw new InvalidInputException("Input is guaranteed to have one exception, however none was found");
	}

}