#include <vector>
#include <unordered_map>
using namespace stf;

class Solution {
    public:
        vector<int> result = {};
        unordered_set<int> visited, cycle;
        vector<vector<int>> adj;

        bool dfs(int courseNum) {
            // Base case: cycle detection
            if (cycle.count(courseNum)) {
                return false;
            }

            // Base case: already visited
            if (visited.count(courseNum)) {
                return true;
            }

            // Push onto stack to keep track of cycles
            cycle.insert(courseNum);

            // Recursive case: check neighbours until we find leaf
            for (const auto& prereq : adj[courseNum]) {
                if (dfs(prereq) == false) {
                    return false;
                }
            }

            // After path is searched remove from cycle since no cycle was found
            cycle.erase(courseNum);
            visited.insert(courseNum);
            // Now:
            //          dfs has traversed as far as it can on current path,
            //          no cycle was detected
            //          current node is now being ignored
            // Therefore:
            //          we can push it onto resule
            result.push_back(courseNum);
            return true;
        }

        vector<int> findOrder(int numCourses, vector<vector<int>>& prerequisites) {
            adj = vector<vector<int>>(numCourses);
            result = {};
            visited.clear();
            cycle.clear();

            // Construct an adjacency list
            for (const auto& edge : prerequisites) {
                // edge[0] is course, edge[1] is a list of prerequisites
                adj[edge[0]].push_back(edge[1]);
                // adj[courseNum] = prereq
            }
            
            // run dfs on every course
            for (int i = 0; i < numCourses; i++) {
                // resolve the cycle base case and return empty vector
                if (dfs(i) == false) {
                    return {};
                }
            }
            return result;
        }
};
