from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse
# Create your views here.

def IndexView(request):
    stock_list = ['Google, GOOGL','Amazon, AMZN','Tesla, TSLA', 'S&P500, SPX', 'Dow Jones, DJI','Nasdaq, NDAQ']
    currency_list = ['EUR','USD','GBP','JPY','CHF','RON','PLN']

    if request.method == 'POST':
        try:
            balance = request.POST.get('balance')        # formula: (balance*risk / 100) / stoploss
            risk = request.POST.get('risk')
            stoploss = request.POST.get('stoploss')
            stock = request.POST.get('stock')

            risk_value = (int(balance) * int(risk)) / 100
            result = round(risk_value / int(stoploss))

            return ResultView(request,result,stock)
        except:
            return HttpResponse("Missing Values")


    return render(request, 'calculator/index.html', {'stock_list':stock_list, 'currency_list':currency_list})

class AboutView(TemplateView):
    template_name = 'calculator/about.html'

def ResultView(request, result, stock):
    return render(request, 'calculator/result.html', {'result': result,'stock':stock} )
