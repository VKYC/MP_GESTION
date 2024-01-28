{
    'name': "MP Gestion",

    'summary': """Se agrega la gestion para la contabilidad""",
    'author': "Tonny Velazquez",
    'website': "corner.store59@gmail.com",
    'category': 'account',
    'version': '15.0.0.0.1',
    'depends': ['account', 'l10n_latam_invoice_document'],
    'data': [
        # 'security/ir.model.access.csv',
        'views/account_move_views.xml',
        # 'views/templates.xml',
    ],
    'license': 'Other proprietary',
}
