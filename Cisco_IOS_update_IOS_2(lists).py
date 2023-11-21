import paramiko

# Set the variables for the SSH connection
username = "cisco"
password = "cisco"

# Set the variables for the IOS upgrade
old_ios = "old_ios.bin"
new_ios = "new_ios.bin"

# Set the IP addresses of the routers
router_ips = ["192.0.2.1", "192.0.2.2", "192.0.2.3", ..., "192.0.2.100"]

# Create an SSH client object
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# Loop through the list of routers and upgrade their IOS
for ip in router_ips:
    try:
        # Connect to the router
        ssh.connect(ip, username=username, password=password)

        # Upgrade the IOS
        stdin, stdout, stderr = ssh.exec_command("copy tftp://" + new_ios + " flash:")

        # Wait for the upgrade to complete
        while not stdout.channel.exit_status_ready():
            pass

        # Save the configuration and reload the router
        stdin, stdout, stderr = ssh.exec_command("wr mem")
        stdin, stdout, stderr = ssh.exec_command("reload")

        # Wait for the router to reload
        while not stdout.channel.exit_status_ready():
            pass

        # Disconnect from the router
        ssh.close()

        print("Successfully upgraded IOS on " + ip)

    except Exception as e:
        print("Failed to upgrade IOS on " + ip)
        print(e)