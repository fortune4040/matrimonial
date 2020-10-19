from rest_framework import serializers
from .models import Profile,ProfileImage


class ImageSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)

    class Meta:
        model = ProfileImage
        fields = [
            'id',
            'profile',
            'image',
        ]
        read_only_fields = ('profile',)


class ProfileSerializers(serializers.ModelSerializer):
    images = ImageSerializer(many=True)

    class Meta:
        model = Profile
        fields = '__all__'
        extra_fields = ['images']

    def create(self, validated_data):
        # print(validated_data)
        images = validated_data.pop('images')
        # print(images)
        profile = Profile.objects.create(**validated_data)
        for image in images:
            ProfileImage.objects.create(**image, profile=profile)
        return profile


