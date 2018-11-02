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
   
            localedir = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'locales')
            t = gettext.translation('base', localedir=localedir, languages=idiomas)
            t.install()
            self.__tr = t.gettext 
        else:
            self.__tr = lambda t: t
    
    def tr(self):
        return self.__tr
    
    def cleanup(self):
        self.__tr = None