class Solution {
public:
    bool isAnagram(string s, string t) {
        std::unordered_map<char, int> my_map; 

        if (s.size() != t.size()) {
            return false;  
        } 

        for (int i = 0; i < s.size(); i++) {
            my_map[s[i]] += 1; 
            my_map[t[i]] -= 1; 
        } 

        for (auto itr = my_map.begin(); itr != my_map.end(); itr++) {
            if (itr->second != 0) {
                return false; 
            }
        }

        return true; 
    }
};
