class Solution {
public:
    void sum(const vector<int>& candidates, vector<int> curr, int i, int curr_sum, int target, vector<vector<int>>& out){

        if (curr_sum == target){
            out.push_back(curr);
            return;
        }
        
        if (curr_sum>target || i >= candidates.size()){
            return;
        } 
        
        
        sum(candidates, curr, i+1, curr_sum, target, out);

        curr.push_back(candidates[i]);
        sum(candidates, curr, i, curr_sum+candidates[i], target, out);
 
        return;
    }


    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        vector<vector<int>> out;
        vector<int> temp;
        sum(candidates, temp, 0, 0, target, out);
        return out;
    }
};
