import java.util.Scanner;

public class Java_variables {
    public static void main(String[] args) {
        //creating a variable
        int x = 123;
        long t = 1234567889454444L;
        float y = 3.14f;
        double u = 3.1415926535;
        boolean z = true;
        char symbol = '@';
        String name = "Vedita1331";
        System.out.println("My number is: "+x);

        //swapping variables
        String name2 = "Wallace";
        String temp = null;
        temp = name;
        name = name2;
        name2 = temp;
        System.out.println(name + " = " + name2);

        //User input
        Scanner scanner1 = new Scanner(System.in);

        System.out.println("What is your name? ");
        String Username = scanner1.nextLine();

        System.out.println("Hello " + Username);

    }
}