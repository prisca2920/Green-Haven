from django.shortcuts import render
from django.http import HttpResponse
from django_daraja.mpesa.core import MpesaClient


def index(request):
    if request.method == 'POST':
        phone_number = request.POST['phone_number']
        amount = request.POST['amount']

        if not phone_number or not amount:
            return HttpResponse("Invalid input. Both phone number and amount are required.")

        amount = int(amount)
        service = MpesaClient()
        account_reference = 'reference'
        transaction_desc = 'Description'
        callback_url = 'https://api.darajambili.com/express-payment'

        response = service.stk_push(phone_number, amount, account_reference, transaction_desc, callback_url)

        if response.response_code == '0':
            success_message = f"A pop up has been sent to your phone number. Please enter your Mpesa pin to authenticate the transaction. Payment of KES{amount} to {phone_number} was successful!"
            return HttpResponse(success_message)
        else:
            error_message = f"Payment failed. ResponseCode: {response.ResponseCode}, ResponseDescription: {response.ResponseDescription}"
            return HttpResponse(error_message)

    return render(request, 'amount.html')
