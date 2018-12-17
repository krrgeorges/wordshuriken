from bs4 import BeautifulSoup as bs
import urllib.request
from tts import speechus,speechuk

class Too_Many_Words(Exception):
    pass

class Not_a_word(Exception):
    pass

class AccentException(Exception):
    pass

class SpeakToggleException(Exception):
    pass

class CheckInternetException(Exception):
    pass

class WordShuriken:
     def __init__ (self,word,speak="off",accent="en-us"):
         
         if accent == "en-us" or accent == "en-uk":
             self.accent = accent
         else:
             raise AccentException("Accent not recognised.")
            
         if len(word.split()) > 1:
                raise Too_Many_Words("Please input only one word at a time.")

         if speak == "on" or speak == "off":
             self.speak = speak
         else:
             raise SpeakToggleException("Speech Toggle not recognised.")
            
         self.word = word.lower()
         
     def explain_word(self,returnstuff=None,display=None):
        if len(self.word) > 1:
            word = self.word
            
            url = "http://dictionary.cambridge.org/dictionary/english/"+word
            
            try:
                urlparse = urllib.request.urlopen(url)
            except urllib.error.URLError:
                raise CheckInternetException("Check your internet connection.")
            
            soup = bs(urlparse,"html.parser")

            paras = soup.find_all("b")
            defs = []
            for para in paras:
                if para.get("class") != None:
                    if "def" in para.get("class"):
                        if para.text not in defs:
                            defs.append(para.text)
                        

            explanations = []
            examples = []
            spans = soup.find_all("span")
            for span in spans:
                if span.get("class") != None:
                    if "pos" in span.get("class"):
                        if span.text != "idiom":
                            if span.text not in explanations:
                                explanations.append(span.text)
                if span.get("title") != None:
                    if "Example" in span.get("title"):
                        if span.text not in examples:
                            examples.append(span.text)

            attributes = []

            for i in explanations:
                attributes.append(i)

            # Display
            if display == "Yes":
                 print("\nWord : " + self.word)

                 
                 print("\nAttributes : " + attributes)

                 print("\nDefinition(s) : ")
                 for i in defs:
                     print(str((defs.index(i))+1) + " . " + i)

                 print("\nExample(s) : ")
                 for i in examples:
                     print(str((examples.index(i))+1) + " . " + i)
                     
            if returnstuff == "word":
                 return self.word
            elif returnstuff == "attributes":
                 return attributes
            elif returnstuff == "definition":
                 return defs
            elif returnstuff == "examples":
                 return examples
            elif returnstuff == "all":
                 return [self.word,attributes,defs,examples]

            # Speech
            if self.speak == "on":
                if self.accent == "en-us":
                    speechus(self.word + " is the US form")
                elif self.accent == "en-uk":
                    speechuk(self.word + " is the UK form")
                        
            
        else:
            raise Not_a_word("Word not a word")
        
     def check_word(self):
        if len(self.word) > 1:
            word = self.word
            
            url = "http://dictionary.cambridge.org/dictionary/english/"+word
            
            try:
                urlparse = urllib.request.urlopen(url)
            except urllib.error.URLError:
                raise CheckInternetException("Check your internet connection.")
            
            soup = bs(urlparse,"html.parser")

            paras = soup.find_all("b")
            defs = []
            for para in paras:
                if para.get("class") != None:
                    if "def" in para.get("class"):
                        if para.text not in defs:
                            defs.append(para.text)
                        
            if defs == []:
                print("False")
                return False
            elif defs != []:
                print("True")
                return True
            
        else:
            raise Not_a_word("Word not a word")

