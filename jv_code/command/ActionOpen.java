package command;

// Create a ActionOpen class that will act as
// an ConcreteCommand
public class ActionOpen implements ActionListenerCommand {
   private Document doc;
   public ActionOpen(Document doc) {
      this.doc = doc;
   }

   @Override
   public void execute() {
      doc.open();
   }
}
