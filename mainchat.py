from tkinter import *
from tkinter import ttk
import threading
import socket

allmsg = []

def RunServer():
    while True:
        server_ip = '192.168.1.29' 
        port = 5000 

        server = socket.socket()
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
        server.bind((server_ip, port))
        server.listen()

        print('Waiting for client...')
        client, addr = server.accept()

        print('Connect from: ',str(addr))
        data = client.recv(1024).decode('utf-8')

        allmsg.append(data)
        print('Message from client: ', data)
        print('Message All: ', allmsg)
        
        try:
            textshow = ''
            if len(allmsg) >= 20:
                for m in allmsg[-20:]:
                    textshow += m + '\n'
            else:
                for m in allmsg:
                    textshow += m + '\n'
            v_result2.set(textshow)
        except:
            print('Error Someting')

        resp_text = 'We resive'
        client.send(resp_text.encode('utf-8'))
        client.close()

def SendMessage():
    server_ip = '192.168.1.29' 
    port = 5000 

    data = v_message.get()
    server = socket.socket()
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)

    server.connect((server_ip, port))
    server.send(data.encode('utf-8'))
    data_server = server.recv(1024).decode('utf-8')

    print('Data from Server: ', data_server)
    server.close()

def ThreadRunServer():
    task1 = threading.Thread(target=RunServer)
    task1.start()

# GUI inner
def Sand(event=None):
    text = v_message.get()
    v_result.set(text)
    # print('Message: ', text)
    task2 = threading.Thread(target=SendMessage)
    task2.start()

GUI = Tk()
GUI.geometry('500x300')
GUI.title('Chat Local Server')
FONT = ('2005_iannnnnMTV',15)

# entry
v_message = StringVar()
emessage = ttk.Entry(GUI, textvariable=v_message, font=FONT , width=55)
emessage.pack()
emessage.place(x=50,y=50)

# v_result
v_result = StringVar()
v_result.set('---------Result---------')
Eresult = ttk.Label(GUI, textvariable=v_result, font=FONT , width=55)
Eresult.pack()
Eresult.place(x=50,y=150)
# v_result2
v_result2 = StringVar()
v_result2.set('---------Result2---------')
Eresult2 = ttk.Label(GUI, textvariable=v_result2, font=FONT , width=55)
Eresult2.pack()
Eresult2.place(x=300,y=150)


bsend = ttk.Button(GUI, text='Sand Message', command=Sand)
bsend.pack()
bsend.place(x=200,y=100)

GUI.bind('<Return>', Sand)

# Run Server  
ThreadRunServer()

GUI.mainloop()