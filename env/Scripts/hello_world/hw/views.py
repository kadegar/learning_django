# Create your views here.
from django.http import HttpResponse
from django.template import Context, loader
from datetime import datetime

def hello_view(request):
	return HttpResponse('<html><body>Hello, World!</body></html>')

def better_hello(request):
	t=loader.get_template('betterhello.html')
	c=Context({'current_time':datetime.now(),})
	return HttpResponse(t.render(c))

def about(request):
	return HttpResponse('''
		<html>
		<body>
		About this app: This app is really not very sophisticated...
		</body>
		</html>
		''')