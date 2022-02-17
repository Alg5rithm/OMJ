import java.util.Scanner;

public class swea_13547 {
    static String YES = "YES";
    static String NO = "NO";
    static int GAMENUM = 15;
    static int WINNUM = 8;

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int num = scanner.nextInt();
        scanner.nextLine();
        for (int i = 1; i <= num; i++) {
            String str = scanner.nextLine();
            int countX = countChar(str, 'x');
            int countO = countChar(str, 'o');
            int countRest = GAMENUM - countX - countO;
            if (countRest + countO >= WINNUM) {
                System.out.println("#" + i + " " + YES);
            } else {
                System.out.println("#" + i + " " + NO);
            }
        }
    }

    private static int countChar(String str, char ch) {
        int count = 0;
        for (int i = 0; i < str.length(); i++) {
            if (str.charAt(i) == ch) {
                count++;
            }
        }
        return count;
    }
}
