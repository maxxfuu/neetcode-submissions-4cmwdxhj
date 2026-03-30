class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int i = 0, j = 0;
        std::unordered_set<char> charSet;
        int total = 0;

        while (i <= j && j < s.length()) {
            while (charSet.find(s[j]) != charSet.end()) {
                charSet.erase(s[i]);
                i++;
            } 
            charSet.insert(s[j]);
            total = std::max(total, j - i + 1);
            j++;
        }

        return total;
    }
};
