import java.util.*;
class Solution {
    static int x,y;
    public int[] solution(String[] park, String[] routes) {
        int[] answer = new int[2];
        x = y = 0;
        int n = park.length;
        int m = park[0].length();
        int[][] arr = new int[park.length][park[0].length()];
        for(int i=0;i<park.length;i++){
            for(int j=0;j<park[i].length();j++){
                if(park[i].charAt(j) == 'S'){
                    x = i;
                    y = j;
                    arr[i][j] = 0;
                }else if(park[i].charAt(j) =='X'){
                    arr[i][j] = 1;
                }
            }
        }
        for(String cmd : routes){
            String[] cmds = cmd.split(" ");
           
            String dir = cmds[0];
            int dis = Integer.parseInt(cmds[1]);
            int dx,dy;
            if(dir.equals("N")){
                dx = -1;
                dy = 0;
            }else if(dir.equals("S")){
                dx = 1;
                dy = 0;
            }else if(dir.equals("W")){
                dx = 0;
                dy = -1;
            }else{
                dx = 0;
                dy = 1;
            }
            int nx = x;
            int ny = y;
            boolean flag = true;
            for(int j=0;j<dis;j++){
                nx+=dx;
                ny+=dy;
                if(0>nx || nx>=n || 0>ny || ny>=m || arr[nx][ny]==1){
                    flag = false;
                    break;
                }
              
            }
            if(flag){
                    x = nx;
                    y = ny;
            }
        }
        answer[0] = x;
        answer[1] = y;
        return answer;
    }
}