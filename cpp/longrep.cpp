#include <iostream>
#include <vector>
#include <string>
#include <unordered_set>

/*
LONGEST SUBSTRING WITHOUT REPEATING CHARACTERS

SLIDING WINDOW TECHNIQUE
with a set

clang++ longrep.cpp -o linout/longrep
linout/longrep

i and j pointer poitns to begin ning of string
and output int 

init a set that keeps track of unique characters
if a character is not in a set, add p to it, and compute the length of window
length will always be i-j+1 , +1 because i and j are indeces

move i , compute new length 
if s[i] is in a set, move j to i, remove all values in the set, and add the value s[i]

output will be maximum of output and current window
*/

class Solution {
public:
    static int lengthOfLongestSubstring(const std::string& s) {
        if(!s.length()) return 0;

        int i=0, j=0, max = 0;
        //key, value
        std::unordered_set<char> set;
        for(int i=0; i<s.length(); ++i){
            char curr = s.at(i);
            while(set.contains(curr)){
                set.erase(s.at(j));
                ++j;
            }
            set.insert(curr);
            max = std::max(max, i-j+1);
            }
        return max;
        }
};

int main(){

    std::cout<< Solution::lengthOfLongestSubstring("abcabcdef");


}