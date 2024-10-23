import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) throws IOException {

        // 1. 입력값
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] input = br.readLine().split(" ");
        int m = Integer.parseInt(input[0]); // 조카 수
        int n = Integer.parseInt(input[1]); // 과자 수

        String[] num_inputs = br.readLine().split(" ");
        int[] snack_array = new int[n];
        for (int i = 0; i < n; i++) {
            snack_array[i] = Integer.parseInt(num_inputs[i]);
        }
        // 2. 이분 탐색
        int start = 1;
        int end = Arrays.stream(snack_array).max().getAsInt();
        int rslt = 0;

        while (start <= end) {
            // 현재 막대과자길이
            int cnt = 0;
            int mid = (start + end) / 2;

            for (int i = 0; i < n; i++) {
                // 조카에게 나눠줄 수 있는 과자 개수 구하기
                // 만약 mid = 5, snack_array[i] = 10 이면, 이 과자는 2명에게 나눠줄 수 있음
                // snack_array[i] = 7 이면, 이 과자는 1명에게만 나눠줄 수 있음
                cnt += snack_array[i] / mid;
            }

            // 나눠 줄 수 있는 과자수 확인
            // 조카들에게 충분히 나눠 줄 수 있으면 start = mid + 1
            if (cnt >= m) {
                if (rslt < mid) {
                    rslt = mid;
                    start = mid + 1;
                }
            } else { // 조카들에게 나눠줄 과자 부족하면 end 범위 줄이기
                end = mid - 1;
            }
        }

        // 3. 결과 출력
        System.out.println(rslt);
    }
}
