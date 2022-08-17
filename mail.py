
import secrets
from random import choice, randint
from string import ascii_lowercase, ascii_letters, digits


def get_mail(n_num: int = 4, n_char: int = 3):
    name = ['khang', 'thien', 'tuong', 'duc', 'dung', 'duy', 'hoang', 'khai', 'khoa', 'khoi', 'minh', 'quan', 'quoc', 'son', 'tai', 'thai', 'tuan', 'tung', 'viet',
                 'cuong', 'loc', 'long', 'phuoc', 'thanh', 'thinh', 'thuc', 'truc', 'nhan', 'bao', 'giang', 'hien', 'hoa', 'huy', 'huynh', 'khanh', 'thach', 'tin', 'toan', 'dat', 'thuan']
    random_number = str(randint(10**(n_num-1), (10**n_num)-1))
    random_mail_provider = "@gmail.com"
    random_name = choice(name)
    random_char = "".join(choice(ascii_lowercase) for _ in range(n_char))

    return random_name + random_char + random_number + random_mail_provider

def get_pass(n: int = 10, is_punctuation: bool = True):
    if is_punctuation:
        punctuation = "!#$%&()*+,-.:?@_~"
        alphabet = ascii_letters + digits + punctuation
        while True:
            password = ''.join(secrets.choice(alphabet) for i in range(n))
            if (any(c.islower() for c in password)
                    and any(c.isupper() for c in password)
                    and any(c.isalnum() for c in password)
                    and sum(c in punctuation for c in password) < 3):
                break
    else:
        alphabet = ascii_letters + digits
        while True:
            password = ''.join(secrets.choice(alphabet) for i in range(10))
            if (any(c.islower() for c in password)
                    and any(c.isupper() for c in password)
                    and any(c.isdigit() for c in password)):
                break
    return password