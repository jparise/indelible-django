from django.conf.urls.defaults import *
from django.views.generic import list_detail

from projects.models import Project

project_info_dict = {
    'queryset': Project.objects.all()
}

urlpatterns = patterns('',
    url(r'^$',
        list_detail.object_list,
        dict(project_info_dict),
        name='projects_index'),
)
