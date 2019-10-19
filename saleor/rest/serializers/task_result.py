from django.apps import apps
from rest_flex_fields import FlexFieldsModelSerializer

__all__ = [
    'TaskResultSerializer',
]

TaskResult = apps.get_model(*'django_celery_results.TaskResult'.split())


class TaskResultSerializer(FlexFieldsModelSerializer):
    """Serializer for :model:`django_celery_results.TaskResult`:

    `**Fields:**`
        01. `content_encoding`            : `CharField`
        02. `content_type`                : `CharField`
        03. `date_done`                   : `DateTimeField`
        04. `hidden`                      : `BooleanField`
        05. `id`                          : `AutoField`
        06. `meta`                        : `TextField`
        07. `result`                      : `TextField`
        08. `status`                      : `CharField`
        09. `task_args`                   : `TextField`
        10. `task_id`                     : `CharField`
        11. `task_kwargs`                 : `TextField`
        12. `task_name`                   : `CharField`
        13. `traceback`                   : `TextField`

    `**Reverse Fields:**`
    """
    class Meta:
        model = TaskResult
        fields = [
            # Fields
            'content_encoding',
            'content_type',
            'date_done',
            'hidden',
            'id',
            'meta',
            'result',
            'status',
            'task_args',
            'task_id',
            'task_kwargs',
            'task_name',
            'traceback',

            # Reverse Fields
        ]
        read_only_fields = []

    # def create(self, validated_data):
    #     return super().create(validated_data)

    # def update(self, instance, validated_data):
    #     return super().update(instance, validated_data)
