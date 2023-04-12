import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

class Main {
    static class Node implements Comparable<Node> {
        int idx;
        double value;
        int cnt;

        public Node(int idx, double value, int cnt) {
            this.idx = idx;
            this.value = value;
            this.cnt = cnt;
        }

        @Override
        public int compareTo(Node o) {
            if (value > o.value) {
                return -1;
            } else if (value < o.value) {
                return 1;
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

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        String a = st.nextToken();
        String b = st.nextToken();
        String mina = "";
        String maxa = "";
        String minb = "";
        String maxb = "";
        for (int i = 0; i < a.length(); i++) {
            if (a.charAt(i) == '6') {
                mina += '5';
                maxa += '6';
            } else if (a.charAt(i) == '5') {
                maxa += '6';
                mina += '5';
            } else {
                mina += String.valueOf(a.charAt(i));
                maxa += String.valueOf(a.charAt(i));
            }
        }
        for (int i = 0; i < b.length(); i++) {
            if (b.charAt(i) == '6') {
                minb += '5';
                maxb += '6';
            } else if (b.charAt(i) == '5') {
                maxb += '6';
                minb += '5';
            } else {
                minb += String.valueOf(b.charAt(i));
                maxb += String.valueOf(b.charAt(i));
            }
        }
        System.out.print(Integer.parseInt(mina) + Integer.parseInt(minb) + " ");
        System.out.println(Integer.parseInt(maxa) + Integer.parseInt(maxb));


    }


}