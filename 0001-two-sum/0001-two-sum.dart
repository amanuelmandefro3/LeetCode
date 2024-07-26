class Solution {
  List<int> twoSum(List<int> nums, int target) {
    var hp = Map(); 
    int n = nums.length;
    for (int i = 0; i < n; i++) {
      if (hp.containsKey(target - nums[i])) {
        return [hp[target - nums[i]]!, i]; 
      }
      hp[nums[i]] = i;
    }
    return [];
  }
}
