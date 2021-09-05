from rest_framework.views import exception_handler

def custom_exception_handler(exc, context):

    response = exception_handler(exc, context)

    if response is not None and response.status_code == 404:
        response.status_code = 406
        response.data = {
            "message": "Переданные параметры отсутствуют в базе данных",
        }

    return response