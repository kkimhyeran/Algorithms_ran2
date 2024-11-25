class Solution {
    public static int solution(String[][] board, int h, int w) {
        // 같은 색으로 칠해진 칸의 개수를 저장할 변수 count
        int count = 0;

        // h와 w의 변화량을 저장할 배열
        int[] dh = {0, 1, -1, 0};
        int[] dw = {1, 0, 0, -1};

        // 보드의 크기 n
        int n = board.length;

        // 현재 선택된 칸의 색깔
        String color = board[h][w];

        // 반복문을 이용해 상하좌우 이웃한 칸을 확인
        for (int i = 0; i < 4; i++) {
            int hCheck = h + dh[i];
            int wCheck = w + dw[i];

            // 이웃한 칸이 보드 범위를 벗어나지 않는지 확인
            if (hCheck >= 0 && hCheck < n && wCheck >= 0 && wCheck < n) {
                // 현재 색깔과 이웃한 칸의 색깔이 같다면 count 증가
                if (board[hCheck][wCheck].equals(color)) {
                    count++;
                }
            }
        }

        // 같은 색으로 칠해진 칸의 개수를 반환
        return count;
    }
}