import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    //오대위 - 오 - 오대아 순서
    static int[] dx = {-1, 0, 1};
    static int[] dy = {1, 1, 1};
    static boolean[][] visit;
    private static StringBuilder sb = new StringBuilder();
    static int r, c;
    static char[][] map;
    static int result;

    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        //지도 크기얌
        r = Integer.parseInt(st.nextToken());
        c = Integer.parseInt(st.nextToken());

        //지도 입력받기
        map = new char[r][c];
        for (int i = 0; i < r; i++) {
            char[] tem = br.readLine().toCharArray();
            for (int j = 0; j < c; j++) {
                map[i] = tem;
            }
        }
        result = 0;
        //방문배열 초기화
        visit = new boolean[r][c];
        for (int i = 0; i < r; i++) {
            dfs(i, 0);
//            System.out.println("--------------------------------------------");
//            for (int q = 0; q < r; q++) {
//                for (int w = 0; w < c; w++) {
//                    System.out.print(map[q][w] + " ");
//                }
//                System.out.println();
//            }
        }


        System.out.println(result);


    }

    private static boolean dfs(int i, int j) {
        if (j == c - 1) { //열에 도달 했다면
            result++;
            return true;
        }
        visit[i][j] = true;
        for (int go = 0; go < 3; go++) {
            int gox = i + dx[go];
            int goy = j + dy[go];

            if (canGo(gox, goy) && map[gox][goy] == '.') { //범위안이면서 갈 수 있다면
                if (!visit[gox][goy]) {
                    map[gox][goy] = '%';
                    visit[gox][goy] = true;
                    if (dfs(gox, goy)) {
                        return true;
                    }
                }
            }
        }
        return false;
    }

    private static boolean canGo(int gox, int goy) {
        if (gox >= 0 && gox < r && goy >= 0 && goy < c) {
            return true;
        }
        return false;
    }
}