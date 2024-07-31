/**
 * CS 1 22fa Final Exam Part B
 * Student Name: Nyasha Makaya
 * 
 * For full credit:
 * - implement the toSnakeCase function as described in the spec and below
 *   B.1 requirements
 * - Write a valid Javadoc comment for your function
 * - Do not modify any provided code
 * - Your program is required to compile when ran with javac PartB.java
 * - Your program should output the PASSED message after the main function
 *   tests your solution when called with java PartB in the terminal
 * - You may not use arrays, lists, regex, etc.
 * - You may include // comments _within_ your function to describe your logic
 */
public class PartB {
    
    /**
     * Main function of PartB.java, testing an implemented toSnakeCase
     * function for Part B.1 of the Final Exam.
     * 
     * DO NOT MODIFY.\
     */
    public static void main(String[] args) {
        String s = toSnakeCase("snek_case");
        int failedCount = assertEquals("snek_case", s);
        int testCount = 7;
        s = toSnakeCase("snakeCase");
        failedCount += assertEquals("snake_case", s);
        s = toSnakeCase("camelCase");
        failedCount += assertEquals("camel_case", s);
        s = toSnakeCase("PascalCase");
        failedCount += assertEquals("pascal_case", s);
        s = toSnakeCase("removeAll3");
        failedCount += assertEquals("remove_all3", s);
        s = toSnakeCase("cAtTeRpIlLaRcAse");
        failedCount += assertEquals("c_at_te_rp_il_la_rc_ase", s);
        s = toSnakeCase("");
        failedCount += assertEquals("", s);

        if (failedCount == 0) {
            System.out.println("[PASSED] All B.1. toSnakeCase tests pass.");
        } else {
            System.out.println("[FAILED] " + failedCount + "/" + testCount + 
                               " B.1 toSnakeCase tests failed.");
        }
    }

    /**
     * A helper function to compare an expected String value with an actual
     * String value. Returns 1 if the assertion failed, otherwise 0.
     * @param expected - Expected String value
     * @param actual - Actual String value
     * @return - 1 if assertion failed (representing 1 failed test, otherwise 0)
     * 
     * DO NOT MODIFY.
     */
    public static int assertEquals(String expected, String actual) {
        int failedCount = 0;
        if (!expected.equals(actual)) {
            failedCount++;
        }
        return failedCount;
    }

    /**
    * This function takes a string as an argument and converts it to snake case.
    * @param string - the original string
    * @return - the original string converted to snake case
    *
    */
    public static String toSnakeCase(String string){
        String newString = "";
        for (int i = 0; i < string.length(); i ++){
            if (Character.isUpperCase(string.charAt(i))){
                if (i == 0){
                    newString = newString + Character.toLowerCase(string.charAt(i));   
                }
                else{
                    newString = newString + '_' + Character.toLowerCase(string.charAt(i));
                }
            }
            else{
                newString += string.charAt(i);
            }
        }
        return newString;
    }
}
