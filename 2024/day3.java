import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;
import java.util.regex.Matcher;
import java.util.regex.Pattern;
import java.util.ArrayList;

public class day3 {
    public static int part1(String fileData) {
        Pattern pattern = Pattern.compile("mul\\(\\d{1,3},\\d{1,3}\\)");
        Matcher matcher = pattern.matcher(fileData);
        int total = 0;
        while (matcher.find()) {
            String[] chopped = matcher.group().split(",");
            int firstNum = Integer.parseInt(chopped[0].substring(4));
            int secondNum = Integer.parseInt(chopped[1].replaceFirst(".$",""));
            total += (firstNum * secondNum);
        }
        return total;
    }

    public static void part2(StringBuilder fileData) {
        // split into substrings of valid, search in there
        ArrayList<String> enabled = new ArrayList<>();
        String[] subs = fileData.toString().split("don't");

        for (int i = 0; i < subs.length; i++) {

            if (i == 0) {
                // first one
                enabled.add(subs[0]);
                continue;
            }
            for (int j = 0; j < subs[i].length(); j++) {

                try {
                if (subs[i].charAt(j) == 'd' && subs[i].charAt(j + 1) == 'o' && subs[i].charAt(j + 2) == '('
                        && subs[i].charAt(j + 3) == ')') {
                    enabled.add(subs[i].substring(j));
                    break;
                }
                } catch (Exception e) {
                    //
                }
            }
        }
        int fin = 0;
        for (String str : enabled) {
            fin += part1(str);
        }
        System.out.println(fin);
    }

    public static void main(String[] args) {
        StringBuilder fileData = new StringBuilder();
        try {
                File myObj = new File("input3.txt");
                Scanner myReader = new Scanner(myObj);
                while (myReader.hasNextLine()) {
                    String data = myReader.nextLine();
                    fileData.append("\n" + data);
                }
                myReader.close();
        } catch (FileNotFoundException e) {
                System.out.println("An error occurred.");
                e.printStackTrace();
        }
        System.out.println(part1(fileData.toString()));
        part2(fileData);
    }
}
