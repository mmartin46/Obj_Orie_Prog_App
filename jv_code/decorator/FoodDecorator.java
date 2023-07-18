package jv_code.decorator;


// Create a FoodDecorator abstract class
// that will implement the Food interface
// and override all its methods and has the
// abiliy to decorate more foods.
public abstract class FoodDecorator implements Food {
   private Food newFood;
   public FoodDecorator(Food newFood) {
      this.newFood = newFood;
   }
   @Override
   public String prepareFood() {
      return newFood.prepareFood();
   }

   public double foodPrice() {
      return newFood.foodPrice();
   }
}
