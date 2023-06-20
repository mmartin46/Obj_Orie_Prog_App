


public class ChainofResponsibilityClient {
   private static Logger doChaining() {
      Logger consoleLogger = new ConsoleBasedLogger(Logger.OUTPUTINFO);

      Logger errorLogger = new ErrorBasedLogger(Logger.ERRORINFO);
      consoleLogger.setNextLevelLogger(errorLogger);
   
      Logger debugLogger = new DebugBasedLogger(Logger.DEBUGINFO);
      errorLogger.setNextLevelLogger(debugLogger);
      
      return consoleLogger;
   }
   
   public static void main(String args[]) {
      Logger chainLogger = doChaining();

      chainLogger.logMessage(Logger.OUTPUTINFO, "Enter the seqence of values ");
      chainLogger.logMessage(Logger.ERRORINFO, "An error has occured");
      chainLogger.logMessage(Logger.DEBUGINFO, "This was the error.");
   }
}
