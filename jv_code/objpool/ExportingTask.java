package objpool;

public class ExportingTask implements Runnable {
   private ObjectPool<ExportingProcess> pool;
   private int threadNo;
   public ExportingTask(ObjectPool<ExportingProcess> pool, int threadNo) {
      this.pool = pool;
      this.threadNo = threadNo;
   }
   public void run() {
      // get an object from the pool
      ExportingProcess exportingProcess = pool.borrowObject();
      System.out.println("Thread " + threadNo + ": Object wih process no."
                        + exportingProcess.getProcessNo() + " was borrowed");

      // return ExportingPocess instance back to the pool
      pool.returnObject(exportingProcess);

      System.out.println("Thread " + threadNo + ": Obejct with process no. "
                        + exportingProcess.getProcessNo() + " was returned");
   }
}
