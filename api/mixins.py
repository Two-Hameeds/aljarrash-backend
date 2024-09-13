from . import serializers
from .models import History

class GlobalIDMixin:
    def create(self, validated_data):
        result = super().create(validated_data)
        if not validated_data.get("global_id"):
            global_id_serializer = serializers.GlobalIDSerializer(data={})
            global_id_serializer.is_valid(raise_exception=True)
            global_id = global_id_serializer.save()
            result.global_id = global_id
            result.save(update_fields=["global_id"])
            
        History.objects.create(
            user=self.context["request"].user,
            project=result.global_id,
            action="created",
            new_stage="reception.reception",
            ip=self.context["request"].META.get("REMOTE_ADDR"),
        )
        return result
        
        