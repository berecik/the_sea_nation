import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

CMS_INSTALLED_APPS = [
    'django.contrib.sites',
    'cms',
    'menus',
    'treebeard',
    'djangocms_admin_style',
    'sekizai',  # static files management
    'filer',
    'easy_thumbnails',
    'mptt',
    'djangocms_text_ckeditor',
    'djangocms_link',
    'djangocms_file',
    'djangocms_picture',
    'djangocms_video',
    'djangocms_googlemap',
    'djangocms_snippet',
    'djangocms_style',
    'djangocms_column',
    # 'djangocms_background_media',  # not working with Django >= 2
]

CMS_CONTEXT_PROCESSORS = [
    'sekizai.context_processors.sekizai',
    'cms.context_processors.cms_settings',
    'django.template.context_processors.i18n',
]

CMS_MIDDLEWARE = [
    'django.middleware.locale.LocaleMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
    'cms.middleware.language.LanguageCookieMiddleware',
    'cms.middleware.utils.ApphookReloadMiddleware',
]

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
] + CMS_INSTALLED_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
] + CMS_MIDDLEWARE

ROOT_URLCONF = 'the_sea_nations.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ] + CMS_CONTEXT_PROCESSORS,
        },
    },
]

SITE_ID = 1

LANGUAGES = [
    ('en', 'English'),
    ('pl', 'Polish'),
]

LANGUAGE_CODE = 'en'


X_FRAME_OPTIONS = 'SAMEORIGIN'

CMS_TEMPLATES = [
    ('home.html', 'Home page template'),
]

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

THUMBNAIL_HIGH_RESOLUTION = True

THUMBNAIL_PROCESSORS = (
    'easy_thumbnails.processors.colorspace',
    'easy_thumbnails.processors.autocrop',
    'filer.thumbnail_processors.scale_and_crop_with_subject_location',
    'easy_thumbnails.processors.filters'
)

DJANGOCMS_PICTURE_TEMPLATES = [
    ('background', _('Background image')),
]

DJANGOCMS_PICTURE_NESTING = True

DJANGOCMS_PICTURE_ALIGN = [
    ('top', _('Top Aligned')),
]

DJANGOCMS_PICTURE_RATIO = 1.618
