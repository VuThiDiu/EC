
#http://127.0.0.1:8000/api/account/login

from django.urls import path, include
from MSV.view.account import LoginView


account_patterns =[
    path('login', LoginView.as_view())
]


urlpatterns =[
    path('account/', include((account_patterns, 'account'))),
]