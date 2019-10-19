from django.apps import apps
from rest_framework.filters import SearchFilter
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_flex_fields import FlexFieldsModelViewSet
from saleor.rest.serializers import TaskResultSerializer


__all__ = [
    'TaskResultViewSet',
]

TaskResult = apps.get_model(*'django_celery_results.TaskResult'.split())


class TaskResultViewSet(FlexFieldsModelViewSet):
    """ViewSet for :model:`django_celery_results.TaskResult`

    `** Actions **`:

    create:
    Create a new `django_celery_results.TaskResult` instance.

    retrieve:
    Return the given `django_celery_results.TaskResult`.

    update:
    Update the given `django_celery_results.TaskResult`..

    delete:
    Delete the given `django_celery_results.TaskResult`, and return an empty response
    with HTTP 204 status code.

    list:
    Return a list of all the existing :model:`TaskResult`.
    """

    lookup_field = 'id'
    queryset = TaskResult.objects.all()
    serializer_class = TaskResultSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter, ]
    filter_fields = [
        # Fields
        # 'content_encoding',
        # 'content_type',
        # 'date_done',
        # 'hidden',
        # 'id',
        # 'meta',
        # 'result',
        # 'status',
        # 'task_args',
        # 'task_id',
        # 'task_kwargs',
        # 'task_name',
        # 'traceback',

        # Reverse Fields
    ]
    search_fields = [
        # Fields
        # 'content_encoding',
        # 'content_type',
        # 'date_done',
        # 'hidden',
        # 'id',
        # 'meta',
        # 'result',
        # 'status',
        # 'task_args',
        # 'task_id',
        # 'task_kwargs',
        # 'task_name',
        # 'traceback',

        # Reverse Fields
    ]
    ordering_fields = [
        # Fields
        # 'content_encoding',
        # 'content_type',
        # 'date_done',
        # 'hidden',
        # 'id',
        # 'meta',
        # 'result',
        # 'status',
        # 'task_args',
        # 'task_id',
        # 'task_kwargs',
        # 'task_name',
        # 'traceback',

        # Reverse Fields
    ]
    # '__all__'

    # def get_object(self):
    #     return super().get_object()

    # def create(self, request, *args, **kwargs):
    #     return super().create(request, *args, **kwargs)

    # def retrieve(self, request, *args, **kwargs):
    #     return super().retrieve(request, *args, **kwargs)

    # def update(self, request, *args, **kwargs):
    #    return super().update(request, *args, **kwargs)

    # def destroy(self, request, *args, **kwargs):
    #     return super().destroy(request, *args, **kwargs)

    # def list(self, request, *args, **kwargs):
    #     return super().list(request, *args, **kwargs)
