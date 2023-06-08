package objpool;

import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.TimeUnit;
import java.util.concurrent.atomic.AtomicLong;

public class ObjectPoolDemo {
   private ObjectPool<ExportingProcess> pool;
   private AtomicLong processNO = new AtomicLong(0);
   public void setUp() {
      
   }
}
