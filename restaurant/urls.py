from django.urls import path
from .views import index,home,SingleMenuItemView,MenuItemsView

urlpatterns = [
    path('', index, name='index'),
    path('',home,name="home"),
    # path('booking/',BookingView.as_view()),
    path('menu/',MenuItemsView.as_view()),
    path('menu/<int:pk>',SingleMenuItemView.as_view()),
    # path('about/',views.about,name="about"),
    # path('book/',views.book,name="book"),
    # path('menu/',views.menu,name="menu"),
    # path('menu_item/<int:pk>/',views.display_menu_item,name="menu_item"),
]