import java.util.*;
class Solution {
    public boolean[] vis;
    public int[] ignore = new int[2];
    public List<List<Integer>> arr = new ArrayList<>();
    public int cnt;
    public void bfs(int j){
        List<Integer> curArr = arr.get(j);
        // System.out.println(curArr.toString());
        for(int i=0;i<curArr.size();i++){
            int curV = curArr.get(i);
            if((ignore[0] == j && ignore[1] == curV) || (ignore[0] == curV && ignore[1] == j)){
                continue;
            }
            if(vis[curV] == false){
                vis[curV] = true;
                cnt+=1;
                bfs(curV);
            }
        }
    }
    public int solution(int n, int[][] wires) {
        int answer = 10000000;
        for(int i=0;i<=n;i++){
            arr.add(new ArrayList<>());
        }
        for(int[] wire:wires){
            arr.get(wire[0]).add(wire[1]);
            arr.get(wire[1]).add(wire[0]);
        }
        for(int i=0;i<n-1;i++){
            ignore[0] = wires[i][0];
            ignore[1] = wires[i][1];
            vis = new boolean[n+1];
            int first = -1;
            int second = -1;
            for(int j=1;j<=n;j++){
                cnt = 0;
                if(vis[j] == false){
                    vis[j] = true;
                    cnt+=1;
                    bfs(j);
                    if(first == -1){
                        first = cnt;                    
                    }else{
                        second = cnt;
                    }
                    
                }
            }
            answer = Math.min(Math.abs(first-second),answer);
        }
        return answer;
    }
}