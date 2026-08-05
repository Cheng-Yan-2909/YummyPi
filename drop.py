import os
import sys
import random
import threading
import time


class DisplayChar:
    char_list = [
        "a", "e", "u", "k", "3", "9", "2", "@", "!", " ", " ", " ",
    ]
    index = 0

    @staticmethod
    def select():
        return random.choice(DisplayChar.char_list)



class Display:
    keep_running = True
    display: list[list] = None
    width = 0
    height = 0

    def __init__(self):
        self.display = [[]]

    def adjust_display(self):
        size = os.get_terminal_size()
        self.width = size.columns
        self.height = size.lines

        while len(self.display) > self.height:
            self.display.pop()
        while len(self.display) < self.height:
            self.display.append(
                ["" for i in range(self.width)]
            )

        for row in self.display:
            while len(row) > self.width:
                row.pop()

            while len(row) < self.width:
                row.append("")

    def draw(self):
        sys.stdout.write("\033[H\033[2J")
        sys.stdout.flush()
        for row in self.display:
            for col in row:
                sys.stdout.write(col)
            sys.stdout.write("\n")
            sys.stdout.flush()

    def scroll(self):
        while len(self.display) >= self.height:
            self.display.pop()
        self.display.insert(
            0,
            [DisplayChar.select() for i in range(self.width)]
        )


def run_display():
    display = Display()
    while Display.keep_running:
        display.adjust_display()
        display.draw()
        display.scroll()
        time.sleep(0.1)


def main():
    t = threading.Thread(target=run_display)
    t.start()
    input("Press enter to quit")
    Display.keep_running = False


main()
