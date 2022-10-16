import os
import docker

print("\n Welcome to BankBazaar's sniper.\n\n")
print(" 1. Enter the docker repo: cyberspidy/secops, 2. Enter command eg sniper or nmap\n\n")
repo = input ("Enter image repo:")
#name = input ("Enter container name:")
command = input ("Enter command to run:")
client = docker.from_env()
client.containers.run(repo, command,
volumes={os.getcwd():{'bind':'/usr/share/sniper/loot','mode':'rw'}}, stream=True)
