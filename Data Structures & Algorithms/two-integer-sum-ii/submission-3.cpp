class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        int i = 0, j = numbers.size() - 1; 

        while(i < j) {
            int total = numbers[i] + numbers[j];

            if (total == target) {
                return {i + 1, j + 1};
            } else {
                if (total > target) {
                    j--;
                } else {
                    i++;
                }
            }
        }
        return {};
    }
};

/*
problem: given an array in ascending order, return the index of two numbers of two distinct index that add up to target
input: int vector & int target
output: int vector, representing the index pair 

constraint: 
- 2 - 1000 numbers 
- number and target can range from -1000 to -1000

pattern:
use two pointer approach 
bottleneck: how do we determine how to move the left and right pointers 

we can set i on the left side and j on the right side. 
if total is greater than target
    - decrease total by j--;
    - increase total by i++;


*/