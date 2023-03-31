import java.io.*;
import java.lang.reflect.Array;
import java.util.*;

class Main {
	static class Node {
		int y;
		int x;

		public Node(int idx, int cost) {
			this.y = idx;
			this.x = cost;
		}

	}

	static int n, m;
	static int[][] arr;
	static int time;
	static boolean[][] check;
	static int[] x = { 1, -1, 0, 0 }, y = { 0, 0, 1, -1 };

	public static void solve(Node cheese) {
		Queue<Node> queue = new ArrayDeque<>();
		queue.add(cheese);

		while (!queue.isEmpty()) {
			Node poll = queue.poll();

			for (int i = 0; i < 4; i++) {
				int nx = poll.x + x[i];
				int ny = poll.y + y[i];
				if (ny >= 0 && ny < n && nx >= 0 && nx < m) {
					if (!check[ny][nx]) {
						if (arr[ny][nx] == 1) {
							arr[ny][nx] = 2;
							check[ny][nx] = true;
						}
						if (arr[ny][nx] == 0) {
							check[ny][nx] = true;
							queue.add(new Node(ny, nx));
						}
					}
				}
			}
		}

		remove();
	}

	public static int getCheeseCount() {
		int count = 0;
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < m; j++) {
				if (arr[i][j] == 1) {
					count++;
				}

			}
		}
		return count;
	}

	public static void remove() {
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < m; j++) {
				if (arr[i][j] == 2) {
					arr[i][j] = 0;
				}
			}
		}
	}

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String[] s = br.readLine().split(" ");
		n = Integer.parseInt(s[0]);
		m = Integer.parseInt(s[1]);

		arr = new int[n][m];
		check = new boolean[n][m];
		for (int i = 0; i < n; i++) {
			String[] s1 = br.readLine().split(" ");
			for (int j = 0; j < m; j++) {
				int num = Integer.parseInt(s1[j]);
				arr[i][j] = num;
			}
		}

		boolean flag = true;
		int lastCount = 0;
		while (flag) {
			time++;
			lastCount = getCheeseCount();
			solve(new Node(0, 0));
			for (int i = 0; i < n; i++) {
				Arrays.fill(check[i], false);
			}
			int count = getCheeseCount();

			if (count == 0) {
				flag = false;
			}
		}

		System.out.println(time);
		System.out.println(lastCount);
	}

}