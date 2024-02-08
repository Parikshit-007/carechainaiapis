from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

from accounts.views.views import (
    ReceiptVoucherListCreateAPIView,
    ReceiptVoucherRetrieveUpdateDestroyAPIView,
    PaymentVoucherListCreateAPIView,
    PaymentVoucherRetrieveUpdateDestroyAPIView,
    CashbookListCreateAPIView,
    CashbookRetrieveUpdateDestroyAPIView,
    AccountLedgerListCreateAPIView,
    AccountLedgerRetrieveUpdateDestroyAPIView,
    BankAccountListCreateAPIView,
    BankAccountRetrieveUpdateDestroyAPIView,
)

urlpatterns = [
    path('api/receipt-vouchers/', ReceiptVoucherListCreateAPIView.as_view(), name='receipt-voucher-list'),
    path('receipt-vouchers/<int:pk>/', ReceiptVoucherRetrieveUpdateDestroyAPIView.as_view(), name='receipt-voucher-detail'),
    path('payment-vouchers/', PaymentVoucherListCreateAPIView.as_view(), name='payment-voucher-list'),
    path('payment-vouchers/<int:pk>/', PaymentVoucherRetrieveUpdateDestroyAPIView.as_view(), name='payment-voucher-detail'),
    path('cashbooks/', CashbookListCreateAPIView.as_view(), name='cashbook-list'),
    path('cashbooks/<int:pk>/', CashbookRetrieveUpdateDestroyAPIView.as_view(), name='cashbook-detail'),
    path('account-ledgers/', AccountLedgerListCreateAPIView.as_view(), name='account-ledger-list'),
    path('account-ledgers/<int:pk>/', AccountLedgerRetrieveUpdateDestroyAPIView.as_view(), name='account-ledger-detail'),
    path('bank-accounts/', BankAccountListCreateAPIView.as_view(), name='bank-account-list'),
    path('bank-accounts/<int:pk>/', BankAccountRetrieveUpdateDestroyAPIView.as_view(), name='bank-account-detail'),
]