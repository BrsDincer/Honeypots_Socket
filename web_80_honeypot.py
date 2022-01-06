import socket

class ATTRIBUTES_CONNECTION():
    def LOCAL_HOST(target_host):
        return target_host
    def LOCAL_PORT(target_port):
        return target_port
    def INFO_LOG_HOST(log_host):
        return log_host
    def INFO_LOG_PORT(log_port):
        return log_port
    
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
    
    def SEND_LOG_INFO(l_ip=str,message_info=str,rhost=str,rport=int,lport=int):
        sc_log = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        sc_log.connect((rhost,rport))
        log_message = f"IP: {l_ip} / PORT: {str(lport)} | {message_info}"
        sc_log.send(log_message.encode())
        sc_log.close()
        
    def SOCKET_CONNECTION(lhost=str,lport=int,lcount=int,dsize=int):
        sc_main = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        sc_main.setblocking(1)
        sc_main.bind((lhost,lport))
        sc_main.listen(lcount)
        while True:
            (inner_u,inner_add) = sc_main.accept()
            # inner_u.settimeout(7)
            print("%s"%ECHO_PRINT.GREEN_ECHO("[+] HONEYPOT ACTIVE"))
            print("%s"%ECHO_PRINT.YELLOW_ECHO(f"CONNECTION FROM {inner_add[0]} {inner_add[1]}"))
            banner_message = 'MESSAGE'
            try:
                inner_u.send(banner_message.encode())
                response_message = inner_u.recv(dsize).decode()
                print("%s"%ECHO_PRINT.INFO_ECHO(response_message))
            except socket.error as sc_:
                CONNECTION_OPS.SEND_LOG_INFO(inner_add[0],f"ERROR: {str(sc_)}",inner_add[0],int(inner_add[1]),lport)
            else:
                CONNECTION_OPS.SEND_LOG_INFO(inner_add[0],response_message,inner_add[0],int(inner_add[1]),lport)
            finally:
                inner_u.close()
                sc_main.close()
    def MAIN_OPS():
        my_ip_info = CONNECTION_OPS.GET_LOCAL_IP()
        print("%s"%ECHO_PRINT.GREEN_ECHO(my_ip_info))
        l_host = ATTRIBUTES_CONNECTION.LOCAL_HOST("0.0.0.0")
        l_port = ATTRIBUTES_CONNECTION.LOCAL_PORT(80)
        CONNECTION_OPS.SOCKET_CONNECTION(l_host,l_port,5,1024)
        
                
if __name__ == '__main__':
    try:
        CONNECTION_OPS.MAIN_OPS()
    except:
        pass
 
