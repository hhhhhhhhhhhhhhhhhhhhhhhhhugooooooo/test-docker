import os 


def main():
    print("Hello World!")
    ssh_command= "ssh 172.17.0.1 ls -l"
    os.popen(ssh_command).read().rstrip()
    print("Done!")
    