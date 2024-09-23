import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;
import java.util.List;

public class Main {
    public static void main(String[] args) throws IOException {
        // 1. 입력값 받기
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] input = br.readLine().split(" ");

        int n = Integer.parseInt(input[0]); // 수빈이 위치
        int k = Integer.parseInt(input[1]); // 동생 위치

        // 2. 큐 선언
        Queue<Integer> q = new LinkedList<>();
        q.add(n); // 수빈이 현재 위치 n 추가

        // 방문 확인 및 이전 위치 추적
        int[] visited = new int[100001];
        int[] previous = new int[100001]; // 경로 추적용 배열
        visited[n] = 1; // 수빈이 처음 위치는 방문 처리
        previous[n] = -1; // 시작점은 이전 위치가 없으므로 -1로 설정

        // 3. BFS
        while (!q.isEmpty()) {
            int now = q.poll();

            if (now == k) {
                break; // 동생 위치에 도달했으면 탐색 종료
            }

            // 방문할 위치
            int[] dest_array = {now * 2, now - 1, now + 1};
            for (int next : dest_array) {
                if (0 <= next && next <= 100000 && visited[next] == 0) {
                    q.add(next);
                    visited[next] = visited[now] + 1; // 이동한 거리 기록
                    previous[next] = now; // 이전 위치를 기록하여 경로 추적 가능하게 만듦
                }
            }
        }

        // 4. 경로 역추적
        List<Integer> path_list = new ArrayList<>();
        int current = k;

        while (current != -1) { // 시작점까지 역추적
            path_list.add(current);
            current = previous[current]; // 이전 위치로 이동
        }

        // 5. 결과 출력
        System.out.println(visited[k] - 1);

        // 경로 출력 (역추적한 경로를 뒤집어서 출력)
        for (int i = path_list.size() - 1; i >= 0; i--) {
            System.out.print(path_list.get(i) + " ");
        }
    }
}
