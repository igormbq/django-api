from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Part
from .serializers import PartSerializer
from collections import Counter
import re

class PartViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows parts to be viewed or edited.
    Provides CRUD operations: list, create, retrieve, update, partial_update, destroy
    """
    queryset = Part.objects.all().order_by('id')
    serializer_class = PartSerializer


    @action(detail=False, methods=['get'])
    def common_words(self, request):
        """
        API endpoint that returns the 5 most common words in part descriptions.
        """
        # Get all part descriptions
        descriptions = Part.objects.values_list('description', flat=True)
        
        # Combine all descriptions and split into words
        all_words = []
        for description in descriptions:
            # Convert to lowercase and remove punctuation
            clean_text = re.sub(r'[^\w\s]', '', description.lower())
            words = clean_text.split()
            all_words.extend(words)
        
        # Count word occurrences and get the 5 most common
        most_common = Counter(all_words).most_common(5)
        
        # Format the response as a list of dictionaries for better readability
        result = [{"word": word, "count": count} for word, count in most_common]
        
        return Response(result)
