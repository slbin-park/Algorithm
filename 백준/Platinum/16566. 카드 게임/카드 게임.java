import java.io.*;
import java.util.Arrays;
import java.util.StringTokenizer;

class Main {
    static class Node {
        int u, v, w;

        public Node(int u, int v, int w) {
            this.u = u;
            this.v = v;
            this.w = w;
        }

    }

    static int INF = Integer.MIN_VALUE;
    static int[] dx = {1, 0};
    static int[] dy = {0, 1};
    static StringTokenizer st;
    static int N;
    static BufferedReader br;

    static BufferedWriter bw = new BufferedWriter(
            new OutputStreamWriter(System.out)
    );

    public static int bs(int[] arr, int a) {
        int start = 0;
        int end = arr.length - 1;
        int mid, res = 0;
        while (start <= end) {
            mid = (start + end) / 2;
            if (arr[mid] <= a) {
                start = mid + 1;
            } else {
                end = mid - 1;
                res = mid;
            }
        }
        return res;
    }

    public static int find(int[] parent, int x) {
        if (parent[x] != x) {
            parent[x] = find(parent, parent[x]);
        }
        return parent[x];
    }

    public static int solve(int[] arr, int a, int[] parent) {
        // 이분탐색으로 크면서 가장작은값의 인덱스 찾음
        int min_v = bs(arr, a);

        // find로 근처 인덱스 찾음
        int get_index = find(parent, min_v);
        // 한칸 올림
        parent[get_index] = get_index + 1;
        return arr[get_index];
    }


    public static void main(String[] args) throws IOException {
        br = new BufferedReader(new InputStreamReader(System.in));
        st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());

        int m = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());
        int[] arr = new int[m];
        int[] parent = new int[m];

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < m; i++) {
            parent[i] = i;
            arr[i] = Integer.parseInt(st.nextToken());
        }

        Arrays.sort(arr);

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < k; i++) {
            int a = Integer.parseInt(st.nextToken());
            bw.write(String.valueOf(solve(arr, a, parent)));
            bw.newLine();
        }
        bw.flush();
    }
}
