from rest_framework import serializers
from .models import Employee, Client, Project, Comment, TableView

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = "__all__"
        
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ["username", "password"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        password = validated_data.pop("password", None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = "__all__"

    

class ProjectSerializer(serializers.ModelSerializer):
    
    def get_filtered_fields(self, default):
        # user = self.context['request'].user
        stage = self.context['request'].query_params.get('stage')
        table_view = self.context['request'].query_params.get('table_view')
        if stage and table_view:
            table_view_data = TableView.objects.values_list().get(stage=stage, name=table_view)[4]
        elif stage:
            table_view_data = TableView.objects.values_list().get(stage=stage, name='default')[4]
        elif table_view:
            table_view_data = TableView.objects.values_list().get(name=table_view)[4]
        else:
            table_view_data = default
        
        table_view_data.append('id')
        
        # print(user.is_staff)
            
            
        
        return {key: default[key] for key in table_view_data if key in default}
    
    def get_fields(self):
        default = super().get_fields()
        
        filtered_fields = self.get_filtered_fields(default)
        return filtered_fields     
    
    class Meta:
        model = Project
        fields = "__all__"


    def get_design_eng_name(self, obj):
        if(obj.design_eng == None):
            return None
        return obj.design_eng.first_name
    
    def get_structural_eng_name(self, obj):
        if(obj.structural_eng == None):
            return None
        return obj.structural_eng.first_name
    
    def get_electrical_eng_name(self, obj):
        if(obj.electrical_eng == None):
            return None
        return obj.electrical_eng.first_name
    
    def get_client_phone(self, obj):
        if(obj.client_number == None):
            return None
        return obj.client_number.phone


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"


class TableViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = TableView
        fields = "__all__"