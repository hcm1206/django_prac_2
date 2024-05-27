from django.contrib import admin
from border.models import Border, Reply

# Register your models here.
class BorderAdmin(admin.ModelAdmin):
    list_display = ('id', '제목', '작성자', '조회수')

class ReplyAdmin(admin.ModelAdmin):
    list_display = ('border_id', '작성자', '내용')

admin.site.register(Border, BorderAdmin)
admin.site.register(Reply, ReplyAdmin)