import java.io.BufferedReader;;
import java.io.IOException;
import java.io.InputStreamReader;


// We need to create an interface Prototype
// that contains a mehod getClone() of 
// Prototype type.
interface Prototype {
   public Prototype getClone();
}

// Then we create a concrete class GameRecord
// which implements Prototype interface that
// does the cloning of GameRecord object.
class GameRecord implements Prototype {
   private String name;
   private int consule;
   private int year;
   private int day;
   private int month;


   public GameRecord() {
      System.out.println("  Records of Games  ");
      System.out.println("---------------------------------");
      System.out.println("Name" + "\t" + "Consule" + "\t" + "Year" + "\t" + "Day" + "\t" + "Month");
   }

   public GameRecord(String name, int consule, int year, int day, int month) {
      this.name = name;
      this.consule = consule;
      this.day = day;
      this.month = month;
   }

   public void showRecord() {
      System.out.println(name + "\t" + consule + "\t" + year + "\t" + day + "\t" + month);
   }

   // Clones the GameRecord
   @Override
   public Prototype getClone() {
      return new GameRecord(name, consule, year, day, month);
   }
}

class PrototypoDemo {
   public static void main(String []args) throws IOException {

      BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
   }
}