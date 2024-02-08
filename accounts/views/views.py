from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from accounts.models.models import ReceiptVoucher, PaymentVoucher, Cashbook, AccountLedger, BankAccount
from accounts.serializers import (
    ReceiptVoucherSerializer,
    PaymentVoucherSerializer,
    CashbookSerializer,
    AccountLedgerSerializer,
    BankAccountSerializer,
)

class ReceiptVoucherListCreateAPIView(generics.ListCreateAPIView):
    queryset = ReceiptVoucher.objects.all()
    serializer_class = ReceiptVoucherSerializer

class ReceiptVoucherRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ReceiptVoucher.objects.all()
    serializer_class = ReceiptVoucherSerializer

class PaymentVoucherListCreateAPIView(generics.ListCreateAPIView):
    queryset = PaymentVoucher.objects.all()
    serializer_class = PaymentVoucherSerializer

class PaymentVoucherRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PaymentVoucher.objects.all()
    serializer_class = PaymentVoucherSerializer

class CashbookListCreateAPIView(generics.ListCreateAPIView):
    queryset = Cashbook.objects.all()
    serializer_class = CashbookSerializer

class CashbookRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cashbook.objects.all()
    serializer_class = CashbookSerializer

class AccountLedgerListCreateAPIView(generics.ListCreateAPIView):
    queryset = AccountLedger.objects.all()
    serializer_class = AccountLedgerSerializer

class AccountLedgerRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = AccountLedger.objects.all()
    serializer_class = AccountLedgerSerializer

class BankAccountListCreateAPIView(generics.ListCreateAPIView):
    queryset = BankAccount.objects.all()
    serializer_class = BankAccountSerializer

class BankAccountRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BankAccount.objects.all()
    serializer_class = BankAccountSerializer
