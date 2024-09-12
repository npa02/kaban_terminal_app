import curses
import random


def get_fortune():
    fortunes = [
        "You will have a great day!",
        "A surprise awaits you around the corner.",
        "Good things come to those who wait.",
        "Today is a lucky day for you.",
        "You will overcome challenges with ease."
    ]
    return random.choice(fortunes)


def main(stdscr):
    while True:
        stdscr.clear()
        stdscr.addstr(0, 0, "Welcome to the Interactive Console!")
        stdscr.addstr(2, 0, "Please choose an option:")
        stdscr.addstr(3, 0, "1. Get a fortune cookie")
        stdscr.addstr(4, 0, "2. Start a countdown timer")
        stdscr.addstr(5, 0, "3. Exit")

        stdscr.refresh()

        choice = stdscr.getch()

        if choice == ord('1'):
            stdscr.clear()
            stdscr.addstr(0, 0, "Your fortune is:")
            stdscr.addstr(2, 0, get_fortune())
            stdscr.addstr(4, 0, "Press any key to continue.")
            stdscr.refresh()
            stdscr.getch()

        elif choice == ord('3'):
            stdscr.clear()
            stdscr.addstr(0, 0, "Exiting the Interactive Console. Goodbye!")
            stdscr.refresh()
            stdscr.getch()
            break

        else:
            stdscr.addstr(7, 0, "Invalid choice. Please enter 1, 2, or 3.")
            stdscr.refresh()
            stdscr.getch()


if __name__ == "__main__":
    curses.wrapper(main)
