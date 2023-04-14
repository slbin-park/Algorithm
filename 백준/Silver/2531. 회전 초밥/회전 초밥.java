import java.io.*;
import java.util.*;

class Main {
	static class Node {
		int x, y;

		public Node(int x, int y) {
			this.x = x;
			this.y = y;
		}

		@Override
		public String toString() {
			return "Node{" + "x=" + x + ", y=" + y + '}';
		}
	}

	static int n, m, hx, hy, ex, ey, answer;
	static int[] arr;
	static int time;
	static int[][] visited;
	static int[] next;
	static int[] prev_next;
	static int[] keys;
	static int[] plug;
	static int[] dx = { 1, -1, 0, 0 }, dy = { 0, 0, 1, -1 };
	static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
	static Deque<Node> dq;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		n = Integer.parseInt(st.nextToken());
		int d = Integer.parseInt(st.nextToken());
		int k = Integer.parseInt(st.nextToken());
		int c = Integer.parseInt(st.nextToken());

		int answer = 1;
		int res = 1;
		arr = new int[n];
		int[] check = new int[d + 1];
		int dish_cnt = 0;
		check[c] += 1;
		for (int i = 0; i < n; i++) {
			st = new StringTokenizer(br.readLine());
			arr[i] = Integer.parseInt(st.nextToken());
			if (check[arr[i]] == 0) {
				answer += 1;
				check[arr[i]] = 1;
			} else {
				check[arr[i]] += 1;
			}
			dish_cnt++;
			if (dish_cnt > k) {
				check[arr[i - k]] -= 1;
				if (check[arr[i - k]] == 0) {
					answer -= 1;
				}
				dish_cnt--;
			}
			res = Math.max(res, answer);
//			System.out.println("i = " + i + " answer = " + answer);
		}
		for (int i = 0; i < n; i++) {
			if (check[arr[i % n]] == 0) {
				answer += 1;
				check[arr[i % n]] = 1;
			} else {
				check[arr[i % n]] += 1;
			}
			dish_cnt++;
			if (dish_cnt > k) {
				int idx = (n - k  + i) % n;
				check[arr[idx]] -= 1;
				if (check[arr[idx]] == 0) {

					answer -= 1;
				}
				dish_cnt--;
			}
			res = Math.max(res, answer);
		}
		System.out.println(res);

	}
}