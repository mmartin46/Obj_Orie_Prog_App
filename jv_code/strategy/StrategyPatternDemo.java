package strategy;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class StrategyPatternDemo {
    
    public static void main(String[] args) throws NumberFormatException, IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        System.out.print("Enter the first value: ");
        float val1 = Float.parseFloat(br.readLine());

        System.out.print("Enter the second value: ");
        float val2 = Float.parseFloat(br.readLine());

        Context context = new Context(new Addition());
        System.out.println("Addition = " + context.executeStrategy(val1, val2));

        context = new Context(new Subtraction());
        System.out.println("Subtraction = " + context.executeStrategy(val1, val2));
    }
}
