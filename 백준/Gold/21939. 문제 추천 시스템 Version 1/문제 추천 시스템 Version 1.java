import java.io.*;
import java.util.HashMap;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

class Main {
    static class MNode implements Comparable<MNode> {
        int idx;
        int rank;

        public MNode(int idx, int rank) {
            this.idx = idx;
            this.rank = rank;
        }

        @Override
        public int compareTo(MNode o) {
            if (rank > o.rank) {
                return -1;
            } else if (rank < o.rank) {
                return 1;
            } else if (rank == o.rank) {
                if (idx > o.idx) {
                    return -1;
                } else {
                    return 1;
                }
            }
            return 0;
        }
    }

    static class NNode implements Comparable<NNode> {
        int idx;
        int rank;

        public NNode(int idx, int rank) {
            this.idx = idx;
            this.rank = rank;
        }

        @Override
        public String toString() {
            return "NNode{" +
                    "idx=" + idx +
                    ", rank=" + rank +
                    '}';
        }

        @Override
        public int compareTo(NNode o) {
            if (rank > o.rank) {
                return 1;
            } else if (rank < o.rank) {
                return -1;
            } else if (rank == o.rank) {
                if (idx > o.idx) {
                    return 1;
                } else {
                    return -1;
                }
            }
            return 0;
        }
    }

    static int[] dx = {-1, -1, 0, 1, 1, 1, 0, -1};
    static int[] dy = {0, -1, -1, -1, 0, 1, 1, 1};
    static int[] sdx = {-1, 0, 1, 0};
    static int[] sdy = {0, -1, 0, 1};
    static int sx, sy, sd, answer, res, cnt, N, M;
    static int[][] fishArr;
    static double[] arr;
    static HashMap<Integer, Integer> map;
    static PriorityQueue<MNode> mPq;
    static PriorityQueue<NNode> nPq;
    static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));


    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        mPq = new PriorityQueue<>();
        nPq = new PriorityQueue<>();
        map = new HashMap<>();
        N = Integer.parseInt(st.nextToken());
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            map.put(a, b);
            mPq.add(new MNode(a, b));
            nPq.add(new NNode(a, b));
        }
        st = new StringTokenizer(br.readLine());
        M = Integer.parseInt(st.nextToken());
        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            String a = st.nextToken();
            if (a.equals("add")) {
                int idx = Integer.parseInt(st.nextToken());
                int rank = Integer.parseInt(st.nextToken());
                addNode(idx, rank);
            } else if (a.equals("recommend")) {
                int number = Integer.parseInt(st.nextToken());
                recommend(number);
                bw.newLine();
            } else {
                int idx = Integer.parseInt(st.nextToken());
                solved(idx);
            }
        }
        bw.flush();
        bw.close();
        br.close();

    }

    static void addNode(int idx, int rank) {
        mPq.add(new MNode(idx, rank));
        nPq.add(new NNode(idx, rank));
        map.put(idx, rank);
    }

    // 출력
    static void recommend(int number) throws IOException {
        if (number == 1) {
            while (map.get(mPq.peek().idx) != mPq.peek().rank) {
                mPq.poll();
            }
            bw.write(String.valueOf(mPq.peek().idx));
        } else {
            while (map.get(nPq.peek().idx) != nPq.peek().rank) {
                nPq.poll();
            }
            bw.write(String.valueOf(nPq.peek().idx));
        }
    }

    // 삭제
    static void solved(int idx) {
        map.put(idx, -1);
    }


}