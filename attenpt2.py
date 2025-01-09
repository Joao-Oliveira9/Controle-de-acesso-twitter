import pyshark
import asyncio

capture = pyshark.LiveCapture(interface="Ethernet",bpf_filter="port 53")

def print_packets(packet) -> None:
    try:
        print(packet)
    except asyncio.TimeoutError:
        pass

try:
    capture.apply_on_packets(print_packets,timeout=5)
except asyncio.TimeoutError:
        pass
