

package builder;
import java.util.ArrayList;
import java.util.List;

/* USE IN SEPERATE FILE */
// Packing.java

// Create Packing interface
public interface Packing {
   public String pack();
   public int price();
}

/* USE IN SEPERATE FILE */
// CD.java

// Create 2 abstract classes 
// CD and Company
public abstract class CD implements Packing{
   public abstract String pack();
}
public abstract class Company extends CD{
   public abstract int price();
}

/* USE IN SEPERATE FILE */
// Sony.java

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

/* USE IN SEPERATE FILE */
// Samsung.java
public class Samsung extends Company {
   @Override
   public int price() {
      return 15;
   }
   @Override
   public String pack() {
      return "Samsung CD";
   }
}

/* USE IN SEPERATE FILE */
// CDType.java
public class CDType {
   private List<Packing> items = new ArrayList<Packing>();
   public void addItem(Packing packs) {
      items.add(packs);
   }

   public void getCost() {
      for (Packing packs : items) {
         packs.price();
      }
   }

   public void showItems() {
      for (Packing packing : items) {
         System.out.print("CD name: " + packing.pack());
         System.out.println("Price: " + packing.price());
      }
   }
}

/* USE IN SEPERATE FILE */
// CDBuilder.java
public class CDBuilder {
   public CDType buildSonyCD() {
      CDType cds = new CDType();
      cds.addItem(new Sony());
      return cds;
   }

   public CDType buildSamsungCD() {
      CDType cds = new CDType();
      cds.addItem(new Samsung());
      return cds;
   }
}

//BuilderDemo.java
public class BuilderDemo {
   public static void main(String args[]) {
      CDBuilder cdBuilder = new CDBuilder();
      CDType cdType1 = cdBuilder.buildSonyCD();
      cdType1.showItems();

      CDType cdType2 = cdBuilder.buildSamsungCD();
      cdType2.showItems();
   }
}