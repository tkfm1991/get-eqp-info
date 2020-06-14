from ntc_templates.parse import parse_output
from pprint import pprint
import telnetlib


class Command(object):
    def __init__(self, HOST):
        
        self.host = {
            'hostname': HOST['hostname'],
            'ip': HOST['ip'],
            'username': HOST['username'],
            'password': HOST['password'],
            'secret': HOST['secret'],
            'login_id_text': HOST['login_id_text'],
            'login_pw_text': HOST['login_pw_text'],
            'enable_pw_text': HOST['enable_pw_text'],
        }
        print('\n--- host data ---')
        print(self.host)

    def login(self):
        print('\n--- login ---')
        port = 23
        timeout = 10

        # TELNET接続
        tn = telnetlib.Telnet(self.host['ip'], port, timeout)

        # ログインID入力
        print(tn.read_until(self.host['login_id_text'].encode()))
        cmd = (self.host['username'] + '\n').encode()
        print(cmd)
        tn.write(cmd)
        # パスワード入力
        print(tn.read_until(self.host['login_pw_text'].encode()))
        cmd = (self.host['password'] + '\n').encode()
        print(cmd)
        tn.write(cmd)
        
        # print(tn.read_until(b'$'))
        tn.read_until(b'$')
        return(tn)

    def enable(self):
        pass

    def configure(self):
        pass

    def input_command_byte(self, tn, cmd):
        """コマンド入力(byte型)"""
        # プロンプトは動作モードにより変化するため、現在の動作モードも変数で管理する
        print('\n--- input_command ---')
        print('input-> ', cmd)
        tn.write(cmd.encode())
        tn.write(b'\n')
        result = tn.read_until(b'$') # プロンプトも変数にする
        return result


