/****************************  TITLE  *****************************/
/*488  Happy Number.java*/



/****************************  DESCRIPTION  *****************************/
/*
Write an algorithm to determine if a number is happy.
*/



/****************************  EXAMPLES  *****************************/
/*
Input:19
Output:true
Explanation:

19 is a happy number

    1^2 + 9^2 = 82
    8^2 + 2^2 = 68
    6^2 + 8^2 = 100
    1^2 + 0^2 + 0^2 = 1


*/



/****************************  CODE  *****************************/
import java.util.*;
import java.io.*;

public class Solution {
    /**
     * @param n: An integer
     * @return: true if this is a happy number or false
     */
    public boolean isHappy(int n) {
        Set<Integer> seen = new HashSet<Integer>();
        seen.add(n);
        while (n!= 1) {
            n = sumDigits(n);
            if (seen.contains(n)) {
                return false;
            }
            seen.add(n);
        }
        return true;
    }
    
    public int sumDigits(int n) {
        int s = 0;
        while (n != 0) {
            int lastDigit = n % 10;
            s += lastDigit * lastDigit;
            n /= 10;
        }
        return s;
    }
}
