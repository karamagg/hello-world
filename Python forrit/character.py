
class Character:
    def __init__(self):
        self._description = '' #Setjum sem private breytu
        self._name = ''

    def setImage():pass

    def getDescription(self):
        return self._description

    def setDescription(self, des):
        self._description = des

    def quitGame():pass
    #Set nafnið með getName
    def getName(self):
        return self._name
    #Sæki nafnið með setName
    def setName(self, name):
        self._name = name
    def choice(): pass

class ChooseChar(Character):
    def __init__ (self):
        pass

    def choice(self):
        #Athuga að setja inn myndir þegar grafíkin kemur inn
        #Setja inn að ef notandi ýtir hvorki á 0 né 1 þá þarf hann að velja aftur,
        #þangað til að hann velur 0 eða 1.
        genderInput = input("Viltu vera töframaður eða norn? (0, 1)\n")
        if genderInput == '0':
            personInput = input("Vilt þú vera Haraldur Pottur eða Rúnar Vilmundarson? (0, 1)\n")
            if personInput == '0':
                return HarryPotter()
            elif personInput == '1':
                return RonWeasly()
        elif genderInput == '1':
            personInput = input("Vilt þú vera Hermína Guðmundsdóttir eða Guðrún Vilmundardóttir? (0, 1)\n")
            if personInput == '0':
                return HermioneGranger()
            elif personInput == '1':
                return GinnyWeasly()

class HarryPotter(Character):
    def __init__(self):
        self.setName('Haraldur Pottur')
        des = "Hinn útvaldi! Haraldur Pottur er 16 ára galdrastrákur sem hefur ekki átt sjö dagana sæla. Hann hefur barist við sjálfan Lávarð Valdimar og býr hann því að mikilli reynslu. Haraldur er fljótur á fótum og ræður við galdra sem fáir jafnaldrar hans þora að kljást við."
        #Setum inn lýsingu sem við sækjum svo í klasanum level með getDescription()
        self.setDescription(des)
        super(Character, self).__init__()

class HermioneGranger(Character):
    def __init__(self):
        self.setName('Hermína Guðmundsdóttir')
        des = "Þú hefur valið bráðkláran mugga sem má líkja við gangandi orðabók. Þegar kemur að erfiðum tímum er ávallt hægt að stóla á visku hennar til þess að sigrast á öllum áskorunum."
        self.setDescription(des)
        super(Character, self).__init__()

class GinnyWeasly(Character):
    def __init__(self):
        self.setName('Guðrún Vilmundardóttir')
        des = "Þú hefur valið einn úr Vilmundarættinni! Guðrún er kraftmikil og öflug galdrakona sem ræður við erfiða galdra og er ein af bestu ,,quidditch” spilurum Hogwarts."
        self.setDescription(des)
        super(Character, self).__init__()

class RonWeasly(Character):
    def __init__(self):
        self.setName('Rúnar Vilmundarson')
        des = "Rúnar kemur frá stórri galdraætt sem er hvað þekktust fyrir sitt eldrauða hár. Alltaf er hægt að treysta á skopskyn og hæfileika hans að hugsa út fyrir kassann í erfiðum aðstæðum."
        self.setDescription(des)
        super(Character, self).__init__()
