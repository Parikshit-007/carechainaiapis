# views.py

from rest_framework import generics, status
from rest_framework.response import Response
from hos_login.models import Custom_User
from accounts.models.models import (
    ReceiptVoucher,
    PaymentVoucher,
    Cashbook,
    AccountLedger,
    BankAccount,
)
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

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class ReceiptVoucherRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ReceiptVoucher.objects.all()
    serializer_class = ReceiptVoucherSerializer

class PaymentVoucherListCreateAPIView(generics.ListCreateAPIView):
    queryset = PaymentVoucher.objects.all()
    serializer_class = PaymentVoucherSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class PaymentVoucherRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PaymentVoucher.objects.all()
    serializer_class = PaymentVoucherSerializer

class CashbookListCreateAPIView(generics.ListCreateAPIView):
    queryset = Cashbook.objects.all()
    serializer_class = CashbookSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class CashbookRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cashbook.objects.all()
    serializer_class = CashbookSerializer

class AccountLedgerListCreateAPIView(generics.ListCreateAPIView):
    queryset = AccountLedger.objects.all()
    serializer_class = AccountLedgerSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class AccountLedgerRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = AccountLedger.objects.all()
    serializer_class = AccountLedgerSerializer

class BankAccountListCreateAPIView(generics.ListCreateAPIView):
    queryset = BankAccount.objects.all()
    serializer_class = BankAccountSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class BankAccountRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BankAccount.objects.all()
    serializer_class = BankAccountSerializer
