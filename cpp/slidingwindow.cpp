#include <iostream>
#include <vector>
#include <string>

/*
SLIDING WINDOW ALGORITHM

COMMON IN CODING

g++ slidingwindow.cpp -o out\slidingwindow
g++ out\slidingwindow
*/

class Solution{
    public:
    static std::vector<int> slide_window(const std::vector<int>& arr, const int& k) {
        std::vector<int> output = {0};
        for(int i=0; i<k; ++i){
            output[0] += arr[i];
        }
        return output;

    }
};


int main() {
    std::cout<<Solution::slide_window({4,5,3,5,4}, 2)[0];


}