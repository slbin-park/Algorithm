import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Deque;
import java.util.StringTokenizer;

public class Main {

	static int answer, n, first_idx;
	static int[][] arr;
	static int[][] dis;
	static int[] visited;
	static BufferedWriter bw;

	public static void dfs(int depth, int idx, int cost) {
//		System.out.println("idx = " + idx);
		if (depth == n) {
			if (arr[idx][first_idx] != 0) {
				cost += arr[idx][first_idx];
//			System.out.println("cost = " + cost);
				answer = Integer.min(answer, cost);
			}

			return;
		}
		for (int i = 0; i < n; i++) {
			if (arr[idx][i] != 0 && visited[i] == 0) {
				visited[i] = 1;
                if(answer > cost+arr[idx][i]){
				dfs(depth + 1, i, cost + arr[idx][i]);
                }
				visited[i] = 0;
			}
		}
	}

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		bw = new BufferedWriter(new OutputStreamWriter(System.out));
		n = Integer.parseInt(st.nextToken());
		arr = new int[n][n];
		answer = Integer.MAX_VALUE;
		for (int i = 0; i < n; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 0; j < n; j++) {
				arr[i][j] = Integer.parseInt(st.nextToken());
			}
		}
			first_idx = 0;
			visited = new int[n];
			visited[0] = 1;
			dfs(1, 0, 0);
		System.out.println(answer);
//		bw.newLine();
//		bw.flush();
		bw.close();
//		System.out.println();
//		System.out.println(Arrays.toString(dis));
		br.close();
	}
}
