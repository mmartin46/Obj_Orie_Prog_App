

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

// Create concrete classes that extend the Loan abstract class
class HomeLoan extends Loan {
   public void getInterestRate(double r) {
      rate=r;
   }  
}
class BusinessLoan extends Loan {
   public void getInterestRate(double r) {
      rate=r;
   }
}

// Create an abstract class to get the factories
// for Bank and Loan objects
abstract class AbstractFactory {
   public abstract Bank getBank(String bank);
   public abstract Loan getLoan(String loan);
}


// Create the factory classes that inherit AbstractFactory
// class to generate the object of concrete class based
// on given information.
class BankFactory extends AbstractFactory {
   public Bank getBank(String bank) {
      if (bank == null) {
         return null;
      }
      if (bank.equalsIgnoreCase("BIG")) {
         return new BigBank();
      } else if (bank.equalsIgnoreCase("SMALL")) {
         return new SmallBank();
      }
      return null;
   }

   public Loan getLoan(String loan) {
      return null;
   }
}
class LoanFactory extends AbstractFactory {
   public Bank getBank(String bank) {
      return null;
   }

   public Loan getLoan(String loan) {
      if (loan == null) {
         return null;
      }

      if (loan.equalsIgnoreCase("HOME")) {
         return new HomeLoan();
      } else if (loan.equalsIgnoreCase("BUSINESS")) {
         return new BusinessLoan();
      }
      return null;
   }
}

// Create a FactoryCreator class to get
// the factories by passing information
// (e.g. Loan or Bank)
class FactoryCreator {
   public static AbstractFactory getFactory(String choice) {
      if (choice.equalsIgnoreCase("BANK")) {
         return new BankFactory();
      } else if (choice.equalsIgnoreCase("LOAN")) {
         return new LoanFactory();
      }
      return null;
   }
}
