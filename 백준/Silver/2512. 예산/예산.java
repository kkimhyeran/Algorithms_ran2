import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {

    public static void main (String[] args) throws IOException {

        // 1. 입력값
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken()); // 도시 개수

        int[] budget_array = new int[n];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            budget_array[i] = Integer.parseInt(st.nextToken());
        } // 도시별 요구 예산


        // 총 예산액
        st = new StringTokenizer(br.readLine());
        int budget = Integer.parseInt(st.nextToken());

        int start = 1;
        int end = Arrays.stream(budget_array).max().getAsInt(); // 현재 예산에서 최대값

        int mid = 0;
        int result = 0;

        // 2. 상한액 찾기
        while (start <= end) {
            mid = (start + end) / 2;
            int total = 0;

            for (int i = 0; i < n; i++){
                if (budget_array[i] >= mid) {
                    total += mid;
                } else {
                    total += budget_array[i];
                }
            }

            // 현재 mid 기준으로 예산 분배 후 예산 남으면 start + 1
            if (total <= budget){
                start = mid + 1;
                result = mid;
            }
            else {
                end = mid -1; // 예산이 부족하면
            }
        }

        // 3. 결과 출력
        System.out.println(result);

    }

}
