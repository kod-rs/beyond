from django.db import models

from src_django.api.models.person import Person
from src_django.api.models.person import RoleChoices


class ManagerAggregator(models.Model):
    id = models.IntegerField(primary_key=True)
    manager = models.ForeignKey(Person,
                                on_delete=models.DO_NOTHING,
                                related_name='manager')
    aggregator = models.ForeignKey(Person,
                                   on_delete=models.DO_NOTHING,
                                   related_name='aggregator')

    def save(self, *args, **kwargs):
        if self.manager.role != RoleChoices.MANAGER.value:
            raise ValueError('manager field '
                             'must have a person that is a manager')
        if self.aggregator.role != RoleChoices.AGGREGATOR.value:
            raise ValueError('aggregator field '
                             'must have a person that is a aggregator')
        super(ManagerAggregator, self).save(*args, **kwargs)
