from rest_framework import viewsets
from rest_framework.response import Response

class BaseViewSet(viewsets.ViewSet):
 
    
    def success_response(self, data, status_code=200):
        return Response({
            'status': 'success',
            'data': data
        }, status=status_code)
    
    def error_response(self, message, status_code=400):
        return Response({
            'status': 'error',
            'message': message
        }, status=status_code)
