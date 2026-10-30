struct T {
  int depth;
  size_t length;
};

class Solution {
 public:
  int lengthLongestPath(string input) {
    size_t ans = 0;
    stack<T> stack{{{-1, 0}}}; // Placeholder for root level
    istringstream iss(input);

    for (string token; getline(iss, token, '\n');) {
      const int depth = count(token.begin(), token.end(), '\t');
      token.erase(remove(token.begin(), token.end(), '\t'), token.end());

      // Backtrack until the top of the stack matches the parent's depth
      while (depth <= stack.top().depth) {
        stack.pop();
      }

      if (isFile(token)) {
        ans = max(ans, stack.top().length + token.length());
      } else {
        // Directory path length + current directory length + 1 (for '/')
        stack.push({depth, stack.top().length + token.length() + 1});
      }
    }

    return ans;
  }

 private:
  bool isFile(const string& token) {
    return token.find('.') != string::npos;
  }
};
