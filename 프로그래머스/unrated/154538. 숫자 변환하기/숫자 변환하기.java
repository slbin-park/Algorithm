import java.util.*;
class Solution {
    static int bfs(int x,int y,int n){
        Deque<int[]> dq = new ArrayDeque<>();
        int[] visited = new int[1_000_001];
        visited[x] = 1;
        int[] arr = {x,0};
        dq.add(arr);
        while(!dq.isEmpty()){
            int[] curArr = dq.pollFirst();
            if(curArr[0] == y){
                return curArr[1];
            }
            if(curArr[0]+n <= 1000000&&visited[curArr[0]+n]==0){
                visited[curArr[0]+n]=1;
                dq.add(new int[]{curArr[0]+n,curArr[1]+1});
            }
            if(curArr[0]*2<= 1000000&& visited[curArr[0]*2]==0){
                visited[curArr[0]*2]=1;
                dq.add(new int[]{curArr[0]*2,curArr[1]+1});
            }
            if(curArr[0]*3 <= 1000000 &&visited[curArr[0]*3]==0){
                visited[curArr[0]*3]=1;
                dq.add(new int[]{curArr[0]*3,curArr[1]+1});
            }
        }
        return -1;
    }
    public int solution(int x, int y, int n) {
        int answer = 0;
        return bfs(x,y,n);
    }
}