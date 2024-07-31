/**
 * CS 1 22fa
 * Lab 09 Java OOP (ChessMini) Provided Coordinates class 
 * (students do not modify)
 * Credit: Leo Jenkins
 * 
 * Defines a class representing (x, y) coordinates.
 */
public class Coordinates {
    // Usually, we want to encapsulate state. But (x, y) coordinates
    // are simple, and commonly accessed with x, y so this is a rare case
    // where it is ok 
    public int x;
    public int y;

    /**
     * Initializes a new Coordinates with the given (x, y) position.
     * @param x
     * @param y
     */
    public Coordinates(int x, int y) {
        this.x = x;
        this.y = y;
    }

    /**
     * Overrides the equals method to add support for comparing Coordinates
     * based on their (x, y) values (without an overridden equals, Coordinates
     * with the same points would not be considered equal).
     */
    @Override
    public boolean equals(Object o) {
        Coordinates coords = (Coordinates) o;
        return (this.x == coords.x && this.y == coords.y);
    }

    @Override
    public int hashCode() {
        int hashCode = 17;
        hashCode = 31 * hashCode + this.x;
        hashCode = 31 * hashCode + this.y;
        return hashCode;
    }
}
