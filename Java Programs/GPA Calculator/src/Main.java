import java.util.*;

public class Main {
    public static void main(String[] args) {
        gradStatus();
    }

    static double inputConvertor(){
        Scanner scanner = new Scanner(System.in); //creating scanner object
        double convertedGrade = 0.0;

        System.out.print("Enter a letter Grade: ");
        String letterGrade = scanner.nextLine().toUpperCase();

        if(letterGrade.contains("A")){
            convertedGrade = 4.0;
        } else if (letterGrade.contains("B")) {
            convertedGrade = 3.0;
        } else if (letterGrade.contains("C")) {
            convertedGrade = 2.0;
        } else if (letterGrade.contains("D")) {
            convertedGrade = 1.0;
        } else if (letterGrade.contains("F")) {
            convertedGrade = 0.0;
        } else {
            System.out.println("Invalid input, please try again");
            inputConvertor();
        }
        return convertedGrade;
    }

    static void gradStatus(){
       double gradeOne = inputConvertor();
       double gradeTwo = inputConvertor();
       double gradeThree = inputConvertor();
       double gradeFour = inputConvertor();

       double finalResult = ((gradeOne + gradeTwo + gradeThree + gradeFour)/4);

       if(finalResult >=3.2 && finalResult <=3.6){
            System.out.println("GPA is " + Double.toString(finalResult) + "\nStudent can graduate cum laude");
       }else if(finalResult >=3.6 && finalResult <=3.8){
            System.out.println("GPA is " + Double.toString(finalResult) + "\nStudent can graduate magna cum laude");
       }else if(finalResult >=3.8 && finalResult <=4.0){
            System.out.println("GPA is " + Double.toString(finalResult) + "\nStudent can graduate summa cum laude");
       }else if(finalResult >=2.0 && finalResult <=3.2){
            System.out.println("GPA is " + Double.toString(finalResult) + "\nStudent can graduate");
       }else{
           System.out.println("Student is not eligible for graduation");
       }

    }
}