from django.contrib.auth.models import User, Group
from .models import Question, Choice
from rest_framework import serializers

# we're using hyperlinked relations in this case with HyperlinkedModelSerializer
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']
        
class QuestionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Question
        fields = ["question_text", "pub_date", 'question_type']
     
    # Change the choice to human readable format
    def to_representation(self, instance):
        # Override to_representation to customize how the data is represented
        representation = super().to_representation(instance)
        # For each choice field get_question_type_display is generated by 
        # Django automatically
        representation['question_type'] = instance.get_question_type_display()
        return representation
          
class ChoiceSerializer(serializers.ModelSerializer):
    # we can related a choice to its foreign key objects
    question = QuestionSerializer()
    class Meta:
        model = Choice
        fields = ['choice_text', 'votes', 'question']