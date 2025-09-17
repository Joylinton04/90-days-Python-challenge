# Day 36-37: Network Sniffing with Scapy
import scapy

from scapy.all import sniff

def packet_callback(packet):
    print("\n📦 Packet Captured:")
    print(packet.summary())  # Quick summary
    if packet.haslayer("IP"):
        ip_layer = packet["IP"]
        print(f"🔹 Source IP: {ip_layer.src}")
        print(f"🔹 Destination IP: {ip_layer.dst}")
        print(f"🔹 Protocol: {ip_layer.proto}")
    if packet.haslayer("TCP"):
        tcp_layer = packet["TCP"]
        print(f"🔸 Source Port: {tcp_layer.sport}")
        print(f"🔸 Destination Port: {tcp_layer.dport}")

# Start sniffing (Ctrl+C to stop)
print("🚀 Starting packet capture... Press Ctrl+C to stop.")
sniff(prn=packet_callback, count=2)  # Capture 2 packets
