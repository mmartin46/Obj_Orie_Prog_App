package objpool;
import java.util.concurrent.ConcurrentLinkedQueue;
import java.util.concurrent.Executors;
import java.util.concurrent.ScheduledExecutorService;
import java.util.concurrent.TimeUnit;

// Create an ObjectPool class thst is used to
// create the number of objects.
public abstract class ObjectPool<T> {
   /*
    * ConcurrentLinkedQueue is a thread
    * safe queue based on linked nodes.
    * Because the queue follows FIFO technique.
   */
   private ConcurrentLinkedQueue<T> pool;

   /*
    * ScheduledExecutorService starts a special task
    * in a sperate thread and observes the minimum and maximum
    * number of objects in the pool periodically in a specified
    * time (using parameter validationInterval)
    *
    * When the number of objects is less than the minimum, missing 
    * instances will be created. If the number is greater than the maximum
    * too many instances will be removed.
   */
   private ScheduledExecutorService executorService;
   /*
    * Creates the pool.
    * @param minObjects : the minimum number of objects
    * residing in the pool.
    */
   public ObjectPool(final int minObjects) {
      // intialize pool
      initialize(minObjects);
   }


   /*
    * Creates the pool.
    * @param minObjects : minimum number of objects residing in the pool.
    * @param maxObjects : maximum number of objects residing in the pool.
    * @param validationInterval : time in seconds for periodical checking of
    *                             minObjects / maxObjects conditions in a seperate
    *                             thread.
    * When the number of objects is less than minObjects, missing instances will be created.
    * WHen the number of objects is greater than maxObjecs, too many instances will be removed.
    */
   public ObjectPool(final int minObjects, final int maxObjects, final long validationInterval) {
      // initialize pool
      initialize(minObjects);
      // check pool conditions in a seperate threads
      executorService = Executors.newSingleThreadScheduledExecutor();
      executorService.scheduleWithFixedDelay(new Runnable() // annoymous class
      {
         @Override
         public void run() {
            int size = pool.size();

            if (size < minObjects) {
               int sizeToBeAdded = minObjects + size;
               for (int i = 0; i < sizeToBeAdded; i++) {
                  pool.add(createObject());
               }
            } else if (size > maxObjects) {
               int sizeToBeRemoved = size - maxObjects;
               for (int i = 0; i < sizeToBeRemoved; i++) {
                  pool.poll();
               }
            }
         }  
      }, validationInterval, validationInterval, TimeUnit.SECONDS);
   }


   /*
    * Gets the next free object from the pool. If the pool doesn't
    * contain any objects, a new object will be created and given to the
    * caller of this method back.
    *
    * @return T borrowed object.
    */
   public T borrowObject() {
      T object;
      if ((object = pool.poll()) == null)
      {
         object = createObject();
      }
      return object;
   }

   /*
    * Returns object back to the pool.
    * @param object object to be returned
   */
   public void returnObject(T object) {
      if (object == null) {
         return;
      }
      this.pool.offer(object);
   }

   /*
    * Shutdown this pool.
   */
   public void shutdown() {
      if (executorService != null) {
         executorService.shutdown();
      }
   }

   /*
    * Creates a new object.
    @return T new object
   */
   protected abstract T createObject();

   private void initialize(final int minObjects) {
      pool = new ConcurrentLinkedQueue<T>();
      for (int i = 0; i < minObjects; i++) {
         pool.add(createObject());
      }
   }
}