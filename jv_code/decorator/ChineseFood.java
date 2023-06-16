package jv_code.decorator;

// Create a ChineseFood concrete class
// that will extend the FoodDecorator
// class and override its all methods.
public class ChineseFood extends FoodDecorator {
   public ChineseFood(Food newFood) {
      super(newFood);
   }

   public String prepareFood() {
      return super.prepareFood() + " With Fried Rice ";
   }

   public double foodPrice() {
      return super.foodPrice() + 65.0;
   }
}
