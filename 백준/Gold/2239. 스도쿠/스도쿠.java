import java.io.*;
import java.lang.reflect.Array;
import java.util.*;

class Main {
	static class Node {
		int idx, cost;

		public Node(int idx, int cost) {
			this.idx = idx;
			this.cost = cost;
		}

	}

	static int n, m;
	static int[] visited;
	static int[] dx = { 1, -1, 0, 0 };
	static int[] dy = { 0, 0, -1, 1 };
	static BufferedWriter bw;
	static int[][] arr;
	static boolean flag;

	private static void dfs(int depth) {

		if (depth == 81) {
			flag = true;
			return;
		}

		int x = depth / 9;
		int y = depth % 9;

		if (arr[x][y] != 0)
			dfs(depth + 1);
		else {
			for (int i = 1; i < 10; i++) {
				if (!isValid(x, y, i))
					continue;
				arr[x][y] = i;
				dfs(depth + 1);
				if (flag)
					return;
				arr[x][y] = 0;

			}
		}

	}

	private static boolean isValid(int r, int c, int n) {

		for (int i = 0; i < 9; i++) {
			if (arr[i][c] == n || arr[r][i] == n)
				return false;
		}

		int sr = r / 3 * 3;
		int sc = c - c % 3;
		for (int row = sr; row < sr + 3; row++) {
			for (int col = sc; col < sc + 3; col++) {
				if (arr[row][col] == n)
					return false;
			}
		}

		return true;

	}

	public static void main(String[] args) throws IOException {
		// BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringTokenizer st;
		arr = new int[9][9];
		for (int i = 0; i < 9; i++) {
			st = new StringTokenizer(br.readLine());
			String a = st.nextToken();
			for (int j = 0; j < 9; j++) {
				String b = String.valueOf(a.charAt(j));
				// System.out.println(b);
				arr[i][j] = Integer.parseInt(b);
			}
		}

		dfs(0);

		for (int i = 0; i < 9; i++) {
			for (int j = 0; j < 9; j++) {
				bw.write(String.valueOf(arr[i][j]));
			}
			bw.newLine();
		}

		bw.flush();
		br.close();
		bw.close();
	}

}