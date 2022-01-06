import socket,requests,random,json
import warnings
import base64 as b64
import mmh3
from encryption_op import ENCRYPTION_OPS as EOP_F
from encryption_op import MANUAL_ENCRYPTION as MAN_F

warnings.filterwarnings(action="ignore",message="CHECK PYTHON VERSION")
warnings.filterwarnings(action="ignore",message="ALREADY IMPORTED",category=UserWarning)
warnings.filterwarnings(action="ignore",category=DeprecationWarning)
from requests.packages.urllib3.exceptions import InsecureRequestWarning 
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

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
            
    def USER_AGENT_LIST():
        try:
            Json_Tar="user_agent_all.json"
            f_op = open(Json_Tar)
            j_op = json.loads(f_op.read())
            list_agent = []
            for x_value in j_op["user_agents"]:
                for ix_values in j_op["user_agents"][x_value]:
                    for ixl_values in j_op["user_agents"][x_value][ix_values]:
                        for ixlp_values in j_op["user_agents"][x_value][ix_values][ixl_values]:
                            list_agent.append(ixlp_values)
            return list_agent
        except:
            print("%s" % (ECHO_PRINT.RED_ECHO("GETTING INFO FAILED, TRY AGAIN")))
    
    def READING_FILE(file_name=str):
        try:
            with open(file_name,"r",errors="replace") as file_tar:
                x_file = []
                for line_x in file_tar:
                    try:
                        ext_tar = line_x.strip()
                        x_file.append(ext_tar)
                    except:
                        pass
            return x_file
        except:
            print("%s" % (ECHO_PRINT.RED_ECHO("GETTING INFO FAILED, TRY AGAIN")))
            pass
            
    def GET_HEADER():
        try:
            list_agent = CONNECTION_OPS.USER_AGENT_LIST()
            user_agent_all = random.choice(list_agent)
            ref_ex_list = CONNECTION_OPS.READING_FILE("ref_list.txt")
            ref_all = random.choice(ref_ex_list)
            date_day = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
            date_month = ["Jan","Feb","Mar","Apr","Aug","Sep","Oct","Nov","Dec"]
            date_day_number = random.randint(1,30)
            date_year = random.randint(2000,2021)
            date_time_x = random.randint(10,23)
            date_time_y = random.randint(10,50)
            date_time_z = random.randint(10,55)
            main_header = {"User-Agent":str(user_agent_all),
                          "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                          "Connection":"Keep-Alive",
                          "Keep-Alive":"155",
                          "Content-Type":"text/html",
                          "Accept-Encoding":"gzip,deflate",
                          "Accept-Language":"en-us,en;q=0.5",
                          "Accept-Charset":"ISO-8859-1,utf-8;q=0.7,*;q=0.7",
                          "Referer":str(ref_all),
                          "Date":f"{random.choice(date_day)}, {date_day_number} {random.choice(date_month)} {date_year} {date_time_x}:{date_time_y}:{date_time_z} GMT"}
            return main_header
        except:
            print("%s" % (ECHO_PRINT.RED_ECHO("GETTING INFO FAILED, TRY AGAIN")))
            pass
        
    def REQUESTS_HEAD(target_site=str):
        global txt_target,content_target,head_target,cookies_target
        header_pois = CONNECTION_OPS.GET_HEADER()
        if "https://" in target_site or "http://" in target_site:
            sr_s = requests.Session()
            c_target = sr_s.get(target_site,verify=False,timeout=12,headers=header_pois)
            txt_target= c_target.text
            content_target = c_target.content
            head_target = c_target.headers
            cookies_target = c_target.cookies
            print("\n")
            # print(cookies_target)
            sr_s.close()
        else:
            new_url = "http://"+target_site
            sr_s = requests.Session()
            c_target = sr_s.get(new_url,verify=False,timeout=12,stream=True,headers=header_pois)
            txt_target= c_target.text
            content_target = c_target.content
            head_target = c_target.headers
            cookies_target = c_target.cookies
            print("\n")
            # print(cookies_target)
            sr_s.close()
        
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
        
    def SOCKET_NET_CONNECTION(lhost=str,lport=int,lcount=int,dsize=int,spoof_target=str):
        CONNECTION_OPS.REQUESTS_HEAD(spoof_target)
        sc_main = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        sc_main.setblocking(1)
        sc_main.bind((lhost,lport))
        sc_main.listen(lcount)
        while True:
            (inner_u,inner_add) = sc_main.accept()
            print("%s"%ECHO_PRINT.GREEN_ECHO("[+] HONEYPOT ACTIVE"))
            print("%s"%ECHO_PRINT.YELLOW_ECHO(f"CONNECTION FROM {inner_add[0]} {inner_add[1]}"))
            try:
                inner_u.send(txt_target.encode())
                response_message = inner_u.recv(dsize).decode()
                print("%s"%ECHO_PRINT.INFO_ECHO(response_message))
            except socket.error as sc_:
                print(sc_)
                CONNECTION_OPS.SEND_LOG_INFO(inner_add[0],f"ERROR: {str(sc_)}",inner_add[0],int(inner_add[1]),lport)
            else:
                CONNECTION_OPS.SEND_LOG_INFO(inner_add[0],response_message,inner_add[0],int(inner_add[1]),lport)
            finally:
                inner_u.close()
                sc_main.close()
            
    def SOCKET_HP_CONNECTION(lhost=str,lport=int,lcount=int,dsize=int):
        sc_main = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        sc_main.setblocking(1)
        sc_main.bind((lhost,lport))
        sc_main.listen(lcount)
        message_target_key = "HELLO WORLD"
        message_target = "\n"
        message_target += "HERE OUR MESSAGE"
        pass_key = MAN_F.MAIN_DECORATION(message_target_key)
        cry_key = MAN_F.PASS_CREATION(pass_key)
        while True:
            (inner_u,inner_add) = sc_main.accept()
            print("%s"%ECHO_PRINT.GREEN_ECHO("[+] HONEYPOT ACTIVE"))
            print("%s"%ECHO_PRINT.YELLOW_ECHO(f"CONNECTION FROM {inner_add[0]} {inner_add[1]}"))
            try:
                inner_u.send(cry_key)
                response_message = inner_u.recv(dsize).decode()
                print("%s"%ECHO_PRINT.INFO_ECHO(response_message))
                inner_u.send(message_target.encode())
            except socket.error as sc_:
                print(sc_)
                CONNECTION_OPS.SEND_LOG_INFO(inner_add[0],f"ERROR: {str(sc_)}",inner_add[0],int(inner_add[1]),lport)
            else:
                CONNECTION_OPS.SEND_LOG_INFO(inner_add[0],response_message,inner_add[0],int(inner_add[1]),lport)
            finally:
                inner_u.close()
                sc_main.close()
    def MAIN_OPS(target_site=str):
        my_ip_info = CONNECTION_OPS.GET_LOCAL_IP()
        print("%s"%ECHO_PRINT.GREEN_ECHO(my_ip_info))
        l_host = ATTRIBUTES_CONNECTION.LOCAL_HOST("0.0.0.0")
        l_port = ATTRIBUTES_CONNECTION.LOCAL_PORT(80)
        CONNECTION_OPS.SOCKET_NET_CONNECTION(l_host,l_port,5,1024,target_site)
        
          
if __name__ == '__main__':
    try:
        CONNECTION_OPS.MAIN_OPS()
    except Exception as err:
        print(str(err))
        pass
         
                
        
