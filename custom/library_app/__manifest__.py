{
    'name':'library_app',
    'summary':'manage all books of library',
    'author':'bishnu bk',
    'version':'1.0.0',
    'depends':["base"],
    'catagory':'Services/Library',
    'application':True,
    'data':[
        'security/ir.model.access.csv',
        'views/library_menu.xml',
        'views/book_view.xml',
        'views/book_list_template.xml'
    ],  
}