/**
 * CS 1 22fa
 * Lab 08 OOP in Java Provided Code
 * Credit: Leo Jenkins
 * 
 * Defines an StorySnipper class to represent a story snipper in an 
 * "Adventure Story" game.
 */
import java.util.List;
import java.util.ArrayList;

public class StorySnippet {
    // Class fields
    private String title;
    private String text;
    private String item;
    // List of next snippets
    private List<StorySnippet> next;
    // If the snippet is the end of the story
    public Boolean endPoint;

    /**
     * StorySnippet constructor
     * @param text the text displayed
     * @param title the title of the snippet
     */
    public StorySnippet(String text, String title) {
        // Initialize fields
        this.title = title;
        this.text = text;
        // List of possible next StorySnippets
        this.next = new ArrayList<>();
        this.endPoint = false;
    }

    public String getTitle() {
        return this.title;
    }

    public void setTitle(String title) {
        this.title = title;
    }

    public String getText() {
        return this.text;
    }

    public void setText(String text) {
        this.text = text;
    }

    public String getItem() {
        return this.item;
    }

    public void setItem(String item) {
        this.item = item;
    }

    public List<StorySnippet> getNext() {
        return this.next;
    }

    public void addNext(StorySnippet snippet) {
        this.next.add(snippet);
    }

    /**
     * Add edges from this to snippet and snippet to this
     * @param snippet the other snippet
     */
    public void addUndirectedEdge(StorySnippet snippet) {
        this.addNext(snippet);
        snippet.addNext(this);
    }

    /**
     * Display the StorySnippet text, title, and next options.
     */
    public void displaySnippet() {
        System.out.println();
        System.out.println();
        System.out.println(this.text);

        if (this.next.size() != 0) {
            // Loop through the possible next snippets
            for (int i = 0; i < this.next.size(); i++) {
                // Format: i: title
                System.out.println(Integer.toString(i) + ": " + 
                                   this.next.get(i).getTitle());
            }
            System.out.println();
        }
    }
}
