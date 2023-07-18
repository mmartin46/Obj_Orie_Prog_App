package command;

// Create a MenuOptions class that will
// act as an invoker.
public class MenuOptions {
   private ActionListenerCommand openCommand;
   private ActionListenerCommand saveCommand;
   
   public MenuOptions(ActionListenerCommand clickOpen, ActionListenerCommand clickSave) {
      this.openCommand = clickOpen;
      this.saveCommand = clickSave;
   }

   public void clickOpen() {
      openCommand.execute();
   }

   public void clickSave() {
      saveCommand.execute();
   }
}

