from django.shortcuts import render
from django.http import HttpResponse

from datetime import datetime
import json

posts = [
    {
        'name': 'Juan Pedro',
        'user': 'Peyo',
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M'),
        'pictures': 'https://i.picsum.photos/id/543/200/200.jpg?imagen=1036'
    },
    {
        'name': 'Vía láctea',
        'user': 'C. Vander',
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M'),
        'pictures': 'https://i.picsum.photos/id/543/200/200.jpg?imagen=903'
    },
    {
        'name': 'Auditorio',
        'user': 'Otro',
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M'),
        'pictures': 'https://i.picsum.photos/id/543/200/200.jpg?imagen=1076'
    }
]

def list_posts(request):
    content = []

    for post in posts:
        content.append(f"""
            <p><strong>{post['name']}</strong></p>
            <p><small>{post['user']} - <i>{post['timestamp']}</i></small></p>
            <figure><img src="{post['pictures']}"</figure>
        """)
    return HttpResponse('<br>'.join(content))