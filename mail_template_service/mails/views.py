from django.shortcuts import render
from django.views.generic import CreateView, TemplateView
from .models import Employee
from .forms import MailCreateForm


class MailCreateView(CreateView):
    form_class = MailCreateForm
    model = Employee
    template_name = 'mail_create.html'
    success_url = 'mail_complete.html'

    def post(self, request, *args, **kwargs):
        # 送信ボタン押下
        print('★ 送信ボタン押下 ★')
        return render(request, self.success_url)


class MailCompeteView(TemplateView):
    # 完了画面
    template_name = 'mail_complete.html'
