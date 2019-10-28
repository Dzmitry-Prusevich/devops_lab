#!/usr/bin/env python
from datetime import datetime
import json
import psutil
import time
import configparser


def read_conf():
    # read info from config.ini
    config = configparser.ConfigParser()
    config.read('config.ini')
    wait_time = 60 * int(config['common']['interval'])
    output_format = config['common']['output']
    # create file for output information
    out_file = "data." + output_format
    with open(out_file, 'w') as the_file:
        the_file.close()
    return config, wait_time, output_format, out_file


# class for updating info of system current state
class Record:
    i = 0

    def __init__(self):
        self.data = {}

    def cur_state(self):
        TIMESTAMP = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        cpu_percent = psutil.cpu_percent()
        memory_overall = psutil.virtual_memory().percent
        virt_mem_info = psutil.Process().memory_info().vms
        disk_io_counters_read = psutil.disk_io_counters().read_count
        disk_io_counters_write = psutil.disk_io_counters().write_count
        net_io_counters_sent = psutil.net_io_counters().bytes_sent
        net_io_counters_recv = psutil.net_io_counters().bytes_recv
        return TIMESTAMP, cpu_percent, memory_overall, virt_mem_info, disk_io_counters_read, \
               disk_io_counters_write, net_io_counters_sent, net_io_counters_recv

    def write_json(self):
        TIMESTAMP, cpu_percent, memory_overall, virt_mem_info, disk_io_counters_read, \
        disk_io_counters_write, net_io_counters_sent, net_io_counters_recv = self.cur_state()
        Record.i += 1
        namekey = 'snapshot' + str(Record.i)
        self.data[namekey] = []
        self.data[namekey].append({
            "time of snap": TIMESTAMP,
            'cpu_percent': cpu_percent,
            'memory_overall': memory_overall,
            'virt_memory_info': virt_mem_info,
            'disk_io_counters_read': disk_io_counters_read,
            'disk_io_counters_write': disk_io_counters_write,
            'net_io_counters_sent': net_io_counters_sent,
            'net_io_counters_recv': net_io_counters_recv,
        })
        with open('data.json', 'w') as outfile:
            json.dump(self.data, outfile)

    def write_text(self):
        TIMESTAMP, cpu_percent, memory_overall, virt_mem_info, disk_io_counters_read, \
        disk_io_counters_write, net_io_counters_sent, net_io_counters_recv = self.cur_state()
        Record.i += 1
        namekey = 'snapshot' + str(Record.i)
        line = "{0}: {1} : cpu_percent = {2}, memory_overall = {3}, virt_mem_info = {4} " \
               "disk_io_counters_read = {5}, disk_io_counters_write = {6}, " \
               "net_io_counters_sent = {7}, net_io_counters_recv = {8}".format(
            namekey, TIMESTAMP, cpu_percent, memory_overall, virt_mem_info, disk_io_counters_read,
            disk_io_counters_write, net_io_counters_sent, net_io_counters_recv)
        with open('data.txt', 'a') as the_file:
            the_file.write(line + "\n")


def write_info():
    config, wait_time, output_format, out_file = read_conf()
    print("Now this program begins to take snapshots of your system and write it in "
          "file {1} every {0} minutes."
          "Use CTRL+C to finish the process".format(config['common']['interval'], out_file))
    # write current system state info into the file
    if output_format == "json":
        jsonrecord = Record()
        while True:
            jsonrecord.write_json()
            time.sleep(wait_time)
    else:
        textrecord = Record()
        while True:
            textrecord.write_text()
            time.sleep(wait_time)


if __name__ == "__main__":
    write_info()
