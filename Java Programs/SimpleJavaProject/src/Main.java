import java.util.*;

public class Main {
    public static void main(String[] args) {
        //create scanner and get input from user
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter the first number: ");
        int numberOne = Integer.parseInt(scanner.nextLine());
        System.out.print("Enter the second number: ");
        int numberTwo = Integer.parseInt(scanner.nextLine());

        //print values
        System.out.println("Sum: " + (numberOne + numberTwo));
        System.out.println("Product: " + (numberOne * numberTwo));
        if (numberOne > numberTwo){
            System.out.println("Difference: " + (numberOne - numberTwo));
            System.out.println("Quotient: " + (numberOne / numberTwo));
        } else {
            System.out.println("Difference: " + (numberTwo - numberOne));
            System.out.println("Quotient: " + (numberOne / numberTwo));
        }
    }
}