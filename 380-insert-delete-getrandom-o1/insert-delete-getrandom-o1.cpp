#include <vector>
#include <unordered_map>
#include <cstdlib>

class RandomizedSet {
private:
    std::vector<int> nums;
    std::unordered_map<int, int> valToIndex;

public:
    RandomizedSet() {}
    
    bool insert(int val) {
        if (valToIndex.find(val) != valToIndex.end()) {
            return false;
        }
        valToIndex[val] = nums.size();
        nums.push_back(val);
        return true;
    }
    
    bool remove(int val) {
        if (valToIndex.find(val) == valToIndex.end()) {
            return false;
        }
        // Move the last element to the place of the element to delete
        int lastElement = nums.back();
        int idxToDelete = valToIndex[val];
        
        nums[idxToDelete] = lastElement;
        valToIndex[lastElement] = idxToDelete;
        
        // Remove the last element
        nums.pop_back();
        valToIndex.erase(val);
        return true;
    }
    
    int getRandom() {
        return nums[rand() % nums.size()];
    }
};
