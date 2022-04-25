from django.urls import path
from . import views
from .views import (
    Sell_page,
    sellcategorie,
	GraphicCardsList, 
	GraphicDetail,
	GraphicCreateView,
    GraphicUpdate,
    GraphicDelete,
    MonitorsList, 
    MonitorsDetail,
    MonitorsCreateView)

urlpatterns = [
    path('sellcategorie/', views.sellcategorie, name='blog-sellcategorie'),
    path('Products/Sell/', views.Sell_page, name='sell'),
    path('GraphicCardsList', GraphicCardsList.as_view(), name='graphic-cards'),
    path('GraphicDetail/<int:pk>/', GraphicDetail.as_view(), name='graphic-cards-detail'),
    path('GraphicCreateView/new/', GraphicCreateView.as_view(), name='graphic-cards-create'),
    path('GraphicUpdate/<int:pk>/update/', GraphicUpdate.as_view(), name='graphic-cards-update'),
    path('GraphicDelete/<int:pk>/delete/', GraphicDelete.as_view(), name='graphic-cards-delete'),
    path('MonitorsList', MonitorsList.as_view(), name='blog-monitors'),
    path('MonitorsDetail/<int:pk>/', MonitorsDetail.as_view(), name='Monitors-detail'),
    path('MonitorsCreateView/new/', MonitorsCreateView.as_view(), name='Monitors-create'),
    ]