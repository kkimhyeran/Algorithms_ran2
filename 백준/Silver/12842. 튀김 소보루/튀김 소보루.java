import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;


public class Main {
    public static void main(String[] args) throws IOException {
        // 1. 입력값
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] input = br.readLine().split(" ");

        int n = Integer.parseInt(input[0]); // 사온 튀김 소보루 개수
        int s = Integer.parseInt(input[1]); // 먹고 남은 튀김 소보루 개수

        StringTokenizer st = new StringTokenizer(br.readLine());
        int m = Integer.parseInt(st.nextToken()); // 튀김 소보루를 먹는 사람 수

        // 튀김 소보루를 먹는 사람들이 먹는데 걸리는 시간
        int[] orders = new int[m];
        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            orders[i] = Integer.parseInt(st.nextToken());
        }

        // 2. 튀김 소보루 먹기

        int eat_cnt = n - s;
        int time = 0;
        int now_person = -1;

        while (eat_cnt > 0) {
            for (int i = 0; i <m; i++ ) {
                // 해당 사람은 자기 먹는 시간 배수일 때만 먹을 수 있다.
                if (time % orders[i] == 0) {
                    eat_cnt -= 1; // 먹으면 소보루 먹었다 한다.
                    now_person = i; // 현재 먹은 사람 저장

                    if (eat_cnt == 0) {
                        break;
                    }
                }

            }
            time ++; // 모두 다먹었으면 시간 업데이트
        }

        // 3. 결과 출력
        System.out.println(now_person + 1);
    }
}
