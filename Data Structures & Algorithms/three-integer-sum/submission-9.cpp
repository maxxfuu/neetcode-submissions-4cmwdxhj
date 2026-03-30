class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        std::vector<std::vector<int>> result;
        std::set<std::vector<int>> my_set;

        std::sort(nums.begin(), nums.end()); // O(log n)

        for (int i = 0; i < nums.size(); i++) {
            int j = i + 1, k = nums.size() - 1; 

            while (j < k) {
                if (nums[i] + nums[j] + nums[k] == 0) {
                    std::vector temp = {nums[i] , nums[j] , nums[k]};
                    std::sort(temp.begin(), temp.end());

                    if (my_set.find(temp) == my_set.end()) {
                        my_set.insert(temp);
                        result.push_back(temp); // hash set instead
                    }
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