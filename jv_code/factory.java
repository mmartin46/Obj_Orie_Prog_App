// Isaiah 40:31

// Create a Plan abstract class
import java.io.*;
abstract class Plan {
   protected double rate;
   abstract void getRate();

   public void calculateBill(int units) {
      System.out.println(units * rate);
   }
}



// Create the concrete classes that extends
// Plan abstract class.
class DomesticPlan extends Plan {
   @Override
   public void getRate() {
      rate = 3.50;
   }
}
class CommercialPlan extends Plan {
   @Override
   public void getRate() {
      rate = 7.50;
   }
}
class InstitutionalPlan extends Plan {
   @Override
   public void getRate() {
      rate = 5.50;
   }
}

// Create a GetPlanFactory to generate object
// based on given information.
class GetPlanFactory {
   
   public Plan getPlan(String planType) {
      if (planType == null) {
         return null;
      }

      if (planType.equalsIgnoreCase("DOMESTICPLAN")) {
         return new DomesticPlan();
      }
      else if (planType.equalsIgnoreCase("INSTITUTIONALPLAN")) {
         return new InstitutionalPlan();
      }
      return null;
   }
}

