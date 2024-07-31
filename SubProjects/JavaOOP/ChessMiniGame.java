/**
 * CS 1 22fa
 * Lab 09 Java OOP (ChessMini) Starter Code
 * Credit: Leo Jenkins
 * 
 * Defines a ChessMiniGame program to represent an 8x8 chess board with a
 * single "Knight" piece the player will try to move in a series of steps
 * to reach a target position (randomly-initialized).
 */
import java.util.List;
import java.util.Scanner;
import java.util.Random;
import java.util.Queue;
import java.util.LinkedList;
import java.util.Map;
import java.util.HashMap;


class ChessMiniGame {
    // Class constants
    // static final fields (same for every instance and cannot be changed)
    private static final int BOARD_LENGTH = 8;
    private static final double OBSTACLE_FREQUENCY = 0.50;

    // Non-static class fields (remember non-static fields are reserved
    // for state unique to a specific ChessMiniGame instance)
    private Piece[][] board;
    private int moves;
    private int currMoves;

    // Coordinates have fields x, y
    private Coordinates endPoint;

    /**
     * ChessMiniGame constructor. Initializes a random 8x8 chess board, with
     * a current move count starting at 0, and a random target position
     * a player will try to reach via a series of moves for their single
     * Knight piece.
     */
    public ChessMiniGame() {
        // New random object
        Random rand = new Random();

        // initialize fields
        // Array of Pieces
        this.board = new Piece[BOARD_LENGTH][BOARD_LENGTH];
        this.currMoves = 0;
        // Randomly select endPoint
        // rand.nextInt(b) returns a random integer in [0, b)
        this.endPoint = new Coordinates(rand.nextInt(BOARD_LENGTH), rand.nextInt(BOARD_LENGTH));
    }

    /**
     * Populates the board with obstacles at a rate of obstacleFrequency.
     * 
     * @param obstacleFrequency (double) the percentage of obstacles
     */
    private void fillOutBoard(double obstacleFrequency) {
        // New random object
        Random rand = new Random();

        // Loop through every square in the board
        for (int i = 0; i < this.board.length; i ++) {
            for (int j = 0; j < this.board[0].length; j++) {
                // Add a coordinate at a rate of obstacleFrequency
                if (rand.nextDouble() <= obstacleFrequency) {
                    // endPoint needs to be a free block
                    if (i != endPoint.x || j != endPoint.y) {
                        // New Coordinates object (see Coordinates constructor
                        // arguments in the provided Coordinates.java)
                        Coordinates coords = new Coordinates(i, j);
                        // Add new Obstacle object to board
                        this.board[i][j] = new Obstacle(coords, this.board);
                    }
                }
            }
        }
    }

    /**
     * Starts the mini game. 
     * 
     * @param startPoint (x, y) Coordinates where the player starts
     */
    public void playMiniGame(Coordinates startPoint) {
        // New Scanner object to receive user input
        Scanner scanner = new Scanner(System.in);

        // Player's initial coordinates
        Piece piece = this.board[startPoint.x][startPoint.y];
        piece.setLocation(startPoint);

        // Play until the user reaches the endPoint
        while (!(piece.getLocation().equals(this.endPoint))) {
            // Display the board
            this.displayBoard();
            // Get user move
            Coordinates newLocation = getNextUserMove("Input next move y:x", 
                                                      piece, scanner);
            // Increment number of player moves by 1
            this.currMoves ++;
            // Move the piece to the new location
            piece.makeMove(newLocation);
        }
        // Output the final score at the end of the game
        System.out.print("Final score: ");
        System.out.print(this.currMoves);
        System.out.print(" / ");
        System.out.println(this.moves);
        // Close the scanner object
        scanner.close();
    }

    /**
     * Find the number of moves it takes to reach the endPoint
     * (using Breadth-First search). (Provided, students shouldn't modify
     * this method).
     * 
     * @param endPoint (Coordinates) target square
     * @param piece (Piece) player's Piece
     * @return (Map<Coordinates, Integer>) number of moves to reach each square
     */
    private Map<Coordinates, Integer> findNumMoves(Coordinates endPoint, 
                                                   Piece piece) {
        // Queue of non-visited coordinates
        Queue<Coordinates> queue = new LinkedList<>();
        // Map from Coordinates to number of steps (to travel to the 
        // Coordinates from the endPoint)
        Map<Coordinates, Integer> steps = new HashMap<>();
        // Start at the endPoint
        queue.add(endPoint);
        // Takes zero steps to get to the endpoint from the endpoint
        steps.put(endPoint, 0);

        // Loop until we have visited every square
        while (!(queue.isEmpty())) {
            // Current square
            Coordinates curr = queue.remove();
            // Number of steps to get to the current square (from the endPoint)
            int currSteps = steps.get(curr);

            // Move the piece to the current location
            piece.setLocation(curr);
            // All of the squares reachable by the piece in one move
            List<Coordinates> neighbors = piece.validMoves();

            // Loop through the reachable neighbors
            for (Coordinates currNeighbor: neighbors) {
                // If we have seen the piece before, then the current number 
                // of steps will be worse
                if (!(steps.containsKey(currNeighbor))) {
                    // Add the neighbor to the queue of non-visited squares
                    queue.add(currNeighbor);
                    // Takes one additional step to reach currNeighbor
                    steps.put(currNeighbor, currSteps + 1);
                }
            } 
        }
        return steps;
    }

    /**
     * Ask user for next move until they make a valid move, returning the
     * corresponding (x, y) Coordinates.
     * 
     * @param prompt (String) Prompting message for user
     * @param piece (Piece) player's piece
     * @param scanner (Scanner) scanner with user input
     * @return
     */
    private Coordinates getNextUserMove(String prompt, Piece piece, 
                                        Scanner scanner) {
        // Dummy new location
        Coordinates newLocation = new Coordinates(-1, -1);
        // Error message depends on counter
        int counter = 0;

        do {
            // The location is not reachable
            if (counter > 0) {
                System.out.println("That is not a valid move!");
            }
            System.out.println(prompt);
            // Receive user input
            String answer = scanner.nextLine();
            try {
                // Extract x,y from user input
                String[] answers = answer.split(":", 2);
                newLocation.x = Integer.parseInt(String.valueOf(answers[0]));
                newLocation.y = Integer.parseInt(String.valueOf(answers[1]));
            } catch(Exception e) {
                // Error message if user input is not in the expected form
                System.out.println("Next move should be in the form y:x");
                counter = -1;
            }
            counter++;
        }
        // loop until the player's move is a valid move
        while (!(piece.validMoves().contains(newLocation)));

        return newLocation;
    }

    /**
     * Display the board including the player's piece, the obstacles,
     * and the endPoint. A board is displayed as an 8x8 board to the
     * terminal.
     */
    public void displayBoard() {
        System.out.println();
        System.out.print("    ");
        // Print the coordinates
        for (int i = 0; i < 8; i++) {
            System.out.print(i);
            System.out.print("   ");
        }
        System.out.println();

        // Print the rows
        for (int i = 0; i < BOARD_LENGTH; i++) {
            System.out.println("  +---+---+---+---+---+---+---+---+");
            System.out.print(i);
            System.out.print(" ");
            for (int j = 0; j < BOARD_LENGTH; j++) {
                // X marks the spot
                if (i == this.endPoint.x && j == this.endPoint.y) {
                    System.out.print("| X ");
                } else if (this.board[i][j] == null) { // Empty square
                    System.out.print("|   ");
                } else { // Occupied square
                    System.out.print("| " + this.board[i][j].letter + " ");
                }
            }
            System.out.println("|");
        }

        System.out.println("  +---+---+---+---+---+---+---+---+");
        // Print the number of moves
        System.out.print("Current number of moves: ");
        System.out.println(this.currMoves);
        System.out.print("Fewest possible moves: ");
        System.out.println(this.moves);
    }

    /**
     * Main function for the ChessMiniGame class
     * 
     * @param args (no arguments)
     */
    public static void main(String args[]) {
        // Initialize a new ChessMiniGame object
        ChessMiniGame game = new ChessMiniGame();
        // Create player's piece
        Piece piece = new Knight(game.board);

        // Map from coordinates to the number of steps it takes to travel 
        // from endPoint to Coordinates
        Map<Coordinates, Integer> steps = new HashMap<>();

        // If steps only has one key, then the startPoint is the endPoint
        while (steps.size() <= 1) {
            // Fill out the board with obstacles
            game.fillOutBoard(OBSTACLE_FREQUENCY);
            // Fill out steps
            steps = game.findNumMoves(game.endPoint, piece);
        }
        
        int maximum = 0;
        Coordinates maxCoords = null;

        // Find the farthest square from the endPoint
        for (Coordinates coords: steps.keySet()) {
            if (steps.get(coords) > maximum) {
                maximum = steps.get(coords);
                maxCoords = coords;
            }
        }

        // Update fields
        Coordinates startCoords = maxCoords;
        game.moves = maximum;
        piece.setLocation(startCoords);
        game.board[startCoords.x][startCoords.y] = piece;

        // Play miniGame
        game.playMiniGame(startCoords);
    }
}