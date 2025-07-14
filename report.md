# Subnet Analysis Report

## 1. Subnet with the Most Hosts
The subnet mask 255.255.252.0 (/22) provides the most host addresses — 1,022 usable IPs per subnet.

Subnets using /22:
- 192.168.100.7
- 10.2.1.56
- 172.16.50.1
- 10.20.4.6
- 192.168.20.44
- 172.16.60.30
- 10.3.3.9
- 10.15.5.50

## 2. Are there any overlapping subnets? If yes, which ones?
No overlapping subnets among the provided IP addresses and subnet masks. Each subnet occupies a distinct and non-overlapping range within the IP address space.

## 3. What is the smallest and largest subnet in terms of address space?
The "address space" refers to the total number of IP addresses available within a subnet, including the network and broadcast addresses.

- **Smallest subnet** (in terms of address space):
  - Subnets with a /24 CIDR prefix (subnet mask 255.255.255.0)
  - Total Addresses: 2^(32-24) = 2^8 = 256 IP addresses

- **Largest subnet** (in terms of address space):
  - Subnets with a /22 CIDR prefix (subnet mask 255.255.252.0)
  - Total Addresses: 2^(32-22) = 2^10 = 1024 IP addresses

## 4. Suggest a subnetting strategy that could reduce wasted IPs in this network
The current network uses some fixed-size subnet masks (/22, /23). This often leads to waste of IP addresses if the actual number of hosts in a segment is much lower than the capacity of the allocated subnet.

The most effective strategy to reduce wasted IPs in this network is to implement Variable Length Subnet Masking (VLSM):

1. **Analyze Actual Host Requirements**: Instead of broadly applying /24, /23, or /22 masks, conduct a detailed analysis of the number of devices or hosts needed in each specific network segment.

2. **Allocate Smallest Necessary Subnets**:
   - If a segment only requires 10 hosts, instead of giving it a /24 (254 usable hosts), allocate a /28 (14 usable hosts) or /27 (30 usable hosts). This immediately saves hundreds of IP addresses that would otherwise be unused.

By implementing VLSM, the network can be designed to match the specific needs of each segment, significantly reducing IP address waste compared to the current fixed-mask approach.
