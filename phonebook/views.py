from django.shortcuts import render, redirect
from phonebook.models import PhoneBook
from django.http import HttpResponse

# Create your views here.
def index(request):
    # 모델클래스.objects.values('컬럼명') : 컬럼명의 데이터만 조회
    # 모델클래스.objects.all() : 전체 데이터 조회
    # 모델클래스.objects.values().get(pk = 1) : 조건에 해당하는 데이터만 조회
    # pk : primary key - 컬럼 중에 유일한 값을 가진 칼럼
    alluser = PhoneBook.objects.values('id', '이름', '전화번호')
    content = {
        "phonebook" : alluser
    }
    return render(request, 'phonebook/index.html', content)

def add(request):
    # request method : get, post 구분 가능
    if request.method == 'GET':
        if request.user.username != "":
            return render(request, 'phonebook/add.html')
        else:
            return render(request, 'error/erroraccess.html')
    elif request.method == "POST":
        # POST로 전달한 값 : name, telnum, address, email, birth
        name = request.POST.get("name")
        telnum = request.POST.get("telnum")
        email = request.POST.get("email")
        address = request.POST.get("address")
        birth = request.POST.get("birth")
        author = request.user.username;

        phonebook = PhoneBook()
        phonebook.이름 = name
        phonebook.전화번호 = telnum
        phonebook.이메일 = email
        phonebook.주소 = address
        phonebook.생년월일 = birth
        phonebook.작성자 = author
        # DB 저장 : 객체.save()
        phonebook.save()
        return redirect('PB:I')

def detail(request, userId):
    content = {
        "userInfo" : PhoneBook.objects.get(id=userId)
    }
    return render(request, 'phonebook/detail.html', content)

def delete(request, userId):
    # DB 삭제 : 클래스객체.objects.get(pk=값).delete()
    phonebook = PhoneBook.objects.get(id=userId)
    name = phonebook.이름
    content = {
        "userId" : userId,
        "name" : name,
    }
    phonebook.delete()
    return render(request, 'phonebook/delete.html', content)

def update(request, userId):
    userInfo = PhoneBook.objects.get(id=userId)
    if request.method == "GET":
        if request.user.username != "":
            if userInfo.작성자 == request.user.username:
                content = {
                    "userInfo" : userInfo,
                }
                return render(request, 'phonebook/update.html', content)
            else:
                return render(request, 'error/erroraccess.html')
        else:
            return render(request, 'error/erroraccess.html')
    elif request.method == "POST":
        # 첫번째 : 기존에 있던 데이터를 가지고 와서 수정
        # phonebook = PhoneBook.objects.get(id=userId)
        # phonebook.이름 = request.POST.get("name")
        # phonebook.전화번호 = request.POST.get("telnum")
        # phonebook.이메일 = request.POST.get("email")
        # phonebook.주소 = request.POST.get("address")
        # phonebook.생년월일 = request.POST.get("birth")
        # phonebook.save()

        # 두번째 : 새로운 객체를 생성하고 id를 기존 id를 저장하면 덮어쓰기가 된다.
        phonebook = PhoneBook()
        phonebook.id = userId
        phonebook.이름 = request.POST.get("name")
        phonebook.전화번호 = request.POST.get("telnum")
        phonebook.이메일 = request.POST.get("email")
        phonebook.주소 = request.POST.get("address")
        phonebook.생년월일 = request.POST.get("birth")
        phonebook.작성자 = request.user.username
        phonebook.save()

        return redirect('PB:I')