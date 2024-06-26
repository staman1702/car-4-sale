from django.shortcuts import render


def handler403(request, exception):
    """ Custom 403 page - Forbidden """
    return render(request, 'errors/403.html', status=403)


def handler404(request, exception):
    """ Custom 404 page - Page Not Found """
    return render(request, 'errors/404.html', status=404)


def handler405(request, exception):
    """ Custom 405 page - Method Not Allowed """
    return render(request, 'errors/405.html', status=405)


def handler500(request):
    """ Custom 500 page - Internal Server Error """
    return render(request, 'errors/500.html', status=500)
