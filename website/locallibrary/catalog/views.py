from django.shortcuts import render
id = 'null'
from .models import det
# Create your views here.
import pyrebase
firebaseConfig = {
  "apiKey": "AIzaSyAV1s2J1_bsldfUySJdWUFo9oXDfmYUryw",
  "authDomain": "covid19hack-81596.firebaseapp.com",
  "databaseURL": "https://covid19hack-81596.firebaseio.com",
  "projectId": "covid19hack-81596",
  "storageBucket": "covid19hack-81596.appspot.com",
  "messagingSenderId": "1090178939668",
  "appId": "1:1090178939668:web:2e5d6c5648180f8e486001",
  "measurementId": "G-Z6DMG0ZJWN"
};
firebase = pyrebase.initialize_app(firebaseConfig)
import itertools
db = firebase.database()
def sub(request , id = None):
    
    return render(request , 'login.html'  )
    
def details(request ):
    id = request.POST["admin"] 

    ids = [] 
    f = 1

    last =  db.child("admin").child(id).child("max").get().val()
    print(last)
    while(f<=last) :
        

        try:

            
            s = det() 
            real = db.child("admin").child(id).child("user"+str(f)).get().val()

            
            s.name = db.child("user").child(real).child("details").child("name").get().val()
            s.phone = db.child("user").child(real).child("details").child("phone").get().val()
            s.loca = db.child("user").child(real).child("details").child("loc").child("x").get().val()
            s.code = real

            ids.append(s)
             

            print("user"+str(f))


            print(type(real))
        except :
            print('s')    
            break 
        f=f+1 
      
    
    return render(request , 'details.html' , { 'info' : ids , 'id':id }  )


def photo(request ) :
    userid = request.POST["userid"] 
    id = request.POST["admin"]
    print(id)
    print(userid)


    
    ids = []    
    try :
        locx=db.child("user").child(userid).child("details").child("loc").child("x").get().val() 
        locy=db.child("user").child(userid).child("details").child("loc").child("y").get().val() 
        name=db.child("user").child(userid).child("details").child("name").get().val() 
        phone=db.child("user").child(userid).child("details").child("phone").get().val() 

        countmap=db.child("user").child(userid).child("count").get().val() 
        countphoto=db.child("user").child(userid).child("count1").get().val() 


        mas = db.child("user").child(userid).child("count1").get().val() 
        f = 1

        print("mass")
        print(mas)
        while(f<=mas) :
            
            print(f)
            ui = db.child("user").child(userid).child("urls").child("url"+str(f)).get().val() 
            ids.append(ui) 
            print(ui)
            f=f+1

        print("over")

        
        return render(request , 'photo.html', {'id':id , 'im':userid  ,  'locx':locx , 'locy':locy , 'name':name , 'phone':phone , 'countmap':countmap , 'countphoto':countphoto,'urls':ids } )

    

    except :
        return ref(request)

                    
            







    
def notuploc(request , id = None):
    id= request.POST["admin"]
    ids = [] 
    f = 1

    last =  db.child("admin").child("admin2").child("max").get().val()
    while(f<=last) :
        

        try:

            
            print("fetch")
            real = db.child("admin").child("admin2").child("user"+str(f)).get().val()
            print(real)
            count = db.child("count").get().val()
            c = db.child("user").child(real).child("count").get().val() 
            print(c)
            
        

            if(count>db.child("user").child(real).child("count").get().val() ) :
                
                s = det() 
                s.name = db.child("user").child(real).child("details").child("name").get().val()
                s.phone = db.child("user").child(real).child("details").child("phone").get().val()
                s.loca = db.child("user").child(real).child("details").child("loc").child("x").get().val()
                s.code = real
                ids.append(s)
             



            print(real)
        except :
            print('s')    
            break 
        f=f+1 
      
    
    return render(request , 'details.html' , { 'id':id,'info' : ids }  )





    
def notupphoto(request , id = None):
    id= request.POST["admin"]
    ids = [] 
    f = 1

    last =  db.child("admin").child("admin2").child("max").get().val()
    while(f<=last) :
        

        try:

            
            print("fetch")
            real = db.child("admin").child("admin2").child("user"+str(f)).get().val()
            print(real)
            count = db.child("count1").get().val()
            c = db.child("user").child(real).child("count1").get().val() 
            print(c)
            
        

            if(count>db.child("user").child(real).child("count1").get().val() ) :
                
                s = det() 
                s.name = db.child("user").child(real).child("details").child("name").get().val()
                s.phone = db.child("user").child(real).child("details").child("phone").get().val()
                s.loca = db.child("user").child(real).child("details").child("loc").child("x").get().val()
                s.code = real
                ids.append(s)


             



            print(real)
        except :
            print('s')    
            break 
        f=f+1 
      
    
    return render(request , 'details.html' , { 'id':id, 'info' : ids }  )





    
def action(request , id = None):
    id= request.POST["admin"]
    ids = [] 
    f = 1

    last =  db.child("admin").child("admin2").child("max").get().val()
    while(f<=last) :
        

        try:

            
            print("fetch")
            real = db.child("admin").child("admin2").child("user"+str(f)).get().val()
            print(real)
            count = db.child("count1").get().val()
            c = db.child("user").child(real).child("count1").get().val() 
            print(c)
            loca =  db.child("user").child(real).child("count").get().val() 
        

            if(loca) :     
                x =    db.child("user").child(real).child("location").child(str(loca)).child("x").get().val()
                y =    db.child("user").child(real).child("location").child(str(loca)).child("y").get().val()          
                s = det() 
                s.code = real
                s.name = db.child("user").child(real).child("details").child("name").get().val()
                s.phone = db.child("user").child(real).child("details").child("phone").get().val()
                s.loca = db.child("user").child(real).child("details").child("loc").child("x").get().val()


                coord =   db.child("user").child(real).child("details").child("loc").child("x").get().val() ,db.child("user").child(real).child("details").child("loc").child("y").get().val() 
                cod = x , y 

                dis = haversine(cod, coord)
                maxd = max(dis , db.child("user").child(real).child("maxdis").get().val() )
                db.child("user").child(real).child("maxdis").set(maxd)
                if(maxd>2000):
                    ids.append(s)
             



            print(real)
        except :
            print('s')    
            break 
        f=f+1 
      
    
    return render(request , 'details.html' , { 'id':id , 'info' : ids }  )







import math

def haversine(coord1, coord2):
    R = 6372800  # Earth radius in meters
    lat1, lon1 = coord1
    lat2, lon2 = coord2
    
    phi1, phi2 = math.radians(lat1), math.radians(lat2) 
    dphi       = math.radians(lat2 - lat1)
    dlambda    = math.radians(lon2 - lon1)
    
    a = math.sin(dphi/2)**2 + \
        math.cos(phi1)*math.cos(phi2)*math.sin(dlambda/2)**2
    
    return 2*R*math.atan2(math.sqrt(a), math.sqrt(1 - a))


def profile(request ):
    userid = request.POST["userid"] 
    id = request.POST["admin"]


    print(id)
    print(userid)
    try :

        locx=db.child("user").child(userid).child("details").child("loc").child("x").get().val() 
        locy=db.child("user").child(userid).child("details").child("loc").child("y").get().val() 
        name=db.child("user").child(userid).child("details").child("name").get().val() 
        phone=db.child("user").child(userid).child("details").child("phone").get().val() 

        countmap=db.child("user").child(userid).child("count").get().val() 
        countphoto=db.child("user").child(userid).child("count1").get().val() 

        print(locx)
        print(name)
        
        print("ok")


        return render(request , 'profile.html' , { 'id':id , 'im':userid  , 'locx':locx , 'locy':locy , 'name':name , 'phone':phone , 'countmap':countmap , 'countphoto':countphoto})

    except :
        
        locx=db.child("user").child(userid).child("details").child("loc").child("x").get().val() 
        locy=db.child("user").child(userid).child("details").child("loc").child("y").get().val() 
        name=db.child("user").child(userid).child("details").child("name").get().val() 
        phone=db.child("user").child(userid).child("details").child("phone").get().val() 

        countmap=db.child("user").child(userid).child("count").get().val() 
        countphoto=db.child("user").child(userid).child("count1").get().val() 

        print(locx)
        print(name)
        
        print("ok")


        return render(request , 'profile.html' , { 'id':id , 'im':userid  , 'locx':locx , 'locy':locy , 'name':name , 'phone':phone , 'countmap':countmap , 'countphoto':countphoto})

        





def locations(request):
    userid=request.POST["userid"]
    id=request.POST["admin"]




    

    try:
        
        locx=db.child("user").child(userid).child("details").child("loc").child("x").get().val() 
        locy=db.child("user").child(userid).child("details").child("loc").child("y").get().val() 
        name=db.child("user").child(userid).child("details").child("name").get().val() 
        phone=db.child("user").child(userid).child("details").child("phone").get().val() 

        countmap=db.child("user").child(userid).child("count").get().val() 
        countphoto=db.child("user").child(userid).child("count1").get().val() 

        

        f =1
        lis =[] 
        while(f<=countmap) :
            x = db.child("user").child(userid).child("location").child(str(f)).child("x").get().val() 
            y = db.child("user").child(userid).child("location").child(str(f)).child("y").get().val()
            li = [f ,x, y]
            lis.append(li)  
            f=f+1
            
        return render(request , "locations.html" , { 'id':id , 'im':userid ,'locx':locx , 'locy':locy , 'name':name , 'phone':phone , 'countmap':countmap , 'countphoto':countphoto ,'lisx':lis,  })

    except :
        return sub(request)











def temperature(request ):

    userid=request.POST["userid"]
    id=request.POST["admin"]



    

    try:
        
        locx=db.child("user").child(userid).child("details").child("loc").child("x").get().val() 
        locy=db.child("user").child(userid).child("details").child("loc").child("y").get().val() 
        name=db.child("user").child(userid).child("details").child("name").get().val() 
        phone=db.child("user").child(userid).child("details").child("phone").get().val() 

        countmap=db.child("user").child(userid).child("count").get().val() 
        countphoto=db.child("user").child(userid).child("count1").get().val() 

        

        f =1
        lis =[] 
        while(f<=countphoto) :
            x = db.child("user").child(userid).child("temp").child(str(f)).get().val() 
            li = [f ,x]
            lis.append(li)  
            f=f+1
            
        return render(request , "temperature.html" , {'id':id , 'im':userid , 'locx':locx , 'locy':locy , 'name':name , 'phone':phone , 'countmap':countmap , 'countphoto':countphoto ,'lisx':lis,  })

    except :
        return sub(request)



def ref(request ):
    id= None
    if(request.POST):
        id = request.POST['admin']

    return render(request , 'home.html' , {'id' : id }  )
def log(request  , id = None):
    
    if request.method == "POST" :
        
        
        
        
        try:
            print("ok1") 
            real = db.child("admin").child(request.POST['user']).child("pass").get().val()
   
            
            
            if(real==request.POST['pass']) :
                print('oj2')
                return render(request, 'home.html' , {'id' : request.POST['user']}  )
            else :

                
                print(real)
                print(request.POST['pass'])
    
                return render(request , 'login.html' )     
        except:


            
            return render(request , 'login.html') 
         

    return render(request , 'home.html')      


