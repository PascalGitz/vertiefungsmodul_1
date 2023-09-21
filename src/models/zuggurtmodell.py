class Zuggurtmodell:
    def __init__(self, einwirkung, beton, betonstahl, verbund) -> None:
        self.einwirkung = einwirkung
        self.einwirkung_spannung = self.einwirkung / beton.querschnittsflaeche
        self.beton = beton
        self.betonstahl = betonstahl
        self.verbund = verbund
        pass
    
    def spannung(self, ungerissen = True):
        sigma_ci = self.verbund.beton_schwindspannung
        f_ct = self.beton.zugfestigkeit
        rho = self.verbund.geom_bewehrungsgehalt
        n = self.verbund.wertigkeit
        
        if self.einwirkung_spannung <= f_ct:
            stahlspannung = (f_ct- sigma_ci) * (1 + rho*(n-1))/rho
        else:
            stahlspannung = sigma_ci
        
          
        return stahlspannung
    

        