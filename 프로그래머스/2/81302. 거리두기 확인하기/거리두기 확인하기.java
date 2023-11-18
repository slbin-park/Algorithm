import java.util.*;
class Solution {
    private static int[] dx = {0,0,1,-1};
    private static int[] dy = {1,-1,0,0};
    class Node{
        int x;
        int y;
        int dis;
        Node(int x,int y,int dis){
            this.x = x;
            this.y = y;
            this.dis = dis;
        }
    }
    public boolean bfs(String[] arr){
        Deque<Node> dq = new ArrayDeque<>();
        for(int i=0;i<5;i++){
            for (int j=0;j<5;j++){
                if(arr[i].charAt(j) == 'P'){
                    boolean[][] vis = new boolean[5][5];
                    vis[i][j] = true;
                    dq.add(new Node(i,j,0));
                    while(dq.size() != 0){
                        Node node = dq.poll();
                        for(int k=0;k<4;k++){
                            int nx = node.x + dx[k];
                            int ny = node.y + dy[k];
                            if(0<=nx && nx<5 && 0<=ny && ny<5){
                                if(vis[nx][ny] == false){
                                    vis[nx][ny] = true;
                                    if(arr[nx].charAt(ny) == 'P'){
                                        return false;
                                    }
                                    if(arr[nx].charAt(ny) == 'O'){
                                        if(node.dis +1 < 2){
                                            dq.add(new Node(nx,ny,node.dis+1));
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
        return true;
    }
    
    public void printArr(boolean[][] arr){
        for(int i=0;i<5;i++){
            for(int j=0;j<5;j++){
                System.out.print(arr[i][j]);
            }
            System.out.println();
        }
    }
    public int[] solution(String[][] places) {
        int[] answer = new int[5];
        for(int i=0;i<5;i++){
            if(bfs(places[i])){
                answer[i] = 1;
            }else{
                answer[i] = 0;
            }
        }
        return answer;
    }
}