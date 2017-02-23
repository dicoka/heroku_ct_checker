SORT_METHOD_ALBUM = 13
SORT_METHOD_ALBUM_IGNORE_THE = 14
SORT_METHOD_ARTIST = 11
SORT_METHOD_ARTIST_IGNORE_THE = 12
SORT_METHOD_BITRATE = 38
SORT_METHOD_DATE = 3
SORT_METHOD_DRIVE_TYPE = 6
SORT_METHOD_DURATION = 8
SORT_METHOD_EPISODE = 22
SORT_METHOD_FILE = 5
SORT_METHOD_GENRE = 15
SORT_METHOD_LABEL = 1
SORT_METHOD_LABEL_IGNORE_THE = 2
SORT_METHOD_LISTENERS = 36
SORT_METHOD_MPAA_RATING = 28
SORT_METHOD_NONE = 0
SORT_METHOD_PLAYLIST_ORDER = 21
SORT_METHOD_PRODUCTIONCODE = 26
SORT_METHOD_PROGRAM_COUNT = 20
SORT_METHOD_SIZE = 4
SORT_METHOD_SONG_RATING = 27
SORT_METHOD_STUDIO = 30
SORT_METHOD_STUDIO_IGNORE_THE = 31
SORT_METHOD_TITLE = 9
SORT_METHOD_TITLE_IGNORE_THE = 10
SORT_METHOD_TRACKNUM = 7
SORT_METHOD_UNSORTED = 37
SORT_METHOD_VIDEO_RATING = 18
SORT_METHOD_VIDEO_RUNTIME = 29
SORT_METHOD_VIDEO_TITLE = 23
SORT_METHOD_VIDEO_YEAR = 17

def getSetting(addon_handle, setting):
    settings = {'res_stream': '1080p', 'res_video': '720p', 'download_fanart': 'true', 'download_thumbnails': 'true'}
    return settings[setting]
    #return "set_" + setting

def setContent(addon_handle, content):
    pass

dirItems_tmp=[]
dirItems=[]

def addDirectoryItem(handle, url, listitem, isFolder):
    item = [handle, url, listitem, isFolder]
    dirItems_tmp.append(item)


def endOfDirectory(addon_handle):
    global dirItems_tmp
    global dirItems
    dirItems=dirItems_tmp
    dirItems_tmp=[]





