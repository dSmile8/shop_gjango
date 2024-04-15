from django.shortcuts import render



def contacts(requests):
    if requests.method == 'POST':
        name = requests.POST.get('name')
        phone = requests.POST.get('phone')
        message = requests.POST.get('message')
        print(f'{name} / {phone} / {message}')
        data = f'Name: {name}. Phone: {phone}. Message: {message}\n'
        with open('user_data.txt', 'a', encoding='UTF-8') as f:
            f.write(data)

    return render(requests, 'catalog/contacts.html')


def home(requests):
    return render(requests, 'catalog/home.html')