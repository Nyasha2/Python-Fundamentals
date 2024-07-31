/**
 * CS 1 22fa
 * Lab 09 Java OOP (ChessMini) Provided Piece class (in Lab 09, this is
 * defined as a superclass which Knight and Obstacle inherit from, similar
 * to the TA class inheriting from Student that was covered in Week 8 Lecture).
 * (students do not modify)
 * Credit: Leo Jenkins
 * 
 * Defines a class representing a chess Piece, which has a string
 * representation, an (x, y) coordinate location, and is associated with
 * a 2D board of Pieces.
 */
import java.util.ArrayList;

public class Piece {
    protected String letter;
    protected Coordinates location;
    protected Piece[][] board;

    /**
     * Apply a given move, moving this Piece to the passed (x, y) location.
     * Does nothing if the passed location is not a valid move for this Piece.
     * @param newLocation - new location to move this Piece.
     */
    public void makeMove(Coordinates newLocation) {
        if (this.validMoves().contains(newLocation)) {
            this.board[this.location.x][this.location.y] = null;
            this.board[newLocation.x][newLocation.y] = this;
            this.location = newLocation;
        }
    }

    /**
     * Returns a list of valid move coordinates.
     * @return list of valid moves coordinates.
     */
    public ArrayList<Coordinates> validMoves() {
        return this.validMoves();
    }

    /**
     * Returns the current (x, y) coordinate location of this Piece.
     * @return current location of this Piece.
     */
    public Coordinates getLocation() {
        return this.location;
    }

    /**
     * Updates the current location for this piece.
     * @param location new location to assign this piece.
     */
    public void setLocation(Coordinates location) {
        this.location = location;
    }
}
