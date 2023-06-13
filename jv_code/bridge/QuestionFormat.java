package bridge;

// Create a QuestionFormat class tha will
// extend the QuestionManager class
public class QuestionFormat extends QuestionManager {
   public QuestionFormat(String catalog) {
      super(catalog);
   }

   public void displayAll() {
      System.out.println("\n-------------------------\n");
      super.displayAll();
      System.out.println("\n-------------------------\n");
   }
}
