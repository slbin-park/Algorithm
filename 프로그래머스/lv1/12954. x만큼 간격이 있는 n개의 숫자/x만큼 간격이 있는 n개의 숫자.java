class Solution {
    public long[] solution(int x, int n) {
        long[] answer = new long[n];
        long cur_v = x;
        for(int i=0;i<n;i++){
            answer[i] = cur_v + (long)x*(long)i;
        }
        return answer;
    }
}