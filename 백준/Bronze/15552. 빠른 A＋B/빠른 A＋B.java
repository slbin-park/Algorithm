import java.io.*;
import java.util.StringTokenizer;
import java.io.IOException;
import java.util.Scanner;

class Main{
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader (new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter (new OutputStreamWriter(System.out));
        StringTokenizer st;

        int n = Integer.parseInt(br.readLine());
        
        for (int i =0;i<n;i++){
            st = new StringTokenizer(br.readLine()," ");
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            bw.write(a+b + "\n");
        }
        bw.flush();
        br.close();
        bw.close();
    }
}