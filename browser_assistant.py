import webbrowser

browser_pathes = {
    'chrome': r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    'firefox': r'C:\Program Files\Mozilla Firefox\firefox.exe'
}
for key in browser_pathes:
    webbrowser.register(key, None, webbrowser.BackgroundBrowser(browser_pathes[key]))

urls = {
    'youtube': 'youtube.com',
    'google': 'google.com',
    'telegram': 'web.telegram.org',
    'outlook': 'outlook.office.com/mail/',
    'gmail': 'mail.google.com/',
    'drive': 'drive.google.com'
}

class BrowserAssistant:
    def __init__(self, url, browser='chrome'):
        self.url = url
        self.browser = browser

    'Open X'
    def open_page(self):
        webbrowser.get(self.browser).open_new_tab(self.url)


class GoogleAssistant:

    def __init__(self, browser='chrome'):
        self.browser = browser

    'Search X'
    def search_google(self, query):
        base_url = "http://www.google.com/search?q="
        if type(query) != 'str':
            query = ' '.join(query)
        webbrowser.open_new(base_url + query)

    'Translate X'
    def translate(self, query):
        sl = "en"
        # target language
        tl = "uk"
        # operation
        operation = "translate"
        if type(query) != 'str':
            query = ' '.join(query)
        url = f"https://translate.google.com/?sl={sl}&tl={tl}&text={query}&op={operation}"

        # This function, from the webbrowser module, opens a link in the default browser
        webbrowser.open(url)

    'Where is X'
    def find_location(self, place):
        base_url = "https://www.google.com/maps/place/"
        if type(place) != 'str':
            query = ' '.join(place)
        webbrowser.open_new(base_url + query)
