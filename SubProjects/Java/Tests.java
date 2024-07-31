/**
 * CS 1 22fa
 * Lab 08 OOP in Java Provided Tests
 * Credit: Leo Jenkins
 * 
 * A simple testing program for Lab 08 exercises.
 */
public class Tests {
    public static void main(String args[]) {
        Player testPlayer = new Player("Name");

        // test_player_init_name (constructor)
        if (testPlayer.getName() == "Name") {
            System.out.println("PASSED | test_player_init_name");
        }
        else {
            System.out.println("FAILED | test_player_init_name");
        }

        // test_player_init_health (constructor)
        if (testPlayer.getHealth() == 100.0) {
            System.out.println("PASSED | test_player_init_health");
        }
        else {
            System.out.println("FAILED | test_player_init_health");
        }

        // test_plyaer_init_strength (constructor)
        if (testPlayer.getStrength() == 10.0) {
            System.out.println("PASSED | test_player_init_strength");
        }
        else {
            System.out.println("FAILED | test_player_init_strength");
        }

        // test_player_init_level (constructor)
        if (testPlayer.getLevel() == 1) {
            System.out.println("PASSED | test_player_init_level");
        }
        else {
            System.out.println("FAILED | test_player_init_level");
        }

        // test_player_init_inventory (constructor)
        if (testPlayer.getInventory().isEmpty()) {
            System.out.println("PASSED | test_player_init_inventory");
        }
        else {
            System.out.println("FAILED | test_player_init_inventory");
        }

        // test_player_take_damage_and_not_alive
        testPlayer.takeDamage(100.0);

        if (!testPlayer.isAlive()) {
            System.out.println("PASSED | test_player_take_damage_and_not_alive");
        }
        else {
            System.out.println("FAILED | test_player_take_damage_and_not_alive");
        }
    }
}
