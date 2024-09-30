import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        // 1. 입력값
        Scanner scanner = new Scanner(System.in);
        String cryingSound = scanner.nextLine();


        // 2. 울음 소리 길이 확인
        //  오리 울음 소리 % 5 != 0 > 오리 수 구할 수 없다.
        if (cryingSound.length() % 5 != 0) {
            System.out.println(-1);
            return;
        }

        // 3. 필요한 변수 설정
        String soundOrder = "quack"; // 오리 울음소리 순서
        int duckCount = 0; // 오리 수 확인 변수
        int[] checkSoundList = new int[cryingSound.length()]; // 해당 울음소리 글자 확인하면 확인 처리

        // 4. 오리 수 세기 시작
        for (int i = 0; i < cryingSound.length(); i++) {
            // q 부터 시작하면 오리 울음 확인 시작
            if (cryingSound.charAt(i) == 'q' && checkSoundList[i] == 0) {
                int j = 0;
                int firstDuck = 0;

                for (int k = i; k < cryingSound.length(); k++) {
                    // 오리 울음 소리 순서 + 아직 확인하지 않은 글자이면
                    if (cryingSound.charAt(k) == soundOrder.charAt(j) && checkSoundList[k] == 0) {

                        checkSoundList[k] = 1; // 울음 확인 처리
                        j++; // 순서 업데이트

                        // 마지막 울음 글자이면
                        if (cryingSound.charAt(k) == 'k') {
                            j = 0; // 순서 리셋 처리

                            if (firstDuck == 0) {
                                duckCount++; // 오리 수 카운트
                                firstDuck = 1;
                            }
                        }
                    }
                }
            }
        }

        // 5. 결과 출력

        // if 오리 수 없음 or 아직 확인하지 않은 글자가 있다면?
        if (duckCount == 0 || countZeros(checkSoundList) >= 1) {
            System.out.println(-1);
        } else { // 그렇지 않으면 오리 수 출력
            System.out.println(duckCount);
        }

        scanner.close();
    }

    // 0 개수 세기 함수 선언
    private static int countZeros(int[] array) {
        int count = 0;
        for (int value : array) {
            if (value == 0) {
                count++;
            }
        }
        return count;
    }
}