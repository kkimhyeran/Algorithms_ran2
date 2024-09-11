import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
    static int n, m;
    static int[][] miro;
    static boolean[][] visited;

    // 이동방향 (상하좌우)
    static int[][] move = {{-1, 0}, {1, 0}, {0, 1}, {0, -1}};

    //  bfs 함수
    public static void bfs(int x, int y) {
        Queue<int[]> q = new LinkedList<>();
        q.add(new int[] {x, y}); //시작 좌표 넣기

        while (!q.isEmpty()){
            int[] now = q.poll();

            for (int i = 0; i <4; i++ ) {
                int nx = now[0] + move[i][0];
                int ny = now[1] + move[i][1];

                // 좌표 범위 확인
                if (nx < 0 || nx >= n || ny < 0 || ny >= m)
                    continue;

                if (visited[nx][ny] || miro[nx][ny]== 0) {
                    continue;
                }

                q.add(new int[]{nx, ny}); // 다음에 방문 시작할 좌표로 큐에 추가
                miro[nx][ny] = miro[now[0]][now[1]] + 1; // 탐색 거리 업데이트
                visited[nx][ny] = true; // 방문처리
            }
        }
    }

    public static void main(String[] args) throws IOException {
        // 1. 입력값 받기
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        visited = new boolean[n][m];
        miro = new int[n][m];

        for (int i = 0; i < n; i++) {
            String le = br.readLine();
            char[] lines = le.toCharArray();

            for (int j = 0; j < lines.length; j++) {
                miro[i][j] = Character.getNumericValue(lines[j]);
            }
        }

        // 2. 시작점에서 목표점(n, m) 까지 거리 구하기
        visited[0][0] = true;
        bfs(0, 0);

        // 3. 결과 출력
        System.out.println(miro[n-1][m-1]);
    }
}
