from netmiko import ConnectHandler
def get_uptime(host):  #host is being called at the end of this code, which is returning the ip address as value to this function.
    switches = {"ip": host, "device_type": "cisco_ios", "username": "admin", "password": "cisco"}
    try:
        connection = ConnectHandler(**switches)
        output = connection.send_command("show version")
        for line in output.splitlines():
            if "uptime" in line:
                uptime = line.strip()
                print(f"Switch {host} Uptime: {uptime}")
                return uptime

        connection.disconnect()
    except Exception as e:
        print(f"Failed to connect to {host}: {e}")
        return None

ip_addr = ["192.168.178.10", "192.168.178.11", "192.168.178.12", "192.168.178.13", "192.168.178.14"]


for host in ip_addr:
    get_uptime(host)
