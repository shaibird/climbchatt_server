from django.http import HttpResponseServerError
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from chattclimbapi.models import Crag



# We need to get all locations for the authenticated user, and all locations with the private property = false
# asdf

class CragView(ViewSet):
    """Crag View"""
    def retrieve(self, request, pk):
        """Handle GET requests for single crag
        
        Returns:
            Response -- JSON serialized crag
        """

        crag = Crag.objects.get(pk=pk)
        serializer = CragSerializer(crag)
        return Response(serializer.data)

    def list(self, request):
        """
        Handle GET requests to get all non-private Crags.

        If the 'exclude_user_pins' query param is present in the request URL, only return public Crags
        that are not created by the authenticated user.
        If the 'exclude_user_pins' query param is not present in the request URL, return all non-private Crags
        including the authenticated user's own private Crags.

        Returns:
            Response -- JSON serialized list of non-private Crags
        """
        crags = Crag.objects.all()
        serializer = CragSerializer(crags, many=True)
        return Response(serializer.data)



    def create(self, request):

        crag = Crag()
        crag.name = request.data['name']
        crag.city = request.data['city']
        crag.latitude = request.data['latitude']
        crag.longitude = request.data['longitude']
        crag.state = request.data['state']
        crag.country = request.data['country']
        crag.description = request.data['description']
        crag.type = request.data['type']
        crag.access = request.data['access']
        crag.private = request.data['private']
        crag.user = request.auth.user
        crag.save()

        serialized = CragSerializer(crag, many=False)

        return Response(serialized.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk=None):
        """Handle PUT requests for Crag
        
        Returns:
            nothing
        """

        crag = Crag.objects.get(pk=pk)
        crag.name = request.data['name']
        crag.city = request.data['city']
        crag.latitude = request.data['latitude']
        crag.longitude = request.data['longitude']
        crag.state = request.data['state']
        crag.country = request.data['country']
        crag.description = request.data['description']
        crag.type = request.data['type']
        crag.access = request.data['access']
        crag.private = request.data['private']
        crag.user = request.auth.user
    
    def destroy(self, request, pk=None):
        """Handle PUT requests for service tickets

        Returns:
            Response: None with 204 status code
        """
        crag = Crag.objects.get(pk=pk)
        crag.delete()
        
        return Response(None, status=status.HTTP_204_NO_CONTENT)
# class ImageSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Image
#         fields = ('id', 'image', 'Crag', 'user', 'private', 'date')
class CragSerializer(serializers.ModelSerializer):
    # images = serializers.SerializerMethodField()

    # def get_images(self, obj):
    #     images = Image.objects.filter(Crag=obj)
    #     serializer = ImageSerializer(images, many=True, context=self.context)
    #     return serializer.data
    class Meta:
        model = Crag
        fields = ('id', 'name', 'city', 'latitude', 'longitude', 'state', 'country', 'description', 'type', 'access', 'private', 'user')
    

    