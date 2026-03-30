class Solution {
public:
    int search(vector<int>& nums, int target) {
        int left = 0; // left index
        int right = nums.size() - 1; // right index  

        while(left <= right) { // condition to end the while loop 
            int middle = left + ((right - left) / 2); 
            if(nums[middle] == target) { 
                return middle; 
            } 

            if(nums[middle] < target) { 
                left = middle + 1; 
            } else {
                right = middle - 1;
            }

        }
        return -1; 
    }
};
