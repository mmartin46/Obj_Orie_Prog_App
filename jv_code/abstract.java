
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
   protected double rate;
   abstract void getInterestRate(double rate);
   public void calculateLoanPayment(double loanamount, int years) {
      double EMI;
      int n;

      n=years*12;
      rate=rate/1200;
      EMI=((rate*Math.pow((1+rate), n)) / ((Math.pow((1 + rate), n)) - 1))*loanamount;

      System.out.println("The monthly EMI is " + EMI + " for the amount" + loanamount + " you have borrowed");
   }
}