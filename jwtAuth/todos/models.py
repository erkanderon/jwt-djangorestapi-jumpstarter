from django.db import models

# Create your models here.




class Todo(models.Model):

    todo_name = models.CharField(max_length=100)
    todo_owner = models.CharField(max_length=100)


class TodoItem(models.Model):

    item = models.ForeignKey(Todo, related_name='list_item', on_delete=models.CASCADE)
    item_name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    duration = models.IntegerField()

    class Meta:
        unique_together = ('item', 'duration')
        ordering = ['duration']

    def __unicode__(self):
        return '%d: %s' % (self.duration, self.title)