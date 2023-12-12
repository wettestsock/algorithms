#include <iostream>
#include <vector>

/*
2 SUM
2 NUMBERS THAT ADD TO THE TARGET

clang++ 2sum.cpp -o linout/2sum
linout/2sum

*/

class Solution {
public:
    static std::vector<int> twoSum(const std::vector<int>& nums, const int& target) {
        for(int i=0; i<nums.size(); ++i){
            int diff = target-nums[i];
            for(int z=i+1; z<nums.size(); ++z){
                if(nums[z]==diff) return {i, z};
            }
            
        }
        //default
        return {0,0};
        
    }
};

int main(){
    std::cout << '{';
    for(int i: Solution::twoSum({2, 7}, 9)){
        std::cout << i << ',';
    }
    std::cout<<'}';
}