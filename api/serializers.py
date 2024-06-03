from rest_framework import serializers
from .models import Employee, Client, Project, Comment, TableView
from django.utils import timezone

class EmployeeSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField(read_only=True)
    
    def to_representation(self, instance):
        default = super().to_representation(instance)
        
        default["name"] = self.get_name(instance)
        
        return super().to_representation(instance)
    
    class Meta:
        model = Employee
        fields = "__all__"
        
    def get_name(self, obj):
        if obj.first_name == "" and obj.last_name == "":
            return None
        return obj.first_name + " " + obj.last_name
        
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
    
    created_at = serializers.DateTimeField(read_only=True)
    
    def get_filtered_fields(self, default):
        # user = self.context['request'].user
        stage = self.context['request'].query_params.get('current_stage')
        table_view = self.context['request'].query_params.get('table_view')
        
        if (not stage and not table_view) or (stage == "13" or stage == "14"):
            table_view_data = list(default.keys())
        elif stage and table_view:
            table_view_data = TableView.objects.values_list().get(stage=stage, name=table_view)[4]
        elif stage:
            table_view_data = TableView.objects.values_list().get(stage=stage, name='default')[4]
        elif table_view:
            table_view_data = TableView.objects.values_list().get(name=table_view)[4]
        
        
        if('attachments' in table_view_data):
            table_view_data = table_view_data[:table_view_data.index('attachments')] + ['f_contract',
        'f_deed',
        'f_report',
        'f_identity',
        'f_container_contract',
        'f_license',
        'f_plan',
        'f_load_bearing_certificate',
        'f_location_certificate',
        'f_land_survey',
        'f_soil_test',
        'f_coordinate_certificate',
        'f_technical_report',
        'f_demolition_letters',
        'f_autocad',
        'f_client_form',
        'f_old_license',
        'f_civil_defense',
        'f_water_authority'] + table_view_data[table_view_data.index('attachments'):]            
            
        table_view_data.insert(0, 'id')

        return {key: default[key] for key in table_view_data if key in default}
    
    def get_fields(self):
        default = super().get_fields()
        
        if not self.context:
            return default
        
        filtered_fields = self.get_filtered_fields(default)
        
        return filtered_fields   
    
    def create(self, validated_data):
        validated_data['created_at'] = timezone.now()
        validated_data['moved_at'] = timezone.now()
        return super().create(validated_data)
    
    # def update(self, instance, validated_data):
    #     print(instance)
    #     print(validated_data)
    #     # validated_data['updated_at'] = timezone.now()
    #     return super().update(instance, validated_data)
    
    design_eng_name = serializers.SerializerMethodField()  
    client_phone = serializers.SerializerMethodField()
    architect_name = serializers.SerializerMethodField()
    construction_eng_name = serializers.SerializerMethodField()
    plumbing_eng_name = serializers.SerializerMethodField()
    electrical_eng_name = serializers.SerializerMethodField()
    architecture_reviewer_name = serializers.SerializerMethodField()
    construction_reviewer_name = serializers.SerializerMethodField()
    plumbing_reviewer_name = serializers.SerializerMethodField()
    electrical_reviewer_name = serializers.SerializerMethodField()
    corrector_name = serializers.SerializerMethodField()
    
    def to_representation(self, instance):
        default = super().to_representation(instance)
        if('design_eng' in default):
            default['design_eng_name'] = self.get_design_eng_name(instance)
        if('client_number' in default):
            default['client_phone'] = self.get_client_phone(instance)
        if('architect' in default):
            default['architect_name'] = self.get_architect_name(instance)
        if('construction_eng' in default):
            default['construction_eng_name'] = self.get_construction_eng_name(instance)
        if('plumbing_eng' in default):
            default['plumbing_eng_name'] = self.get_plumbing_eng_name(instance)
        if('electrical_eng' in default):
            default['electrical_eng_name'] = self.get_electrical_eng_name(instance)
        if('architecture_reviewer' in default):
            default['architecture_reviewer_name'] = self.get_architecture_reviewer_name(instance)
        if('construction_reviewer' in default):
            default['construction_reviewer_name'] = self.get_construction_reviewer_name(instance)
        if('plumbing_reviewer' in default):
            default['plumbing_reviewer_name'] = self.get_plumbing_reviewer_name(instance)
        if('electrical_reviewer' in default):
            default['electrical_reviewer_name'] = self.get_electrical_reviewer_name(instance)
        if('corrector' in default):
            default['corrector_name'] = self.get_corrector_name(instance)
            
            
        return default
    
    class Meta:
        model = Project
        fields = "__all__"


    def get_design_eng_name(self, obj):
        if(obj.design_eng == None):
            return None
        return obj.design_eng.first_name
    
    def get_client_phone(self, obj):
        if(obj.client_number == None):
            return None
        return obj.client_number.phone
    
    def get_architect_name(self, obj):
        if(obj.architect == None):
            return None
        return obj.architect.first_name
    
    def get_construction_eng_name(self, obj):
        if(obj.construction_eng == None):
            return None
        return obj.construction_eng.first_name
    
    def get_plumbing_eng_name(self, obj):
        if(obj.plumbing_eng == None):
            return None
        return obj.plumbing_eng.first_name
    
    def get_electrical_eng_name(self, obj):
        if(obj.electrical_eng == None):
            return None
        return obj.electrical_eng.first_name
    
    def get_architecture_reviewer_name(self, obj):
        if(obj.architecture_reviewer == None):
            return None
        return obj.architecture_reviewer.first_name
    
    def get_construction_reviewer_name(self, obj):
        if(obj.construction_reviewer == None):
            return None
        return obj.construction_reviewer.first_name
    
    def get_plumbing_reviewer_name(self, obj):
        if(obj.plumbing_reviewer == None):
            return None
        return obj.plumbing_reviewer.first_name
    
    def get_electrical_reviewer_name(self, obj):
        if(obj.electrical_reviewer == None):
            return None
        return obj.electrical_reviewer.first_name
    
    def get_corrector_name(self, obj):
        if(obj.corrector == None):
            return None
        return obj.corrector.first_name
    
    # def get_structural_eng_name(self, obj):
    #     if(obj.structural_eng == None):
    #         return None
    #     return obj.structural_eng.first_name
    
    
class CommentSerializer(serializers.ModelSerializer):
    written_at = serializers.DateTimeField(read_only=True)
    
    def create(self, validated_data):
        validated_data['written_at'] = timezone.now()
        return super().create(validated_data)
    
    class Meta:
        model = Comment
        fields = "__all__"


class TableViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = TableView
        fields = "__all__"