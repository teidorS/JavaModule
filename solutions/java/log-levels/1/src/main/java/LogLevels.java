public class LogLevels {
    
    public static String message(String logLine) {
        String[] logArr = logLine.split(":");
        return logArr[1].trim();
        // throw new UnsupportedOperationException("Please implement the (static) LogLevels.message() method");
    }

    public static String logLevel(String logLine) {
        String[] level = logLine.split(":");
        int lastIdx = level[0].indexOf("]");
        String levelCleaned = level[0].substring(1, lastIdx);
        return levelCleaned.toLowerCase();
        // throw new UnsupportedOperationException("Please implement the (static) LogLevels.logLevel() method");
    }

    public static String reformat(String logLine) {
        String logMessage = message(logLine);
        String level = logLevel(logLine);
        return logMessage + " (" + level + ")";
        // throw new UnsupportedOperationException("Please implement the (static) LogLevels.reformat() method");
    }
}
