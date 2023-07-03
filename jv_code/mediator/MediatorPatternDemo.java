public class MediatorPatternDemo {
   public static void main(String args[])
   {
      ApnaChatRoom chat = new ApnaChatRoomlml();
      User1 u1 = new User1(chat);
      u1.setname("John");
      u1.sendMsg("Hey John!");

      User2 u2 = new User2(chat);
      u2.sendMsg("Parker");
      u2.sendMsg("How are you?");
   }  
}
