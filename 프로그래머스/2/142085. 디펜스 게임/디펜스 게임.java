import java.util.*;
class Solution {
    public int solution(int n, int k, int[] enemy) {
        PriorityQueue<Integer> pq = new PriorityQueue<>(Collections.reverseOrder());
        int answer = 0;
        int sum = 0;
        for(int i=0;i<enemy.length;i++){
            sum+=enemy[i];
            pq.add(enemy[i]);
            if(sum > n){
                while(pq.size() != 0 && k>0){
                    k-=1;
                    Integer curV = pq.poll();
                    sum -= curV;
                    if(sum <= n){
                        break;
                    }
                }
                if(k==0 && sum >n){
                    return i;
                }
            }
            answer+=1;
        }
        return answer;
    }
}