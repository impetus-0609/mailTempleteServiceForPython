from django.urls import path
from . import views

app_name = 'mails'
urlpatterns = [
    path(r'create', views.MailCreateView.as_view(), name='mail_create'),   # 作成
    path(r'complete', views.MailCompeteView.as_view(), name='mail_complete'),  # 完了
]