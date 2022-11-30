class Solution {
public:
    vector <int> generate_list (string str) {
        unordered_map <char, int> seq;
        vector <int> list;
        for (int i = 0; i < str.size(); i++) {
            if ((seq.find(str[i]) != seq.end()) == false) {
                seq[str[i]] = i;
                list.push_back(i);
            }
            else {
                list.push_back(seq[str[i]]);
            }
        }
        return list;
    }
    
    bool isIsomorphic(string s, string t) {
        vector <int> s_list = generate_list(s);
        vector <int> t_list = generate_list(t);
        for (int i = 0; i < s_list.size(); i++) {
            if (s_list[i] != t_list[i]) {
                return false;
            }
        }
        return true;
    }
};