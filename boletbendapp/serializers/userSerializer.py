from boletbendapp.models.user import User
from rest_framework           import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'cedula', 'email', 'telefono', 'password', 'repassword']

    def to_representation(self, obj):#inner join
        user = User.objects.get(id=obj.id)
        return{
            'id' : user.id,
            'username' : user.username,
            'cedula' : user.cedula,
            'email' : user.email,
            'telefono' : user.phone,
        }