class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums) {
        const set = new Set();
        for (const item of nums) {
            if (set.has(item)) {
                return true;
            }
            set.add(item)
        }
        return false;
    }
}
