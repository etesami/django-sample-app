from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import UserSerializer, GroupSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    # authentication_classes = (JSONWebTokenAuthentication, )
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]




from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.decorators import permission_classes
from rest_framework.decorators import authentication_classes
from rest_framework.authentication import BasicAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication

from .models import Question, Choice
from .serializers import QuestionSerializer, ChoiceSerializer

@api_view(['GET', 'POST'])
@authentication_classes([JWTAuthentication, BasicAuthentication])
@permission_classes([permissions.IsAuthenticated])
# @permission_classes([permissions.IsAdminUser])
# @permission_classes([permissions.IsAuthenticatedOrReadOnly])
def hello_world(request):
    if request.method == 'POST':
        return Response({"message": "Got some data!", "data": request.data})
    
    # questions = Question.objects.all()
    # serializer = QuestionSerializer(questions, many=True)
    
    choices = Choice.objects.all()
    serializer = ChoiceSerializer(choices, many=True)
    
    return Response(serializer.data)
    # return Response({"message": "Hello, world!"})
    
    
