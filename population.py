import random as rd
class Vorace:
    "Creation d'un vilain vorace"
    def __init__(self,heure,minute):
        motivation=rd.random()
        self.TTPP=False
        self.reveille=False
        self.lieu="absent"
        self.specialite=""
        self.ip=""
        if motivation>0.1:
            self.motivation=True
        else:
            self.motivation=False
        
    def update_motivation(self):
        m=rd.random()
        if m>0.25:
            self.motivation=True
        else:
            self.motivation=False
    def update_reveil(self,h,m):
        if h>=7:
            self.reveille=True
        else:
            m=rd.random()
            if m>0.8:
                self.reveille=True
            else:
                self.reveille=False
    def update_lieu(self):
        if self.lieu=="absent":
            m=rd.random()
            if m>0.9:
                self.lieu="Bureau"
        else:
            m=rd.random()
            if m>0.15:
                self.lieu="Bureau"
            else:
                self.lieu="absent"
    def update_TTPP(self):
        a=0
    def update_arrivee(self,h,m):
        if self.lieu=="absent":
            m=rd.random()
            if m>0.7:
                self.lieu="Bureau"
                self.reveille=True
        if h>=7 and m>10:
            self.lieu="Bureau"
            self.reveille=True
    def update_ip(self,chiffre):
        self.ip="192.168.10."+str(chiffre)


class SDI:
    "Creation d'un SDI"
    def __init__(self,heure,minute):
        motivation=rd.random()
        self.TTPP=False
        self.ip=""
        self.reveille=False
        self.lieu="peigne"
        if motivation>0.1:
            self.motivation=True
        else:
            self.motivation=False
        choix=rd.randint(1,3)
        if choix==1:
            choix2=rd.randint(1,3)
            if choix2==1:
                self.specialite="cyber"
            elif choix2==2:
                self.specialite="simu"
            else:
                self.specialite="RO"
        elif choix==2:
            self.specialite="elec"
        else:
            self.specialite="meca"
        
    def update_motivation(self):
        m=rd.random()
        if m>0.25:
            self.motivation=True
        else:
            self.motivation=False
    def update_reveil(self,h,m):
        if not self.reveille:
            if h>=7:
                self.reveille=True
            else:
                m=rd.random()
                if m>0.9:
                    self.reveille=True
                else:
                    self.reveille=False
    def update_lieu(self):
        if self.lieu=="absent":
            m=rd.random()
            if m>0.95:
                self.lieu="DGER"
        else:
            m=rd.random()
            if m>0.001:
                self.lieu="DGER"
            else:
                self.lieu="absent"
    def update_TTPP(self):
        m=rd.random()
        if m>0.9:
            self.TTPP=True
            self.lieu="peigne"
    def update_ip(self,chiffre):
        self.ip="192.168.20."+str(chiffre)

class SSP:
    "Creation d'un SSP"
    def __init__(self,heure,minute):
        self.TTPP=False
        self.reveille=False
        self.lieu="peigne"
        self.ip=""
        self.specialite=""
        motivation=rd.random()
        if motivation>0.1:
            self.motivation=True
        else:
            self.motivation=False
        
    
    def update_motivation(self):
        m=rd.random()
        if m>0.25:
            self.motivation=True
        else:
            self.motivation=False
    def update_reveil(self,h,m):
        if not self.reveille:
            if h>=7:
                self.reveille=True
            else:
                m=rd.random()
                if m>0.9:
                    self.reveille=True
                else:
                    self.reveille=False
    def update_lieu(self):
        if self.lieu=="absent":
            m=rd.random()
            if m>0.95:
                self.lieu="DGER"
        else:
            m=rd.random()
            if m>0.001:
                self.lieu="DGER"
            else:
                self.lieu="absent"
    def update_TTPP(self):
        m=rd.random()
        if m>0.65:
            self.TTPP=True
            self.lieu="peigne"
    def update_ip(self,chiffre):
        self.ip="192.168.30."+str(chiffre)




#v1=Vorace(6,30)
#print(v1.motivation)
#print(v1.reveille)
#print(v1.lieu)

#for k in range (10):
#    v1.update_motivation()
#    print(v1.motivation)