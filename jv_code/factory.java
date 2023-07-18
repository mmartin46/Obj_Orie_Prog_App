

// Create a Book abstract class
abstract class Book {
   protected double price;
   abstract void getPrice();

   public void calculateTotal(int quantity) {
      System.out.println(quantity * price);
   }
}

// Create the concrete classes than
// extends the Book abstract class
class RedBook extends Book {
   @Override
   public void getPrice() {
      price = 3.00;
   }
}
class BlackBook extends Book {
   @Override
   public void getPrice() {
      price = 2.00;
   }
}
class BlueBook extends Book {
   @Override
   public void getPrice() {
      price = 9.00;
   }
}

// Create a GetBookFactory
// to generate an object
// based on given information.
class GetBookFactory {
   public Book getBook(String bookType) {
      if (bookType == null) {
         return null;
      }

      if (bookType.equalsIgnoreCase("RED")) {
         return new RedBook();
      }
      else if (bookType.equalsIgnoreCase("BLACK")) {
         return new BlackBook();
      }
      else if (bookType.equalsIgnoreCase("BLUE")) {
         return new BlueBook();
      }
      return null;
   }
}




