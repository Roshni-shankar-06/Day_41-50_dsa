import java.util.*;

class Solution {
    public List<Integer> busiestServers(int k, int[] arrival, int[] load) {
        // Keeps track of the number of requests each server handled
        int[] count = new int[k];
        
        // Available servers sorted by their IDs
        TreeSet<Integer> available = new TreeSet<>();
        for (int i = 0; i < k; i++) {
            available.add(i);
        }
        
        // Min-heap tracking busy servers: stores pairs as int[] {end_time, server_id}
        PriorityQueue<int[]> busy = new PriorityQueue<>((a, b) -> Integer.compare(a[0], b[0]));
        
        for (int i = 0; i < arrival.length; i++) {
            int arrivalTime = arrival[i];
            int loadTime = load[i];
            
            // Free up servers that finished their tasks before or at the current arrival time
            while (!busy.isEmpty() && busy.peek()[0] <= arrivalTime) {
                int[] freed = busy.poll();
                available.add(freed[1]);
            }
            
            // If no servers are available, drop the request
            if (available.isEmpty()) {
                continue;
            }
            
            // Find the ideal preferred server index
            int pref = i % k;
            
            // Find the smallest server ID >= pref
            Integer targetServer = available.ceiling(pref);
            
            // If none found >= pref, wrap around and take the smallest available server ID overall
            if (targetServer == null) {
                targetServer = available.first();
            }
            
            // Assign the task to the selected server
            available.remove(targetServer);
            busy.offer(new int[]{arrivalTime + loadTime, targetServer});
            count[targetServer]++;
        }
        
        // Find the maximum number of requests handled by any server
        int maxRequests = 0;
        for (int c : count) {
            maxRequests = Math.max(maxRequests, c);
        }
        
        // Collect all servers that achieved this maximum
        List<Integer> result = new ArrayList<>();
        for (int i = 0; i < k; i++) {
            if (count[i] == maxRequests) {
                result.add(i);
            }
        }
        
        return result;
    }
}
