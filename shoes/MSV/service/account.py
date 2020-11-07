# các chức năng của account : register, login, changpass
#base64: chuyển đổi dữ liệu bằng cách thay thế kí tự trong bảng ASCII 8 bit thành bảng mã 6 bit
#encode : chuyển đổi dữ liệu phục vụ cho việc lưu trữ
#decode : chuyển đổi dữ liệu phục vụ cho việc sử dụng
from MSV.models.account import Account 
from MSV.exception import InvalidInput
import re
import jwt


PASSWORD_SALT = 'PASS'
#create account
def create_account (*, username: str, password : str,email: str, account_type: str) -> Account:
        check_username(username)
        check_password(password)
        check_email(email)

        account = Account.objects.filter(username=username).first()
        if account:
            return None
        account = Account(username = username, password = password, account_type =account_type, email = email )
        account.save()
        return account

def login (*, username: str, password : str) -> dict:
    account = Account.objects.filter(username=username, password = hashed_password(password)).first()
    if not account:
        raise InvalidInput("Check username or password again!")
    access_token = generate_access_token(account)
    return {
        'access_token' : access_token,
        'account':{
            'id': account.id,
            'username': account.username,
            'password': account.password,
            'account_type' : account.account_type,
            'email': account.email
        }
    }
    
def changpassword (*, account: Account, curr_pass : str, new_pass: str) -> Account :
    if account.password != hashed_password(curr_pass):
        raise InvalidInput("Wrong current pass.")
    check_password(new_pass)
    account.password= hashed_password(new_pass)
    account.save()


def generate_access_token(account: Account) -> str:
    """
    Generate JWT access token for a particular account.
    """
    access_token_payload = {
        'user_id': account.id,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(days=10),
        'iat': datetime.datetime.utcnow(),
    }
    access_token = jwt.encode(access_token_payload,
                              SECRET_KEY, algorithm='HS256').decode('utf-8')
    return access_token


def check_username(username : str) -> bool:
    if len(username) > 36 or len(username) < 6 :
        raise InvalidInput ("Username must be 6 to 36 characters long.")
    match = re.fullmatch(r'[A-Za-z0-9.]', username)
    if not match:
        raise InvalidInput ("Username must be alphanumeric")
    return True

def hashed_password(password : str) -> str:
    m = sha256()
    m.update((password + PASSWORD_SALT).encode('utf-8'))
    return m.hexdigest()


def check_password(password:str) -> bool:
    if len(password) > 36 or len(password) < 6:
        raise InvalidInput("Password must be 6 to 36 characters long")
    return True 

def check_email (email: str) -> bool:
    match = re.fullmatch(r'[\w\_\-\.]+@([\w\-]+\.)+[\w-]{2,4}', email)
    if not match:
        raise InvalidInput("Invalid email input.")
    return True



