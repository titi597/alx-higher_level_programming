#!/usr/bin/python3
"""Log parsing."""
import sys
import signal


def print_statistics(total_size, status_count):
    """a script that reads stdin line by line and computes metrics."""
    print("Total file size: {}".format(total_size))
    for status_code in sorted(status_count.keys()):
        print("{}: {}".format(status_code, status_count[status_code]))


def signal_handler(sig, frame):
    print_statistics(total_size, status_count)
    sys.exit(0)


def parse_line(line):
    parts = line.split()
    return int(parts[-1]), int(parts[-2])


total_size = 0
status_count = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0

signal.signal(signal.SIGINT, signal_handler)

try:
    for line in sys.stdin:
        line_count += 1
        file_size, status_code = parse_line(line)
        total_size += file_size

        if status_code in status_count:
            status_count[status_code] += 1

        if line_count % 10 == 0:
            print_statistics(total_size, status_count)

except KeyboardInterrupt:
    print_statistics(total_size, status_count)
    sys.exit(0)
