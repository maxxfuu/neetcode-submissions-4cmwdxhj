class Solution {
public:
    bool isAnagram(string s, string t) {
        // key, value, typeName 
       std::unordered_map<char, int> map1;
       std::unordered_map<char, int> map2; 

        if (s.size() != t.size()) { 
            return false; 
        }

        for(int i = 0; i < s.size(); i++) { 
           map1[s[i]] += 1; 
           map2[t[i]] += 1;  
        }

        for(char character : s) { 
            if (map1[character] != map2[character]) { 
                return false; 
            }
        }
        return true; 
    }
};


// Constraints 
// - The length has to be the same for both string 
// - the letters type and amount have to be the same 

// unordered_map 


