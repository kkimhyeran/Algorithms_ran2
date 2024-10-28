import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Collections;

public class Main {
    public static void main(String[] argr) throws IOException {
        // 1. 입력값
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());


        // 첫번째 수열 (재정렬 가능)
        String[] input_a = br.readLine().split(" ");
        int[] a_array = new int[n];
        for (int i = 0; i < n; i++) {
            a_array[i] = Integer.parseInt(input_a[i]);
        }

        // 두번째 수열
        String[] input_b = br.readLine().split(" ");
        Integer[] b_array = new Integer[n];
        for (int i = 0; i < n; i++) {
            b_array[i] = Integer.parseInt(input_b[i]);
        }

        // 2. 첫번째 수열을 두번째 배열 기준으로 정렬하기?
        Arrays.sort(a_array); // 오름차순 정렬
        Arrays.sort(b_array, Collections.reverseOrder()); // 내림차순 정렬

        // 3. 최솟값 계산
        int rslt = 0;
        for (int i = 0; i <n; i++) {
            rslt += a_array[i]*b_array[i];
        }

        // 4. 출력
        System.out.println(rslt);

    }
}
