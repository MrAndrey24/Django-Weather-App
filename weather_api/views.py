import requests
from django.conf import settings
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


# Create your views here.
@api_view(['GET'])
def get_weather(request, city):
    if not city:
        return Response({'error': 'City cannot be empty'}, status=status.HTTP_400_BAD_REQUEST)

    try:
        api_url = f"{settings.BASE_URL}{city}?unitGroup=metric&key={settings.API_KEY}&contentType=json"
        response = requests.get(api_url)

        if response.status_code != 200:
            return Response({'error': 'Failed to fetch data from the weather API'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        data = response.json()
        return Response({
            'city': data.get('address'),
            'temperature': data.get('currentConditions', {}).get('temp'),
            'humidity': data.get('currentConditions', {}).get('humidity'),
            'description': data.get('currentConditions', {}).get('conditions'),
            'icon': data.get('currentConditions', {}).get('icon'),
        }, status=status.HTTP_200_OK)

    except requests.RequestException as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)