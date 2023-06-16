package jv_code.decorator;

// Create a VegFood class that  will implements
// the Food interface and overrie
// all the methods.
public class VegFood implements Food {
   public String prepareFood() {
      return "Veg Food";
   }

   public double foodPrice() {
      return 50.0;
   }
}
