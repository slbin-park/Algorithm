import java.io.*;
import java.util.StringTokenizer;
import java.io.IOException;
import java.util.ArrayDeque;
import java.util.Arrays;
import java.util.Collections;
import java.util.Deque;

class Main{
    static int n,m,prev;
    static int[] arr;
    static boolean[] visited;
    public static void back(int depth,BufferedWriter bw)throws IOException{
        if (depth == m){
            for(int i=0;i<m;i++){
                bw.write(arr[i] + " ");
            }
            bw.write("\n");
            return;
        }
        else{
            for(int i=prev+1;i<=n;i++){
                arr[depth] = i;
                back(depth+1,bw);
            }
        }
    }
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader (new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter (new OutputStreamWriter(System.out));
        StringTokenizer st;
        Deque<Integer> dq = new ArrayDeque<>();
        st = new StringTokenizer(br.readLine()," ");
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        visited = new boolean[n+1];
        arr = new int[m+1];
        prev= 0;
        back(0,bw);
        bw.flush(); // 남아있는데이터 모두 출력
        br.close();
        bw.close();
    }
}