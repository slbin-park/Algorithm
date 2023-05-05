class Solution {
    public int solution(int n, int m, int[] section) {
        int answer = 0;
        int prevTape = Integer.MIN_VALUE;
        for(int i=0;i<section.length;i++){
            if(section[i] >=prevTape){
                answer++;
                prevTape = section[i] +m;
            }
        }
        return answer;
    }
}