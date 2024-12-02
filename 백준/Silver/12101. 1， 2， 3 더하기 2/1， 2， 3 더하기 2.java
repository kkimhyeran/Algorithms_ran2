import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Main {
    static int[] values = {1, 2, 3}; // 더하기로 만들 수 있는 수
    static List<List<Integer>> results = new ArrayList<>(); // 결과 저장

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // 1. 입력값
        int n = scanner.nextInt();
        int k = scanner.nextInt();

        // 2. dfs
        dfs(new ArrayList<>(), 0, n);

        // 3. 결과 출력
        if (k - 1 < results.size()) {
            List<Integer> result = results.get(k - 1);
            System.out.println(String.join("+", result.stream().map(String::valueOf).toArray(String[]::new)));
        } else {
            System.out.println(-1);
        }

    }

    // dfs
    public static void dfs(List<Integer> numbers, int totalSum, int target) {
        // 합에 도달하면 저장
        if (totalSum == target) {
            results.add(new ArrayList<>(numbers));
            return;
        }

        // 초과
        if (totalSum > target) {
            return;
        }


        for (int val : values) {
            numbers.add(val); // 더하깉
            dfs(numbers, totalSum + val, target); // dfs 재귀
            numbers.remove(numbers.size() - 1);
        }
    }
}
