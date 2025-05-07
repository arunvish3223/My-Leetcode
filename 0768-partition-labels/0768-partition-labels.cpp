class Solution {
public:
    vector<int> partitionLabels(string s) {
        unordered_map<char, int> last_idx;
        vector<int> res;
        int end = 0, size = 0;
        for(int i = 0; i< s.length();i++){
            last_idx[s[i]]=i;
        }
        for(int i = 0; i< s.length();i++){
            size++;
            end=max(end,last_idx[s[i]]);
            if(i==end){
                res.push_back(size);
                size=0;
            }
        }
        return res;
        
    }
};