class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        std::stack<int> stk;
        std::stack<std::string> op;

        for (auto token : tokens) {
            if (token != "+" && token != "-" && token != "*" && token != "/") {
                stk.push(std::stoi(token));
            } else {
                op.push(token);
            }

            if (op.size()) {
                std::string oper = op.top();
                op.pop();

                int val1 = stk.top();
                stk.pop();
                int val2 = stk.top();
                stk.pop();

                if (oper == "+") {
                    stk.push(val2 + val1);
                } else if (oper == "-") {
                    stk.push(val2 - val1);
                } else if (oper == "*") {
                    stk.push(val2 * val1);
                } else {
                    stk.push(val2 / val1);
                }
            }
        }        
        return stk.top();
    }
};

/*
Problem use reverse polish notation to given the tokens to compute the integer value 

*/