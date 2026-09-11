from rest_framework import serializers
from useraccount.serializers import UserDetailSerializer

from .models import Conversation, ConversationMessage


class ConversationListSerializer(serializers.ModelSerializer):
    users = UserDetailSerializer(many=True, read_only=True)

    class Meta:
        model = Conversation
        fields = (
            "id",
            "users",
            "modified_at",
        )
