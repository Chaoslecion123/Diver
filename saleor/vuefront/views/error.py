from django.views.generic import TemplateView


def bad_request(request, *args, **kwargs):
    view = TemplateView.as_view(template_name="app.html")
    response = view(request, *args, **kwargs)
    response.status_code = 400
    return response


def forbidden(request, *args, **kwargs):
    view = TemplateView.as_view(template_name="app.html")
    response = view(request, *args, **kwargs)
    response.status_code = 403
    return response


def not_found(request, *args, **kwargs):
    view = TemplateView.as_view(template_name="app.html")
    response = view(request, *args, **kwargs)
    response.status_code = 404
    return response


def server_error(request, *args, **kwargs):
    view = TemplateView.as_view(template_name="app.html")
    response = view(request, *args, **kwargs)
    response.status_code = 500
    return response
