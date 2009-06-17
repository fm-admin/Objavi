
POINT_2_MM = 0.35277777777777777

KEEP_TEMP_FILES=True
TMPDIR = 'tmp'

#keep book lists around for this time without refetching
BOOK_LIST_CACHE = 3600 * 2
BOOK_LIST_CACHE_DIR = 'cache'

TOC_URL = "http://%s/pub/%s/_index/TOC.txt"
BOOK_URL = "http://%s/bin/view/%s/_all?skin=text"
PUBLISH_URL = "/books/"

#leave out vowels so as to avoid accidental words, and punctuation for bidi consistency
CHAPTER_COOKIE_CHARS = 'BCDFGHJKLMNPQRSTVWXYZ'

#XXX could be reading these in from a config file, which can be edited
#by a cgi script

DEFAULT_SERVER = 'en.flossmanuals.net'
#DEFAULT_CSS = 'file://' + os.path.abspath('static/default.css')
SERVER_DEFAULTS = {
    'en.flossmanuals.net': {
        'css': 'static/en.flossmanuals.net.css',
        'lang': 'en',
        'dir': 'LTR',
        },
    'fr.flossmanuals.net': {
        'css': 'static/fr.flossmanuals.net.css',
        'lang': 'fr',
        'dir': 'LTR',
        },
    'translate.flossmanuals.net': {
        'css': 'static/translate.flossmanuals.net.css',
        'lang': 'translate',
        'dir': 'LTR',
        },
    'nl.flossmanuals.net': {
        'css': 'static/nl.flossmanuals.net.css',
        'lang': 'nl',
        'dir': 'LTR',
        },
    'bn.flossmanuals.net': {
        'css': 'static/bn.flossmanuals.net.css',
        'lang': 'bn',
        'dir': 'LTR',
        },
    'fa.flossmanuals.net': {
        'css': 'static/fa.flossmanuals.net.css',
        'lang': 'fa',
        'dir': 'RTL',
        },
}

DEBUG_MODES = (
    #'STARTUP',
    #'INDEX',
    #'PDFEDIT',
    #'PDFGEN',
    #'HTMLGEN',
    )
DEBUG_ALL = False

PAGE_SIZE_DATA = {
    # name      --> should be the same as the key
    # wksize    --> the size name for wkhtml2pdf
    # wkmargins --> margins for wkhtml2pdf (css style, clockwise from top)
    # shift     --> how many points to shift each page left or right.

    'COMICBOOK' : dict(wksize='B5',
                       wkmargins=[20, 30, 20, 30], #mm
                       numberpos=[50, 40], #points, after page resize, from corner
                       shift=20,
                       pointsize=((6.625 * 72), (10.25 * 72)),
                       ),
    'COMICBOOK2' : dict(wksize='A4',
                        wkmargins=[45, 45, 45, 45], #mm
                        numberpos=[50, 40], #points, after page resize, from corner
                        shift=20,
                        pointsize=((6.625 * 72), (10.25 * 72)),
                       )
}

ENGINES = {
    'webkit' : [],
}



if __name__ == '__main__':
    print ', '.join(x for x in globals().keys() if not x.startswith('_'))
