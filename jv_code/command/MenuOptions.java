package command;

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
