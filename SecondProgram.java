
import java.util.Scanner;

public class SecondProgram {
    public static void main(String[] args) {
        Scanner se=new Scanner(System.in);
        System.out.println("Enter first number : ");
        int num1=se.nextInt();
        System.out.println("Enter second number : ");
        int num2=se.nextInt();
        System.out.printf("The sum of %d + %d = %d",num1,num2,(num1+num2));
    }
}
