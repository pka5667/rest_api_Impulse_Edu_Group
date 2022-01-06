from django.http.response import Http404
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Assignment
from .serializers import AssignmentSerializer

@api_view()
def get_assignments(request):
    assignments = Assignment.objects.all()
    assignment_serializer = AssignmentSerializer(assignments, many=True)
    return Response({'data': assignment_serializer.data})

@api_view(['POST'])
def post_assignments(request):
    if request.method == 'POST':
        serialzer = AssignmentSerializer(data=request.data)
        if serialzer.is_valid():
            serialzer.save()
            return Response({'message': 'Data successfully created'})
        return Response(serialzer.errors)

    return Http404()
