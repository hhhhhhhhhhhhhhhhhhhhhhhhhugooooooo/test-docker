import os 


def main():
    print("Hello World!")
    ssh_command= "ssh 172.17.0.1 echo 'Hello World!'"
    print(os.popen(ssh_command).read().rstrip()=='Hello World!')
    print("Done!")
    
main()