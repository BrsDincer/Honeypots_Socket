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
    def START_CLIENT(rhost=str,
                     rport=int,
                     sfamily=socket.AF_INET,
                     sstream=socket.SOCK_STREAM,
                     dsize=2048):
        sc_client = socket.socket(sfamily,sstream)
        sc_client.connect((rhost,rport))
        while True:
            try:
                message_ok = sc_client.recv(dsize)
                print(message_ok.decode())
                send_command = str(input(">"))
                sc_client.send(send_command.encode())
                command_response = sc_client.recv(dsize).decode()
                print(command_response)
            except:
                break
            
if __name__ == '__main__':
    try:
        CONNECTION_OPS.START_CLIENT("",21)
    except Exception as err:
        print(str(err))
        pass
    
