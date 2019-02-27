# Scapy Scan - Main
# Author: Colin Raymond (colin.k.raymond@gmail.com)
# Github: https://github.com/ckraymond/scapy_scripts

import scapy.all as scapy
import scapy_config as config
import scapy_disp_stats as display
import os

# Class for individual stat information
class Stat:

    def __init__(self, short_name, disp_name, value):
        self.disp_name = disp_name
        self.short_name = short_name
        self.value = value

# Class to store all applicable scan information
class ScanStats:

    def __init__(self, count = 0, size = 0):
        self.stats = {}
        self.stats['total_count'] = Stat('total_count', 'Total Packet Count', count)
        self.stats['total_size'] = Stat('total_size', 'total Size of Packets', size)

    def __getitem__(self, stat):
        return self.stats[stat]

    # Returns list of all stats in the class
    def get_stats(self):
        stat_list = []
        for stat in self.stats:
            stat_list += stat

        return stat_list

    def set_value(self, stat, value):
        self.stats[stat].value = value

# Main class for the program
class ScapyScan:

    # Initalization of scanner
    def __init__(self):
        self.stats = {}
        self.stats['total_count'] = Stat('total_count', 'Total Packet Count', 0)
        self.stats['total_size'] = Stat('total_size', 'total Size of Packets', 0)

        self.display = display.ScapyDisplayStats(self.stats)

    def update_stats(self, pkt):
        if self.stats['total_count'] is not None:
            self.stats['total_count'].value += 1
        if self.stats['total_size'] is not None:
            self.stats['total_size'].value += int(pkt.sprintf("%IP.len%"))
        self.display.update_screen(self.stats)

        # print 'Packet Count: ' + str(self.stats['total_count'].value)
        # print 'Packet Size (bytes):' + str(self.stats['total_size'].value)

    def sniff_pkts(self):
        scapy.sniff(filter = config.FILTERS['basic'],
            prn = self.update_stats, count = 0)

new_scan = ScapyScan()
new_scan.sniff_pkts()
