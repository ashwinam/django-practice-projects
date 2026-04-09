from django.urls import path
from .views import index, detail, result, vote

urlpatterns = [
    # /polls/
    path("", index, name="index"),
    # /polls/5/
    path("<int:question_id>/", detail, name="detail"),
    # /polls/5/result/
    path("<int:question_id>/result/", result, name="result"),
    # /polls/5/vote/
    path("<int:question_id>/vote/", vote, name="vote"),
]