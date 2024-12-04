from rest_framework import views, response, status


class WebhookView(views.APIView):
    
    def post(self, request):
        data = request.data
        
        print(data)

        return response.Response(
            data=data,
            status=status.HTTP_200_OK
        )
