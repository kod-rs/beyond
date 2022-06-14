from django.views.generic import TemplateView
from django.views.decorators.cache import never_cache
from rest_framework import viewsets

from .models import Message, MessageSerializer

# Serve Vue Application
index_view = never_cache(TemplateView.as_view(template_name='index.html'))


class MessageViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows messages to be viewed or edited.
    """
    queryset = Message.objects.all()
    serializer_class = MessageSerializer


from .models import Person

class TmpViewSet(viewsets.ModelViewSet):

    queryset = Person.objects.all()

    print("tmp view called")
    # print(queryset)
    serializer_class = MessageSerializer


