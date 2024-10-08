class Solution {
    public int minSwaps(String s) {
        int unbalanced = 0;
        int swaps = 0;
        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == '[') {
                unbalanced--;
            } else if (s.charAt(i) == ']') {
                unbalanced++;
            }
            if (unbalanced > 0) {
                swaps++;
                unbalanced -= 2;
            }
        }
        return swaps;
    }
}