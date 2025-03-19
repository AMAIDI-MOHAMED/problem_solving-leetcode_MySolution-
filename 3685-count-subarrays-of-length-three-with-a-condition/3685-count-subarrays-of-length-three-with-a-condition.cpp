#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    int countSubarrays(vector<int>& nums) {
        int s = 0;  
        for (int i = 0; i <= nums.size() - 3; ++i) {
   
            if (nums[i + 1] % 2 == 0) {
    
                if (nums[i] + nums[i + 2] == nums[i + 1] / 2) {
                    s++;  
                }
            }
        }
        
        return s; 
    }
};
