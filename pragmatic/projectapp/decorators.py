from django.contrib.auth.models import User
from django.http import HttpResponseForbidden

from profileapp.models import Profile
from projectapp.models import Project


def project_ownership_required(func):
    def decorated(request, *args, **kwargs):
        project = Project.objects.get(pk=kwargs['pk'])
        if not project.user == request.user:
            return HttpResponseForbidden()
        return func(request, *args, **kwargs)
    return decorated