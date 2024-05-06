import time
from datetime import datetime

class RequestLoggerMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start_time = time.time()
        response = self.get_response(request)
        execution_time = time.time() - start_time

        with open('request_logs.txt', 'a', encoding='utf-8') as f:
            log_message = (f"{datetime.now()} - {request.method} {request.path} - Время выполнения: "
                           f"{execution_time} секунд\n")
            f.write(log_message)

        print(f"{datetime.now()} - {request.method} {request.path} - "
              f"Время выполнения: {execution_time} секунд")

        return response