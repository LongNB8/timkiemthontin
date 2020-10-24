from django.shortcuts import render
from django.http import HttpResponse
from . import models
from django.core.files.storage import FileSystemStorage
import face_recognition
import os
import cv2
import shutil
from collections import Counter


known_faces = []
known_names = []


# def index(request) :
#     KNOWN_FACES_DIR = 'media/kno'
#     UNKNOWN_FACES_DIR = 'media/unknow'
#     TOLERANCE = 0.4
#     MODEL = 'cnn'  
#     for i in os.listdir(UNKNOWN_FACES_DIR):
#         file_path = os.path.join(UNKNOWN_FACES_DIR, i)
#         if os.path.isfile(file_path) or os.path.islink(file_path):
#             os.unlink(file_path)
#         elif os.path.isdir(file_path):
#             shutil.rmtree(file_path)
    
#     # query = models.StudentImage.objects.raw('SELECT * from face_student, face_studentimage Where face_student.id = face_studentimage.student_id ORDER BY face_student.id')
#     # print('Loading known faces...')
#     # # known_faces = []
#     # # known_names = []
#     # for i in query:
#     #     image = face_recognition.load_image_file(f'{os.getcwd()}{i.image.url}')
#     #     encoding = face_recognition.face_encodings(image)[0]
#     #     known_faces.append(encoding)
#     #     known_names.append(i.name)

#     if request.method == 'POST' and request.FILES['myfile']:
#         myfile = request.FILES['myfile']
#         fs = FileSystemStorage()
#         filename = fs.save('unknow/' + myfile.name, myfile)
#         uploaded_file_url = fs.url(filename)
#         # img = cv2.imread(f'{os.getcwd()}{uploaded_file_url}')
#         # cv2.imshow('out',  img)
#         # cv2.waitKey(0)

#         # print(known_names)
#         # print(known_faces)

       


#         print('Processing unknown faces...')
#         #print(known_names)
#         if len(known_names) == 0 and len(known_faces) == 0 :
#             return render(request, 'pages/result.html', {'loaddb':'ok', 'rs' : 'Không có dữ liệu người này, bạn chưa load dữ liệu từ DB về vui lòng làm việc này', 'img' : uploaded_file_url})


#         for filename in os.listdir(UNKNOWN_FACES_DIR):
           
#             print(f'Filename {filename}', end='')
#             image = face_recognition.load_image_file(f'{UNKNOWN_FACES_DIR}/{filename}')

#             locations = face_recognition.face_locations(image, model=MODEL)

#             encodings = face_recognition.face_encodings(image, locations)

#             image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
            
#             print(f', found {len(encodings)} face(s)')
#             if len(encodings) == 0 :
#                 return render(request, 'pages/uploadfile.html', {
#                     'uploaded_file_url': 'không nhận diện được vui lòng thay ảnh khác rõ khuôn mặt hơn'
#                 })

#             for face_encoding, face_location in zip(encodings, locations):
#                 #print(face_location)

#                 results = face_recognition.compare_faces(known_faces, face_encoding, TOLERANCE)
               

#                 #match = "unknow"
#                 #print(match)

#                 if True not in results:  
#                     return render(request, 'pages/result.html', {'rs' : 'Không có dữ liệu người này', 'img' : uploaded_file_url})
                   
#                 else :
#                     print(results)
#                     arr = []
#                     for i in range(len(known_names)): 
#                         if results[i] == True:
#                             if known_names[i] not in arr:
#                                 arr.append(known_names[i])
#                             else :
#                                 arr.append(known_names[i])  
                    
#                     print(arr)
#                     dem = Counter(arr)
#                     sl=[] 
                    
#                     pt = [] 
#                     if len(arr) != 0:
#                         sl.append(dem[arr[0]])
#                         pt.append(arr[0])
#                     for i in range(len(arr)-1):
#                         if arr[i] != arr[i+1] :
#                             sl.append(dem[arr[i+1]])
#                             pt.append(arr[i+1])
#                     print(sl)
#                     print(pt)

#                     if len(sl) != 0:
#                         max1 = max(sl)
                
#                     print(max1)


#                     arrName = []
#                     for i in range(len(pt)):
#                         if sl[i] == max1:
#                             arrName.append(pt[i])

#                     print(arrName)
#                     if len(arrName) != 0:
#                         qr = models.StudentImage.objects.raw('SELECT * from face_student, face_studentimage Where face_student.id = face_studentimage.student_id AND face_student.name=%s  ORDER BY face_student.id LIMIT 4',[arrName[0]])
#                         return render(request, 'pages/result.html', {'rs' : arrName[0], 'img' : uploaded_file_url, 'item' : qr})
                        
        
        

#     return render(request, 'pages/uploadfile.html')


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
    
    # query = models.StudentImage.objects.raw('SELECT * from face_student, face_studentimage Where face_student.id = face_studentimage.student_id ORDER BY face_student.id')
    # print('Loading known faces...')
    # # known_faces = []
    # # known_names = []
    # for i in query:
    #     image = face_recognition.load_image_file(f'{os.getcwd()}{i.image.url}')
    #     encoding = face_recognition.face_encodings(image)[0]
    #     known_faces.append(encoding)
    #     known_names.append(i.name)

    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save('unknow/' + myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        # img = cv2.imread(f'{os.getcwd()}{uploaded_file_url}')
        # cv2.imshow('out',  img)
        # cv2.waitKey(0)

        # print(known_names)
        # print(known_faces)

       


        print('Processing unknown faces...')
        #print(known_names)
        if len(known_names) == 0 and len(known_faces) == 0 :
            return render(request, 'pages/result.html', {'loaddb':'ok', 'rk' : 'Không có dữ liệu người này, bạn chưa load dữ liệu từ DB về vui lòng làm việc này', 'img' : uploaded_file_url})


        for filename in os.listdir(UNKNOWN_FACES_DIR):
           
            print(f'Filename {filename}', end='')
            image = face_recognition.load_image_file(f'{UNKNOWN_FACES_DIR}/{filename}')

            locations = face_recognition.face_locations(image, model=MODEL)

            encodings = face_recognition.face_encodings(image, locations)

            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
            
            print(f', found {len(encodings)} face(s)')
            if len(encodings) == 0 :
                return render(request, 'pages/uploadfile.html', {
                    'uploaded_file_url': 'không nhận diện được vui lòng thay ảnh khác rõ khuôn mặt hơn'
                })
            
            elif len(encodings) > 1 :
                arrSaveImage = []
                arrSaveInfo = []
                counter1=0
                arrName1 = []
                for face_encoding, face_location in zip(encodings, locations):
                #print(face_location)

                    results = face_recognition.compare_faces(known_faces, face_encoding, TOLERANCE)
                    if True not in results:  
                        counter1 = counter1 + 1

                    else :
                        #print(results)
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
                        arrName1.append(arrName[0])
                        for i in arrName:
                            qr = models.StudentImage.objects.raw('SELECT * from face_student, face_studentimage Where face_student.id = face_studentimage.student_id AND face_student.name=%s  ORDER BY face_student.id LIMIT 2',[i])
                            for j in qr:
                                information = "Tên: " + j.name + " - Tuổi: " + str(j.age)  + " - SDT: " + str(j.phone) + " - Địa Chỉ : " + j.address
                                arrSaveImage.append(j.image.url)
                                arrSaveInfo.append(information)

                arrSaveImage = list(set(arrSaveImage))
                arrSaveInfo = list(set(arrSaveInfo))
                return render(request, 'pages/rs.html', {'rs' : arrName1, 'img' : uploaded_file_url, 'item' : arrSaveInfo, 'image':arrSaveImage,'count':counter1})
                
                

                            


            for face_encoding, face_location in zip(encodings, locations):
                #print(face_location)

                results = face_recognition.compare_faces(known_faces, face_encoding, TOLERANCE)
               

                #match = "unknow"
                #print(match)

                if True not in results:  
                    return render(request, 'pages/result.html', {'rk' : 'Không có dữ liệu người này', 'img' : uploaded_file_url})
                   
                else :
                    #print(results)
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
                    if len(arrName) == 1:
                        qr = models.StudentImage.objects.raw('SELECT * from face_student, face_studentimage Where face_student.id = face_studentimage.student_id AND face_student.name=%s  ORDER BY face_student.id LIMIT 3',[arrName[0]])
                        return render(request, 'pages/result.html', {'rs' : arrName[0], 'img' : uploaded_file_url, 'item' : qr})
                    else :
                        arrSaveImage = []
                        arrSaveInfo = []
                        for i in arrName:
                            qr = models.StudentImage.objects.raw('SELECT * from face_student, face_studentimage Where face_student.id = face_studentimage.student_id AND face_student.name=%s  ORDER BY face_student.id LIMIT 3',[i])
                            for j in qr:
                                information = "Tên: " + j.name + " - Tuổi: " + str(j.age)  + " - SDT: " + str(j.phone) + " - Địa Chỉ : " + j.address
                                arrSaveImage.append(j.image.url)
                                arrSaveInfo.append(information)
                        
                        arrSaveImage = list(set(arrSaveImage))
                        arrSaveInfo = list(set(arrSaveInfo))
                        print(arrSaveImage)
                        return render(request, 'pages/rs.html', {'rs' : arrName, 'img' : uploaded_file_url, 'item' : arrSaveInfo, 'image':arrSaveImage})
                        
        
        

    return render(request, 'pages/uploadfile.html')


def test(request):
    print(len(known_names), len(known_faces), 11)
    folder = 'media/unknow'
    return render(request, 'pages/test.html')

def loadDB(request):
    # file1 = open("face/filesavename.txt", 'w', encoding="utf-8")
    # file2 = open("face/filesavevectorface.txt", 'w', encoding="utf-8")
    query = models.StudentImage.objects.raw('SELECT * from face_student, face_studentimage Where face_student.id = face_studentimage.student_id ORDER BY face_student.id')
    print('Loading known faces...')
   
    for i in query:
        image = face_recognition.load_image_file(f'{os.getcwd()}{i.image.url}')
        print(i.image.url)
        encoding = face_recognition.face_encodings(image)[0]
        known_faces.append(encoding)
        known_names.append(i.name)
        # studentName = i.name
        # file1.write("{}\n".format(studentName))
        # file2.write("{}\n".format(encoding))
        
    print(len(known_names), len(known_faces))
    
    # file1.close()
    # file2.close()

    # file3 = open("face/filesavename.txt", 'r', encoding="utf-8")
    # file4 = open("face/filesavevectorface.txt", 'r', encoding="utf-8")
    # arrname = []
    # arrface = []
    
    # for i in file3:
    #     arrname.append(i.split("\n")[0])
    
    # for i in file4:
    #     print(i)

    # print(arrname, len(arrname))
    # #print(arrface, len(arrface))
    # #print(len(arrname), '---' + len(known_names))
    # #print(len(arrface), '---' + len(known_faces))
    # file3.close()
    # file4.close()
    return render(request, 'pages/uploadfile.html', {
                    'uploaded_file_url': 'loaddb thành công'
                })
