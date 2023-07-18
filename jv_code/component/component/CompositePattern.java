package component;

import java.util.ArrayList;

public class CompositePattern {
   public static void main(String args[]) {
      Employee emp1 = new Cashier(201, "Josh Beard", 20000.0);
      Employee emp2 = new Accountant(401, "John Heard", 20000.0);
      Employee emp3 = new Accountant(401, "John Pat", 10000.0);
      Employee manager1 = new BankManager(100, "Thomas Liz", 300000.0);

      manager1.add(emp1);
      manager1.add(emp2);
      manager1.add(emp3);


   }
}
