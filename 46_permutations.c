class Solution {
public:
    void swap(int& in1, int& in2){
        int temp = in1;
        in1 = in2;
        in2=temp;
    }

    void perm(vector<int>& nums, int curr, vector<vector<int>>& out){
        if(curr == nums.size()-1){
            out.push_back(nums);
            return;
        }

        for(int i = curr; i<nums.size(); i++){
            swap(nums[i], nums[curr]);
            perm(nums, curr+1, out);
            swap(nums[i], nums[curr]); //swaps them back
        }
    }

    vector<vector<int>> permute(vector<int>& nums) {
        vector<vector<int>> out;
        perm(nums, 0, out);

        return out;


    }
};
