# -*- coding: utf-8 -*-
# © 2017-2018 Savoir-faire Linux
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

{
    'name': 'Product Reference',
    'version': '11.0.1.0.0',
    'author': 'Savoir-faire Linux',
    'maintainer': 'Savoir-faire Linux',
    'website': 'http://www.savoirfairelinux.com',
    'license': 'LGPL-3',
    'category': 'Product',
    'summary': 'Add new field references to product.template',
    'depends': [
        'stock',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/product_template.xml',
        'views/product_template_reference_type.xml',
    ],
    'installable': True,
    'application': False,
}
