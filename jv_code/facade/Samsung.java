package jv_code.facade;

public class Samsung implements MobileShop {
   @Override
   public void modelNo() {
      System.out.println(" Samsung Galaxy ");
   }

   @Override
   public void price() {
      System.out.println("40000.00");
   }
}
