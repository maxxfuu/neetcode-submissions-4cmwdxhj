class MinStack {
private:
    std::stack<int> stk;
    std::stack<int> min_stk;

public:
    MinStack() : stk(), min_stk() {}
    
    void push(int val) {
        stk.push(val);
    }
    
    void pop() {
        stk.pop();
    }
    
    int top() {
        return stk.top();
    }
    
    int getMin() {
        // create a; temporary stack 
        std::stack<int> temp;

        // create a minimum val 
        int mini = stk.top();

        // unload the stack and find mini, store all the values from the original stack to temporary stack
        while (stk.size()) {
            mini = std::min(mini, stk.top());
            temp.push(stk.top());
            stk.pop();
        }

        // repopulating the original stack again 
        while (temp.size()) {
            stk.push(temp.top());
            temp.pop();
        }

        return mini;
    }
};

