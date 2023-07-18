import java.text.DateFormat;
import java.text.SimpleDateFormat;
import java.util.Date;

// Create a ApnaChatRoomlmpl class that will implement ApnaChatRoom
// interface and will also use the # of participants involved in chatting
// through Participant interface.
public class ApnaChatRoomlmpl implements ApnaChatRoom {
   DateFormat dateFormat = new SimpleDateFormat("E dd-MM-yyyy hh:mm a");
   Date date = new Date();
   @Override
   public void showMsg(String msg, Participant p) {
      System.out.println(p.getName() + " gets message: " + msg);
      System.out.println("\t\t\t\t" + "[" + dateFormat.format(date).toString() + "]");
   }
}

