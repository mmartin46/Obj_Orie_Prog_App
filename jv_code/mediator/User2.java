// Create a User2 class that will extend Participant
// abstract class and will use the ApnaChatRoom interface.
public class User2 extends Participant {

   private String name;
   private ApnaChatRoom chat;

   @Override
   public void sendMsg(String msg) {
      this.chat.showMsg(msg, this);
   }

   @Override
   public void setname(String name) {
      this.name = name;
   }

   @Override
   public String getName() {
      return name;
   }

   public User2(ApnaChatRoom chat) {
      this.chat = chat;
   }
}
