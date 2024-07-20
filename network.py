import socket
import struct
import binascii

def mac_addr(address):
    """Convert a MAC address to a readable/printable string."""
    return ':'.join(f'{b:02x}' for b in address)

def main():
    # Create a raw socket and bind it to the interface
    conn = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(0x0003))
    conn.bind(("eth0", 0))  # Change "eth0" to your network interface

    while True:
        # Receive a packet
        raw_data, addr = conn.recvfrom(65535)

        # Unpack the Ethernet frame
        dest_mac, src_mac, proto = struct.unpack('! 6s 6s H', raw_data[:14])
        dest_mac = mac_addr(dest_mac)
        src_mac = mac_addr(src_mac)
        proto = socket.htons(proto)

        # Print the extracted information
        print(f'\nEthernet Frame:')
        print(f'Destination MAC: {dest_mac}')
        print(f'Source MAC: {src_mac}')
        print(f'Protocol: {proto}')

if __name__ == "__main__":
    main()
