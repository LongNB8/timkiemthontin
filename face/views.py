from django.shortcuts import render
from django.http import HttpResponse
from . import models
from django.core.files.storage import FileSystemStorage
import face_recognition
import os
import cv2
import shutil
from collections import Counter

def index(request) :
    KNOWN_FACES_DIR = 'media/kno'
    UNKNOWN_FACES_DIR = 'media/unknow'
    TOLERANCE = 0.4
    MODEL = 'cnn'  
    for i in os.listdir(UNKNOWN_FACES_DIR):
        file_path = os.path.join(UNKNOWN_FACES_DIR, i)
        if os.path.isfile(file_path) or os.path.islink(file_path):
            os.unlink(file_path)
        elif os.path.isdir(file_path):
            shutil.rmtree(file_path)

    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save('unknow/' + myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        # img = cv2.imread(f'{os.getcwd()}{uploaded_file_url}')
        # cv2.imshow('out',  img)
        # cv2.waitKey(0)
        query = models.StudentImage.objects.raw('SELECT * from face_student, face_studentimage Where face_student.id = face_studentimage.student_id ORDER BY face_student.id')


     

        print('Loading known faces...')
        known_faces = []
        known_names = []
        for i in query:
            image = face_recognition.load_image_file(f'{os.getcwd()}{i.image.url}')
            encoding = face_recognition.face_encodings(image)[0]
            known_faces.append(encoding)
            known_names.append(i.name)

        # print(known_names)
        # print(known_faces)

       


        print('Processing unknown faces...')
        print(known_names)

        for filename in os.listdir(UNKNOWN_FACES_DIR):
           
            print(f'Filename {filename}', end='')
            image = face_recognition.load_image_file(f'{UNKNOWN_FACES_DIR}/{filename}')

            locations = face_recognition.face_locations(image, model=MODEL)

            encodings = face_recognition.face_encodings(image, locations)

            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
            
            print(f', found {len(encodings)} face(s)')
            if len(encodings) == 0 :
                return render(request, 'pages/uploadfile.html', {
                    'uploaded_file_url': 'khong nhan dien duoc vui long thay anh khac ro khuon mat hon'
                })

            for face_encoding, face_location in zip(encodings, locations):
                print(face_location)

                results = face_recognition.compare_faces(known_faces, face_encoding, TOLERANCE)

                match = "unknow"
                #print(match)

                if True not in results:  
                     return render(request, 'pages/result.html', {'rs' : 'Không có dữ liệu người này', 'img' : uploaded_file_url})
                   
                else :
                    arr = []
                    for i in range(len(known_names)): 
                        if results[i] == True:
                            if known_names[i] not in arr:
                                arr.append(known_names[i])
                            else :
                                arr.append(known_names[i])  
                    
                    print(arr)
                    dem = Counter(arr)
                    sl=[] 
                    
                    pt = [] 
                    if len(arr) != 0:
                        sl.append(dem[arr[0]])
                        pt.append(arr[0])
                    for i in range(len(arr)-1):
                        if arr[i] != arr[i+1] :
                            sl.append(dem[arr[i+1]])
                            pt.append(arr[i+1])
                    print(sl)
                    print(pt)

                    if len(sl) != 0:
                        max1 = max(sl)
                
                    print(max1)


                    arrName = []
                    for i in range(len(pt)):
                        if sl[i] == max1:
                            arrName.append(pt[i])

                    print(arrName)
                    if len(arrName) != 0:
                        qr = models.StudentImage.objects.raw('SELECT * from face_student, face_studentimage Where face_student.id = face_studentimage.student_id AND face_student.name=%s  ORDER BY face_student.id LIMIT 4',[arrName[0]])
                        return render(request, 'pages/result.html', {'rs' : arrName[0], 'img' : uploaded_file_url, 'item' : qr})
                        
        
        

    return render(request, 'pages/uploadfile.html')


def test(request):
    folder = 'media/unknow'
    
   
    return render(request, 'pages/test.html')
