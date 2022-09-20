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
        for (int i=0;i<n;i++){
            st = new StringTokenizer(br.readLine()," ");
            switch(st.nextToken()){
                case "push":
                // 뒤에 추가
                    dq.offer(Integer.parseInt(st.nextToken()));
                    break;
                case "pop":
                    Integer item = dq.poll();
                    // 가장 앞에 있는 요소를 삭제
                    if(item == null){
                        bw.write(-1+"\n");
                    }
                    else{
                        bw.write(item+"\n");
                    }
                    break;
                case "size":
                    bw.write(dq.size()+"\n");
                    break;
                case "empty":
                    if(dq.isEmpty()){
                        bw.write(1+"\n");
                    }
                    else{
                        bw.write(0+"\n");
                    }
                    break;
                case "front":
                    Integer item2 = dq.peek();
                    if(item2 == null){
                        bw.write(-1+"\n");
                    }
                    else{
                        bw.write(item2+"\n");
                    }
                    break;
                case "back":
                    Integer item3 = dq.peekLast();
                    if(item3 == null){
                        bw.write(-1+"\n");
                    }
                    else{
                        bw.write(item3+"\n");
                    }
                    break;
            }
        }
        // st = new StringTokenizer(br.readLine()," ");
        bw.flush(); // 남아있는데이터 모두 출력
        br.close();
        bw.close();
    }
}