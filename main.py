from string import digits, punctuation, ascii_letters
import subprocess
import itertools
import requests

def brute_excel_doc():
    try:
        password_length = input("start, end --> ")
        password_length = [int(item) for item in password_length.split("-")]
    except:
        print("error start, end !!!")

    print("1 - numerik\n2 - alpavit\n3 - numerik and alphabit")

    try:
        choice = int(input(":  "))
        if choice == 1:
            possible_symbol = digits

        elif choice == 2:
            possible_symbol = ascii_letters
        
        elif choice == 3:
            possible_symbol = digits + ascii_letters

        elif choice == 4:
            possible_symbol = digits + ascii_letters + punctuation
        else:
            possible_symbol = "Ow no ...."

    except:
        print("error")

    for pass_length in range(password_length[0], password_length[1] + 1):
        for password in itertools.product(possible_symbol, repeat=pass_length):
            password = "".join(password)
            return password

def xacking(iter_password: str):
    url = "http://127.0.0.1:8000/admin/login/?next=/admin/"
    data = {
        "username":"Akromjon",
        "password":"2007"
    }
    response = requests.get(url,params=data)
    print(response.status_code)
    print(response.content)

def main():
    # iteration = brute_excel_doc()
    xacking('')


if __name__ == '__main__':
    import os

    from django.core.asgi import get_asgi_application

    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

    application = get_asgi_application()

    main()