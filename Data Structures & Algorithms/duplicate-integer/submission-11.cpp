class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        std::unordered_set<int> my_set;  
        
        if (nums.size() == 0) {
            return false; 
        } 

        for (int i = 0; i <= nums.size() - 1; i++) {
            if (my_set.find(nums[i]) == my_set.end()) {
                my_set.insert(nums[i]); 
            } else {
                return true; 
            }
        } 
        return false;  
    }
};
