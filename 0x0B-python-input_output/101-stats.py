#!/usr/bin/python3
"""Log parsing.

After every ten lines or the input of a keyboard interruption (CTRL + C),
prints the following statistics:
    - Total file size of that point.
    - Count of read status codes up to that point.
"""


def print_statistics(size, status_counts):
    """Print acquired metrics.

    Args:
        size (int): The acquired read file size.
        status_counts (dict): The acquired count of status codes.
    """
    print("File size: {}".format(size))
    for key in sorted(status_counts):
        print("{}: {}".format(key, status_counts[key]))


if __name__ == "__main__":
    import sys

    size = 0
    status_counts = {}
    valid_codes = ['200', '301', '400', '401', '403', '404', '405', '500']
    count = 0

    try:
        for line in sys.stdin:
            if count == 10:
                print_statistics(size, status_counts)
                count = 1
            else:
                count += 1

            line = line.split()

            try:
                size += int(line[-1])
            except (IndexError, ValueError):
                pass

            try:
                if line[-2] in valid_codes:
                    if status_counts.get(line[-2], -1) == -1:
                        status_counts[line[-2]] = 1
                    else:
                        status_counts[line[-2]] += 1
            except IndexError:
                pass

        print_statistics(size, status_counts)

    except KeyboardInterrupt:
        print_statistics(size, status_counts)
        raise
