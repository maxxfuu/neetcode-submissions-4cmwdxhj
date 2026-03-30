class Solution {
public:
    int maxProfit(vector<int>& prices) {
        if (prices.size() < 2) {
            return 0;
        }

        int i = 0, j = 1;
        int maxProfit = 0;

        while (j < prices.size()) {
            if (prices[i] > prices[j]) {
                i = j;
            } else {
                maxProfit = std::max(maxProfit, prices[j] - prices[i]);
            }
            j++;
        }
        return maxProfit;
    }
};

// [10,1,5,6,7,1]
//     i       j