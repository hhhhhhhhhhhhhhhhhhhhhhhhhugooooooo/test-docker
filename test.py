import os 


def main():
    print("Hello World!")
    ssh_command= "ssh 172.17.0.1 echo 'Hello World!'"
    os.popen(ssh_command).read().rstrip()
    print("Done!")
    
main()