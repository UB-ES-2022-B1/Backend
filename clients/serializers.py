from rest_framework import serializers

from clients.models import Client


class RegistrationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Client
        fields = ['email','name','surname','password','phone', 'birthdate','country','failedLoginAttemps']

    def save(self):
        user = Client(email=self.validated_data['email'], birthdate=self.validated_data['birthdate'],name=self.validated_data['name'], phone=self.validated_data['phone'],surname=self.validated_data['surname'], country=self.validated_data['country'])
        password = self.validated_data['password']
        user.set_password(password)
        user.save()

        return user


class PasswordChangeSerializer(serializers.Serializer):
    current_password = serializers.CharField(style={"input_type": "password"}, required=True)
    new_password = serializers.CharField(style={"input_type": "password"}, required=True)

    def validate_current_password(self, value):
        if not self.context['request'].user.check_password(value):
            raise serializers.ValidationError({'current_password': 'Does not match'})
        return value

