class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        std::vector<int> res;

        for (int i = 0; i < numbers.size() - 1; i++) {
            for (int j = i + 1; j < numbers.size(); j++) {
                if (numbers[i] + numbers[j] == target) {
                    res.push_back(i + 1);
                    res.push_back(j + 1);
                }
            }
        }
        return res;
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