from rest_framework import serializers
from .models import approvals

class approvalsSerializers(serializers.ModelSerializers):
    class Meta:
        model = approvals
        fields = '__all__'