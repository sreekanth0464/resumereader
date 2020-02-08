#import dependancies
import os,re, json,string,sys,importlib, logging
import pandas as pd
import time
import os, datetime
import spacy
from django.shortcuts import render,redirect
from django.http import HttpResponse
from pyresparser import ResumeParser
from django.core.files.storage import FileSystemStorage
from django.http import JsonResponse
# from pyresparser import ResumeParser
import nltk
from spacy.matcher import matcher
import multiprocessing as mp
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from time import process_time
ALLOWED_EXTENSIONS = set(['docx','pdf','doc'])

nlp = spacy.load('en_core_web_sm')

def index_redirect(request):
    return redirect('skillreader/')


def index(request):
    if request.method == 'POST' and request.FILES['file']:
        start_time = time.time()

        upload_file = request.FILES['file']
        # print("upload file :",upload_file)
        extension = os.path.splitext(upload_file.name)[1]
        if extension=='.pdf' or '.doc':
            rename = datetime.datetime.now().strftime("%Y_%m_%d %H_%M_%S") + extension
            fss = FileSystemStorage()
            filename = fss.save(rename, upload_file)
            upload_file_path = fss.path(filename)
            print("upload file path:", upload_file_path)
            data = ResumeParser(upload_file_path).get_extracted_data()
            print("resume data:", data)
            # os.remove(upload_file_path)
        stop_time = time.time()
        response = {
            #'upload_file_path': upload_file_path,
            # 'Name': data['name'],
            'Email': data['email'],
            'Skills': data['skills'],
            #'time': format(stop_time - start_time, '.2f'),
        }

        return render(request, 'skillreader/index.html', context=response )


    else:
        return render(request, 'skillreader/index.html')



















    #     #get only skills values from the data dictionary
    #     dict_df=data.get("skills")
    #     #convert dictionary objects to string
    #     result = str(dict_df)
    #     result = json.dumps(result)
    #     return render(request, 'index.html', {'context':result})
    # # else:
    # #     return render(request, 'index.html')

    # #return JsonResponse({'skill_list': result,'processing_time':processing_time})
