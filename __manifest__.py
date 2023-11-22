{
    'name': 'Grads Gateway',
    'version': '16.0.0.0.0',
    'sequence': -15,
    'author': "Dizital Pods Technologies",
    'category': '',
    'depends': ['base', 'mail', 'board', ],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/student_dashboard.xml',
        'views/student_my_application.xml',
        'views/grads_rep_dashboard.xml',
        'views/bank_rep_dashboard.xml',
        'views/student_upload_document.xml',
        'views/admin_dashboard.xml',
        'views/grads_gateway_bank.xml',
        # 'views/sanctioned_loan.xml',
        # 'views/template.xml',

        'data/sequence.xml',

    ],
    'assets':{
        'web.assets_backend':[
            '/grads_gateway/static/src/css/styles.css'
        ]

    },

    'installable': True,
    'application': True
}
