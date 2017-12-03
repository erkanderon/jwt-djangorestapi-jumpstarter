from rest_framework import serializers
from rest_framework.reverse import reverse
from .models import Todo



class TodoSerializer(serializers.ModelSerializer):

	

	class Meta:
		model = Todo
		#fields = ('ticker', 'volume')
		fields = ('id', 'todo_name', 'todo_owner')