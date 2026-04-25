from django.shortcuts import render
import requests
import requests
from django.http import JsonResponse

def location_view(request):
    ip = request.META.get('HTTP_X_FORWARDED_FOR', request.META.get('REMOTE_ADDR'))
    ip = ip.split(',')[0] if ip else None

    url = f"https://ipinfo.io/{ip}/json"

    try:
        response = requests.get(url, timeout=5)

        # 👇 check if response is valid
        if response.status_code != 200:
            return JsonResponse({"error": "API failed", "status": response.status_code})

        data = response.json()

    except requests.exceptions.RequestException:
        return JsonResponse({"error": "Request failed"})

    except ValueError:
        return JsonResponse({"error": "Invalid JSON response"})

    loc = data.get("loc", "")
    lat, lon = (loc.split(",") + [None, None])[:2]

    return JsonResponse({
        "ip": ip,
        "city": data.get("city"),
        "region": data.get("region"),
        "country": data.get("country"),
        "latitude": lat,
        "longitude": lon,
        "timezone": data.get("timezone"),
        "postal": data.get("postal"),
    })

def index(request):
    return render(request, 'locate/index.html')