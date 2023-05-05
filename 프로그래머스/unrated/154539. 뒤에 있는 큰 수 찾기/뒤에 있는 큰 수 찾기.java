import java.util.*;
class Solution {
    public int[] solution(int[] numbers) {
        int[] answer = new int[numbers.length];
        Deque<int[]> dq = new ArrayDeque<>();
        for(int i=0;i<numbers.length;i++){
            answer[i] = -1;
        }
        dq.add(new int[]{numbers[0],0});
        for(int i=1;i<numbers.length;i++){
            while(!dq.isEmpty()){
                int[] curArr = dq.pollLast();
                if(curArr[0] <numbers[i]){
                    answer[curArr[1]] = numbers[i];
                }else{
                    dq.add(curArr);
                    break;
                }
            }
            dq.add(new int[]{numbers[i],i});
        }
        return answer;
    }
}