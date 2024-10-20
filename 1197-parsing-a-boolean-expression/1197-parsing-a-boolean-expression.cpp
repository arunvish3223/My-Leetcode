class Solution {
    void eval(stack<char>& o, stack<char>& op) {
        char p = o.top();
        o.pop();
        bool ans;
        
        if (p == '|') {
            ans = false;
            while (op.top() != '(') {
                ans |= (op.top() == 't');
                op.pop();
            }
            op.pop();
        }
        else if (p == '&') {
            ans = true;
            while (op.top() != '(') {
                ans &= (op.top() == 't');
                op.pop();
            }
            op.pop();
        }
        else if (p == '!') {
            ans = (op.top() == 't');
            ans = !ans;
            op.pop();
            op.pop();
        }

        if (ans) op.push('t');
        else op.push('f');
    }

public:
    bool parseBoolExpr(string expression) {
        stack<char> o, op;
        int i = 0;

        while (i < expression.size()) {
            if (expression[i] == '!' || expression[i] == '&' || expression[i] == '|') {
                o.push(expression[i]);
            }
            else if (expression[i] == 't' || expression[i] == 'f') {
                op.push(expression[i]);
            }
            else if (expression[i] == '(') {
                op.push(expression[i]);
            }
            else if (expression[i] == ')') {
                eval(o, op);
            }
            i++;
        }

        return op.top() == 't';
    }
};
