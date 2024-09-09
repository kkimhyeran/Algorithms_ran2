import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static int cnt = 0;
    static boolean[] visited;
    static int[][] graph;
    static int n;

    public static void main(String[] args) throws IOException {
        // 1. 입력값 받기
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine()); // 컴퓨터의 수
        int p = Integer.parseInt(br.readLine()); // 연결된 쌍의 수

        // 네트워크 정보 2차원 배열로 입력받기
        graph = new int[n+1][n+1];

        for(int i=0; i<p; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());

            graph[a][b] = graph[b][a] = 1;
        }

        // 방문확인 배열 초기화
        visited = new boolean[n+1];

        // dfs 실행
        dfs(1);
        System.out.println(cnt - 1);  // 1번 컴퓨터는 제외해야 하므로 cnt-1
    }

    public static void dfs(int start){
        visited[start] = true;
        cnt++;

        for(int i = 1; i <= n; i++) {  // i는 1부터 시작해야 함
            if(graph[start][i] == 1 && !visited[i])
                dfs(i);
        }
    }
}
