#include <vector>
#include <string>
#include <queue>
#include <tuple>

using namespace std;

class Solution {
public:
    int shortestPath(int n, vector<vector<int>>& edges, string labels, int k) {
        // Build the adjacency list: graph[u] = {(v, weight)}
        vector<vector<pair<int, int>>> graph(n);
        for (const auto& edge : edges) {
            graph[edge[0]].push_back({edge[1], edge[2]});
        }

        // dist[node][run] stores the minimum path weight to reach `node` 
        // with `run` number of consecutive identical characters.
        vector<vector<int>> dist(n, vector<int>(k + 1, 1e9));
        
        // Min-heap storing tuples of {distance, node, run}
        priority_queue<tuple<int, int, int>, vector<tuple<int, int, int>>, greater<tuple<int, int, int>>> pq;

        // Initialize with node 0, run = 1 (since the first character counts as 1)
        dist[0][1] = 0;
        pq.push({0, 0, 1});

        while (!pq.empty()) {
            auto [d, u, run] = pq.top();
            pq.pop();

            // If we found a shorter path to this state already, skip it
            if (d > dist[u][run]) continue;

            // Since it's a min-heap, the first time we pop node n - 1, 
            // it is guaranteed to be the shortest valid path.
            if (u == n - 1) return d;

            for (const auto& [v, w] : graph[u]) {
                int nextRun = (labels[u] == labels[v]) ? run + 1 : 1;

                // Ensure the consecutive run constraint is not violated
                if (nextRun <= k) {
                    if (d + w < dist[v][nextRun]) {
                        dist[v][nextRun] = d + w;
                        pq.push({dist[v][nextRun], v, nextRun});
                    }
                }
            }
        }

        return -1;
    }
};
