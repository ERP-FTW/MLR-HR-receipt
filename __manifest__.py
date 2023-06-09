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
            ['MLR-HR-receipt-main/static/src/xml/OrderReceipt.xml',
             'MLR-HR-receipt-main/static/src/js/mlr_hr_receipt.js',
             'MLR-HR-receipt-main/static/src/js/ln_address.js',
            ],
    },
    "installable": True,
}
