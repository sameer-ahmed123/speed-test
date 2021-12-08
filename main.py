# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import speedtest

s = speedtest.Speedtest()

print("testing....\n")
downloadspeed = s.download() / 1048576
uploadspeed = s.upload() / 1048576
pingResult  = round(s.results.ping)

print(f"download speed: {downloadspeed:.2f} Mbps")
print(f"upload speed: {uploadspeed:.2f} Mbps")
print(f"ping: {pingResult} ms")