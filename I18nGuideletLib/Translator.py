import gettext
import os

class Translator:
    def __init__(self, SelectedLanguage):
        
        if not "English" == SelectedLanguage:
            if "Spanish" == SelectedLanguage:
                idiomas = ['es']
            elif "Arabic" == SelectedLanguage:
                idiomas = ['ar']
            else:
              # "France" == SelectedLanguage 
                idiomas = ['fr']
   
            localedir = os.path.join(os.path.abspath(os.path.dirname(__file__)) + '/Resources', 'locales')
            t = gettext.translation('base', localedir=localedir, languages=idiomas)
            t.install()
            self.__tr = t.gettext 
        else:
            self.__tr = lambda t: t
    
    def Translate(self, data):
        return  unicode(self.__tr(data), "utf8")   
    
    def cleanup(self):
        self.__tr = None