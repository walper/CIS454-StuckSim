from django.shortcuts import render, redirect 
from .models import Stock
from .forms import StockForm
from django.contrib import messages

# views of home templates
#pk_c5033bf2cd31462ab6d6e7599671dc27 iekcloud publishable key 


def home(request): #browser request: passing request to access home dashboard
	import requests
	import json 

	if request.method == 'POST': 
		ticker = request.POST['ticker']
		api_request = requests.get("https://cloud.iexapis.com/stable/stock/" + ticker + "/quote?token=pk_c5033bf2cd31462ab6d6e7599671dc27&period=annual")

		try: 
			api = json.loads(api_request.content)
		except Exception as e: 
			api = "Error"
		return render(request, 'home.html', {'api': api})

	else: 
		return render(request, 'home.html', {'ticker': "Please Utilize the search bar for real-time Stock Data"})


	
	#return render(request, 'home.html', {'api': api})

def about(request): #browser request: passing request to about project page
	return render(request, 'about.html', {})

def add_stock(request):
	import requests
	import json 

	if request.method == 'POST': 
		form = StockForm(request.POST or None)

		if form.is_valid():
			form.save()
			messages.success(request, ("Stock has been added to portfolio"))
			return redirect('add_stock')
		
	else:
		ticker = Stock.objects.all()
		output = []
		for item in ticker: 

			api_request = requests.get("https://cloud.iexapis.com/stable/stock/" + str(item) + "/quote?token=pk_c5033bf2cd31462ab6d6e7599671dc27&period=annual")

			try: 
				api = json.loads(api_request.content)
				output.append(api)
			except Exception as e: 
				api = "Error"

		return render(request, 'add_stock.html', {'ticker':ticker, 'output':output})

def delete(request, stock_id):
	item = Stock.objects.get(pk=stock_id)
	item.delete()
	messages.success(request, ("Stock Removed!"))
	return redirect(delete_stock)

def delete_stock(request):
	ticker = Stock.objects.all()
	return render(request, 'delete_stock.html', {'ticker':ticker})

def portfolio_check(request):
	return render(request, 'portfolio_check.html', {})

def help(request):
	return render(request, 'help.html', {})