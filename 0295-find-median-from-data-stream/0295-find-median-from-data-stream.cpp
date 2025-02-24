class MedianFinder {
public:
    MedianFinder() {
        nums = vector<int>();
    }
    
    void addNum(int num) {
        int l = 0;
        int r = nums.size();
        int mid;
        while (l <r) {
            mid = (l + r) / 2;
            if (nums[mid] < num) {
                l = mid + 1;
            } else {
                r = mid;
            }
        }
        nums.insert(nums.begin() + l, num);
    }
    
    double findMedian() {
        int n = nums.size();
        if (n % 2 == 1) {
            return nums[n / 2];
        } else {
            int mid1 = n / 2 - 1;
            int mid2 = n / 2;
            return (nums[mid1] + nums[mid2]) / 2.0;
        }
    }

private:
    vector<int> nums;
};

/**
 * Your MedianFinder object will be instantiated and called as such:
 * MedianFinder* obj = new MedianFinder();
 * obj->addNum(num);
 * double param_2 = obj->findMedian();
 */