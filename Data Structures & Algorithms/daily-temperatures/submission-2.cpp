class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
        std::vector<int> result(temperatures.size(), 0);

        for (int i = 0; i < temperatures.size() - 1; i++) {
            for (int j = i + 1; j < temperatures.size(); j++) {
                if (temperatures[i] < temperatures[j]) {
                    result[i] = j - i;
                    break; 
                }
            }
        }

        return result;
    }
};
