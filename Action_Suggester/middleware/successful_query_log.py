import json
from datetime import datetime
from Action_Suggester.models import QueryLog

class DBAPILoggerMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        request_time = datetime.now()
        response = self.get_response(request)
        response_time = datetime.now()

        # ✅ Log only API endpoints and only if status code == 200
        if request.path.startswith("/api/v1/analyze") and response.status_code == 200:
            user = request.user.username if request.user.is_authenticated else None
            try:
                response_body = json.loads(response.content.decode("utf-8"))
            except:
                response_body = None

            QueryLog.objects.create(
                original_query=response_body.get("original_query"),
                tone = response_body.get("tone"),
                intent = response_body.get("intent"),
            )

        return response
