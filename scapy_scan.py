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

    def get_stats(self):
        stat_list = []
        for stat in self.stats:
            print stat

        p = read()
        return stat_list

class ScapyScan:

    # Initalization of scanner
    def __init__(self):
        self.stats = ScanStats()
        self.display = display.ScapyDisplayStats(self.stats)

    def alert(self, pkt):
        self.stats.count += 1
        self.stats.size += int(pkt.sprintf("%IP.len%"))

        print 'Packet Count: ' + str(self.stats.count)
        print 'Packet Size (bytes):' + str(self.stats.size)

    def sniff_pkts(self):
        scapy.sniff(filter = config.FILTERS['basic'],
            prn = self.alert, count = 0)

new_scan = ScapyScan()
new_scan.sniff_pkts()
