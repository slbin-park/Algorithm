import java.io.*;
import java.util.Stack;
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


    public static int op_rank(String oper) {
        if (oper.equals("(")) {
            return 0;
        }
        if (oper.equals("+") || oper.equals("-")) {
            return 1;
        }
        if (oper.equals("*") || oper.equals("/")) {
            return 2;
        }
        return 3;
    }

    public static boolean is_oper(String oper) {
        if (oper.equals("(") || oper.equals(")") || oper.equals("+") ||
                oper.equals("-") || oper.equals("*") || oper.equals("/"))
            return true;
        return false;
    }


    public static void main(String[] args) throws IOException {
        br = new BufferedReader(new InputStreamReader(System.in));
        st = new StringTokenizer(br.readLine());
//        N = Integer.parseInt(st.nextToken());
        String postfix = st.nextToken();
        // 피연산자 저장
        StringBuilder sb = new StringBuilder();
        // 연산자 저장
        Stack<String> p = new Stack<>();
        for (int i = 0; i < postfix.length(); i++) {
            String oper = String.valueOf(postfix.charAt(i));
            // 연산자라면
            if (is_oper(oper)) {
                // 연산자가 비어있다면
                if (p.isEmpty()) {
                    p.push(oper);
                } else if (oper.equals("(")) {
                    p.push(oper);
                }
                // 괄호가 닫힐경우 전부 뱉어냄
                else if (oper.equals(")")) {
                    while (!p.peek().equals("(")) {
                        sb.append(p.pop());
                    }
                    p.pop();
                    // 우선순위가 낮은게 나올 경우 전부 뱉어낸다
                } else if (op_rank(p.peek()) >= op_rank(oper)) {
                    while (!p.isEmpty() && op_rank(p.peek()) >= op_rank(oper)) {
                        sb.append(p.pop());
                    }
                    p.push(oper);
                } else {
                    p.push(oper);
                }
            } else {
                sb.append(oper);
            }
        }
        while (!p.isEmpty()) {
            sb.append(p.pop());
        }
        System.out.println(sb.toString());
        bw.flush();
    }
}
