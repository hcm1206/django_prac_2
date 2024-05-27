from django.db import models
# Create your models here.

# DB 연동 클래스
class PhoneBook(models.Model):
    # 컬럼명은 영어로 사용하는게 기본
    # CharField() : 문자열
    # max_length=최대길이 : 문자열의 최대 길이
    # null=False : 입력을 반드시 해야 함
    # null=True 또는 생략 : 입력을 받느시 하지 않아도 됨
    # EmailField() : 이메일 형식으로 값이 입력되어야 함
    # DateField() : 날짜 형식
    이름 = models.CharField(max_length=50, null=False)
    전화번호 = models.CharField(max_length=15)
    이메일 = models.EmailField()
    주소 = models.CharField(max_length=100)
    생년월일 = models.DateField()
    작성자 = models.CharField(max_length=50)

    def __str__(self):
        return f"객체이름 : {self.이름}"
