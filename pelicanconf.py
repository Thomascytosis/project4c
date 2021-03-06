AUTHOR = 'Thomascytosis'
SITENAME = 'project4c'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/Denver'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'https://getpelican.com/'),
         ('Python.org', 'https://www.python.org/'),
         ('Jinja2', 'https://palletsprojects.com/p/jinja/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
#Theme
THEME = "./theme"

# Favicon
STATIC_PATHS = ['images', 'extra']
EXTRA_PATH_METADATA = {'extra/favicon.ico': {'path': 'favicon.ico'},}

# Disable cache while developing
LOAD_CONTENT_CACHE = False

# Display Categories on Menu 
DISPLAY_CATEGORIES_ON_MENU = False

# Display Pages on Menu
DISPLAY_PAGES_ON_MENU = True