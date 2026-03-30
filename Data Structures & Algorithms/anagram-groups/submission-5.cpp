class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        std::unordered_map<std::string, std::vector<string>> result; 

        for (auto& word : strs) {
            std::vector<int> count(26, 0); // size and value
            for (char character : word) {
                count[character - 'a']++; 
            }

            // convert vector inot a unqiue key
            std::string key = ""; 
            for (int num : count) {
                key += to_string(num) + ",";
            }

            // create key
            result[key].push_back(word);
        }

        // Move the grouped words into the final result vector  
        std::vector<std::vector<string>> output; 
        for (const auto& pair : result) {
            output.push_back(pair.second);     
        }

        return output;
    }
};
