import java.io.*;
import java.util.StringTokenizer;
import java.io.IOException;
import java.util.Scanner;

class Main{
    public static int get_num(int abc){
        abc = 3;
        return 1234;
    }
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader (new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter (new OutputStreamWriter(System.out));
        StringTokenizer st;
        // st = new StringTokenizer(br.readLine()," ");
        int n = Integer.parseInt(br.readLine());
        int[][] arr = new int[n][2];
        for (int i = 0;i<n;i++){
            st = new StringTokenizer(br.readLine()," ");
            arr[i][0] = Integer.parseInt(st.nextToken());
            arr[i][1] = Integer.parseInt(st.nextToken());
        }
        for (int i = 0 ; i < n;i++){
            int cur_cnt = 0;
            for (int j=0;j<n;j++){
                if (i!=j){
                    if (arr[j][0] > arr[i][0] && arr[j][1] > arr[i][1]){
                        cur_cnt++;
                    }
                }
            }
            if(i!=n-1){
                bw.write(cur_cnt+1 +" ");
            }
            else{
                bw.write(cur_cnt+1 + "\n");
            }
        }
        // bw.write(abc+"\n");
        bw.flush(); // 남아있는데이터 모드 출력
        br.close();
        bw.close();
    }
}