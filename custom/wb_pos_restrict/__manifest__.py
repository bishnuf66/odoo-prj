{
    'name':'Weblearns pos Restriction',
    'author':'bishnu bk',
    'version':'1.0.0',
    
    'depends':["base","point_of_sale"],
    'catagory':'Bishnu/Customs',
    'application':True,
    'website':'https://www.bishnubk.com',
    'license':'LGPL-3',
    'data':[
        'xml/view.xml'
        
    ],  
    'assets':{
        'point_of_sale.assets':[
            'wb_pos_restrict/static/src/js/wb_sample_button.js',
            'wb_pos_restrict/static/src/xml/wb_sample_button.xml',
        ]
    }

}