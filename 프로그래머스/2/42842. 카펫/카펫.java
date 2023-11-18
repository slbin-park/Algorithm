class Solution {
    public int x = 3;
    public int y = 3;
    public int brownV = 0;
    public int yellowV = 0;
    public void dfs(){
        for(int i=3;i<=y;i++){
            int curB = 2*y + 2*i -4;
            int curY = y*i - curB;
            if(curB == brownV && curY == yellowV){
                x = i;
                return;
            }
        }
        y+=1;
        dfs();
    }
    public int[] solution(int brown, int yellow) {
        int[] answer = new int[2];
        brownV = brown;
        yellowV = yellow;
        dfs();
        answer[0] = y;
        answer[1] = x;
        return answer;
    }
}