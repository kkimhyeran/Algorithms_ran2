import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) throws IOException {

        // 1. 입력값 받기
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        String[] input_source = br.readLine().split(" ");
        int[] source_array = new int[n];
        for (int i = 0; i < n; i++) {
            source_array[i] = Integer.parseInt(input_source[i]);
        }

        int m = Integer.parseInt(br.readLine());
        String[] input_target = br.readLine().split(" ");
        int[] target_array = new int[m];
        for (int i = 0; i < m; i++) {
            target_array[i] = Integer.parseInt(input_target[i]);
        }

        // 2. source_array 정렬
        Arrays.sort(source_array);

        // 3. target_array의 각 값을 이분 탐색으로 확인
        for (int i = 0; i < m; i++) {
            if (binary_search(source_array, target_array[i])) {
                System.out.println(1);  // target 값이 source_array에 존재하는 경우
            } else {
                System.out.println(0);  // target 값이 source_array에 없는 경우
            }
        }
    }

    // 이분 탐색 메소드 (target 값을 찾으면 true, 없으면 false 반환)
    private static boolean binary_search(int[] source_array, int target) {
        int start = 0;
        int end = source_array.length - 1;

        while (start <= end) {
            int mid = (start + end) / 2;
            if (source_array[mid] == target) {
                return true;  // target 값을 찾은 경우
            } else if (source_array[mid] > target) {
                end = mid - 1;  // target이 더 작다면 왼쪽 부분 탐색
            } else {
                start = mid + 1;  // target이 더 크다면 오른쪽 부분 탐색
            }
        }
        return false;  // target 값을 찾지 못한 경우
    }
}
