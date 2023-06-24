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

def add_data(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        symptoms = request.POST.get('symptoms')
        medicines = request.POST.get('medicines')

        disease = Disease(name=name, symptoms=symptoms, medicines=medicines)
        disease.save()

        return render(request, 'disease_app/add_data.html', {'success': True})

    return render(request, 'disease_app/add_data.html', {'success': False})

import csv
import pandas as pd

def import_data(request):
    if request.method == 'POST':
        csv_file = request.FILES['csv_file']

        if csv_file.name.endswith('.csv'):
            df = pd.read_csv(csv_file)

            for _, row in df.iterrows():
                name = row['Disease']
                symptoms = row['Symptoms']
                medicines = row['Medicines']

                disease = Disease(name=name, symptoms=symptoms, medicines=medicines)
                disease.save()

            return render(request, 'disease_app/import_data.html', {'success': True})
        else:
            return render(request, 'disease_app/import_data.html', {'success': False, 'error': 'Invalid file format. Only .csv files are supported.'})

    return render(request, 'disease_app/import_data.html', {'success': False})
