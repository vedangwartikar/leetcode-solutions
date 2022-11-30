class Solution {
public:
    vector <int> generate_list (string str) { // helper function to generate index based list from map
        map <char, int> seq; // map for keeping the same number to same characters
        vector <int> list; // result
        for (int i = 0; i < str.size(); i++) { // for each character in string
            if ((seq.find(str[i]) != seq.end()) == false) { // if character not found in map
                seq[str[i]] = i; // add the pair character: index to the map
                list.push_back(i); //add the index value to the result
            }
            else { // else if the character is already present
                list.push_back(seq[str[i]]); // add the already known index to the new character
            }
        }
        return list; // return result
    }
    
    bool isIsomorphic(string s, string t) {
        vector <int> s_list = generate_list(s); // get the index-based list
        vector <int> t_list = generate_list(t); // get the index-based list
        for (int i = 0; i < s_list.size(); i++) { // for each character
            if (s_list[i] != t_list[i]) { // if the index-based elements don't match
                return false; // return false (non-isomorphic character encountered)
            }
        }
        return true; // ll characters are isomorphic
    }
};