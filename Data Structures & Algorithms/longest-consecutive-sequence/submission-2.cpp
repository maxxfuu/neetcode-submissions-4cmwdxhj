class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        std::unordered_set<int> numSet(nums.begin(), nums.end());
        int longest = 0; 

        for (const int& num : numSet) {
            // if cannot find the starting number, then itself is the starting number
            if (numSet.find(num - 1) == numSet.end()) {
                // set the count to 1
                int length = 1; 

                while (numSet.find(num + length) != numSet.end()) {
                    length += 1; 
                }

                longest = std::max(longest, length);
            }
        }
        
        return longest;
    }
};
