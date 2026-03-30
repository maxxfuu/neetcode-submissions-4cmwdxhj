class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        std::unordered_set<int> my_set(nums.begin(), nums.end()); 
        int longest = 0; 

        for (int i = 0; i < nums.size(); i++) {
            if (my_set.find(nums[i] - 1) == my_set.end()) {
                int length = 1;

                while(my_set.find(nums[i] + length) != my_set.end()) {
                    length += 1; 
                }

                longest = std::max(longest, length);
            }
        }
        return longest; 
    }
};