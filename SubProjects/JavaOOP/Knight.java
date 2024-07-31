/**
 * CS 1 22fa
 * Lab 09 Java OOP (ChessMini) Provided Knight Piece class 
 * (students do not modify)
 * Credit: Leo Jenkins
 * 
 * Defines a class representing (x, y) coordinates.
 */
import java.util.ArrayList;

// Students aren't expected to use inheritance in Java, but this is the
// analog to class Knight(Piece): in Python
public class Knight extends Piece {

    /**
     * Initializes a new Knight piece associated with a given board of chess
     * Pieces.
     * @param board
     */
    public Knight(Piece[][] board) {
        this.letter = "N";
        this.board = board;
    }

    @Override
    public ArrayList<Coordinates> validMoves() {
        ArrayList<Coordinates> moves = new ArrayList<>();
        int x = this.location.x;
        int y = this.location.y;

        // Fancy logic to determine what moves are possible for a Knight,
        // which can move in any "L-shaped" direction (e.g. 3 tiles to the
        // right and 1 tile up).  
        for (int i = -2; i < 6; i += 4) {
            for (int j = -1; j < 3; j += 2) {
                // Make sure we only consider moves that are within the
                // board's dimensions
                if (0 <= x + i && x + i < this.board.length && 
                    0 <= y + j && y + j < this.board.length) {
                    Piece square1 = this.board[x + i][y + j];
                    // We can only consider Pieces that are not Obstacles
                    if (!(square1 instanceof Obstacle)) {
                        // Add the possible position to the list of
                        // move candidates
                        Coordinates coords = new Coordinates(x + i, y+ j);
                        moves.add(coords);
                    }
                }
                
                // Next, consider other orientation
                if (0 <= x + j && x + j < this.board.length && 
                    0 <= y + i && y + i < this.board.length) {
                    Piece square2 = this.board[x + j][y + i];
                    if (!(square2 instanceof Obstacle)) {
                        Coordinates coords = new Coordinates(x + j, y + i);
                        moves.add(coords);
                    }
                }
            }
        }
        return moves;
    }
}
