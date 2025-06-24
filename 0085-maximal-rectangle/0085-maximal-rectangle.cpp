class Solution {
public:
    int maximalRectangle(vector<vector<char>>& matrix) {
        vector<int>area;
        for(int j=0;j<matrix[0].size();j++){
            area.push_back(matrix[0][j] - '0'); 
        }
        int mx=getMaxArea(area);
        for(int i=1;i<matrix.size();i++){
            for(int j=0;j<matrix[0].size();j++){
                if(matrix[i][j]=='0'){
                    area[j]=0;
                }
                else{
                    area[j] = area[j] + (matrix[i][j] - '0');
                }
            }
            mx=max(mx,getMaxArea(area));
        }
        return mx;
    }
    int getMaxArea(vector<int> &arr) {
        vector<int> nsi;
        stack<int> stack;

        for(int i = arr.size() - 1; i >= 0; i--) {
            if(stack.empty()) {
                nsi.push_back(arr.size());
            }
            else if(arr[stack.top()] < arr[i]) {
                nsi.push_back(stack.top());
            }
            else if(!stack.empty() && arr[stack.top()] >= arr[i]) {
                while(!stack.empty() && arr[stack.top()] >= arr[i]) {
                    stack.pop();
                }
                if(stack.empty()) {
                    nsi.push_back(arr.size());
                }
                else if(arr[stack.top()] < arr[i]) {
                    nsi.push_back(stack.top());
                }
            }
            stack.push(i);
        }

        reverse(nsi.begin(), nsi.end());

        vector<int> psi;
        while (!stack.empty()) { stack.pop(); }

        for(int i = 0; i < arr.size(); i++) {
            if(stack.empty()) {
                psi.push_back(-1);
            }
            else if(arr[stack.top()] < arr[i]) {
                psi.push_back(stack.top());
            }
            else if(!stack.empty() && arr[stack.top()] >= arr[i]) {
                while(!stack.empty() && arr[stack.top()] >= arr[i]) {
                    stack.pop();
                }
                if(stack.empty()) {
                    psi.push_back(-1);
                }
                else if(arr[stack.top()] < arr[i]) {
                    psi.push_back(stack.top());
                }
            }
            stack.push(i);
        }

        for(int i = 0; i < arr.size(); i++) {
            psi[i] = arr[i] * (nsi[i] - psi[i] - 1);
        }

        return *max_element(psi.begin(), psi.end());
    }
};