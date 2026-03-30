class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        std::set<int> my_set;

        for (auto val : nums) {
            if (my_set.find(val) == my_set.end()) {
                my_set.insert(val);
            } else {
                return true;
            }
        }
        return false;
    }
};