from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from educationApp.models import Datas
from educationApp.services import NameMatcherService, DataService
from django.views.decorators.http import require_http_methods
import json
@csrf_exempt
@require_http_methods(["POST"])
def search(request):
    jsonBody = json.loads(request.body)
    dataService = DataService()
    datas = dataService.getAllIndex(jsonBody['words'])
    return HttpResponse(json.dumps(datas, ensure_ascii=False),
           content_type="application/json")

@require_http_methods(["GET"])
def getDatas(request):
    dataService = DataService()
    datas = dataService.getDatas(request.GET['name'])
    return HttpResponse(json.dumps(datas.__dict__, ensure_ascii=False),
           content_type="application/json")
