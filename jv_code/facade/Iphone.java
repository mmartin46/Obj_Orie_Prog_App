package jv_code.facade;

public class Iphone implements MobileShop {
   @Override
   public void modelNo() {
      System.out.println(" Iphone 7 ");
   }

   @Override
   public void price() {
      System.out.println("65000.00");
   }
}
