public class ObserverPattern {

   public static void main(String[] args) {
      // Subject
      MyTopic topic = new MyTopic();

      // Observers
      Observer obj1 = new MyTopicSubscriber("Obj1");
      Observer obj2 = new MyTopicSubscriber("Obj2");
      Observer obj3 = new MyTopicSubscriber("Obj3");

      // Register Observers to the Subject
      topic.register(obj1);      
      topic.register(obj2);   
      topic.register(obj3);
      
      // Attack Observer o the Subject
      obj1.setSubject(topic);
      obj2.setSubject(topic);
      obj3.setSubject(topic);   

      // Check for any update
      obj1.update();

      // Send message
      topic.postMessage("New Message");
   }
   
}

