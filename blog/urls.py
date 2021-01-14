from django.conf.urls import url
from django.urls import path
from blog import views


app_name = "blog"
urlpatterns = [
    # path('posts/<int:post_id>/<str:rest>/', views.get_single_post),
    # path('<slug:cat_url>/', views.get_posts),
    url(r'^$', views.get_all_posts),
]


# urlpatterns = [
#     # ex: /polls/
#     path('', views.index, name='index'),
#     # ex: /polls/5/
#     path('<int:question_id>/', views.detail, name='detail'),
#     # ex: /polls/5/results/
#     path('<int:question_id>/results/', views.results, name='results'),
#     # ex: /polls/5/vote/
#     path('<int:question_id>/vote/', views.vote, name='vote'),
# ]