# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from asgiref.sync import async_to_sync
# from channels.layers import get_channel_layer
# from .models import Project

# @receiver(post_save, sender=Project)
# def notify_stage_update(sender, instance, **kwargs):
#     print("triggered")
#     stage_name = instance.current_stage
#     channel_layer = get_channel_layer()
#     async_to_sync(channel_layer.group_send)(
#         f'stage_{stage_name}',
#         {
#             'type':'send_stage_message',
#             'message': f'Stage {stage_name} updated for project {instance.project_name}'
#         }
#     )