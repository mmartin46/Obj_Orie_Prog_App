
package command;


// Create a ActionSave class that will act as a ConcreteCommand.
public class ActionSave implements ActionListenerCommand {
   private Document doc;
   public ActionSave(Document doc) {
      this.doc = doc;
   }

   @Override
   public void execute() {
      doc.save();
   }
}