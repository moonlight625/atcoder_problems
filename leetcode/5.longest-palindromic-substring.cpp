/*
 * @lc app=leetcode id=5 lang=cpp
 *
 * [5] Longest Palindromic Substring
 */

// @lc code=start
class Solution {
public:
    string longestPalindrome(string s) {
        // if(s.size() == 1){
        //     return s;
        // }
        // else if(s.size() == 2){
        //     if(s[0] != s[1]){
        //         string ret(1, s[0]);
        //         return ret;
        //     }
        // }
        string ret;
        bool kaibun = true;

        int i = 0, center_index = 0, r, l;
        pair<int,int> maxl;//(left,right)
        for(center_index = 0; center_index < s.size(); center_index++){
            printf("center = %d\n", center_index);
            //2n+1
            l = center_index; r = center_index;
            while(0 < l && r < s.size()){
                if(s[l] != s[r]){
                    if(r - l > maxl.second - maxl.first){
                        maxl.second = l;
                        maxl.first = r;
                    }
                }
                l--; r++;
                printf("l = %d, r = %d\n",l,r);
            }

            //2n
            l = center_index; r = center_index + 1;
            while(0 < l && r < s.size()){
                if(s[l] != s[r]){
                    if(r - l > maxl.second - maxl.first){
                        maxl.second = l;
                        maxl.first = r;
                    }
                }
                l--; r++;
                printf("l = %d, r = %d\n",l,r);
            }
        }


        ret = s.substr(l, r-l+1);
        
        return ret;
    }
};
// @lc code=end

