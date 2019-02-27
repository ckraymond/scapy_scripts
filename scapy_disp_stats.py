# Scapy Scan - Display
# Author: Colin Raymond (colin.k.raymond@gmail.com)
# Github: https://github.com/ckraymond/scapy_scripts

import os

class ScapyDisplayStats:

    screen = []

    def __init__(self, stats):
        self.get_screen_info()
        self.build_screen(stats)
        self.disp_screen()

    def update_screen(self, stats):
        self.build_screen(stats)
        self.disp_screen()

    # Gets the terminal size to fit the window correctly
    def get_screen_info(self):
        self.rows, self.columns = os.popen('stty size', 'r').read().split()
        self.columns = int(self.columns)
        self.rows = int(self.rows)

    # Draws a simple line across the screen
    def draw_line(self):
        line = ''
        for i in range(self.columns):
            line += '*'
        return line

    # Overwrites the screen with the new display cache
    def build_screen(self, stats):
        self.screen = []

        # Build header
        self.screen.append(self.draw_line())
        self.screen.append("Scapy Scanner v0.1")
        self.screen.append(self.draw_line())

        # Add fields being tracked
        for stat in stats:
            new_line = stats[stat].disp_name + ": " + str(stats[stat].value)
            self.screen.append(new_line)
        self.screen.append(self.draw_line())

        # Add alerts and other stats

    def disp_screen(self):
        os.system('clear')
        for line in self.screen:
            print line
