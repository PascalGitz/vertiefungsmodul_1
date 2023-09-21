class Beton:
    def __init__(self, elastizitaetsmodul, dichte, druckfestigkeit, zugfestigkeit, querschnittsflaeche, schwinddehnung) -> None:
        self.elastizitaetsmodul = elastizitaetsmodul
        self.dichte = dichte
        self.druckfestigkeit = druckfestigkeit
        self.zugfestigkeit = zugfestigkeit
        self.querschnittsflaeche = querschnittsflaeche
        self.schwinddehnung = schwinddehnung
        pass


class Betonstahl:
    def __init__(self, elastizitaetsmodul, dichte, druckfestigkeit, zugfestigkeit, querschnittsflaeche) -> None:
        self.elastizitaetsmodul = elastizitaetsmodul
        self.dichte = dichte
        self.druckfestigkeit = druckfestigkeit
        self.zugfestigkeit = zugfestigkeit
        self.querschnittsflaeche = querschnittsflaeche
        pass


class Verbund:
    def __init__(self, beton, betonstahl, dichte) -> None:

        self.wertigkeit = betonstahl.elastizitaetsmodul / beton.elastizitaetsmodul
        self.dichte = dichte
        self.geom_bewehrungsgehalt = beton.querschnittsflaeche / betonstahl.querschnittsflaeche
        self.beton_schwindspannung = -beton.schwinddehnung * beton.elastizitaetsmodul * self.wertigkeit * self.geom_bewehrungsgehalt / (1 + self.geom_bewehrungsgehalt*(self.wertigkeit-1)) 
        pass
