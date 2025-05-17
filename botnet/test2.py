import customtkinter as ctk
import paramiko
import asyncio

my = ctk.CTk()
my.geometry('400x200')

ent = ctk.CTkEntry(my)
ent.place(x=60, y=100)

def coba():
    hosts = [
        {'ip': '172.24.25.74', 'port': 22, 'username': 'benz', 'password': '03061122'},
        {'ip': '192.168.2.3', 'port': 22, 'username': 'kali', 'password': 'kali'},
        {'ip': '192.168.2.4', 'port': 22, 'username': 'kali', 'password': 'kali'},
        {'ip': '192.168.2.5', 'port': 22, 'username': 'kali', 'password': 'kali'},
    ]
    return hosts

async def coba2(host):
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        await asyncio.get_event_loop().run_in_executor(None, ssh_client.connect, host['ip'], host['port'], host['username'], host['password'])
        print(f"Connected to {host['ip']}")

    except Exception as e:
        print(f"Failed to connect to {host['ip']}: {str(e)}")

def coba3():
    loop = asyncio.get_event_loop()
    tasks = [coba2(host) for host in coba()]
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()
    
    my.quit()  # Memberhentikan program setelah selesai

button = ctk.CTkButton(my, text='press me', command=coba3)
button.place(x=60, y=150)

my.mainloop()
import customtkinter as ctk
import paramiko
import asyncio

my = ctk.CTk()
my.geometry('400x200')

ent = ctk.CTkEntry(my)
ent.place(x=60, y=100)

def coba():
    hosts = [
        {'ip': '172.24.25.74', 'port': 22, 'username': 'benz', 'password': '03061122'},
        {'ip': '192.168.2.3', 'port': 22, 'username': 'kali', 'password': 'kali'},
        {'ip': '192.168.2.4', 'port': 22, 'username': 'kali', 'password': 'kali'},
        {'ip': '192.168.2.5', 'port': 22, 'username': 'kali', 'password': 'kali'},
    ]
    return hosts

async def coba2(host):
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        await asyncio.get_event_loop().run_in_executor(None, ssh_client.connect, host['ip'], host['port'], host['username'], host['password'])
        print(f"Connected to {host['ip']}")

    except Exception as e:
        print(f"Failed to connect to {host['ip']}")

def coba3():
    loop = asyncio.get_event_loop()
    tasks = [coba2(host) for host in coba()]
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()
    
    my.quit()

button = ctk.CTkButton(my, text='press me', command=coba3)
button.place(x=60, y=150)

my.mainloop()