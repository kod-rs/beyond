from django.http import JsonResponse
from rest_framework.views import APIView


class IndexView(APIView):

    def get(self, request):
        response = {
            "auth": {
                "status": True,
                "access-token": request.access_token,
                "refresh-token": request.refresh_token
            },
            "payload": {
                "page": "index"
            }
        }

        return JsonResponse(response)

# todo write custom auth
# https://docs.djangoproject.com/en/4.0/topics/auth/customizing/


# class Person(models.Model):
#     username = models.CharField(max_length=200)
#     password = models.CharField(max_length=200)
#
#
# class PersonSerializer(serializers.Serializer):
#     username = serializers.CharField(max_length=200)
#     password = serializers.CharField(max_length=200)
#
#     def create(self, validated_data):
#         """
#         Create and return a new `Snippet` instance, given the validated data.
#         """
#         return Person.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         """
#         Update and return an existing `Snippet` instance, given the validated data.
#         """
#         instance.username = validated_data.get('username', instance.username)
#         instance.password = validated_data.get('password', instance.password)
#
#         instance.save()
#         return instance


