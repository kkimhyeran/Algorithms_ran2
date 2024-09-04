import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        // 1. 입력값
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine());
        long[] machine_array = new long[n]; // 운동기구 별 근손실 정도
        for (int i = 0; i < n; i++){
            machine_array[i] = Long.parseLong(st.nextToken());
        }

        // 2. 정렬
        Arrays.sort(machine_array);

        // 3. 근손실 m 구하기
        long max_val = 0;

        // 운동기구 개수가 짝수이면
        if (n%2 == 0){
            for (int i = 0; i < n/2; i++){
                max_val = Math.max(max_val, machine_array[i] + machine_array[n-1-i]);
            }
        } else {
            max_val = machine_array[n-1]; // 마지막 운동기구 근손실 값을 최대값으로 설정하고
            // 나머지 운동기구들의 근손실 합 구하기
            for (int i = 0; i < (n-1)/2; i++){
                max_val = Math.max(max_val, machine_array[i] + machine_array[n-2-i]);
            }
        }

        System.out.println(max_val);

    }
}
