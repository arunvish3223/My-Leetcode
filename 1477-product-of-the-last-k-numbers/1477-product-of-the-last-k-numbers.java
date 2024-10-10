class ProductOfNumbers {
    private ArrayList<Integer> arr;

    public ProductOfNumbers() {
        arr = new ArrayList<>();
    }
    
    public void add(int num) {
        arr.add(num);
    }
    
    public int getProduct(int k) {
        int n = arr.size();
        int mul = 1;
        for (int i = n - 1; i > n - k - 1; i--) {
            mul *= arr.get(i);
        }
        return mul;
    }
}

/**
 * Your ProductOfNumbers object will be instantiated and called as such:
 * ProductOfNumbers obj = new ProductOfNumbers();
 * obj.add(num);
 * int param_2 = obj.getProduct(k);
 */