import java.util.ArrayList;
import java.util.Scanner;
import java.util.stream.IntStream;
import java.util.List;

public class Main {
    public static void main(String[] args) {
        celToFah(); //used to call defined code
    }
    static void celToFah(){
        Scanner scanner = new Scanner(System.in); //initialize new scanner object

        System.out.print("Enter the name of the city you are visiting: ");
        String city = scanner.nextLine();
        System.out.print("Enter a temperature in degrees Celsius: ");
        String cels = scanner.nextLine();

        System.out.println("The temperature in " + city + " is likely to be: ");
        System.out.println("Celsius\t\tFahrenheit");

        IntStream range = IntStream.range(Integer.parseInt(cels), Integer.parseInt(cels) + 10); // initializing range
        //initialize new lists for cel and fah
        List tbl1 = new ArrayList();
        List tbl2 = new ArrayList();

        if(Integer.parseInt(cels) <= 15) {
            for (double i : range.toArray()) {
                int cel = (int) (i - 9);
                tbl1.add(cel);
                double fah = ((i - 9) * 9 / 5) + 32;
                tbl2.add(fah);
                System.out.println(Integer.toString(cel) + "\t\t\t" + Double.toString(fah));
            }
        }else if (Integer.parseInt(cels) >=16){
           for (double i: range.toArray()){
               int cel = (int) i;
               tbl1.add(cel);
               double fah = (i * 9/5) + 32;
               tbl2.add(fah);
               System.out.println(Integer.toString(cel) + "\t\t\t" + Double.toString(fah));
           }
        }
    }
}