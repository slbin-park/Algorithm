import java.io.*;
import java.util.StringTokenizer;
import java.io.IOException;
import java.util.ArrayDeque;
import java.util.Arrays;
import java.util.Collections;
import java.util.Deque;
import java.util.Scanner;

class Main{
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader (new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter (new OutputStreamWriter(System.out));
        StringTokenizer st;
        Deque<Integer> dq = new ArrayDeque<>();
        int n = Integer.parseInt(br.readLine());
        for(int i=1;i<=n;i++){
            dq.offer(i);
        }
        while (dq.size()>1){
            dq.pop();
            dq.offer(dq.poll());
        }
        System.out.println(dq.poll());
       // st = new StringTokenizer(br.readLine()," ");
        bw.flush(); // 남아있는데이터 모두 출력
        br.close();
        bw.close();
    }
}