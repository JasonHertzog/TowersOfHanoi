class HanoiVisualization:
    def __init__(self, n):
        """The __init__ method is a special method in Python classes that is used to initialize the object when it is
            created. In this case, the __init__ method takes a single argument n (the number of disks in the
            Towers of Hanoi problem).

            The first line of the method sets the self.n attribute to the minimum of n and 10. This is done because
            the visualization of the problem is limited to 10 disks. If n is greater than 10, a message is printed to
            inform the user that the number of disks has been limited to 10. Technically you could remove this
            limitation, but it's just a lot.

            The next three lines initialize the attributes self.pegA, self.pegB, and self.pegC. self.pegA is a list
            that represents the first peg in the Towers of Hanoi problem. The list is created using a list
            comprehension, which generates a list of numbers from self.n down to 1. self.pegB and self.pegC are both
            empty lists, which will be used to represent the second and third pegs, respectively."""
        self.n = min(n, 10)
        if n > 10:
            print("Number of disks limited to 10 for visualization purposes.")
        self.pegA = [i for i in range(self.n, 0, -1)]
        self.pegB = []
        self.pegC = []

    def draw_state(self):
        """The draw_state method can be thought of as a way to display the current state of a game of Towers of Hanoi,
           much like a visual game board. Just like on a game board, there are three different "pegs" (representing the
           source, auxiliary, and target pegs), and each peg can hold several "disks" (represented by numbers).

           The for loop in the draw_state method acts like a cursor that moves from the top of the game board down to
           the bottom, checking each space to see if it is empty or contains a disk. If the space is empty,
           it is represented by three spaces in between two vertical bars (| |), much like an empty space on a game
           board. If the space contains a disk, the disk number is displayed in the center of the space,
           centered within three characters (e.g. | 3 |).

           The if statement in the draw_state method acts as a decision-making mechanism, determining whether a space
           is empty or contains a disk based on the current iteration of the for loop. If the current iteration is
           greater than or equal to the length of the self.pegA list, then the space is considered to be empty,
           and the line "| " is printed. If the current iteration is not greater than or equal to the length of the
           self.pegA list, then a disk is present in the space, and the disk number is displayed.

           Finally, the print("|\n") statement at the end of the method acts like a way to separate the different
           pegs and create a new line for the next iteration of the method."""
        print("Peg A: ", end="")
        for i in range(self.n - 1, -1, -1):
            if i >= len(self.pegA):
                print("|   ", end="")
            else:
                print(f"|{self.pegA[i]:^3}", end="")
        print("|")
        print("Peg B: ", end="")
        for i in range(self.n - 1, -1, -1):
            if i >= len(self.pegB):
                print("|   ", end="")
            else:
                print(f"|{self.pegB[i]:^3}", end="")
        print("|")
        print("Peg C: ", end="")
        for i in range(self.n - 1, -1, -1):
            if i >= len(self.pegC):
                print("|   ", end="")
            else:
                print(f"|{self.pegC[i]:^3}", end="")
        print("|\n")

    def move_disk(self, source, target):
        """Two arguments: source and target. source represents the peg that the disk is being moved from,
        and target represents the peg that the disk is being moved to.

        The first line of the method uses the pop method to remove the last element from the source list. This
        element represents a disk on the peg, and it is assigned to the variable disk. The pop method is used instead
        of simply accessing the last element of the list because it also removes the element from the list,
        effectively "popping" it off the end of the list.

        The second line of the method uses the append method to add the disk to the end of the target list. This
        effectively "appends" the disk to the end of the target list, moving it from the source peg to the target
        peg."""
        disk = source.pop()
        target.append(disk)

    def tower_of_hanoi(self, n, source, auxiliary, target):
        """The tower_of_hanoi method is the core of the Towers of Hanoi problem. It takes four arguments: n, source,
        auxiliary, and target. n represents the number of disks in the problem, and source, auxiliary, and target
        represent the pegs that the disks are being moved between.

        This method uses a recursive approach to solve the problem. Recursion is a technique in computer science
        where a function calls itself in order to solve a problem.

        The first line of the method uses an if statement to check if n is equal to 1. If it is, then only one disk
        is present, and it can be moved directly from the source peg to the target peg. The move_disk method is
        called to move the disk, and the current state of the problem is displayed using the draw_state method. The
        return statement is used to exit the function and stop the recursion.

        If n is greater than 1, the method first calls itself with n - 1 as the first argument, and the source,
        target, and auxiliary arguments swapped. This causes the method to solve the subproblem of moving n - 1 disks
        from the source peg to the auxiliary peg, using the target peg as an intermediary.

        Once the subproblem has been solved, the method moves the nth disk from the source peg to the target peg
        using the move_disk method. The current state of the problem is displayed using the draw_state method.

        Finally, the method calls itself again with n - 1 as the first argument, and the auxiliary, source,
        and target arguments swapped. This causes the method to solve the subproblem of moving n - 1 disks from the
        auxiliary peg to the target peg, using the source peg as an intermediary.

        This process is repeated until all n disks have been moved from the source peg to the target peg,
        and the problem is solved. The recursion continues until the base case (n equal to 1) is reached,
        at which point the function stops calling itself and returns."""
        if n == 1:
            self.move_disk(source, target)
            print(f"Move disk 1 from {source} to {target}")
            self.draw_state()
            return

        self.tower_of_hanoi(n - 1, source, target, auxiliary)
        self.move_disk(source, target)
        print(f"Move disk {n} from {source} to {target}")
        self.draw_state()
        self.tower_of_hanoi(n - 1, auxiliary, source, target)

    def main(self):
        """The main method is the starting point for the Towers of Hanoi problem. It is used to call the
        tower_of_hanoi method and start solving the problem.

        The method takes no arguments, and simply calls self.tower_of_hanoi with the arguments self.n, self.pegA,
        self.pegB, and self.pegC. These arguments represent the number of disks in the problem, and the pegs that the
        disks are being moved between.

        By calling self.tower_of_hanoi with these arguments, the method starts the process of solving the Towers of
        Hanoi problem, and displays each step of the solution using the draw_state method."""
        self.tower_of_hanoi(self.n, self.pegA, self.pegB, self.pegC)


if __name__ == "__main__":
    # Main program
    num_of_disks = int(input("Enter number of disks: "))
    hanoi = HanoiVisualization(num_of_disks)
    hanoi.main()
