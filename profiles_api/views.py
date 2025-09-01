from rest_framework.views import APIView
from rest_framework.response import Response 


class HelloApiView(APIView):
    """test API View"""

    def get(self, request, format=None):
        """returns a list of ApiView features"""
        an_apiview = [
        'uses HTTP methods as functions (get , post , patch, put, delete)'
        'is similiar to a traditional django view',
        'gives you the most control over you application logic ',
        'Is mapped manually to urls'
        ]

        return Response({'message': 'Hello', 'an_apiview': an_apiview})