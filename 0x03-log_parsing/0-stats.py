#!/usr/bin/python3
"""
A script that reads standardinput line by line and computes metrics
"""
import sys

if __name__ == "__main__":
    default_status_codes = {
        200: 0,
        301: 0,
        400: 0,
        401: 0,
        403: 0,
        404: 0,
        405: 0,
        500: 0,
    }
    counter = 1
    totalFileSize = 0
    try:
        for ln in sys.stdin:
            inputs = ln.split()
            if (len(inputs) >= 7):
                try:
                    file_size = inputs[-1]
                    status_code = inputs[-2]
                    totalFileSize += int(file_size)
                    default_status_codes[int(status_code)] += 1
                except ValueError:
                    cnt -= 1
            if (cnt % 10 == 0):
                print("File size: {:d}".format(totalFileSize))
                for code in sorted(default_status_codes.keys()):
                    if (default_status_codes[code] > 0):
                        print("{}: {:d}".format(
                            str(code), default_status_codes[code]))
            cnt += 1
    except KeyboardInterrupt:
        pass

    print("File size: {:d}".format(totalFileSize))
    for code in sorted(default_status_codes.keys()):
        if (default_status_codes[code] > 0):
            print("{}: {:d}".format(str(code), default_status_codes[code]))
