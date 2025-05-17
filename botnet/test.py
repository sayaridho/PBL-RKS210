import customtkinter as ctk
import paramiko
from concurrent.futures import ThreadPoolExecutor

my = ctk.CTk()
my.geometry('400x200')

ent = ctk.CTkEntry(my)
ent.place(x=60,y=100)



def coba():
    hosts = [
                {'ip': '172.24.25.74', 'port': 22, 'username': 'benz', 'password': '03061122'},
                {'ip': '192.168.2.3', 'port': 22, 'username': 'kali', 'password': 'kali'},
                {'ip': '192.168.2.4', 'port': 22, 'username': 'kali', 'password': 'kali'},
                {'ip': '192.168.2.5', 'port': 22, 'username': 'kali', 'password': 'kali'},
            ]
    return hosts

def coba2(host):
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        ssh_client.connect(host['ip'], host['port'],host['username'], host['password'])
        print(f"connected to {host['ip']}")

    except:
        print(f"not connected to {host['ip']} \n")
        

def coba3():
    with ThreadPoolExecutor() as executor:
        executor.map(coba2, coba())

    my.quit()

button = ctk.CTkButton(my, text='press me', command=coba3)
button.place(x=60,y=150)


my.mainloop()