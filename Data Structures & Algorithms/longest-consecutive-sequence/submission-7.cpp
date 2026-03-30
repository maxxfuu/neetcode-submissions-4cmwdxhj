class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        std::unordered_set<int> my_set(nums.begin(), nums.end()); 
        int longest = 0; 

        for (const auto& num : my_set) {
            if (my_set.find(num - 1) == my_set.end()) {
                int length = 1;

                while(my_set.find(num + length) != my_set.end()) {
                    length += 1; 
                }

                longest = std::max(longest, length);
            }
        }
        return longest; 
    }
};