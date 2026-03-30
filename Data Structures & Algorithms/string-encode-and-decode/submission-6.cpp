class Solution {
public:

    string encode(vector<string>& strs) {
        if (strs.size() == 0) {
            return "";
        }

        std::string res;

        for (std::string& word : strs) {
            res += std::to_string(word.size()) + "#" + word; 
        }

        return res;
    }

    vector<string> decode(string s) {
        std::vector<std::string> res;

        int i = 0;

        while (i < s.size()) {
            int j = i;

            while (s[j] != '#') j++;
            int length = stoi(s.substr(i, j - i));
            j++;
            res.push_back(s.substr(j, length));

            i = j + length;
        }

        return res;
    }
};