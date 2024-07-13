from django.http import HttpResponse
title = "Hello, world!"

HTML_STRING = f"""
<html>
    <head>
        <title>{title}</title>
    </head>
    <body>
        <h1>{title}</h1>
        <p>This is a paragraph.</p>
    </body>
</html>
"""

def home_view(request):
    return HttpResponse(HTML_STRING)
