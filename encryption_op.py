import socket,json,os,hashlib,mmh3,random
import base64 as b64
from itertools import count, product

class ENC_PARAMETERS():
    def NUMBER_LIST():
        numbers_list_int = [1,2,3,4,5,6,7,8,9,0]
        numbers_list_str = ["2","3","4","5","6","7","8","9"]
        return numbers_list_int,numbers_list_str
    def WORD_LIST():
        word_list = ["a","b","c","d","e",
                     "f","g","h","i","j","k",
                     "l","m","n","o","p","r",
                     "s","t","u","v","y","z","w","x","q"]
        vowels_list = ["a","e","i","u","o"]
        return word_list,vowels_list
    def SYMBOL_LIST():
        symbol_list = ["!","'","%","+","&","/",
                       "(",")","=","?","*","-","#",
                       "<",">","{","}",":",".",",","[","]"]
        return symbol_list
    def NUMBER_PLAIN():
        number_plain = "23456789"
        return number_plain
    def WORD_PLAIN():
        word_plain = "abcdefghijklmnoprstuvyzwxq"
        return word_plain
    def SYMBOL_PLAIN():
        symbol_plain = "!'+%&/()=?*-#<>{}[]:.,"
        return symbol_plain


class READING_MESSAGE():
    def GETTING_DOC_AS_LIST(target_dir=str):
        read_f = open(target_dir,"r",errors="replace")
        com_list = []
        for line_st in read_f:
            ex_tar = line_st.strip()
            com_list.append(ex_tar)
        return com_list
    def GETTING_DOC_DIRECTLY(target_dir=str):
        open_f = open(target_dir,"r",errors="replace")
        read_f = open_f.read()
        return read_f
    
    
class ENCRYPTION_OPS():
    def B64_TYPE(target_plain=str):
        enc_64 = b64.b64encode(target_plain.encode())
        return enc_64.decode()
    def MD5_B_2_B(target_plain=str):
        md5_byte_to_byte = hashlib.md5(bytes(target_plain,encoding="utf-8"))
        return md5_byte_to_byte.digest()
    def MD5_S_2_B(target_plain=str):
        md5_byte_to_string = hashlib.md5(bytes(target_plain,encoding="utf-8"))
        return md5_byte_to_string.hexdigest()
    def MMH_32(target_plain=str):
        b_32 = mmh3.hash(target_plain,signed=False)
        return b_32
    def MMH_128(target_plain=str):
        b_128 = mmh3.hash128(target_plain,signed=False)
        return b_128
    def MMH_B(target_plain=str):
        b_b = mmh3.hash_bytes(target_plain)
        return b_b
    
class MANUAL_ENCRYPTION():
    def B64_DECORATION(target_plain=str):
        b64_e = ENCRYPTION_OPS.B64_TYPE(target_plain)
        return b64_e
    def B64_ENC(target_b64):
        decry_plain = b64.b64decode(target_b64)
        return decry_plain
    def PASS_CREATION(target_pass=str):
        new_pass = ""
        get_plain_symbol = ENC_PARAMETERS.SYMBOL_PLAIN()
        get_plain_word = ENC_PARAMETERS.WORD_PLAIN()
        get_plain_number = ENC_PARAMETERS.NUMBER_PLAIN()
        get_list_symbol = ENC_PARAMETERS.SYMBOL_LIST()
        get_list_word,get_list_vowel = ENC_PARAMETERS.WORD_LIST()
        reverse_list_word = list(reversed(get_list_word))
        get_list_number,get_str_number = ENC_PARAMETERS.NUMBER_LIST()
        split_pass = list(target_pass)
        for x_count,x_pass in enumerate(split_pass):
            try:
                if x_pass.lower() in get_list_vowel:
                    chr_pass = ord(x_pass)
                    p_define = f"{0}0.00.{chr_pass}{0}0.00.{reverse_list_word[x_count]}.{get_list_symbol[x_count]}{reverse_list_word[x_count]}"
                    new_pass += p_define
                    new_pass += get_plain_word [-x_count]
                    new_pass += get_plain_number [-x_count]
                    new_pass += get_plain_symbol [-x_count]
                else:
                    chr_pass = ord(x_pass)
                    p_define = f"{1}1.11.{chr_pass}{1}1.11.{reverse_list_word[x_count]}.{get_list_symbol[x_count]}{reverse_list_word[x_count]}"
                    new_pass += p_define
                    new_pass += get_plain_word [-x_count]
                    new_pass += get_plain_number [-x_count]
                    new_pass += get_plain_symbol [-x_count]
            except:
                pass
        return new_pass

    def MAIN_DECORATION(target_plain=str):
        main_key = "" 
        get_list_word,get_list_vowel = ENC_PARAMETERS.WORD_LIST()
        for x_plain in target_plain:
            if x_plain in get_list_vowel:
                pass
            else:
                main_key += x_plain
        return main_key
        
    def MAIN_CRACKING(target_pass=str):
        get_pass_one = ""
        get_pass_zero = ""
        get_list_word,get_list_vowel = ENC_PARAMETERS.WORD_LIST()
        get_list_number,get_str_number = ENC_PARAMETERS.NUMBER_LIST()
        dot_1_target = target_pass.split("11.11.")
        dot_0_target = target_pass.split("00.00.")
        for x_lane in range(len(dot_1_target)):
            if (x_lane % 2) == 0:
                pass
            else:
                cry_else = chr(int(dot_1_target[x_lane]))
                get_pass_one += cry_else
                
        for x_lane in range(len(dot_0_target)):
            if (x_lane % 2) == 0:
                pass
            else:
                cry_else = chr(int(dot_0_target[x_lane]))
                get_pass_zero += cry_else     
        return get_pass_one,get_pass_zero
        
        
       





        
