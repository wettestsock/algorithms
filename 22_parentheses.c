class Solution {
public:
    void parentheses(int n, int open, int close, string input, vector<string>& arr){
        if (open+close == n*2){ //base case
            arr.push_back(input);
            return;
        }
        
        if(open>close){
            parentheses(n, open, close+1, input+")", arr);

        }

        if (open < n){
            parentheses(n, open+1, close, input+"(", arr);
        }
        
    }
    vector<string> generateParenthesis(int n) {
            vector<string> out;
            
            parentheses(n, 0, 0, "", out);


            return out;
    }
};
