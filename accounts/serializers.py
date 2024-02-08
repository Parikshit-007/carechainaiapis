from rest_framework import serializers
from accounts.models.models import ReceiptVoucher, PaymentVoucher, Cashbook, AccountLedger, BankAccount

class ReceiptVoucherSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReceiptVoucher
        fields = '__all__'

class PaymentVoucherSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentVoucher
        fields = '__all__'

class CashbookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cashbook
        fields = '__all__'

class AccountLedgerSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountLedger
        fields = '__all__'

class BankAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = BankAccount
        fields = '__all__'
