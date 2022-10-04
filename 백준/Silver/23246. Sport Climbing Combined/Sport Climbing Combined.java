import java.io.*;
import java.io.IOException;
import java.util.*;

class Main{
    static int n,m;
    static int a,b,c,d;
    static int[] result;
    static class Node implements Comparable<Node>{
        int number;
        int score;
        int pscore;

        public Node(int number,int score,int pscore){
            this.number = number;
            this.score = score;
            this.pscore = pscore;
        }
        @Override
        public int compareTo(Node node2){
            if(this.score < node2.score){
                return -1;
            }else if(this.score == node2.score){
                if (this.pscore == node2.pscore){
                    if(this.number > node2.number){
                        return 1;
                    }else{
                        return -1;
                    }
                }else if(this.pscore > node2.pscore){
                    return 1;
                }
                else{
                    return -1;
                }
            }else{
                return 1;
            }
        }
    }

    // static LinkedList<Integer> result_dfs = new LinkedList<Integer>();
    // static LinkedList<Integer> result_bfs = new LinkedList<Integer>();
    public static void main(String[] args) throws IOException{
        PriorityQueue<Node> pq = new PriorityQueue<Node>();
        BufferedReader br = new BufferedReader (new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter (new OutputStreamWriter(System.out));
        StringTokenizer st;
        st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        result = new int[4];
        for(int i=0;i<n;i++){
            st = new StringTokenizer(br.readLine()," ");
            a = Integer.parseInt(st.nextToken());
            b = Integer.parseInt(st.nextToken());
            c = Integer.parseInt(st.nextToken());
            d = Integer.parseInt(st.nextToken());
            pq.add(new Node(a,b*c*d,b+c+d));
        }
        int idx = 0;
        while(idx !=3){
            Node cur_node = pq.poll();
            result[idx] = cur_node.number;
            idx++;
        }
        for(int i=0;i<3;i++){
            System.out.print(result[i]+" ");
        }
        br.close();
        bw.close();
    }

}