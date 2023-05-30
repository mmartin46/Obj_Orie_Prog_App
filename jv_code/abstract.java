
// Create a Bank Interface
interface Bank {
   String getBankName();
}

// Create concrete classes
// that implement the Bank interface
class BigBank implements Bank {
   private final String BANK_NAME;
   public BigBank() {
      BANK_NAME="BigBank";
   }

   public String getBankName() {
      return BANK_NAME;
   }
}
class SmallBank implements Bank {
   private final String BANK_NAME;
   public SmallBank() {
      BANK_NAME = "SmallBank";
   }

   public String getBankName() {
      return BANK_NAME;
   }
}
class MediumBank implements Bank {
   private final String BANK_NAME;
   public MediumBank() {
      BANK_NAME = "MediumBank";
   }

   public String getBankName() {
      return BANK_NAME;
   }
}


// Create the Loan Abstract Class
abstract class Loan {
   
}