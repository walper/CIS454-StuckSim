from django.urls import path 
from . import views

urlpatterns = [
	path('', views.home, name="home"), 
	path('home.html', views.home, name="dash"), #for the dashboard button path url at base.html
	path('about.html', views.about, name="about"), 
	path('add_stock.html', views.add_stock, name="add_stock"), 
	path('delete_stock.html', views.delete_stock, name="delete_stock"), 
	path('delete/<stock_id>', views.delete, name="delete"), 
	path('portfolio_check.html', views.portfolio_check, name="portfolio_check"), 
	path('help.html', views.help, name="help"), 
]
