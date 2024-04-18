from rest_framework.response import Response
from rest_framework.views import APIView



class RootView(APIView):
    # permission_classes = (IsAuthenticated, )
    
    def get(self, request):
        content = {'message': 'Aljarrash Backend!'}
        return Response(content)