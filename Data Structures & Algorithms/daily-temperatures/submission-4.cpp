class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
        std:vector<int> res(temperatures.size(), 0);
        std::stack<int> stk; // indicies 

        for (int i = 0; i < temperatures.size(); i++) {
            while (stk.size() && temperatures[stk.top()] < temperatures[i]) {
                res[stk.top()] = i - stk.top();
                stk.pop();
            }
            stk.push(i);
        }
        return res;
    }
};

/*
[30,38,30,36,35,40,28]
[38, 36, ]

result = {0, 1, 0, 1, 1}

<>

*/