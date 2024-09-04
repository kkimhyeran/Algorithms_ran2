import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {

        // 1. 입력값
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());

        // 교실별 방문 점수 입력 처리
        st = new StringTokenizer(br.readLine());
        long[] visit_class_array = new long[n];
        for (int i = 0; i < n; i++) {
            visit_class_array[i] = Integer.parseInt(st.nextToken());
        }

        // 2. 누적합 + 정렬
        for (int i = 1; i < n; i++) {
            visit_class_array[i] = visit_class_array[i] +  visit_class_array[i-1];
        }
        Arrays.sort(visit_class_array);

        
        // 3. 점수 계산
        long total_sum =  0;
        while (k > 0) {
            total_sum += visit_class_array[--n];
            k--;
        }

        // 4. 출력
        System.out.println(total_sum);

    }
}
