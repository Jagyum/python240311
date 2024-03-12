import re

def check_email(email):
    # 이메일 주소 형식에 맞는지 정규식으로 체크
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if re.search(pattern, email):
        return True
    else:
        return False

# 샘플 데이터 생성
sample_emails = [
    "example@example.com",
    "user123@example.com",
    "john.doe@example.co.uk",
    "alice_123@example.co.jp",
    "testuser1234@test.co.in",
    "invalid.email@",
    "invalid.email@com",
    "invalidemail.com",
    "not.an.email@domain",
    "12345@67890"
]

# 샘플 데이터의 이메일 주소 체크
for email in sample_emails:
    if check_email(email):
        print(f"{email}: Valid")
    else:
        print(f"{email}: Invalid")
