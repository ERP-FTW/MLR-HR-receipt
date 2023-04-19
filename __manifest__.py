{
    "name": "MLR Point of Sale - HR",
    "summary": "MLR Point of Sale HR",
    "author": "ERP",
    "website": "https://www.milightningrod.com",
    "category": "Point of Sale",
    "version": "1.0",
    "depends": ["base", "point_of_sale", "pos_hr_restaurant"],
    'data': ["views/employee_view.xml"
    ],
    'assets': {
        'point_of_sale.assets':
            ['mrl_hr_receipt/static/src/xml/OrderReceipt.xml',
            'mrl_hr_receipt/static/src/js/OrderReceipt.js',
            #'mrl_hr_receipt/static/src/js/mlr_hr_receipt.js'
            ],
    },
    "installable": True,
}