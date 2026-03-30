class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        std::vector<int> answer; 
        for (int i = 0; i < nums.size(); i++) {
            int to_find = target - nums[i]; 
            for (int j = 0; j < nums.size(); j++) {
                if (nums[j] == to_find && j != i) {
                    answer.push_back(i); 
                    answer.push_back(j); 
                    return answer; 
                }
            }
        } 
        return answer;   
    }
};
