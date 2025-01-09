import pyshark
import asyncio

capture = pyshark.LiveCapture(interface="Ethernet",bpf_filter="port 53")
count = 0

def print_packets(packet) -> None:
    try:
        print(packet.dns.qry_name)
        if packet.dns.qry_name == "x.com":
             count = count + 1
    except asyncio.TimeoutError:
        pass

try:
    capture.apply_on_packets(print_packets,timeout=5)
    print(count)
except asyncio.TimeoutError:
        pass
