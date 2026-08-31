# SmartBranch 360 - Network Configuration Validation Tool
# Author: Srikanth Paleti

print("--- Starting SmartBranch 360 Configuration Check ---\n")

# 1. Define the Expected Network Plan
expected_vlans = ["10", "20", "30", "99"]
expected_gateways = {
    "10": "192.168.10.1",
    "20": "192.168.20.1",
    "30": "192.168.30.1",
    "99": "192.168.99.1"
}

# 2. Simulated 'show ip interface brief' output from R1
router_show_output = """
Interface                  IP-Address      OK? Method Status                Protocol
GigabitEthernet0/0/0       unassigned      YES unset  up                    up
GigabitEthernet0/0/0.10    192.168.10.1    YES manual up                    up
GigabitEthernet0/0/0.20    192.168.20.1    YES manual up                    up
GigabitEthernet0/0/0.30    192.168.30.1    YES manual up                    up
GigabitEthernet0/0/0.99    192.168.99.1    YES manual up                    up
"""

# 3. Validation Logic
error_count = 0

for vlan in expected_vlans:
    target_interface = f"GigabitEthernet0/0/0.{vlan}"
    target_ip = expected_gateways[vlan]
    
    # Check if the interface and correct IP exist in the router output
    if target_interface in router_show_output and target_ip in router_show_output:
        print(f"[PASS] VLAN {vlan} Gateway ({target_ip}) is active and configured correctly.")
    else:
        print(f"[FAIL] Configuration error detected on VLAN {vlan}!")
        print(f"       Suggested Fix: Check sub-interface {target_interface} or IP assignment.")
        error_count += 1

print(f"\n--- Validation Complete. Errors Found: {error_count} ---")