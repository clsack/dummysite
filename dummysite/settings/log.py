LOGGING = {
    'version': 1,
    'root': {
        'level': 'NOTSET',
        'handlers': ['file', 'smtp'],
    },
    'disable_existing_loggers': False,
    'formatters': {
        'detailed': {
            'format': '{asctime} - {levelname} - {message}\n'
            'Module: {module} \n',
            'datefmt': '%d-%b-%y %H:%M:%S',
            'style': '{',
        },
        'simple': {
            'format': '{asctime} - {levelname} - {module} - {message}',
            'datefmt': '%d-%b-%y %H:%M:%S',
            'style': '{',
        },
        'empty': {
            'format': '{asctime} - {levelname} - {module}',
            'datefmt': '%d-%b-%y %H:%M:%S',
            'style': '{',
        },
    },
    'handlers': {
        'file': {
            'class': 'logging.handlers.RotatingFileHandler',
            'level': 'INFO',
            'formatter': 'simple',
            'filename': 'C:\\logs\\dummyapp.log',
            'maxBytes': 10485760,
            'backupCount': 5,
        },
        'smtp': {
            'class': 'django.utils.log.AdminEmailHandler',
            'level': 'ERROR',
            'formatter': 'detailed',
        },
        'smtp_info': {
            'class': 'django.utils.log.AdminEmailHandler',
            'level': 'INFO',
            'formatter': 'empty',
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['file'],
            'propagate': False,
        },
        'django': {
            'handlers': ['smtp'],
            'propagate': True,
        },
    }
}
