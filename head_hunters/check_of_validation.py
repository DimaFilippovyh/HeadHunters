from django.http import Http404


def check_object_owner(object, request):
    if object.owner != request.user:
        raise Http404
