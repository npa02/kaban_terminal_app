import json
import os

from rich.console import Console
from rich.table import Table

KANBAN_FILE = "kanban.json"


class KanbanApplication:
    def __init__(self):
        self.kanban_board = load_kanban_board()
        self.current_col = 0
        self.current_row = 0
        self.console = Console()

    def display_kanban(self):
        table = Table(title="Kanban Board")
        for col in self.kanban_board.keys():
            table.add_column(col)

        max_len = max(len(tasks) for tasks in self.kanban_board.values())

        for i in range(max_len):
            row = []
            for col, tasks in self.kanban_board.items():
                if i < len(tasks):
                    row.append(tasks[i])
                else:
                    row.append("")

            table.add_row(*row)

        self.console.print(table)

    def add_task(self):
        column_name = input("Enter the column name to add the task: ")
        task_name = input("Enter the task name: ")

        if column_name in self.kanban_board:
            self.kanban_board[column_name].append(task_name)
            save_kanban_board(self.kanban_board)
            self.console.print(f"Task '{task_name}' added to '{
                               column_name}' column.")
        else:
            self.console.print(f"Column '{column_name}' not found.")

    def move_task(self):
        from_column = input("Enter the source column name: ")
        to_column = input("Enter the destination column name: ")

        if from_column in self.kanban_board and to_column in self.kanban_board:
            if not self.kanban_board[from_column]:
                self.console.print(
                    f"No tasks in '{from_column}' column to move.")
            else:
                task_to_move = self.kanban_board[from_column].pop()
                self.kanban_board[to_column].append(task_to_move)
                save_kanban_board(self.kanban_board)
                self.console.print(f"Task '{task_to_move}' moved from '{
                                   from_column}' to '{to_column}' column.")
        else:
            self.console.print("Invalid column names.")

    def delete_task(self):
        column_name = input("Enter the column name to delete the task from: ")
        task_name = input("Enter the task name to delete: ")

        if column_name in self.kanban_board:
            if task_name in self.kanban_board[column_name]:
                self.kanban_board[column_name].remove(task_name)
                save_kanban_board(self.kanban_board)
                self.console.print(f"Deleted task '{task_name}' from '{
                                   column_name}' column.")
            else:
                self.console.print(f"Task '{task_name}' not found in '{
                                   column_name}' column.")
        else:
            self.console.print(f"Column '{column_name}' not found.")

    def run(self):
        try:
            while True:
                self.display_kanban()
                action = input(
                    "Press 'a' to add a task, "
                    "'m' to move a task, "
                    "'d' to delete a task, "
                    "or 'q' to quit: ")
                if action.lower() == 'q':
                    break
                elif action.lower() == 'a':
                    self.add_task()
                elif action.lower() == 'm':
                    self.move_task()
                elif action.lower() == 'd':
                    self.delete_task()
        except KeyboardInterrupt:
            pass


def load_kanban_board():
    if os.path.exists(KANBAN_FILE):
        with open(KANBAN_FILE, "r") as file:
            return json.load(file)
    else:
        return {"To Do": [], "In Progress": [], "Done": []}


def save_kanban_board(kanban_board):
    with open(KANBAN_FILE, "w") as file:
        json.dump(kanban_board, file)


def main():
    app = KanbanApplication()
    app.run()


if __name__ == "__main__":
    main()
