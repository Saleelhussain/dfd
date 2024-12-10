{
    'name': 'Asset Management',
    'version': '18.0',
    'category': 'Human Resources/Employees',
    'summary': 'This application streamlines the management of employee assets, allowing users to track, allocate, and maintain company assets efficiently. , Employee Asset Management, Asset Tracking Tool, Asset Allocation System, Company Asset Management, Employee Equipment Management, Asset Lifecycle Management, Asset Assignment for Employees, Asset Maintenance Tracker, Digital Asset Management, Asset Reporting System, Employee Asset Tracking, Asset Inventory Management, Asset Ownership Records, Equipment Allocation Software, Resource Management Tool, Asset Usage Monitoring, Asset Handover Process, Asset Return Management, Asset Compliance Tracker, Employee Resource Management',
    'description': """
        The Asset Management application helps users track and manage assets allocated to employees. It allows for easy asset categorization, location management, and tracking of asset movements within the organization. Users can monitor assets from a central interface and maintain accurate records of each asset's location and status.
        
        Key Features:
        - View and manage employee assets.
        - Track asset movement between locations.
        - Organize assets by categories and locations.
        - Create and manage asset categories and locations.
    """,
    'author': 'INKERP',
    'website': 'https://www.inkerp.com/',
    'depends': ['hr', 'mail'],

    'data': [
        'security/ir.model.access.csv',
            'data/ir_sequence.xml',
        'views/asset_category_view.xml',
        'views/asset_detail_view.xml',
        'views/asset_location_view.xml',
        'views/asset_move_view.xml',
    ],

    'images': ['static/description/banner.png'],
    'license': "OPL-1",
    'installable': True,
    'application': True,
    'auto_install': False,
}
