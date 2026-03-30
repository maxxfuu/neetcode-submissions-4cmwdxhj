class Solution {
public:
    int maxArea(vector<int>& heights) {
        int total = 0;

        for (int i = 0; i < heights.size(); i++) {
            for (int j = i + 1; j < heights.size(); j++) {
                int minHeight = std::min(heights[i], heights[j]);
                int width = j - i; 

                int temp = minHeight * width; 
                total = std::max(temp, total);
            }
        }
        return total;
    }
};

/*
Problem: Find the largest amount of water that can be contained

Input: int vector.
Output: int.

Constraits:
1. height length 2 to 1000 inclusive
2. bar itself can be 0 to 100 inclusive



Pattern: 
two pointers, lowest bar * length between bars

Brute Force:
- try every pair of heights possible O(n^2)

*/
