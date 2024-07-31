/**
 * CS 1 22fa
 * Lab 08 OOP in Java Starter Code
 * Credit: Leo Jenkins
 * 
 * Defines a Player class with health, level, and other stats, offering
 * abilities to get the player's data, update their stats/level, and
 * manage an item inventory.
 */
// Imports for Lists in Java, which students shouldn't need to worry about
// (you should not use lists in MP7!)
import java.util.List;
import java.util.ArrayList;

public class Player {
    // Class fields (all private)
    // Initial conditions
    // static fields are the same for every instance of the class
    // these are analogous to Python's class constants
    private static double INIT_HEALTH = 100;
    private static double INIT_STRENGTH = 10;
    private static int INIT_LEVEL = 1;

    // Non-static fields: Unique to the state of specific instances
    private String name;
    private double health;
    private double strength;
    private int level;

    // Inventory is a list of strings
    private List<String> inventory;

    /**
    * Player constructor, initializing the state of a player with a provided
    * name and with initial health and strength stats and an starting level 
    * of 1. A new Player also has an empty inventory of items starting out. 
    *
    * @param name (String) the name of the player
    */
    public Player(String name) {
        // Initialize the fields
        this.name = name;
        this.health = INIT_HEALTH;
        this.strength = INIT_STRENGTH;
        this.level = INIT_LEVEL;
        this.inventory = new ArrayList<>();
    }

    // Getters and setters
    /**
     * Returns the name of the player.
     * @return name of the player
     */
    public String getName() {
        return this.name;
    }

    /**
     * Returns the current health of the player.
     * @return the current health of the player
     */
    public double getHealth() {
        return this.health;
    }

    /**
     * Updates the current health of the player given a new health value.
     * @param health - new health value
     */
    public void setHealth(double health) {
        this.health = health;
    }

    /**
     * Decreases the player's health by damage amount
     * @param damage - damage to take
     */
    public void takeDamage(double damage) {
        // Optional improvement: don't allow health to go below 0
        // (hint: use if/else in Java!)
        this.setHealth(this.health - damage);
    }
    javac AdventureStory.java Player.java StoryExample.java StorySnippet.java Tests.java
    /**
     * Returns the current strength stat of the player.
     * @return - current strength stat of the player
     */
    public double getStrength() {
        return this.strength;
    }

    /**
     * Updates the strength of the player, replacing their current stat.
     * @param strength - new strength stat of the player
     */
    public double setStrength(double strength) {
        this.strength = strength;
    }

    /**
     * Returns the player's current level.
     * @return the player's current level
     */
    public int getLevel() {
        return this.level;
    }

    /**
     * Sets the player's level, replacing their current level.
     * @param level - new level for player
     */
    public void setLevel(int level) {
        this.level = level;
    }

    /**
     * Levels up the player, increasing their level by 1.
     */
    public void incrementLevel() {
        this.setLevel(this.level + 1);
    }

    /**
     * Returns true iff the player is "alive" (their health is > 0)
     * @return true if the player is alive, else false
     */
    public boolean isAlive() {
        return this.health > 0;
    }

    /**
     * Returns a list of the player's current inventory.
     * @return list of the player's current inventory
     */
    public List<String> getInventory() {
        return this.inventory;
    }

    /**
     * Adds an item to the player's current inventory.
     * @param item - item to add to the player's inventory
     */
    public void addToInventory(String item) {
        this.inventory.add(item);
    }

    /**
     * Prints out the player's current inventory in the form:
     * Inventory [<items>]
     * where each item is comma-separated.
     */
    public void displayInventory() {
        String inventoryString = "Inventory: [";
        // Don't print anything if the inventory is empty
        if (this.inventory.size() == 0) {
            inventoryString += "]";
            System.out.println(inventoryString);
            return;
        }

        // Print the items in the inventory
        for (String item: this.inventory) {
            inventoryString += item + ", ";
        }
        // Remove any trailing ", "
        inventoryString = inventoryString.substring(0, inventoryString.length() - 2);
        inventoryString += "]";
        System.out.println(inventoryString);  
    }
}
