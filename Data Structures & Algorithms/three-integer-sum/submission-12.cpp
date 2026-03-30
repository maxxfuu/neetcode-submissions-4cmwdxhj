class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        std::vector<std::vector<int>> result;
        std::sort(nums.begin(), nums.end()); // O(log n)

        for (int i = 0; i < nums.size(); i++) {
            if (i > 0 && nums[i] == nums[i - 1]) continue;

            int j = i + 1, k = nums.size() - 1; 
            while (j < k) {
                int sum = nums[i] + nums[j] + nums[k];
                if (sum == 0) {
                    result.push_back({nums[i], nums[j], nums[k]});

                    while (j < k && nums[j] == nums[j + 1]) j++;
                    while (j < k && nums[k] == nums[k - 1]) k++;

                    k--;
                    j++;
                } else { // not equal to 0 
                    if (nums[i] + nums[j] + nums[k] > 0) {
                        k--;
                    } else {
                        j++;
                    }
                }
            }
        }

        return result;
    }
};


/*
problem: find distinct triplets within nums and their sum is 0
input: int vector
output: vector of vectors that holds integers 
contraits: 
- nums 3 to 1000 integers 
- value range -10^5 to 10^5

Pattern:
for loop w/ two pointer 

before storing validate if triplet exists already through sort

// -4,-1,-1,0,1,2


*/