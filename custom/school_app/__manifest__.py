{
    "name": "school",
    "summary":"this is a school app",
    "description":"school management system",
    "author":"bishnu bk",
    "application":True,
    "version":"1.0.0",
    "depends":["base","mail"],
    "category":"Services/school",
    "data":[
        "security/ir.model.access.csv",
        "data/sequence.xml",
        "wizard/create_appointment_view.xml",
        "views/school.xml",
        "views/student.xml",
        "views/parents_views.xml",
        "views/teacher_views.xml",
        
    ],  
    "installable":True,
    
 
}

