//
// Created by ruijie on 2020-03-05.
//



#include "find_first_unique.h"



string find_first_unique(vector<string> v) {
    unordered_map<string, int> counter;
    for(string s: v) {
        counter[s] ++;
    }
    for (string s: v) {
        if (counter[s] == 1) {
            return s;
        }
    }
    return "";
}


int main ()
{

    vector<string> testcase1{ "a", "a", "a" };
    cout << find_first_unique(testcase1) << endl;   // empty line

    vector<string> testcase2{ "a", "a", "c" };
    cout << find_first_unique(testcase2) << endl;   // c

    vector<string> testcase3{ "a", "b", "c" };      // a
    cout << find_first_unique(testcase3) << endl;

    vector<string> testcase4{  "a", "b", "c", "c" , "a"};      // b
    cout << find_first_unique(testcase4) << endl;

    vector<string> testcase5{  "a", "a", "c", "c" , "a"};      // empty line
    cout << find_first_unique(testcase5) << endl;

    return 0;
}

