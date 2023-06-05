import java.io.BufferedReader;
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
   private String consule;
   private int year;


   public GameRecord() {
      System.out.println("  Records of Games  ");
      System.out.println("---------------------------------");
      System.out.println("Name" + "\t" + "Consule" + "\t" + "Year");
   }

   public GameRecord(String name, String consule, int year) {
      this.name = name;
      this.consule = consule;
      this.year = year;
   }

   public void showRecord() {
      System.out.println(name + "\t" + consule + "\t" + year);
   }

   // Clones the GameRecord
   @Override
   public Prototype getClone() {
      return new GameRecord(name, consule, year);
   }
}




class PrototypoDemo {
   public static void main(String []args) throws IOException {

      BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
      System.out.println("Game Name: ");
      String n = br.readLine();
      System.out.print("\n");

      System.out.println("Game Consule: ");
      String c = br.readLine();
      System.out.print("\n");

      System.out.println("Game Year: ");
      int y = Integer.parseInt(br.readLine());
      System.out.print("\n");

      GameRecord game1 = new GameRecord(n, c, y);
      game1.showRecord();
      System.out.print("\n\n");
      
      GameRecord game2 = (GameRecord) game1.getClone();
      game2.showRecord();
   }
}