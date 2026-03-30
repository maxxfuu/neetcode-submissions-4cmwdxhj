class Solution {
public:
    int carFleet(int target, vector<int>& position, vector<int>& speed) {
        std::stack<double> stk;
        std::vector<std::pair<int, double>> ps;

        for (int i = 0; i < position.size(); i++) {
            int p = position[i];
            double t = (target - position[i]) * 1.0 / speed[i];
            ps.push_back({p, t});
        }

        std::sort(ps.begin(), ps.end());

        for (int i = ps.size() - 1; i >= 0; i--) {
            if (stk.empty() || ps[i].second > stk.top()) {
                stk.push(ps[i].second);
            }

        }

        return stk.size();
    }

};