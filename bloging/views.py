from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from pytils.translit import slugify
from bloging.models import Blog
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import smtplib

smtp_server = smtplib.SMTP("smtp.yandex.ru", 587)  # Введите свои данные/настройки
smtp_server.starttls()
smtp_server.login("sender email", "your password")  # Введите свои данные/настройки

msg = MIMEMultipart()
msg["From"] = "sender email"  # Введите свои данные/настройки
msg["To"] = "recipient email"  # Введите свои данные/настройки
msg["Subject"] = "Тестовое письмо от Django"  # Введите свои данные/настройки

text = "Привет! Это тестовое письмо, отправленное с помощью Python-Django"
msg.attach(MIMEText(text, "plain"))


class BlogListView(ListView):
    model = Blog

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset().order_by(*args, **kwargs)
        queryset = queryset.filter(is_published=True)
        return queryset


class BlogDetailView(DetailView):
    model = Blog

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.view_count += 1
        if self.object.view_count == 100:
            # Введите свои данные/настройки
            smtp_server.sendmail("sender email", "recipient email", msg.as_string())
            smtp_server.quit()
        self.object.save()
        return self.object


class BlogCreateView(CreateView):
    model = Blog
    fields = ('title', 'body', 'image', 'is_published',)
    success_url = reverse_lazy('bloging:list')

    def form_valid(self, form):
        if form.is_valid():
            new_blog = form.save()
            new_blog.slug = slugify(new_blog.title)
            new_blog.save()

        return super().form_valid(form)


class BlogUpdateView(UpdateView):
    model = Blog
    fields = ('title', 'body', 'image',)

    def get_success_url(self):
        return reverse('bloging:detail', args=[self.kwargs.get('pk')])


class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy('bloging:list')
