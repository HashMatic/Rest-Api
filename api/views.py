# views.py

import nltk
from nltk.corpus import stopwords
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Resume
from .serializers import ResumeSerializer

@api_view(['GET', 'POST'])
def resume_list(request):
    if request.method == 'GET':
        resumes = Resume.objects.all()
        serializer = ResumeSerializer(resumes, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ResumeSerializer(data=request.data)
        if serializer.is_valid():
            # Determine if the resume is for a backend or frontend developer
            resume = request.FILES.get('resume')
            text = resume.read().decode('utf-8')
            developer_type = 'backend' if 'backend' in text.lower() else 'frontend'
            serializer.save(developer_type=developer_type)
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
