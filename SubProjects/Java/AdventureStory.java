/**
 * CS 1 22fa
 * Lab 08 OOP in Java Starter Code
 * Credit: Leo Jenkins
 * 
 * Defines an AdventoryStory class managing a current story and player.
 */

// Scanner is used to "scan" through a file in Java
import java.util.Scanner;

public class AdventureStory {
    // Class fields
    // current story snippet
    private StorySnippet current;
    // player
    private Player player;

    /**
     * AdventureStory constructor, initializing the story and player.
     * @param opening - the first message to the player
     * @param scanner - scanner object with access to user input
     */
    public AdventureStory(String opening, Scanner scanner) {
        // Initialize the fields
        this.current = new StorySnippet(opening, "Start");
        this.setPlayer(scanner);
    }

    /**
     * Prompts a user for player information to set up a new player
     * @param scanner - scanner object with access to user input
     */
    public void setPlayer(Scanner scanner) {
        System.out.println();
        System.out.println("Welcome! What is your name?");

        // Get the name the user inputs
        // Here, scanner.nextLine() is analogous to input() in Python
        String name = scanner.nextLine();

        // Initialize the player with the name the user inputs
        this.player = new Player(name);
    }

    /**
     * Returns the current StorySnippet.
     * @return the current StorySnippet
     */
    public StorySnippet getCurrent() {
        return this.current;
    }

    /**
     * Returns the current Player.
     * @return the current Player
     */
    public Player getPlayer() {
        return this.player;
    }

    /**
     * Displays the story using the title, text, and player inventory.
     */
    public void displayStory(Scanner scanner) {
        // Note to students: We do not go into data structures like Lists
        // in CS1, and you don't need to worry about this code (but are 
        // welcome to ask about it if you're curious!). As a reminder,
        // you should not be using any Lists in MP7 (ask if you 
        // know what Lists are in Java, but are unsure about the trade-offs)
        while (true) {
            // If the current snippet has an item and the player does not 
            // already hold it
            if (this.current.getItem() != null && 
                !(this.player.getInventory().contains(this.current.getItem()))) {
                // Add current item to the player's inventory
                this.player.addToInventory(this.current.getItem());
            }

            // Display the snippet
            this.current.displaySnippet();
            // Display the inventory
            this.player.displayInventory();

            // If the current snippet is the end, stop
            if (this.current.endPoint) {
                break;
            }

            System.out.println();
            System.out.println("Type the number corresponding to the " +
                               "location you want to go to.");
            // Get next user input
            String answer = scanner.nextLine();
            try {
                // Get player input
                int index = Integer.parseInt(answer);
                // Change the current story snippet
                this.current = this.current.getNext().get(index);
            } catch (NumberFormatException e) {
                System.out.println("Invalid input; must be a number.");
            } catch (Exception e) {
                // If the player input does not work
                System.out.println("Some other error occurred.");
            }
        }
    }
}
