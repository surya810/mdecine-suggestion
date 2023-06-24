from django.shortcuts import render
from .models import Disease
from difflib import SequenceMatcher

def home(request):
    if request.method == 'POST':
        user_symptoms = [symptom.strip().lower() for symptom in request.POST.get('symptoms', '').split(',')]
        diseases = Disease.objects.all()

        best_match_score = 0
        best_match_disease = None

        for disease in diseases:
            disease_symptoms = [symptom.strip().lower() for symptom in disease.symptoms.split(',')]
            match_score = len(set(user_symptoms) & set(disease_symptoms)) / len(disease_symptoms)
            if match_score > best_match_score:
                best_match_score = match_score
                best_match_disease = disease.name

        if best_match_disease is not None:
            medicine_suggestions = Disease.objects.get(name=best_match_disease).medicines
        else:
            medicine_suggestions = "No medicine suggestions found."

        context = {
            'best_match_disease': best_match_disease,
            'medicine_suggestions': medicine_suggestions
        }
        return render(request, 'disease_app/result.html', context)

    return render(request, 'disease_app/home.html')

