# SmartBranch 360 - Enterprise Network Architecture

An enterprise-grade network architecture designed in Cisco Packet Tracer, featuring automated configuration validation via Python. Built as the final capstone for the Cisco Virtual Internship Program (VIP) 2026.

## 🏗 Architecture & Topology
Designed a 4-VLAN network utilizing Router-on-a-Stick (ROAS) for Inter-VLAN routing:
* **VLAN 10 (Employee):** Core internal operations.
* **VLAN 20 (Guest):** Isolated public access network.
* **VLAN 30 (Server):** Internal server hosting segment.
* **VLAN 99 (Management):** Restricted network for admin device access.

## ⚙️ Core Implementations
* **DHCP Provisioning:** Configured router-based DHCP pools to automatically assign IPs across respective VLAN subnets.
* **Security & Access Control (ACLs):** Implemented strict standard ACLs to isolate Guest traffic from internal servers and restrict SSH management access exclusively to the VLAN 99 subnet.
* **Troubleshooting:** Diagnosed and resolved 5 critical fault scenarios including missing trunk allowed lists, APIPA assignments due to broken DHCP pools, and administratively down sub-interfaces.

## 🐍 Python Automation
Developed `validate.py` to automate the verification of router interface configurations. The script acts as a testing pipeline, cross-referencing expected gateway IPs against simulated `show ip interface brief` outputs to ensure all sub-interfaces are correctly provisioned and active.

## 🚀 How to Run
1. Open the `.pkt` file in **Cisco Packet Tracer**.
2. Run the validation script in your terminal:
   ```bash
   python3 validate.py