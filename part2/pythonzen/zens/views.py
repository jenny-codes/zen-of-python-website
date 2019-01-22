from django.http import HttpResponse
from zens.models import Quote
from random import random

# for importing the quotes file
import os
from django.conf import settings

def index(request):

	# import the quotes to the database first if not yet initialized
	if Quote.objects.count() == 0:
		file = open(os.path.join(settings.BASE_DIR, 'quotes.txt'), 'r')
		for line in file:
			print(line)
			Quote.objects.create(text=line)

	count = Quote.objects.count()
	index = round(random() * 100) % count - 1
	display_quote = Quote.objects.get(id=index)

	return HttpResponse("%s" % display_quote.text)