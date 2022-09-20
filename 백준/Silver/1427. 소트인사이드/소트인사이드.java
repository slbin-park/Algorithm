import java.io.*;
import java.util.StringTokenizer;
import java.io.IOException;
import java.util.Arrays;
import java.util.Collections;
import java.util.Scanner;

class Main{
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader (new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter (new OutputStreamWriter(System.out));
        StringTokenizer st;
        // st = new StringTokenizer(br.readLine()," ");
        String n =br.readLine();
        Integer[] arr = new Integer[n.length()];
        for (int i=0;i<n.length();i++){
            char cur = n.charAt(i);
            arr[i] = Integer.parseInt(String.valueOf(cur));
        }
        Arrays.sort(arr,Collections.reverseOrder());
        for (int i=0;i<n.length();i++){
            bw.write(arr[i]+"");
        }
        bw.write("\n");
        bw.flush(); // 남아있는데이터 모두 출력
        br.close();
        bw.close();
    }
}