from user import views
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^generate_token/', views.Generate_Unique_Token.as_view()),
    url(r'^assign_token/', views.Assign_Unique_Token.as_view()),
    url(r'^unblock_token/', views.Unblock_Unique_Token.as_view()),
    url(r'^delete_token/', views.Delete_Unique_Token.as_view()),
    url(r'^token_alive/', views.Token_Alive.as_view()),
    # url(r'^delete_employee/', views.Delete_Employee_Api.as_view()),
]
