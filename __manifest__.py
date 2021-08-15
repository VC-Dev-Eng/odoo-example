{
    'name': "virtucent",

    'author': "Yusuf Muhammad",
    'website': "http://www.virtucent.com",

    'category': 'Uncategorized',
    'version': '0.1',

    'depends': [
        # 'base'
        'website',
        # 'crm',
        # 'sale_management',
        # 'note',
        # 'account',
        # 'board',
        # 'calendar',
        # 'im_livechat_mail_bot',
        # 'hr',
        # 'hr_expense',
        # 'link_tracker',
        # 'muk_web_theme',
    ],

    'data': [
        'data/res_company_data.xml',
        'security/security.xml',
        'security/ir.model.access.csv',
        'data/crm_stage_data.xml',
        'data/res_currency_data.xml',
        'data/res_users_data.xml',
        'data/website_data.xml',
        'data/transfer_request_sequence.xml',
        'views/employee_views.xml',
        'views/transfer_request_views.xml',
        'views/crm_stage_views.xml',
        'views/res_bank_views.xml',
    ],
    'demo': [
        'demo/demo.xml',
    ],
}
