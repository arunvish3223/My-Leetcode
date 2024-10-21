class Solution {
    void allPossibleSubstrings(string& s, int pos, int& ms, unordered_set<string>& us) {
        if (pos == s.size()) {
            if (ms < us.size())
                ms = us.size();
            return;
        }  
        string temp;
        for (int i = pos; i < s.size(); ++i) {
            temp.push_back(s[i]);
            if (us.count(temp) == 0) {
                us.insert(temp);
                allPossibleSubstrings(s, i + 1, ms, us);
                us.erase(temp);
            }
        }
    }
    
public:
    int maxUniqueSplit(string s) {
        int ms = 0;
        unordered_set<string> us;
        allPossibleSubstrings(s, 0, ms, us);
        return ms;
    }
};
