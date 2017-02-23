import urlparse
import urllib2
#from xbmcswift2.mockxbmc import xbmcplugin
import xbmcplugin
import addon

def send_email():
    import smtplib

    server = smtplib.SMTP('smtp.meta.ua', 465)
    server.set_debuglevel(True)
    server.ehlo()
    server.starttls()
    server.login("gnedoyla@meta.ua", "sdtu")

    msg = "YOUR MESSAGE!"
    server.sendmail("gnedoyla@meta.ua", "dicoka@ukr.net", msg)
    server.quit()


def run_addon(addon_url='?'):
    addon.addon_main("addon.py", "123", addon_url)
    print [e[1] for e in xbmcplugin.dirItems]
    for handle, url, listitem, isFolder in xbmcplugin.dirItems:
        args = urlparse.parse_qs(url[9:])
        mode = args.get('mode', [None])[0]
        folder_url = args.get('folderurl', [None])[0]
        folder_title = args.get('title', [None])[0]
        folder_level = int(args.get('level', '0')[0])
        folder_name = args.get('name', [None])[0]

        if mode == 'play' and file_exists(folder_url):
            continue

        if ((mode == 'lastvids+next') and (folder_level < 2)) \
                or ((mode == 'lastvids+archive') and (folder_level < 3))\
                or (mode == 'tvshows'):
            run_addon(url[8:])


def file_exists(url):
    request = urllib2.Request(url)
    request.get_method = lambda : 'HEAD'
    response = urllib2.urlopen(request)

def checker():
    print'Starting Checker'
    try:
        run_addon()
        print "\nNo Exceptions!\n"
    except Exception as e:
        print "\nException: " + e.message + "\n"
        # send_email()
        import requests
        r = requests.get(
            'https://maker.ifttt.com/trigger/currenttime_addon_error/with/key/eY4xDpJMgo53SrcMtIVoVxoHkrkPrunC2AlNzUCys9x')


if __name__ == "__main__":
    checker()

