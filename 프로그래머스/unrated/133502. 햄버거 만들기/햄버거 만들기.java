import java.util.*;
class Solution {
    public int solution(int[] ingredient) {
        int answer = 0;
        int prevIg = -1;
        Deque<Integer> dq = new ArrayDeque<>();
        for(int i=0;i<ingredient.length;i++){
            dq.add(ingredient[i]);
            if(ingredient[i]==1){
                while(dq.size()>=4 ){
                    int fouth = dq.pollLast();
                    int third = dq.pollLast();
                    int second = dq.pollLast();
                    int first = dq.pollLast();
                    if (first==1 && second==2 && third==3 && fouth ==1){
                        answer++;
                    }else{
                        dq.add(first);
                        dq.add(second);
                        dq.add(third);
                        dq.add(fouth);
                        break;
                    }
                }
            }
        }
        return answer;
        
    }
}