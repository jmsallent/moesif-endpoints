from django.views.decorators.http import require_POST
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
@require_POST
def health_check(request):
    return JsonResponse({"message": "Health check endpoint"})

@csrf_exempt
@require_POST
def sign_documents(request):
    return JsonResponse({"message": "Sign documents endpoint"})

@csrf_exempt
@require_POST
def get_signature_status(request):
    return JsonResponse({"message": "Get signature status endpoint"})

@csrf_exempt
@require_POST
def download_signed_document(request):
    return JsonResponse({"message": "Download signed document endpoint"})