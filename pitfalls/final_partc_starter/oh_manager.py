"""
CS 1 22fa Final Exam
Part C: OH Queue Manager
Student Name: Nyasha

Part C.1 Exercises (Entry and OHManager Classes)

This program defines an Entry class and an OHManager class, providing
functionality to manage an Office Hour queue with entries submitted by
Students and resolved by TAs.
"""

from student_classes import Student, TA
# Use the time module for real-time timestamps when processing OH question
# entries
from time import localtime, time


class Entry:
    """
    Represents an OH Queue Entry, managing information for a single OH
    Queue entry with the following:

    Attributes:
        - student (Student): Student instance corresponding to the student
        - question (str): The student's submitted question
        - assignment (str): the name of the assignment, such as 'MP8'
        - entry_time (str): Time of entry in "HH:MM" format (24-hour notation)
        - response_ta (TA): TA assigned to the queue Entry, or None if none
                            yet assigned (-1 if currently unresolved)
        - response_time (int): # of minutes it took to respond

    Note that our Entry is a simplification, and does not account for
    different dates, only times. As such, we choose to represent response_time
    as # of minutes elapsed as opposed to a string timestamp, since some
    ambitious staff members may help students past 00:00 midnight. Room
    for improvement!
    """

    def __init__(self, question, student, assignment, entry_time):
        """
        Constructs a new Entry with provided arguments, initializing
        a response_TA to None and response_time to -1 (representing an
        active/unresolved entry).

        Arguments:
            - question (str): Question submitted by student
            - student (Student): Student associated with new Entry
            - assignment (str): Name of assignment (e.g. 'MP8')
            - entry_time (str): time of creation in form HH:MM
        """
        self.question = question
        self.student = student
        self.assignment = assignment
        self.entry_time = entry_time
        self.response_ta = None
        self.response_time = -1

    def get_question(self):
        """
        Returns the question asked by the Student.

        Returns:
            - (str): the student's question
        """
        return self.question

    def get_student(self):
        """
        Returns the entry's corresponding Student. Note to clients: the
        Student is returned as-is instead of as a copy, so care should be
        taken to avoid mutating the returned Student. Otherwise, the client
        is on their own with resulting side-effects (room for improvement!).

        Returns:
            - (Student): Student that this Entry is assigned to.
        """
        return self.student

    def get_response_ta(self):
        """
        Returns the TA that responded to the entry. If the entry is
        unresolved, returns None. Note that the TA object is returned as-is,
        so a client should take care not to modify it with unexpected
        side-effects.

        Returns:
            - (TA): TA who responded to this Entry, or None if none.
        """
        return self.response_ta

    def get_assignment(self):
        """
        Returns the name of the assignment (e.g. 'MP8') associated with the
        Entry question.

        Returns:
            - (str): the assignment name
        """
        return self.assignment

    def get_response_time(self):
        """
        Returns the number of minutes that it took for a TA to respond (-1 if
        no response time has been set, such as for an unresolved/active Entry).

        Returns:
            - (int): Number of minutes to respond, or -1 if none yet set.
        """
        return self.response_time

    def __str__(self):
        """
        Returns the string representation of the entry, in the form:
        'Name: <name>
        UID: <uid>
        Email: <email>
        Year: <year>
        Question for <assignment>: <question>'
        where each line is separated with the \n character (no trailing \n).

        Returns:
            - (str): string representation of the Entry
        """
        entry = self.get_student().__str__() + "\n" + \
            f'Question for {self.get_assignment()}: {self.get_question()}'
        return entry

    # Given
    def resolve_entry(self, ta):
        """
        Resolves an Entry given a TA, setting the response TA and the
        response and resolution times based on the current time.

        Arguments:
            - ta (TA): the TA resolving the entry

        Returns:
            - None
        """
        completion_time = localtime(time())
        completion_hour = completion_time.tm_hour
        completion_min = completion_time.tm_min
        # Parse out the hours and minutes for our simplified 'HH:MM'
        # representation
        (entry_hour, entry_min) = tuple(self.entry_time.split(':'))
        (total_hours, total_min) = (completion_hour - int(entry_hour),
                                    completion_min - int(entry_min))
        # Converts to minutes
        self.response_time = total_min + (total_hours * 60)
        self.response_ta = ta


class QueueManager:
    """
    Manages the OH queue by keeping track of resolved and unresolved entries.

    Attributes:
        - unresolved_entries (list): a list that manages unresolved entries.
        - resolved_entries (list): a list that manages resolved entries
        - tas (dictionary): maps TA;s string UIDs to corresponding TA objects
    """

    def __init__(self):
        """
        Construct a new QueueManager, creating and initialising the
        unresolved_entries list, resolved_entries list, and the ta dictionary
        to empty. It does not take any arguments
        """
        self.unresolved_entries = []
        self.resolved_entries = []
        self.ta = {}

    def __len__(self):
        """
        Returns the length of the unresolved entries list.
        """
        return len(self.unresolved_entries)

    def enter_ta(self, ta):
        """
        Takes a ta object as an argument and adds the ta to the QueueMangager's
        dictionary of mappings.

        Arguments:
            - ta (ta): a ta object to be added to the dictionary
        """
        if ta.uid in self.ta.keys():
            print('This TA is already in the QueueManager.')
        else:
            self.ta[ta.uid] = ta

    def get_ta(self, uid):
        """
        retrieves a TA with a specified uid from the ta dictionary.

        Arguments:
            - uid (string): the uid of the ta to be retrieved

        Returns:
            - TA (TA): the TA with the specified uid
        """
        if uid in self.ta.keys():
            return self.ta[uid]
        else:
            return None

    def add_entry(self, entry):
        """
        Takes an entry and add it to the end of the unresoled entries list.

        Arguments:
            - entry (Entry)

        """
        self.unresolved_entries.append(entry)

    def get_next_entry(self):
        """
        Return the Entry at the front of the unresolved entries list and remove
        it from the list.

        """
        if self.unresolved_entries == []:
            return None
        else:
            # is the next entry the object at the start or end of the list?
            next_entry = self.unresolved_entries[0]
            self.unresolved_entries.remove(next_entry)
            return next_entry

    def add_resolved_entry(self, entry, ta):
        """
        Takes in an Entry object and a TA object and resolves the entry, adding
        it to the resolved entries list.

        Arguments:
            - entry (Entry): the Entry object to be resolved
            - ta (TA): The TA who resolved the entry

        """
        entry.resolve_entry(ta)
        self.resolved_entries.append(entry)

    def get_resolved_entries(self):
        """
        Returns the current list of resolved entries.

        """
        return self.resolved_entries

    def get_unresolved_entries(self):
        """
        Returns the current list of unresolved entries.

        """
        return self.unresolved_entries
