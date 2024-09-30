import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Stack;
import java.util.StringTokenizer;

public class Main {
    static Stack<Assignment> stack;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int totalTime = Integer.parseInt(br.readLine()); // 총 공부시간
        stack = new Stack<>();

        int rslt = 0; // 총 점수 저장

        // 총 시간만큼 루프 돌면서 과제 처리
        for (int i = 0; i < totalTime; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());

            // (1) 과제가 주어졌다면
            int taskInfo = Integer.parseInt(st.nextToken());
            if (taskInfo == 1) { // 과제가 있는 경우
                int score = Integer.parseInt(st.nextToken()); // 과제 점수
                int time = Integer.parseInt(st.nextToken());  // 필요한 시간

                // 과제를 스택에 넣을 때, 시간이 남아있으면 넣음
                if (time - 1 > 0) {
                    stack.push(new Assignment(score, time - 1));
                } else {
                    rslt += score; // 시간이 다되면 바로 점수 추가
                }

            } else { // 과제가 없을 때
                if (!stack.isEmpty()) { // 현재 해야할 과제가 있다면
                    Assignment current = stack.pop(); // 스택에서 과제 꺼내기
                    current.time--; // 남은 시간 감소

                    // 시간이 다 끝나면 점수 추가
                    if (current.time == 0) {
                        rslt += current.score;
                    } else {
                        stack.push(current); // 다시 스택에 넣어 작업 이어서 진행
                    }
                }
            }
        }

        System.out.println(rslt); // 최종 점수 출력
    }

    // 과제 클래스: 점수와 남은 시간을 관리
    static class Assignment {
        int score;
        int time;

        public Assignment(int score, int time) {
            this.score = score;
            this.time = time;
        }
    }
}
