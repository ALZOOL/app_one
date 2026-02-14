{
    'name':"App One",
    'author':'Ayman Jammaa',
    'category':'',
    'version':'18.0.0.1',
    'depends':['base',
                'sale',
                'account',
                'mail',
                
              ],
    'data':[
        'security/ir.model.access.csv',
        'views/base_menu.xml',
        'views/property_view.xml',
        'views/owner_view.xml',
        'views/tag_view.xml',        
        'views/sale_order_inherit_view.xml',        
    ],

    'assets': {
        'web.assets_backend': [
            'app_one/static/src/css/property.css',
        ],
    },


    'installable': True,
    'application': True,

}