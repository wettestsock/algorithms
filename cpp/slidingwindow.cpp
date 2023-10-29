#include <iostream>
#include <vector>
#include <string>

/*
SLIDING WINDOW ALGORITHM

COMMON IN CODING

g++ slidingwindow.cpp -o out\slidingwindow
out\slidingwindow

g++ slidingwindow.cpp -o linout/slidingwindow
out/slidingwindow

*/

struct node{
  int data;
  node* next;  

};

class linked_list{
    node* head = nullptr;
    public:
    linked_list(){

    }
    
};


class Solution{
    public:
    static std::vector<int> slide_window(const std::vector<int>& arr, const int& k) {
        std::vector<int> output;

        int curr = 0;
        for(int i=0; i<k; ++i){ //gets the current (initial sum)
            curr += arr[i];
        }
        output.push_back(curr);
        for(int i =0; i<arr.size()-k; ++i) {
            output.push_back(curr - arr[i] + arr[i+k]);
        };
    
        return output;

    }
};

template<typename T>
std::ostream& operator<<(std::ostream& out, const std::vector<T>& temp) {
    int i;
    for(i=0; i<temp.size()-1; ++i) {
        out<< temp[i] << ' ';
    }
    out<<temp[i]<<'\n';
    return out;
}


int main() {
    std::cout<< Solution::slide_window({4,3,2,5,3,5},2);
}