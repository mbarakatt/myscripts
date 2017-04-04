from goose import Goose
from django.utils.encoding import smart_str, smart_unicode
import sys

url = sys.argv[1]

g = Goose({'browser_user_agent': 'Mozilla'})
article = g.extract(url=url)
print "Title", article.title
print "Text", smart_str(article.cleaned_text)


