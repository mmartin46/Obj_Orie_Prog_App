package builder;

// Create 2 implementation classes of Company:
// Sony and Samsung
public class Sony extends Company {
   @Override
   public int price() {
      return 20;
   }
   @Override
   public String pack() {
      return "Sony CD";
   }
}
