/**
 * CS 1 22fa
 * Lab 08 OOP in Java Provided Code
 * Credit: Leo Jenkins
 *
 * Defines an StoryExample client program to run an "Adventure Story"
 * game.
 *
 * Note to students: Remember the difference between a class (constructor,
 * no main) and an executable Java program with main (see Lab 08/Lecture 24
 * materials if you still have questions about this!).
 */
import java.util.Scanner;

public class StoryExample {
    public static void main(String args[]) {
        Scanner scanner = new Scanner(System.in);
        String opening =
            "Your potions teacher, Professor Dearing, has been poisoned. Wanting to respond quickly to the crisis, the administrators at Tralemyc,\n" +
            "the foremost school for magical students, have falsely accused your friend Carynth of murder. Collect evidence to clear their name.\n";

        AdventureStory story = new AdventureStory(opening, scanner);

        String libraryText =
            "The library reported an after-hours break-in, but nothing was reported stolen. Could that be related to Professor Dearing's poisoning?\n" +
            "Explore the library to learn about the ins-and-outs of the wizarding world. Specifically, the forbidden section\n" +
            "contains knowledge of evil-doers and deadly hexes. But be careful that you don't get caught.\n";

        StorySnippet library = new StorySnippet(libraryText, "Go to the Library");
        String forbiddenSectionText =
            "You sneak into the forbidden section of the library under the cover of darkness. Using a magical orb for light, you observe\n" +
            "a book that is slightly removed from its nook on the shelf. The cover reads \"The Kabal Family, a Bloodline of Evil.\"\n" +
            "You realize that they are referring to Dark Arts Professor Kabal's family. Professor Kabal was everyone's least favorite\n" +
            "professor. Creepy, dark, and some say, evil. You flip through the book and learn about the Kabal family's history\n" +
            "of mercenary killings, blood feuds, and poisonings...\n";
        StorySnippet forbiddenSection = new StorySnippet(forbiddenSectionText, "Go to the Library: Forbidden Section");
        forbiddenSection.setItem("\"The Kabal Family, a Bloodline of Evil\"");

        library.addUndirectedEdge(forbiddenSection);


        String infirmaryText =
            "Unlike the rest of the building which had been oddly silent since the news of Professor Dearing's death, the infirmary is\n" +
            "loud from the bustling of doctors and nurses at work. Trying to stay out of their way, you steal a quick glance at the patients\n" +
            "who were in the infirmary the day of the crime. The list reads as follows:\n" +
            "    Professor Crumplebottom (love hex)\n" +
            "    Emory Jasper (self-amputation)\n" +
            "    Basil Hexweaver (tongue removal)\n";

        // Professor Crumplebottom (potion burns)
        StorySnippet infirmary = new StorySnippet(infirmaryText, "Go to the Infirmary");
        infirmary.setItem("List of infirmary patients");


        String staffRoomText =
            "You enter the staff lounge. The room is empty except for a woman crying in the corner. You recognize her as Elysabeth Darcy,\n" +
            "one of Professor Dearing's two TAs. You go to comfort her and ask what is wrong, but you already know the answer.\n" +
            "It had long been rumored that Professor Dearing was having an affair with Elysabeth. The rumors had only become louder\n" +
            "when Maxine Dearing had been seen storming out of the Professor's office after they had been heard having a verbal altercation.\n" +
            "After you comfort Elysabeth, Professor Crumplebottom enters the room with a few other professors. You overhear him say that\n" +
            "Professor Dearing was a second-rate professor who should never have been promoted over him in the Potions department.\n";
        StorySnippet staffRoom = new StorySnippet(staffRoomText, "Go to the staff room");

        String officeText =
            "Professor Dearing's office is in even more of a mess than it usually is. Maybe because of the loud fight that he had with\n" +
            "his wife. Everything was left as it was when Professor Dearing collapsed in his office except for his half eaten meatloaf,\n" +
            "which was removed by the investigators because they believed it was the source of the poison. You sort thorugh the knocked\n" +
            "over stacks of papers to find the log of people who entered the building. The list reads as follows:\n" +
            "    Green McBride\n" +
            "    Elysabeth Darcy\n" +
            "    Maxine Dearing\n" +
            "    Carynth Abbot\n" +
            "    Professor Crumplebottom\n" +
            "    Leopold Jennings\n" +
            "    Hester Johnson\n" +
            "You also see TAs Elysabeth and Leopold's desks in the corner. While Elysabeth's desk is empty, Jenning's desk is covered in\n" +
            "papers for him to grade. Ever since Professor Dearing began to court Elysabeth, Jennings has shouldered the work of two TAs.\n";
        StorySnippet office = new StorySnippet(officeText, "Go to Professor Dearing's office");
        office.setItem("Office access list");

        staffRoom.addUndirectedEdge(office);

        String classroomText =
            "Dearing's classroom is empty as all classes have been cancelled for the day. Just as you are about to leave you notice\n" +
            "a crumpled up piece of paper in the trash. You unfurl it and realize that it is one of Eliana Marigold's potions projects.\n" +
            "She had been given a failing grade, unheard of for a top student like Eliana who was always so quick to remind people that\n" +
            "she was top of the class. This could explain why Eliana had been acting so eratic recently, even getting detention from\n" +
            "Dearing the day before his death.\n";

        StorySnippet classroom = new StorySnippet(classroomText, "Go to Professor Dearing's classroom");
        classroom.setItem("Eliana Marigold's failed project");

        String storageRoomText =
            "Connected to Dearing's Classroom, potions storgage room B housed all of the most dangerous ingredients and concoctions.\n" +
            "Only Professors, TAs, and top students were allowed to even enter the room. You look at the sheet of everyone who had\n" +
            "accessed the room in the week leading up to Dearing's poisoning. The list reads as follows:\n" +
            "        Leopold Jennings,\n" +
            "        Professor Crumplebottom,\n" +
            "        Eliana Marigold,\n" +
            "        Carynth Abbot.\n" +
            "You also notice that one vial of the hemlock is missing! The missing vial could be the murder weapon!\n";

        StorySnippet storageRoom = new StorySnippet(storageRoomText, "Go to the potions storage room B");
        storageRoom.setItem("Potions storage room access list");

        classroom.addUndirectedEdge(storageRoom);

        String headmasterText =
            "Headmaster Belladona Crisp closes the book she is reading and puts it down on her desk. She asks you what brought\n" +
            "you to her office. You say that you think Carynth was falsely accused and that you know who the real murderer is.\n" +
            "Who do you accuse of Professor Dearing's murder? Be careful, a wrongful accusation will result in your expulsion from the school.\n";

        StorySnippet headmasterOffice = new StorySnippet(headmasterText, "Go to the Headmaster's Office");

        String homeRoomText =
            "The home room connects to many of the relavant sections of the school. Once you have collected your evidence," +
            "go to the Headmaster's Office to accuse one of the suspects and clear Carynth of murder.\n";

        StorySnippet homeRoom = new StorySnippet(homeRoomText, "Go to the home room");
        homeRoom.addUndirectedEdge(library);
        homeRoom.addUndirectedEdge(staffRoom);
        homeRoom.addUndirectedEdge(classroom);
        homeRoom.addUndirectedEdge(infirmary);
        homeRoom.addUndirectedEdge(headmasterOffice);


        StorySnippet suspect1 = new StorySnippet("Eliana Marigold is innocent! You are expelled from Tralemyc!\n", "Accuse Eliana Marigold");
        suspect1.endPoint = true;
        StorySnippet suspect2 = new StorySnippet("Mrs. Maxine Dearing is innocent! You are expelled from Tralemyc!\n", "Accuse Mrs. Maxine Dearing");
        suspect2.endPoint = true;
        StorySnippet suspect3 = new StorySnippet("Leopold Jennings is guilty! You saved Carynth from being imprisoned!\n", "Accuse Leopold Jennings");
        suspect3.endPoint = true;
        StorySnippet suspect4 = new StorySnippet("Professor Crumplebottom is innocent! You are expelled from Tralemyc!\n", "Accuse Professor Crumplebottom");
        suspect4.endPoint = true;
        StorySnippet suspect5 = new StorySnippet("Professor Kabal is innocent! You are expelled from Tralemyc!\n", "Accuse Professor Kabal");
        suspect5.endPoint = true;
        headmasterOffice.addNext(suspect1);
        headmasterOffice.addNext(suspect2);
        headmasterOffice.addNext(suspect3);
        headmasterOffice.addNext(suspect4);
        headmasterOffice.addNext(suspect5);

        story.getCurrent().addNext(homeRoom);

        story.displayStory(scanner);

        scanner.close();
    }
}
