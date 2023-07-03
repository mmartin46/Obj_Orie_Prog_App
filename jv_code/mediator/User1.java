/*
 * Create a User1 class that will extend Participant abstract class
 * and will use the ApnaChatRoom interface.
 */
public class User1 extends Participant {
   
   private String name;
   private ApnaChatRoom chat;

   @Override
   public void sendMsg(String msg) {
      chat.showMsg(msg, this);
   }

   @Override
   public void setname(String name) {
      this.name = name;
   }

   @Override
   public String getName() {
      return name;
   }

   public User1(ApnaChatRoom chat) {
      this.chat = chat;
   }
}

