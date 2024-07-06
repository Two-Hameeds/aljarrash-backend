from rest_framework import serializers
from .models import Employee, Client, Project, Attachment, Comment, TableView, BaladyProject, LandSurveyProject, SortingDeedsProject
from django.utils import timezone
from pathlib import Path



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

class RemoveTokensSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ["username"]

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = "__all__"

    

class ProjectSerializer(serializers.ModelSerializer):
    
    created_at = serializers.DateTimeField(read_only=True)
    
    def get_filtered_fields(self, default):
        user = self.context['request'].user
        stage = self.context['request'].query_params.get('current_stage')
        table_view = self.context['request'].query_params.get('table_view')
        
        if (not stage and not table_view) or (stage == "completed_projects" or stage == "inactive_projects"):
            table_view_data = list(default.keys())
        elif stage and table_view:
            table_view_data = TableView.objects.values_list().get(stage=stage, name=table_view)[4]
        elif stage:
            table_view_data = TableView.objects.values_list().get(stage=stage, name='default')[4]
        elif table_view:
            table_view_data = TableView.objects.values_list().get(name=table_view)[4]
                  
            
        table_view_data.insert(0, 'id')
        
        if(not user.is_staff):
            table_view_data = list(filter(lambda element: not element.startswith("s_"), table_view_data))
            

        return {key: default[key] for key in table_view_data if key in default}
    
    def get_fields(self):
        default = super().get_fields()
        if not self.context:
            return default
        if(str(self.context["request"].method) == "POST" and self.context["request"].data):
            Client.objects.get_or_create(phone=self.context["request"].data["client_phone"])
        
        filtered_fields = self.get_filtered_fields(default)
        
        return filtered_fields   
    
    def create(self, validated_data):
        validated_data['created_at'] = timezone.now()
        validated_data['moved_at'] = timezone.now()

        common_attachments = [
        "contract",
        "deed",
        "identity",
        "land_survey",
        "client_form",
        "architecture_plan",
        "construction_plan",
        "plumbing_plan",
        "electrical_plan",
        "energy_efficiency_plan",
        ]

        new_residential_commercial = ["soil_test", "civil_defense"]

        new_other = ["soil_test"]
        addition = ["old_license", "plan", "building_pictures"]
        add_floors = ["old_license", "load_bearing_certificate", "plan", "building_pictures"]
        restoration = [
        "old_license",
        "report",
        "container_contract",
        "plan",
        "building_pictures"
        ]
        destruction = [
        "old_license",
        "coordinate_certificate",
        "technical_report",
        "demolition_letters",
        "civil_defense",
        "water_authority",
        ]

        required_attachments = common_attachments


        project_type = validated_data['project_type']
        use_type = validated_data['use_type']

        if(project_type == "new"):
            if(use_type == "residential_commercial"):
                required_attachments.extend(new_residential_commercial)
            else:
                required_attachments.extend(new_other)
        elif(project_type == "addition"):
            required_attachments.extend(addition)
        elif(project_type == "add_floors"):
            required_attachments.extend(add_floors)
        elif(project_type == "restoration"):
            required_attachments.extend(restoration)
        elif(project_type == "destruction"):
            required_attachments.extend(destruction)

        validated_data['required_attachments'] = required_attachments

        return super().create(validated_data)
    
    design_eng_name = serializers.SerializerMethodField()  
    architect_name = serializers.SerializerMethodField()
    construction_eng_name = serializers.SerializerMethodField()
    plumbing_eng_name = serializers.SerializerMethodField()
    electrical_eng_name = serializers.SerializerMethodField()
    architecture_reviewer_name = serializers.SerializerMethodField()
    construction_reviewer_name = serializers.SerializerMethodField()
    plumbing_reviewer_name = serializers.SerializerMethodField()
    electrical_reviewer_name = serializers.SerializerMethodField()
    corrector_name = serializers.SerializerMethodField()
    
    def get_attachments(self, obj_id):
        if(not self.context):
            return {}
        
        attachments = {}
        attachments_list = list(Attachment.objects.filter(uploaded_for=obj_id))

        for attachment in attachments_list:
            # if(attachment.type == 'other'):
            #     if(attachments.get(attachment.type) == None):
            #         attachments[attachment.type] = {}
            #     attachments[attachment.type][attachment.title] = self.context['request'].build_absolute_uri(attachment.attachment.url)
            #     continue
            if(attachment.type not in attachments):
                attachments[attachment.type] = []
            
            attachments[attachment.type].insert(0,self.context['request'].build_absolute_uri(attachment.attachment.url))
        return attachments
    
    def get_comments_count(self, obj_id):
        return Comment.objects.filter(written_for=obj_id).count()
    
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
            
        default['attachments'] = self.get_attachments(instance.id)
        default['comments_count'] = self.get_comments_count(instance.id)
        
            
            
        return default
    
    class Meta:
        model = Project
        fields = "__all__"

    def get_design_eng_name(self, obj):
        if(obj.design_eng == None):
            return None
        return obj.design_eng.first_name
    
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
    
    
class AttachmentSerializer(serializers.ModelSerializer):
    uploaded_at = serializers.DateTimeField(read_only=True)
    
    def create(self, validated_data):
        validated_data['uploaded_at'] = timezone.now()
        return super().create(validated_data)
    
    class Meta:
        model = Attachment
        fields = "__all__"
   
class CommentSerializer(serializers.ModelSerializer):
    written_at = serializers.DateTimeField(read_only=True)
    written_by = serializers.CharField(read_only=True)
    
    def create(self, validated_data):
        validated_data['written_at'] = timezone.now()
        if(str(self.context['request'].user) == "AnonymousUser"):
            validated_data['written_by'] = None
        else:
            validated_data['written_by'] = self.context['request'].user
        return super().create(validated_data)
    
    class Meta:
        model = Comment
        fields = "__all__"


class TableViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = TableView
        fields = "__all__"


class BaladyProjectSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(read_only=True)



    def get_fields(self):
        if(str(self.context["request"].method) == "POST" and self.context["request"].data):
            Client.objects.get_or_create(phone=self.context["request"].data["client_phone"])
        return super().get_fields()


    
    

    class Meta:
        model = BaladyProject
        fields = "__all__"


class LandSurveyProjectSerializer(serializers.ModelSerializer):

    def get_fields(self):
        if(str(self.context["request"].method) == "POST" and self.context["request"].data):
            Client.objects.get_or_create(phone=self.context["request"].data["client_phone"])
        return super().get_fields()

    class Meta:
        model = LandSurveyProject
        fields = "__all__"

class SortingDeedsProjectSerializer(serializers.ModelSerializer):

    def get_fields(self):
        if(str(self.context["request"].method) == "POST" and self.context["request"].data):
            Client.objects.get_or_create(phone=self.context["request"].data["client_phone"])
        return super().get_fields()

        
    class Meta:
        model = SortingDeedsProject
        fields = "__all__"