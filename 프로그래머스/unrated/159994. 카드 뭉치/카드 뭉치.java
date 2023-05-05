class Solution {
    public String solution(String[] cards1, String[] cards2, String[] goal) {
        String answer = "Yes";
        int cards1Idx = 0;
        int cards2Idx = 0;
        for(int i=0;i<goal.length;i++){
            if(cards1Idx <cards1.length &&goal[i].equals(cards1[cards1Idx])){
                cards1Idx++;
            } else if(cards2Idx < cards2.length &&goal[i].equals(cards2[cards2Idx])){
                cards2Idx++;
            } else{
                answer = "No";
            }
        }
        return answer;
    }
}