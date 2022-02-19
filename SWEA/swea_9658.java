import java.util.Scanner;

public class swea_9658 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in); // input
        int num = scanner.nextInt();
        scanner.nextLine();
        for (int i = 1; i <= num; i++) {
            String str = scanner.nextLine();
            /*
             * 1. input을 입력받음
             * 2. x.xxx*10^n 형태로 변형
             * 3. 소수 둘째자리에서 반올림
             * 4. 만약 9.99인 경우 n+1
             * */
            int N = Integer.parseInt(str.substring(0, 3));
            double NSecondRound = Double.parseDouble(String.format("%.1f", (double) N / 100.0));
            int NSecondRoundInt = (int) NSecondRound;
            if (Math.log10(NSecondRoundInt) + 1 >= 2) {
                System.out.println("#" + i + " " + NSecondRound / 10 + "*" + "10^" + str.length());
            } else {
                System.out.println("#" + i + " " + NSecondRound + "*" + "10^" + (str.length() - 1));
            }
        }
    }
}
