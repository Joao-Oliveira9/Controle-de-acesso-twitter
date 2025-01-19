import pyshark
import asyncio

capture = pyshark.LiveCapture(interface="Ethernet",bpf_filter="port 53")
count = 0

def mostrar_pacotes(packet) -> None:
    global count
    try:
        if packet.dns.qry_name == "x.com":
             print(packet.dns.qry_name)
             count += 1
             print(count)
    except asyncio.TimeoutError:
        pass


def capturar_pacotes() -> None:
     capture = pyshark.LiveCapture(interface="Ethernet",bpf_filter="port 53")
     capture.apply_on_packets(mostrar_pacotes,timeout=100)

def main() -> None:
    try:
        capturar_pacotes()
    except KeyboardInterrupt:
        print("Shutting down...") 

main()