from django.urls import path
from lectures.views import lecture_detail_view
# from lectures.views import lecture_create_view
from lectures.views import dynamic_lookup_view
# from lectures.views import lecture_delete_view
from lectures.views import lecture_list_view
from lectures.views import lecture_search_view

app_name = 'lectures'

urlpatterns = [
    path('', lecture_detail_view, name='lecture'),
    # path('create/', lecture_create_view, name='product_create'),
    path('<int:id>/', dynamic_lookup_view, name='lecture_detail'),
    # path('<int:id>/delete/', lecture_delete_view, name='lecture_delete'),
    path('list/', lecture_list_view, name='lecture_list'),
    path('search/', lecture_search_view, name='lecture_search'),
]