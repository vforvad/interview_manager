from rest_framework import serializers
from .models import Vacancy

class VacancySerializer(serializers.ModelSerializer):
    """ Serializer for vacancies object """

    class Meta:
        model = Vacancy
        fields = ('id', 'title', 'description', 'created_at', 'updated_at')
