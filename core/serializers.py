from rest_framework.serializers import ModelSerializer

from core.models import User

class UserSerializer(ModelSerializer):
    class Meta:
        model=User
        field = ["id","first_name","last_name","email","password"]