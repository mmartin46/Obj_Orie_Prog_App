package jv_code.facade;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class FacadePatternClient {
   private static int choice;
   public static void main(String args[]) throws NumberFormatException, IOException {
      do {
         System.out.print("  1. Iphone     \n")
         System.out.print("  2. Samsung    \n")
         System.out.print("  3. Exit       \n")   
      
         BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
         choice = Integer.parseInt(br.readLine());
         ShopKeeper sk = new ShopKeeper();

         switch (choice) {
            case 1:
            {
               sk.iphoneSale();
            }
            break;
            case 2:
            {
               sk.samsungSale();
            }
            break;
            default:
            {
               System.out.println("Nothing purchased");
            }
            return;
         }
      } while (choice != 4);
   }
}