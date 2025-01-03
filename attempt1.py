import pyshark

capture = pyshark.LiveCapture(interface="Ethernet",bpf_filter="port 53")

capture.sniff(timeout=5)  # Captura por 10 segundos
print(f"Número de pacotes capturados: {len(capture)}")
print(capture[0].dns.qry_name1)
