#!/usr/local/var/pyenv/shims/python3
from ntc_templates.parse import parse_output
from pprint import pprint
import command


def main():
    print('=== main ===')

    device = {
        'hostname': 'myComputer',
        'ip': '***.***.***.***',
        'username': '***',
        'password': '***',
        'secret': '***',
        'login_id_text': 'login:',
        'login_pw_text': 'Password:',
        'enable_pw_text': 'Password:',
    }

    TARGET = command.Command(device)
    tn = TARGET.login()
    result = TARGET.input_command_byte(tn, 'ifconfig')
    #print(result)
    parsed = parse_output(platform="ubuntu", command="ifconfig", data=result.decode())
    pprint(parsed)

    tn.close()
    print('=== main end ===')


if __name__ == "__main__":
    main()