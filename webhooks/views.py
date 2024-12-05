import json
from rest_framework import views, response, status
from webhooks.models import Webhook
from webhooks.message import outflow_message
from services.callmebot import CallMeBot


class WebhookView(views.APIView):
    
    def post(self, request):
        data = request.data
        
        Webhook.objects.create(
            event_type=data.get('event_type'),
            event=json.dumps(data, ensure_ascii=False),
        )

        product_name = data.get('product')
        quantity = data.get('quantity')
        product_cost_price = data.get('product_cost_price')
        product_selling_price = data.get('product_selling_price')
        total_value = quantity * product_selling_price
        profit_value = total_value - (quantity * product_cost_price)

        message = outflow_message.format(
            product_name,
            quantity,
            total_value,
            profit_value
        )
        callmebot = CallMeBot()
        callmebot.send_message(message)

        return response.Response(
            data=data,
            status=status.HTTP_200_OK
        )
