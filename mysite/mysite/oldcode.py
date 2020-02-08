#import dependancies
import os,re, json,string,sys,importlib, logging
import pandas as pd
import spacy
from django.shortcuts import render
from django.http import HttpResponse
from pyresparser import ResumeParser
nlp = spacy.load('en_core_web_sm')
from django.http import JsonResponse
from pyresparser import ResumeParser
import nltk
from spacy.matcher import matcher
import multiprocessing as mp
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from time import process_time
ALLOWED_EXTENSIONS = set(['csv','docx','pdf','doc'])


def index_redirect(request):
    return redirect('/skillreader/')


def index(request):
    if request.method == 'POST':
    	#save the file 
    	file = request.FILES['file']
    	file_name = default_storage.save(file.name, file)
    	#  Reading file from storage
    	file = default_storage.open(file_name)
    	file_url = default_storage.url(file_name)
    	#Use resume Parser library to read the informationn
    	# Start the stopwatch / counter
    	t1_start = process_time() 
    	data = ResumeParser(file_url).get_extracted_data()
    	#get only skills values from the data dictionary
    	dict_df=data.get("skills")
    	#convert dictionary objects to string
    	result = str(dict_df)
    	result = json.dumps(result)
    	#default_storage.delete(file_name)
    	# Stop the stopwatch / counter
    	t1_stop = process_time()
        #print("Elapsed time:", t1_stop, t1_start)
        #print("Elapsed time during the whole program in seconds:",t1_stop-t1_start)
        #processing_time= t1_stop-t1_start
        # response = {'Skills': result,}
            # 'time': format(t1_stop-t1_startime, '.2f'),
        #         response = {
        #     'upload_file_path': upload_file_path,
        #     'Name': data['name'],
        #     'Email': data['email'],
        #     'Skills': data['skills'],
        #     'time': format(stop_time - start_time, '.2f'),
        # }

        return render(request, 'skillreader/index.html', context=result)
    else:
        return render(request, 'skillreader/index.html')

    #return JsonResponse({'skill_list': result,'processing_time':processing_time})
 {% if upload_file_path %}
    Uploaded at: <label class="text-primary">{{ upload_file_path }}</label><br>