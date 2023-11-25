from rest_framework import serializers
from .models import *

class OptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Option
        fields = ('id', 'title', 'score')


class VoteSerializer(serializers.ModelSerializer):
    options = OptionSerializer(many=True, read_only=True)

    class Meta:
        model = Vote
        fields = ('id', 'title', 'options')


class StoriesVoteImgSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stories_Vote_Img
        fields = ('id', 'vote_img')



class StorisImgSerializer(serializers.ModelSerializer):
    class Meta:
        model = Storis_img
        fields = ('id', 'img')



class StoriesVoteSerializer(serializers.ModelSerializer):
    img = StoriesVoteImgSerializer(read_only=True)
    votes = VoteSerializer(many=True, read_only=True)

    class Meta:
        model = Stories_Vote
        fields = ('id', 'img', 'votes')