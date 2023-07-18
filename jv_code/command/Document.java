package command;


// Create a Document class that will act as
// a Receiver.
public class Document {
   public void open() {
      System.out.println("Document Opened");
   }

   public void save() {
      System.out.println("Document Saved");
   }
}
