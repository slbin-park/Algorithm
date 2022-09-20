import java.io.*;
import java.util.StringTokenizer;
import java.io.IOException;
import java.util.Arrays;
import java.util.Scanner;

class Main{
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader (new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter (new OutputStreamWriter(System.out));
        StringTokenizer st;
        // st = new StringTokenizer(br.readLine()," ");
        int n = Integer.parseInt(br.readLine());
        int[] arr = new int[n];
        for(int i=0;i<n;i++){
            arr[i] = Integer.parseInt(br.readLine());
        }
        Arrays.sort(arr);
        for(int i=0;i<n;i++){
            System.out.println(arr[i]);
        }
        bw.flush(); // 남아있는데이터 모두 출력
        br.close();
        bw.close();
    }
}