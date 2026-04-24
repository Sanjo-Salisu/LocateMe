from django.shortcuts import render
import requests
from django.http import JsonResponse

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def location_view(request):
    ip = get_client_ip(request)

    res = requests.get(f"https://ipapi.co/{ip}/json/")
    data = res.json()

    return JsonResponse({
        "ip": ip,
        "city": data.get("city"),
        "region": data.get("region"),
        "country": data.get("country_name"),
        "country_code": data.get("country_code"),
        "latitude": data.get("latitude"),
        "longitude": data.get("longitude"),
        "timezone": data.get("timezone"),
        "postal": data.get("postal"),
    })

def index(request):
    return render(request, 'locate/index.html')