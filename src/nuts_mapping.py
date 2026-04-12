# NUTS codes for every city in Green2022.csv
# Format: "City name (as in CSV)": "NUTS code"
# NUTS level used: lowest available that unambiguously identifies the city
#   - NUTS3 where possible (e.g. AT13, DE212)
#   - NUTS2 for metropolitan areas or where NUTS3 covers the whole urban area
#   - Country code (2-letter) for countries not in the NUTS system (NO, CH, IS)
#   - "UK" predecessor codes kept as UKxxx (post-Brexit NUTS equivalent)

city_nuts = {
    # ── Austria (AT) ──────────────────────────────────────────────────────────
    "Vienna":                                   "AT13",   # Wien
    "Graz":                                     "AT22",   # Graz (Steiermark)
    "Linz":                                     "AT31",   # Linz-Wels (Oberösterreich)
    "Innsbruck":                                "AT33",   # Innsbruck (Tirol)
    "Salzburg":                                 "AT32",   # Salzburg
    "Klagenfurt":                               "AT21",   # Klagenfurt (Kärnten)

    # ── Belgium (BE) ──────────────────────────────────────────────────────────
    "Brussels":                                 "BE10",   # Région de Bruxelles-Capitale
    "Antwerp":                                  "BE21",   # Provincie Antwerpen
    "Ghent":                                    "BE23",   # Provincie Oost-Vlaanderen
    "Liège":                                    "BE33",   # Liège
    "Bruges":                                   "BE25",   # Provincie West-Vlaanderen
    "Charleroi":                                "BE32",   # Hainaut
    "Namur":                                    "BE35",   # Namur
    "Leuven":                                   "BE24",   # Provincie Vlaams-Brabant
    "Courtrai":                                 "BE25",   # Provincie West-Vlaanderen (Kortrijk)
    "Ostend":                                   "BE25",   # Provincie West-Vlaanderen (Oostende)
    "Mons":                                     "BE32",   # Hainaut

    # ── Bulgaria (BG) ─────────────────────────────────────────────────────────
    "Sofia":                                    "BG411",  # Sofia (столица)
    "Plovdiv":                                  "BG421",  # Plovdiv
    "Varna":                                    "BG331",  # Varna
    "Burgas":                                   "BG341",  # Burgas
    "Stara Zagora":                             "BG344",  # Stara Zagora
    "Sliven":                                   "BG343",  # Sliven
    "Dobrich":                                  "BG332",  # Dobrich
    "Shumen":                                   "BG333",  # Shumen
    "Haskovo":                                  "BG422",  # Haskovo
    "Pleven":                                   "BG314",  # Pleven
    "Vratsa":                                   "BG313",  # Vratsa
    "Vidin":                                    "BG311",  # Vidin
    "Ruse":                                     "BG323",  # Ruse
    "Pernik":                                   "BG414",  # Pernik
    "Pazardzhik":                               "BG423",  # Pazardzhik
    "Yambol":                                   "BG345",  # Yambol
    "Blagóevgrad":                              "BG413",  # Blagoevgrad
    "Veliko Tarnovo":                           "BG321",  # Veliko Tarnovo

    # ── Cyprus (CY) ───────────────────────────────────────────────────────────
    "Limassol":                                 "CY000",  # Cyprus (single NUTS1)
    "Nicosia":                                  "CY000",

    # ── Czech Republic (CZ) ───────────────────────────────────────────────────
    "Prague":                                   "CZ010",  # Praha
    "Brno":                                     "CZ064",  # Jihomoravský kraj
    "Ostrava":                                  "CZ080",  # Moravskoslezský kraj
    "Plzen":                                    "CZ032",  # Plzeňský kraj
    "Liberec":                                  "CZ051",  # Liberecký kraj
    "Olomouc":                                  "CZ071",  # Olomoucký kraj
    "Ústí nad Labem":                           "CZ042",  # Ústecký kraj
    "Chomutov - Jirkov":                        "CZ042",  # Ústecký kraj
    "Hradec Králové":                           "CZ052",  # Královéhradecký kraj
    "Pardubice":                                "CZ053",  # Pardubický kraj
    "Ceské Budejovice":                         "CZ031",  # Jihočeský kraj
    "Karviná":                                  "CZ080",  # Moravskoslezský kraj
    "Kladno":                                   "CZ020",  # Středočeský kraj
    "Zlín":                                     "CZ072",  # Zlínský kraj
    "Jihlava":                                  "CZ063",  # Kraj Vysočina
    "Most":                                     "CZ042",  # Ústecký kraj
    "Havírov":                                  "CZ080",  # Moravskoslezský kraj
    "Karlovy Vary":                             "CZ041",  # Karlovarský kraj

    # ── Germany (DE) ──────────────────────────────────────────────────────────
    "Berlin":                                   "DE300",  # Berlin
    "Hamburg":                                  "DE600",  # Hamburg
    "Munich":                                   "DE212",  # München, Kreisfreie Stadt
    "Cologne":                                  "DEA23",  # Köln, Kreisfreie Stadt
    "Frankfurt":                                "DE712",  # Frankfurt am Main
    "Stuttgart":                                "DE111",  # Stuttgart, Stadtkreis
    "Düsseldorf":                               "DEA11",  # Düsseldorf
    "Dortmund":                                 "DEA52",  # Dortmund
    "Essen":                                    "DEA13",  # Essen
    "Leipzig":                                  "DED51",  # Leipzig
    "Bremen":                                   "DE501",  # Bremen
    "Dresden":                                  "DED21",  # Dresden
    "Hanover":                                  "DE929",  # Hannover (Region)
    "Hannover":                                 "DE929",
    "Nuremberg":                                "DE213",  # Nürnberg
    "Duisburg":                                 "DEA12",  # Duisburg
    "Bochum":                                   "DEA51",  # Bochum
    "Wuppertal":                                "DEA14",  # Wuppertal
    "Bielefeld":                                "DEA41",  # Bielefeld
    "Bonn":                                     "DEA22",  # Bonn
    "Mannheim":                                 "DE126",  # Mannheim
    "Karlsruhe":                                "DE122",  # Karlsruhe, Stadtkreis
    "Wiesbaden":                                "DE714",  # Wiesbaden
    "Gelsenkirchen":                            "DEA32",  # Gelsenkirchen
    "Münster":                                  "DEA33",  # Münster
    "Augsburg":                                 "DE271",  # Augsburg
    "Chemnitz":                                 "DED41",  # Chemnitz
    "Aachen":                                   "DEA21",  # Aachen
    "Krefeld":                                  "DEA15",  # Krefeld
    "Halle":                                    "DEE02",  # Halle (Saale)
    "Magdeburg":                                "DEE03",  # Magdeburg
    "Freiburg im Breisgau":                     "DE131",  # Freiburg im Breisgau
    "Oberhausen":                               "DEA16",  # Oberhausen
    "Lübeck":                                   "DEF03",  # Lübeck
    "Erfurt":                                   "DEG01",  # Erfurt
    "Mainz":                                    "DEB35",  # Mainz
    "Rostock":                                  "DE803",  # Rostock
    "Kassel":                                   "DE734",  # Kassel
    "Hagen":                                    "DEA53",  # Hagen
    "Saarbrücken":                              "DEC01",  # Saarbrücken
    "Hamm":                                     "DEA55",  # Hamm
    "Mülheim an der Ruhr ":                     "DEA17",  # Mülheim an der Ruhr
    "Potsdam":                                  "DE401",  # Potsdam
    "Oldenburg":                                "DE922",  # Oldenburg (Oldenburg)
    "Osnabrück":                                "DE944",  # Osnabrück
    "Leverkusen":                               "DEA24",  # Leverkusen
    "Solingen":                                 "DEA19",  # Solingen
    "Herne":                                    "DEA56",  # Herne
    "Neuss":                                    "DEA1D",  # Rhein-Kreis Neuss
    "Heidelberg":                               "DE125",  # Heidelberg
    "Darmstadt":                                "DE711",  # Darmstadt
    "Regensburg":                               "DE232",  # Regensburg
    "Göttingen":                                "DE915",  # Göttingen
    "Paderborn":                                "DEA47",  # Paderborn
    "Würzburg":                                 "DE263",  # Würzburg
    "Wolfsburg":                                "DE913",  # Wolfsburg
    "Ulm":                                      "DE144",  # Ulm
    "Ingolstadt":                               "DE214",  # Ingolstadt
    "Heilbronn":                                "DE115",  # Heilbronn
    "Pforzheim":                                "DE123",  # Pforzheim
    "Reutlingen":                               "DE141",  # Reutlingen
    "Offenbach am Main":                        "DE716",  # Offenbach am Main
    "Flensburg":                                "DEF01",  # Flensburg
    "Kiel":                                     "DEF02",  # Kiel
    "Neumünster":                               "DEF05",  # Neumünster
    "Cottbus":                                  "DE403",  # Cottbus
    "Brandenburg an der Havel":                 "DE402",  # Brandenburg an der Havel
    "Frankfurt (Oder)":                         "DE404",  # Frankfurt (Oder)
    "Greifswald":                               "DE803",  # Vorpommern-Rügen / Greifswald
    "Stralsund":                                "DE803",  # Vorpommern-Rügen
    "Neubrandenburg":                           "DE804",  # Mecklenburgische Seenplatte
    "Schwerin":                                 "DE802",  # Schwerin
    "Koblenz":                                  "DEB11",  # Koblenz
    "Trier":                                    "DEB15",  # Trier
    "Kaiserslautern":                           "DEB32",  # Kaiserslautern
    "Ludwigshafen am Rhein":                    "DEB33",  # Ludwigshafen am Rhein
    "Frankenthal":                              "DEB31",  # Frankenthal
    "Speyer":                                   "DEB37",  # Speyer
    "Worms":                                    "DEB39",  # Worms
    "Bamberg":                                  "DE241",  # Bamberg
    "Schweinfurt":                              "DE261",  # Schweinfurt
    "Bayreuth":                                 "DE221",  # Bayreuth
    "Erlangen":                                 "DE252",  # Erlangen
    "Fürth":                                    "DE253",  # Fürth
    "Landshut":                                 "DE221",  # Landshut
    "Rosenheim":                                "DE21D",  # Rosenheim
    "Passau":                                   "DE222",  # Passau
    "Konstanz":                                 "DE138",  # Konstanz
    "Friedrichshafen":                          "DE148",  # Bodenseekreis
    "Villingen-Schwenningen":                   "DE133",  # Schwarzwald-Baar-Kreis
    "Recklinghausen":                           "DEA36",  # Recklinghausen
    "Siegen":                                   "DEA5A",  # Siegen-Wittgenstein
    "Bottrop":                                  "DEA31",  # Bottrop
    "Moers":                                    "DEA1B",  # Wesel
    "Witten":                                   "DEA54",  # Ennepe-Ruhr-Kreis
    "Iserlohn":                                 "DEA57",  # Märkisches Sauerland
    "Remscheid":                                "DEA18",  # Remscheid
    "Mönchengladbach":                          "DEA1C",  # Mönchengladbach
    "Bocholt":                                  "DEA34",  # Borken
    "Düren":                                    "DEA25",  # Düren
    "Aschaffenburg":                            "DE261",  # Aschaffenburg
    "Hanau":                                    "DE71E",  # Main-Kinzig-Kreis
    "Dessau-Roßlau":                            "DEE01",  # Dessau-Roßlau
    "Zwickau":                                  "DED44",  # Zwickau
    "Görlitz":                                  "DED2D",  # Görlitz
    "Weimar":                                   "DEG05",  # Weimar
    "Gera":                                     "DEG02",  # Gera
    "Jena":                                     "DEG03",  # Jena
    "Plauen":                                   "DED43",  # Vogtlandkreis
    "Wilhelmshaven":                            "DE925",  # Wilhelmshaven
    "Bremerhaven":                              "DE502",  # Bremerhaven
    "Hildesheim":                               "DE926",  # Hildesheim
    "Salzgitter":                               "DE912",  # Salzgitter
    "Braunschweig":                             "DE911",  # Braunschweig
    "Wolfsburg":                                "DE913",  # Wolfsburg
    "Kempten (Allgäu)":                         "DE27A",  # Kempten (Allgäu)
    "Tübingen":                                 "DE142",  # Tübingen
    "Ludwigsburg":                              "DE116",  # Ludwigsburg
    "Sindelfingen":                             "DE114",  # Böblingen
    "Esslingen":                                "DE113",  # Esslingen
    "Schwäbisch Gmünd":                         "DE119",  # Ostalbkreis
    "Marburg":                                  "DE722",  # Marburg-Biedenkopf
    "Wetzlar":                                  "DE721",  # Lahn-Dill-Kreis
    "Giessen":                                  "DE722",  # Gießen
    "Fulda":                                    "DE731",  # Fulda
    "Lüneburg":                                 "DE939",  # Lüneburg
    "Celle":                                    "DE929",  # Celle
    "Soest":                                    "DEA58",  # Soest
    "Bergisch Gladbach":                        "DEA2C",  # Rheinisch-Bergischer Kreis
    "Sankt Augustin":                           "DEA2B",  # Rhein-Sieg-Kreis
    "Offenburg":                                "DE137",  # Ortenaukreis
    "Göppingen":                                "DE117",  # Göppingen
    "Neu-Ulm":                                  "DE279",  # Neu-Ulm

    # ── Denmark (DK) ──────────────────────────────────────────────────────────
    "Copenhagen (metropolitan area)":           "DK011",  # Byen København
    "Aarhus":                                   "DK042",  # Aarhus
    "Odense":                                   "DK031",  # Fyn
    "Aalborg":                                  "DK050",  # Nordjylland

    # ── Estonia (EE) ──────────────────────────────────────────────────────────
    "Tallinn":                                  "EE001",  # Põhja-Eesti
    "Tallin?":                                  "EE001",
    "Narva":                                    "EE006",  # Kirde-Eesti
    "Tartu":                                    "EE009",  # Lõuna-Eesti

    # ── Greece (EL) ───────────────────────────────────────────────────────────
    "Athens (metropolitan area)":              "EL301",  # Βόρειος Τομέας Αθηνών
    "Thessaloniki (metropolitan area)":        "EL522",  # Θεσσαλονίκη
    "Patras":                                  "EL232",  # Αχαΐα
    "Irakleio":                                "EL431",  # Ηράκλειο
    "Larissa":                                 "EL141",  # Λάρισα
    "Volos":                                   "EL142",  # Μαγνησία
    "Kavala":                                  "EL515",  # Καβάλα
    "Serres":                                  "EL527",  # Σέρρες
    "Xanthi":                                  "EL511",  # Ξάνθη
    "Trikala":                                 "EL143",  # Τρίκαλα
    "Kalamata":                                "EL222",  # Μεσσηνία
    "Chania":                                  "EL432",  # Χανιά
    "Ioannina":                                "EL211",  # Ιωάννινα
    "Katerini":                                "EL521",  # Πιερία

    # ── Spain (ES) ────────────────────────────────────────────────────────────
    "Madrid (metropolitan area)":              "ES300",  # Comunidad de Madrid
    "Barcelona (metropolitan area)":           "ES511",  # Barcelona
    "Valencia (metropolitan area)":            "ES523",  # Valencia
    "Seville (metropolitan area)":             "ES618",  # Sevilla
    "Bilbao (metropolitan area)":              "ES213",  # Bizkaia
    "Granada (metropolitan area)":             "ES616",  # Granada
    "Pamplona (metropolitan area)":            "ES220",  # Comunidad Foral de Navarra
    "Santa Cruz de Tenerife (Metropolitan Area)": "ES709",  # Santa Cruz de Tenerife
    "Zaragoza":                                "ES243",  # Zaragoza
    "Málaga":                                  "ES617",  # Málaga
    "Las Palmas":                              "ES705",  # Las Palmas
    "Murcia":                                  "ES620",  # Región de Murcia
    "Palma de Mallorca":                       "ES532",  # Illes Balears
    "Valladolid":                              "ES413",  # Valladolid
    "Córdoba":                                 "ES615",  # Córdoba
    "Alicante":                                "ES521",  # Alicante/Alacant
    "Vigo":                                    "ES114",  # Pontevedra
    "Gijón":                                   "ES120",  # Asturias
    "A Coruña":                                "ES111",  # A Coruña
    "Vitoria/Gasteiz":                         "ES211",  # Álava
    "Oviedo":                                  "ES120",  # Asturias
    "Granada":                                 "ES616",
    "Santander":                               "ES130",  # Cantabria
    "Castellón de la Plana":                   "ES522",  # Castellón
    "Badajoz":                                 "ES431",  # Badajoz
    "Burgos":                                  "ES415",  # Burgos
    "Albacete":                                "ES421",  # Albacete
    "Logroño":                                 "ES230",  # La Rioja
    "Salamanca":                               "ES416",  # Salamanca
    "Tarragona":                               "ES514",  # Tarragona
    "León":                                    "ES418",  # León
    "Cádiz":                                   "ES611",  # Cádiz
    "Huelva":                                  "ES612",  # Huelva
    "Jaen":                                    "ES614",  # Jaén
    "Algeciras":                               "ES611",  # Campo de Gibraltar (Cádiz)
    "Almería":                                 "ES611",  # Almería
    "San Sebastián":                           "ES212",  # Guipúzcoa
    "Ferrol":                                  "ES111",  # A Coruña
    "Lugo":                                    "ES112",  # Lugo
    "Ourense":                                 "ES113",  # Ourense
    "Pontevedra":                              "ES114",  # Pontevedra
    "Santiago de Compostela":                  "ES111",  # A Coruña
    "Jerez de la Frontera":                    "ES611",  # Cádiz
    "Marbella":                                "ES617",  # Málaga
    "Benalmádena":                             "ES617",  # Málaga
    "Torremolinos":                            "ES617",  # Málaga
    "Fuengirola":                              "ES617",  # Málaga
    "Cartagena":                               "ES620",  # Región de Murcia
    "Elche":                                   "ES521",  # Alicante
    "Alcalá de Henares":                       "ES300",  # Comunidad de Madrid
    "Torrejón de Ardoz":                       "ES300",  # Comunidad de Madrid
    "Valdemoro":                               "ES300",  # Comunidad de Madrid
    "Collado Villalba":                        "ES300",  # Comunidad de Madrid
    "Alcalá de Guadaíra":                      "ES618",  # Sevilla
    "Dos Hermanas":                            "ES618",  # Sevilla
    "Ceuta":                                   "ES630",  # Ciudad de Ceuta
    "Melilla":                                 "ES640",  # Ciudad de Melilla
    "Ibiza":                                   "ES532",  # Illes Balears
    "Manresa":                                 "ES511",  # Barcelona
    "Mataró":                                  "ES511",  # Barcelona
    "Granollers":                              "ES511",  # Barcelona
    "Mollet del Vallès":                       "ES511",  # Barcelona
    "Vilanova i la Geltrú":                    "ES511",  # Barcelona
    "Igualada (metropolitan area)":            "ES511",  # Barcelona
    "Reus":                                    "ES514",  # Tarragona
    "Girona":                                  "ES512",  # Girona
    "Lleida":                                  "ES513",  # Lleida
    "Sagunto":                                 "ES523",  # Valencia
    "Gandia":                                  "ES523",  # Valencia
    "Torrelavega":                             "ES130",  # Cantabria
    "Alcoy":                                   "ES521",  # Alicante
    "Elda (metropolitan area)":                "ES521",  # Alicante
    "Benidorm":                                "ES521",  # Alicante
    "San Fernando":                            "ES611",  # Cádiz
    "Chiclana de la Frontera":                 "ES611",  # Cádiz
    "Sanlúcar de Barrameda":                   "ES611",  # Cádiz
    "Línea de la Concepción, La":              "ES611",  # Campo de Gibraltar (Cádiz)
    "Irun":                                    "ES212",  # Guipúzcoa
    "Avilés":                                  "ES120",  # Asturias
    "Toledo":                                  "ES422",  # Toledo
    "Ciudad real":                             "ES423",  # Ciudad Real
    "Guadalajara":                             "ES424",  # Guadalajara
    "Cuenca":                                  "ES422",  # Cuenca (same NUTS2 as Toledo)
    "Zamora":                                  "ES414",  # Zamora
    "Ávila":                                   "ES411",  # Ávila
    "Palencia":                                "ES419",  # Palencia
    "Segovia":                                 "ES412",  # Segovia
    "Soria":                                   "ES417",  # Soria
    "Ponferrada":                              "ES418",  # León
    "Lorca":                                   "ES620",  # Región de Murcia
    "Arrecife":                                "ES705",  # Las Palmas (Lanzarote)
    "Telde":                                   "ES705",  # Las Palmas (Gran Canaria)
    "Santa Lucía de Tirajana":                 "ES705",  # Las Palmas (Gran Canaria)
    "Puerto de la Cruz (metropolitan area)":   "ES709",  # Santa Cruz de Tenerife
    "San Vicente del Raspeig / Sant Vicent del Raspeig": "ES521",  # Alicante
    "El Puerto de Santa María\n":              "ES611",  # Cádiz
    "Torrevieja":                              "ES521",  # Alicante
    "Merida":                                  "ES431",  # Badajoz (Mérida)
    "Linares":                                 "ES614",  # Jaén
    "Albacete":                                "ES421",
    "Cáceres":                                 "ES432",  # Cáceres
    "Marbella":                                "ES617",

    # ── Finland (FI) ──────────────────────────────────────────────────────────
    "Helsinki (metropolitan area)":            "FI1B1",  # Helsinki-Uusimaa
    "Tampere":                                 "FI197",  # Pirkanmaa
    "Turku-Abo":                               "FI195",  # Varsinais-Suomi
    "Oulu":                                    "FI1D1",  # Pohjois-Pohjanmaa
    "Jyväskylä":                               "FI193",  # Keski-Suomi
    "Lahti":                                   "FI196",  # Päijät-Häme
    "Kuopio":                                  "FI1C2",  # Pohjois-Savo

    # ── France (FR) ───────────────────────────────────────────────────────────
    "Paris (metropolitan area)":               "FR101",  # Paris
    "Lyon":                                    "FRK21",  # Métropole de Lyon
    "Marseille":                               "FRL01",  # Bouches-du-Rhône
    "Toulouse":                                "FRJ21",  # Haute-Garonne
    "Nice":                                    "FRL03",  # Alpes-Maritimes
    "Nantes":                                  "FRG01",  # Loire-Atlantique
    "Strasbourg":                              "FRF11",  # Bas-Rhin
    "Bordeaux":                                "FRI12",  # Gironde
    "Lille":                                   "FRE11",  # Nord
    "Rennes":                                  "FRH01",  # Ille-et-Vilaine
    "Reims":                                   "FRF22",  # Marne
    "Grenoble":                                "FRK23",  # Isère
    "Dijon":                                   "FRK11",  # Côte-d'Or
    "Angers":                                  "FRG04",  # Maine-et-Loire
    "Nîmes":                                   "FRJ11",  # Gard
    "Clermont-Ferrand":                        "FRK11",  # Puy-de-Dôme
    "Montpellier":                             "FRJ12",  # Hérault
    "Tours":                                   "FRB02",  # Indre-et-Loire
    "Amiens":                                  "FRE21",  # Somme
    "Caen":                                    "FRD11",  # Calvados
    "Metz":                                    "FRF32",  # Moselle
    "Nancy":                                   "FRF31",  # Meurthe-et-Moselle
    "Rouen":                                   "FRD22",  # Seine-Maritime
    "Toulon":                                  "FRL04",  # Var
    "Orléans":                                 "FRB05",  # Loiret
    "Le Havre":                                "FRD22",  # Seine-Maritime
    "Mulhouse":                                "FRF12",  # Haut-Rhin
    "Brest":                                   "FRH02",  # Finistère
    "Perpignan":                               "FRJ13",  # Pyrénées-Orientales
    "Besançon":                                "FRC21",  # Doubs
    "Limoges":                                 "FRI23",  # Haute-Vienne
    "Avignon":                                 "FRL02",  # Vaucluse
    "Cannes":                                  "FRL03",  # Alpes-Maritimes
    "Bayonne":                                 "FRI31",  # Pyrénées-Atlantiques
    "Saint-Étienne":                           "FRK24",  # Loire
    "Annecy":                                  "FRK27",  # Haute-Savoie
    "Chambéry":                                "FRK26",  # Savoie
    "La Rochelle":                             "FRI14",  # Charente-Maritime
    "Lorient":                                 "FRH03",  # Morbihan
    "Vannes":                                  "FRH03",  # Morbihan
    "Quimper":                                 "FRH02",  # Finistère
    "Saint-Brieuc":                            "FRH01",  # Côtes-d'Armor
    "Saint-Nazaire":                           "FRG01",  # Loire-Atlantique
    "Dunkirk":                                 "FRE12",  # Nord
    "Calais":                                  "FRE12",  # Pas-de-Calais
    "Valenciennes":                            "FRE12",  # Nord
    "Boulogne-sur-Mer":                        "FRE12",  # Pas-de-Calais
    "Tarbes":                                  "FRJ22",  # Hautes-Pyrénées
    "Pau":                                     "FRI31",  # Pyrénées-Atlantiques
    "Le Mans":                                 "FRG05",  # Sarthe
    "Poitiers":                                "FRI22",  # Vienne
    "Angoulême":                               "FRI11",  # Charente
    "Niort":                                   "FRI14",  # Deux-Sèvres
    "Troyes":                                  "FRF23",  # Aube
    "Châlons-en-Champagne":                    "FRF22",  # Marne
    "Roanne":                                  "FRK24",  # Loire
    "Belfort":                                 "FRC22",  # Territoire de Belfort
    "Béziers":                                 "FRJ12",  # Hérault
    "Albi":                                    "FRJ24",  # Tarn
    "Valence":                                 "FRK25",  # Drôme
    "Bourges":                                 "FRB01",  # Cher
    "Évreux":                                  "FRD23",  # Eure
    "Charleville-Mézières":                    "FRF21",  # Ardennes
    "Châteauroux":                             "FRB03",  # Indre
    "Cherbourg":                               "FRD12",  # Manche
    "Saint-Quentin":                           "FRE21",  # Aisne
    "Colmar":                                  "FRF12",  # Haut-Rhin
    "Montbéliard":                             "FRC21",  # Doubs
    "Chalon-sur-Saône":                        "FRK12",  # Saône-et-Loire
    "Ajaccio":                                 "FRM01",  # Corse-du-Sud
    "Brive-la-Gaillarde":                      "FRI21",  # Corrèze
    "Arras":                                   "FRE12",  # Pas-de-Calais
    "Douai":                                   "FRE12",  # Nord
    "Doway":                                   "FRE12",  # Nord (Douai)
    "Fréjus":                                  "FRL04",  # Var
    "Aix-en-Provence":                         "FRL01",  # Bouches-du-Rhône
    "Aubagne":                                 "FRL01",  # Bouches-du-Rhône
    "Martigues":                               "FRL01",  # Bouches-du-Rhône
    "CA de Sophia-Antipolis":                  "FRL03",  # Alpes-Maritimes
    "Versailles":                              "FR102",  # Yvelines
    "Melun":                                   "FR104",  # Seine-et-Marne
    "Creil":                                   "FR221",  # Oise
    "Beauvais":                                "FR221",  # Oise
    "Compiègne":                               "FR221",  # Oise
    "Meaux":                                   "FR104",  # Seine-et-Marne
    "Evry":                                    "FR107",  # Essonne
    "Marne la Vallée":                         "FR104",  # Seine-et-Marne / Paris Est
    "Cergy-Pontoise":                          "FR108",  # Val-d'Oise
    "Sénart":                                  "FR104",  # Seine-et-Marne
    "Saint-Quentin en Yvelines":               "FR102",  # Yvelines
    "Annemasse":                               "FRK27",  # Haute-Savoie
    "Argenteuil - Bezons":                     "FR108",  # Val-d'Oise
    "Communauté d'Agglomération Seine-Essonne (CASE)": "FR107",  # Essonne
    "Communauté d'Agglomération Les Portes de l'Essonne": "FR107",  # Essonne
    "CA des Lacs de l'Essonne":               "FR107",  # Essonne
    "Communauté d'Agglomération Europ'Essonne": "FR107",  # Essonne
    "Communauté d'Agglomération du Val d'Orge": "FR107",  # Essonne
    "Plateau de Saclay":                       "FR107",  # Essonne
    "CA Val et Forêt":                         "FR108",  # Val-d'Oise
    "CA de la Vallée de Montmorency":          "FR108",  # Val-d'Oise
    "Communauté d'Agglomération Val de France": "FR108",  # Val-d'Oise
    "Communauté d'Agglomération Val de Seine": "FR106",  # Hauts-de-Seine
    "CA des deux Rives de la Seine":           "FR106",  # Hauts-de-Seine / Yvelines
    "Communauté d'agglomération de Mantes-en-Yvelines": "FR102",  # Yvelines
    "CC des Coteaux de la Seine":              "FR102",  # Yvelines
    "Communauté de Communes de la Boucle de la Seine": "FR102",  # Yvelines
    "Communauté de Communes de lOuest de la Plaine de France (CCOPF)": "FR108",  # Val-d'Oise
    "Communauté d'Agglomération Val d'Yerres Val de Seine (CAVYVS)": "FR107",  # Essonne
    "Communauté d'agglomération de Marne et Chantereine": "FR105",  # Seine-et-Marne / Seine-St-Denis
    "Communauté d'agglomération de la Brie Francilienne": "FR104",  # Seine-et-Marne
    "Communauté d'Agglomération Val Parisis":  "FR108",  # Val-d'Oise
    "Communauté d'Agglomération de Lens  Liévin": "FRE12",  # Pas-de-Calais
    "Hénin - Carvin":                          "FRE12",  # Pas-de-Calais

    # ── Croatia (HR) ──────────────────────────────────────────────────────────
    "Zagreb":                                  "HR050",  # Grad Zagreb
    "Split":                                   "HR035",  # Splitsko-dalmatinska županija
    "Rijeka":                                  "HR031",  # Primorsko-goranska županija
    "Osijek":                                  "HR025",  # Osječko-baranjska županija
    "Zadar":                                   "HR033",  # Zadarska županija
    "Pula":                                    "HR036",  # Istarska županija
    "Slavonski Brod":                          "HR024",  # Brodsko-posavska županija

    # ── Hungary (HU) ──────────────────────────────────────────────────────────
    "Budapest":                                "HU110",  # Budapest
    "Debrecen":                                "HU321",  # Hajdú-Bihar
    "Miskolc":                                 "HU311",  # Borsod-Abaúj-Zemplén
    "Pécs":                                    "HU231",  # Baranya
    "Győr":                                    "HU221",  # Győr-Moson-Sopron
    "Gyõr":                                    "HU221",
    "Nyíregyháza":                             "HU323",  # Szabolcs-Szatmár-Bereg
    "Kecskemét":                               "HU331",  # Bács-Kiskun
    "Székesfehérvár":                          "HU211",  # Fejér
    "Szombathely":                             "HU222",  # Vas
    "Szolnok":                                 "HU322",  # Jász-Nagykun-Szolnok
    "Tatabánya":                               "HU212",  # Komárom-Esztergom
    "Kaposvár":                                "HU232",  # Somogy
    "Sopron":                                  "HU221",  # Győr-Moson-Sopron
    "Zalaegerszeg":                            "HU223",  # Zala
    "Eger":                                    "HU312",  # Heves
    "Szeged":                                  "HU333",  # Csongrád-Csanád
    "Veszprém":                                "HU213",  # Veszprém
    "Dunaújváros":                             "HU211",  # Fejér
    "Békéscsaba":                              "HU332",  # Békés

    # ── Ireland (IE) ──────────────────────────────────────────────────────────
    "Dublin (metropolitan area)":              "IE061",  # Dublin
    "Cork":                                    "IE025",  # Cork
    "Limerick":                                "IE031",  # Mid-West
    "Galway":                                  "IE013",  # West
    "Waterford":                               "IE024",  # South-East

    # ── Iceland (IS) — not in NUTS, use national code ─────────────────────────
    "Reykjavík":                               "IS",

    # ── Italy (IT) ────────────────────────────────────────────────────────────
    "Rome":                                    "ITI43",  # Roma
    "Milan (metropolitan area)":              "ITC4C",  # Milano
    "Naples (metropolitan area)":             "ITF33",  # Napoli
    "Turin":                                  "ITC11",  # Torino
    "Palermo":                                "ITG12",  # Palermo
    "Genoa":                                  "ITC33",  # Genova
    "Bologna":                                "ITH55",  # Bologna
    "Florence":                               "ITI14",  # Firenze
    "Bari":                                   "ITF47",  # Bari
    "Catania":                                "ITG17",  # Catania
    "Venice":                                 "ITH35",  # Venezia
    "Verona":                                 "ITH31",  # Verona
    "Messina":                                "ITG13",  # Messina
    "Padua":                                  "ITH36",  # Padova
    "Trieste":                                "ITH44",  # Trieste
    "Brescia":                                "ITC47",  # Brescia
    "Taranto":                                "ITF43",  # Taranto
    "Bergamo":                                "ITC16",  # Bergamo
    "Reggio Calabria":                        "ITF65",  # Reggio di Calabria
    "Modena":                                 "ITH53",  # Modena
    "Reggio Emilia":                          "ITH52",  # Reggio nell'Emilia
    "Perugia":                                "ITI21",  # Perugia
    "Livorno":                                "ITI16",  # Livorno
    "Cagliari":                               "ITG25",  # Cagliari
    "Foggia":                                 "ITF45",  # Foggia
    "Salerno":                                "ITF35",  # Salerno
    "Rimini":                                 "ITH59",  # Rimini
    "Syracuse":                               "ITG15",  # Siracusa
    "Ferrara":                                "ITH57",  # Ferrara
    "Sassari":                                "ITG28",  # Sassari
    "Pescara":                                "ITF14",  # Pescara
    "Ancona":                                 "ITI31",  # Ancona
    "Prato":                                  "ITI13",  # Prato
    "Lecce":                                  "ITF44",  # Lecce
    "La Spezia":                              "ITC32",  # La Spezia
    "Udine":                                  "ITH42",  # Udine
    "Bolzano":                                "ITH10",  # Bolzano/Bozen
    "Trento":                                 "ITH20",  # Trento
    "Treviso":                                "ITH34",  # Treviso
    "Pisa":                                   "ITI17",  # Pisa
    "Parma":                                  "ITH51",  # Parma
    "Vicenza":                                "ITH32",  # Vicenza
    "Novara":                                 "ITC15",  # Novara
    "Piacenza":                               "ITH51",  # Piacenza
    "Como":                                   "ITC14",  # Como
    "Varese":                                 "ITC13",  # Varese
    "Lecco":                                  "ITC19",  # Lecco
    "Gallarate":                              "ITC13",  # Varese
    "Busto Arsizio":                          "ITC13",  # Varese
    "Saronno":                                "ITC13",  # Varese
    "Savona":                                 "ITC31",  # Savona
    "Cosenza":                                "ITF61",  # Cosenza
    "Caserta":                                "ITF31",  # Caserta
    "Avellino":                               "ITF34",  # Avellino
    "Brindisi":                               "ITF42",  # Brindisi
    "Catanzaro":                              "ITF63",  # Catanzaro
    "Potenza":                                "ITF51",  # Potenza
    "Matera":                                 "ITF52",  # Matera
    "L'Aquila":                               "ITF11",  # L'Aquila
    "Campobasso":                             "ITF22",  # Campobasso
    "Terni":                                  "ITI22",  # Terni
    "Latina":                                 "ITI45",  # Latina
    "Ragusa":                                 "ITG16",  # Ragusa
    "Trapani":                                "ITG11",  # Trapani
    "Gela":                                   "ITG14",  # Caltanissetta
    "Massa":                                  "ITI11",  # Massa-Carrara
    "Grosseto":                               "ITI18",  # Grosseto
    "Asti":                                   "ITC17",  # Asti
    "Alessandria":                            "ITC18",  # Alessandria
    "Cremona":                                "ITC48",  # Cremona
    "Molfetta":                               "ITF47",  # Bari (province)
    "Barletta":                               "ITF41",  # Barletta-Andria-Trani
    "Trani":                                  "ITF41",  # Barletta-Andria-Trani
    "Andria":                                 "ITF41",  # Barletta-Andria-Trani
    "Bisceglie":                              "ITF47",  # Bari (province)
    "Bitonto":                                "ITF47",  # Bari (province)
    "Altamura":                               "ITF47",  # Bari (province)
    "Cerignola":                              "ITF45",  # Foggia (province)
    "Battipaglia":                            "ITF35",  # Salerno (province)
    "Forlì":                                  "ITH58",  # Forlì-Cesena
    "Carpi":                                  "ITH53",  # Modena (province)
    "Pavia":                                  "ITC48",  # Pavia
    "Pordenone":                              "ITH41",  # Pordenone
    "Sassuolo":                               "ITH53",  # Modena (province)
    "Ravenna":                                "ITH57",  # Ravenna
    "Arezzo":                                 "ITI19",  # Arezzo
    "Acireale":                               "ITG17",  # Catania (province)
    "Bagheria":                               "ITG12",  # Palermo (province)
    "Anzio":                                  "ITI43",  # Roma (province)
    "Pesaro":                                 "ITI32",  # Pesaro e Urbino

    # ── Lithuania (LT) ────────────────────────────────────────────────────────
    "Vilnius":                                "LT011",  # Vilniaus apskritis
    "Kaunas":                                 "LT023",  # Kauno apskritis
    "Klaipėda":                               "LT003",  # Klaipėdos apskritis
    "Klaip?da":                               "LT003",
    "Šiauliai":                               "LT007",  # Šiaulių apskritis
    "Siauliai ":                              "LT007",
    "Panevėžys":                              "LT005",  # Panevėžio apskritis
    "Paneveys":                               "LT005",
    "Alytus":                                 "LT001",  # Alytaus apskritis

    # ── Latvia (LV) ───────────────────────────────────────────────────────────
    "Riga":                                   "LV006",  # Rīga
    "Daugavpils":                             "LV005",  # Latgale
    "Liepaja":                                "LV003",  # Kurzeme
    "Jelgava":                                "LV007",  # Zemgale

    # ── Luxembourg (LU) ───────────────────────────────────────────────────────
    "Luxembourg":                             "LU000",  # Luxembourg

    # ── Malta (MT) ────────────────────────────────────────────────────────────
    "Valletta":                               "MT001",  # Malta Island

    # ── Netherlands (NL) ──────────────────────────────────────────────────────
    "Amsterdam":                              "NL326",  # Groot-Amsterdam
    "Rotterdam":                              "NL33A",  # Groot-Rijnmond
    "The Hague":                              "NL332",  # Agglomeratie 's-Gravenhage
    "Utrecht":                                "NL31U",  # Utrecht (gemeente)
    "Eindhoven":                              "NL414",  # Zuidoost-Noord-Brabant
    "Tilburg":                                "NL412",  # Midden-Noord-Brabant
    "Groningen":                              "NL111",  # Oost-Groningen
    "Almere":                                 "NL230",  # Flevoland
    "Breda":                                  "NL411",  # West-Noord-Brabant
    "Nijmegen":                               "NL226",  # Arnhem/Nijmegen
    "Enschede":                               "NL211",  # Twente
    "Haarlem":                                "NL325",  # Groot-Amsterdam / Kennemerland
    "Haarlemmermeer":                         "NL325",  # Kennemerland
    "Arnhem":                                 "NL226",  # Arnhem/Nijmegen
    "Zaanstad":                               "NL326",  # Groot-Amsterdam
    "Amersfoort":                             "NL31U",  # Utrecht (province)
    "Apeldoorn":                              "NL221",  # Veluwe
    "Zoetermeer":                             "NL332",  # Agglomeratie 's-Gravenhage
    "Zwolle":                                 "NL213",  # Noord-Overijssel
    "Maastricht":                             "NL423",  # Maastricht en Mergelland
    "Leiden":                                 "NL33B",  # Leiden en Bollenstreek
    "Dordrecht":                              "NL33B",  # Drechtsteden
    "Deventer":                               "NL212",  # Oost-Overijssel
    "Hengelo":                                "NL211",  # Twente
    "Almelo":                                 "NL211",  # Twente
    "Hilversum":                              "NL31H",  # Het Gooi en Vechtstreek
    "Leeuwarden":                             "NL112",  # Friesland
    "Assen":                                  "NL131",  # Noord-Drenthe
    "Lelystad":                               "NL230",  # Flevoland
    "Purmerend":                              "NL326",  # Groot-Amsterdam
    "Gouda":                                  "NL33B",  # Oost-Zuid-Holland
    "Middelburg":                             "NL341",  # Zeeland
    "Roosendaal":                             "NL411",  # West-Noord-Brabant
    "Bergen op Zoom":                         "NL411",  # West-Noord-Brabant
    "Sittard-Geleen":                         "NL423",  # Westelijke Mijnstreek
    "Helmond":                                "NL414",  # Zuidoost-Noord-Brabant
    "Venlo":                                  "NL422",  # Noord-Limburg
    "'s-Hertogenbosch":                       "NL413",  # Noordoost-Noord-Brabant
    "Nissewaard":                             "NL33A",  # Groot-Rijnmond
    "Veenendaal":                             "NL31U",  # Utrecht (province)
    "Soest":                                  "NL31U",  # Utrecht (province)
    "Ede":                                    "NL221",  # Veluwe
    "Hoorn":                                  "NL327",  # Kop van Noord-Holland
    "Heemskerk":                              "NL325",  # IJmond
    "Heerlen":                                "NL423",  # Parkstad Limburg
    "Alphen aan den Rijn":                    "NL33B",  # Oost-Zuid-Holland
    "Oss":                                    "NL413",  # Noordoost-Noord-Brabant
    "Dordrecht":                              "NL33C",  # Drechtsteden

    # ── Norway (NO) — not in NUTS, use national code ──────────────────────────
    "Oslo":                                   "NO011",  # Oslo
    "Bergen":                                 "NO051",  # Hordaland
    "Stavanger":                              "NO043",  # Rogaland
    "Trondheim":                              "NO061",  # Sør-Trøndelag
    "Tromsø":                                "NO072",  # Troms
    "Kristiansand":                           "NO042",  # Vest-Agder

    # ── Poland (PL) ───────────────────────────────────────────────────────────
    "Warsaw":                                 "PL911",  # Miasto Warszawa
    "Kraków":                                 "PL213",  # Miasto Kraków
    "Łódź":                                   "PL711",  # Miasto Łódź
    "Lódz":                                   "PL711",
    "Wroclaw":                                "PL514",  # Miasto Wrocław
    "Poznań":                                 "PL415",  # Miasto Poznań
    "Poznan":                                 "PL415",
    "Gdańsk":                                 "PL634",  # Trójmiejski
    "Gda?sk":                                 "PL634",
    "Szczecin":                               "PL424",  # Miasto Szczecin
    "Bydgoszcz":                              "PL613",  # Miasto Bydgoszcz
    "Lublin":                                 "PL814",  # Miasto Lublin
    "Katowice / Metropolitan Association of Upper Silesia": "PL22A",
    "Metropolitan Association of Upper Silesia": "PL22A",  # Katowicki
    "Białystok":                              "PL841",  # Miasto Białystok
    "Bialystok":                              "PL841",
    "Gdynia":                                 "PL634",  # Trójmiejski
    "Częstochowa":                            "PL224",  # Miasto Częstochowa
    "Czestochowa":                            "PL224",
    "Radom":                                  "PL921",  # Radomski
    "Sosnowiec":                              "PL22A",  # Katowicki
    "Toruń":                                  "PL613",  # Bydgosko-Toruński
    "Torun":                                  "PL613",
    "Kielce":                                 "PL721",  # Miasto Kielce
    "Rzeszów":                                "PL823",  # Miasto Rzeszów
    "Rzeszów":                                "PL823",
    "Gliwice":                                "PL22A",  # Katowicki
    "Zabrze":                                 "PL22A",
    "Olsztyn":                                "PL622",  # Miasto Olsztyn
    "Bielsko-Biala":                          "PL225",  # Bielski
    "Rybnik":                                 "PL227",  # Rybnicki
    "Rybnik":                                 "PL227",
    "Wałbrzych":                              "PL517",  # Wałbrzyski
    "Walbrzych":                              "PL517",
    "Zielona Góra":                           "PL432",  # Miasto Zielona Góra
    "Zielona Góra":                           "PL432",
    "Opole":                                  "PL524",  # Miasto Opole
    "Gorzów Wielkopolski":                    "PL431",  # Miasto Gorzów Wlkp.
    "Gorzów Wielkopolski":                    "PL431",
    "Legnica":                                "PL516",  # Legnicko-Głogowski
    "Koszalin":                               "PL426",  # Koszaliński
    "Tarnów":                                 "PL217",  # Tarnowski
    "Tarnów":                                 "PL217",
    "Płock":                                  "PL922",  # Płocki
    "Plock":                                  "PL922",
    "Elbląg":                                 "PL621",  # Elbląski
    "Elbl?g":                                 "PL621",
    "Włocławek":                              "PL619",  # Włocławski
    "Wloclawek":                              "PL619",
    "Tychy":                                  "PL22A",  # Katowicki
    "Nowy Sącz":                              "PL218",  # Nowosądecki
    "Nowy Sacz":                              "PL218",
    "Piotrków Trybunalski":                   "PL712",  # Piotrkowski
    "Siemianowice Śląskie":                   "PL22A",
    "Siedlce":                                "PL912",  # Siedlecki
    "Stalowa Wola":                           "PL824",  # Stalowowolski
    "Ostrów Wielkopolski":                    "PL416",  # Kaliski
    "Kalisz":                                 "PL416",  # Kaliski
    "Łomża":                                  "PL842",  # Łomżyński
    "Lomza":                                  "PL842",
    "Przemyśl":                               "PL822",  # Przemyski
    "Przemysl":                               "PL822",
    "Grudziądz":                              "PL616",  # Grudziądzki
    "Grudziadz":                              "PL616",
    "Gniezno":                                "PL418",  # Gnieźnieński
    "Jelenia Góra":                           "PL515",  # Jeleniogórski
    "Jelenia Góra":                           "PL515",
    "Inowrocław":                             "PL617",  # Inowrocławski
    "Inowroclaw":                             "PL617",
    "Konin":                                  "PL414",  # Koniński
    "Suwałki":                                "PL843",  # Suwalski
    "Suwa?ki":                                "PL843",
    "Swidnica":                               "PL517",  # Świdnicki
    "Stargard":                               "PL428",  # Stargardzki
    "Slupsk":                                 "PL636",  # Słupski
    "Tczew":                                  "PL634",  # Starogardzki
    "Ostrowiec Świętokrzyski":                "PL722",
    "Ostrowiec Swietokrzyski":                "PL722",
    "Zamosc":                                 "PL812",  # Zamojski
    "Glogów":                                 "PL516",  # Legnicko-Głogowski
    "Glogów":                                 "PL516",
    "Tomaszów Mazowiecki":                    "PL714",
    "Tomaszów Mazowiecki":                    "PL714",
    "Leszno":                                 "PL417",  # Leszczyński
    "Zgierz":                                 "PL711",  # Łódź agglomeration
    "Pabianice":                              "PL711",
    "Chelm":                                  "PL811",  # Chełmski
    "Ełk":                                    "PL623",  # Ełcki
    "E?k":                                    "PL623",
    "Łubin":                                  "PL516",
    "Lubin":                                  "PL516",
    "Piła":                                   "PL411",
    "Pi?a":                                   "PL411",
    "Jastrzębie-Zdrój":                       "PL227",  # Rybnicki
    "Jastrzebie-Zdrój":                       "PL227",
    "Żory":                                   "PL227",
    "Zory":                                   "PL227",

    # ── Portugal (PT) ─────────────────────────────────────────────────────────
    "Lisbon (metropolitan area)":             "PT170",  # Área Metropolitana de Lisboa
    "Porto (metropolitan area)":             "PT11A",  # Área Metropolitana do Porto
    "Braga":                                  "PT111",  # Cávado
    "Funchal":                                "PT300",  # Região Autónoma da Madeira
    "Ponta Delgada":                          "PT200",  # Região Autónoma dos Açores
    "Coimbra":                                "PT166",  # Região de Coimbra
    "Setúbal":                                "PT170",  # AML (Setúbal sub-region)
    "Sintra":                                 "PT170",  # AML
    "Guimarães":                              "PT112",  # Ave
    "Aveiro":                                 "PT161",  # Região de Aveiro
    "Faro":                                   "PT150",  # Algarve
    "Viana do Castelo":                       "PT116",  # Alto Minho
    "Viseu":                                  "PT168",  # Viseu Dão-Lafões
    "Vila Franca de Xira":                    "PT170",  # AML
    "Paredes":                                "PT11A",  # AMP
    "Póvoa de Varzim":                        "PT11A",  # AMP

    # ── Romania (RO) ──────────────────────────────────────────────────────────
    "Bucharest":                              "RO321",  # Municipiul București
    "Bucarest":                               "RO321",
    "Cluj-Napoca":                            "RO113",  # Cluj
    "Timișoara":                              "RO124",  # Timiș
    "Timisoara":                              "RO124",
    "Iași":                                   "RO212",  # Iași
    "Ia?i":                                   "RO212",
    "Constanța":                              "RO223",  # Constanța
    "Constan?a":                              "RO223",
    "Craiova":                                "RO411",  # Dolj
    "Brașov":                                 "RO122",  # Brașov
    "Bra?ov":                                 "RO122",
    "Galați":                                 "RO224",  # Galați
    "Galati":                                 "RO224",
    "Ploiești":                               "RO316",  # Prahova
    "Ploiesti":                               "RO316",
    "Oradea":                                 "RO111",  # Bihor
    "Brăila":                                 "RO221",  # Brăila
    "Braila":                                 "RO221",
    "Bacău":                                  "RO211",  # Bacău
    "Bac?u":                                  "RO211",
    "Arad":                                   "RO121",  # Arad
    "Pitești":                                "RO313",  # Argeș
    "Pite?ti":                                "RO313",
    "Sibiu":                                  "RO126",  # Sibiu
    "Târgu Mureș":                            "RO125",  # Mureș
    "Târgu Mures":                            "RO125",
    "Baia Mare":                              "RO114",  # Maramureș
    "Buzău":                                  "RO222",  # Buzău
    "Buz?u":                                  "RO222",
    "Botosani":                               "RO212",  # Botoșani
    "Boto?ani":                               "RO212",
    "Satu Mare":                              "RO115",  # Satu Mare
    "Râmnicu Vâlcea":                         "RO415",  # Vâlcea
    "Drobeta-Turnu Severin":                  "RO413",  # Mehedinți
    "Suceava":                                "RO215",  # Suceava
    "Piatra Neamț":                           "RO214",  # Neamț
    "Piatra Neam?\n":                         "RO214",
    "Roman":                                  "RO214",  # Neamț
    "Tulcea":                                 "RO225",  # Tulcea
    "Focșani":                                "RO226",  # Vrancea
    "Foc?ani":                                "RO226",
    "Giurgiu":                                "RO312",  # Giurgiu
    "Bistrita":                               "RO112",  # Bistrița-Năsăud
    "Bistri?a":                               "RO112",
    "Târgoviște":                             "RO315",  # Dâmbovița
    "Târgovi?te":                             "RO315",
    "Târgu Jiu":                              "RO412",  # Gorj
    "Slatina":                                "RO414",  # Olt
    "Drobeta-Turnu Severin":                  "RO413",
    "Bârlad":                                 "RO216",  # Vaslui
    "Alba Iulia":                             "RO121",  # Alba
    "Călărași":                               "RO311",  # Călărași
    "C?l?ra?i":                               "RO311",

    # ── Sweden (SE) ───────────────────────────────────────────────────────────
    "Stockholm (metropolitan area)":          "SE110",  # Stockholms län
    "Göteborg":                               "SE232",  # Göteborgs och Bohus
    "Malmö":                                  "SE224",  # Malmö-Lund
    "Uppsala":                                "SE121",  # Uppsala län
    "Västerås":                               "SE122",  # Västmanlands län
    "Örebro":                                 "SE124",  # Örebro län
    "Linköping":                              "SE213",  # Östergötlands län
    "Helsingborg":                            "SE224",  # Skåne
    "Jönköping":                              "SE211",  # Jönköpings län
    "Norrköping":                             "SE213",  # Östergötlands län
    "Umeå":                                   "SE331",  # Västernorrlands / Västerbottens
    "Lund":                                   "SE224",  # Skåne
    "Borås":                                  "SE231",  # Älvsborgs
    "Sundsvall":                              "SE332",  # Västernorrlands

    # ── Slovakia (SK) ─────────────────────────────────────────────────────────
    "Bratislava":                             "SK010",  # Bratislavský kraj
    "Košice":                                 "SK042",  # Košický kraj
    "Koice":                                  "SK042",
    "Prešov":                                 "SK041",  # Prešovský kraj
    "Preov":                                  "SK041",
    "Žilina":                                 "SK031",  # Žilinský kraj
    "ilina":                                  "SK031",
    "Banská Bystrica":                        "SK032",  # Banskobystrický kraj
    "Banská Bystrica":                        "SK032",
    "Nitra":                                  "SK023",  # Nitriansky kraj
    "Trnava":                                 "SK021",  # Trnavský kraj
    "Trenčín":                                "SK022",  # Trenčiansky kraj
    "Trencín":                                "SK022",

    # ── Slovenia (SI) ─────────────────────────────────────────────────────────
    "Ljubljana":                              "SI041",  # Osrednjeslovenska
    "Maribor":                                "SI032",  # Podravska

    # ── Switzerland (CH) — not in NUTS, use cantonal codes ────────────────────
    "Geneva (metropolitan area)":             "CH013",  # Genève
    "Zürich (metropolitan area)":             "CH011",  # Zürich
    "Basel (metropolitan area)":              "CH031",  # Basel-Stadt
    "Lausanne (metropolitan area)":           "CH022",  # Vaud
    "Bern (metropolitan area)":               "CH021",  # Bern
    "Lugano (metropolitan area)":             "CH070",  # Ticino
    "Lucerne (metropolitan area)":            "CH061",  # Luzern
    "St. Gallen":                             "CH055",  # St. Gallen
    "Winterthur":                             "CH011",  # Zürich (Kanton)
    "Biel/Bienne":                            "CH021",  # Bern (Kanton)

    # ── United Kingdom (UK) ───────────────────────────────────────────────────
    "London (metropolitan area)":             "UKI",    # London
    "Manchester (metropolitan area)":         "UKD3",   # Greater Manchester
    "Birmingham":                             "UKG31",  # Birmingham
    "West Midlands urban area":               "UKG3",   # West Midlands
    "Liverpool (metropolitan area)":          "UKD7",   # Merseyside
    "Glasgow (metropolitan area)":            "UKM82",  # Glasgow City
    "Sheffield":                              "UKE32",  # Sheffield
    "Leeds":                                  "UKE42",  # Leeds
    "Bristol":                                "UKK11",  # Bristol, City of
    "Edinburgh":                              "UKM25",  # City of Edinburgh
    "Cardiff":                                "UKL22",  # Cardiff
    "Leicester (metropolitan area)":          "UKF21",  # Leicester
    "Belfast (metropolitan area)":            "UKN06",  # Belfast
    "Nottingham (metropolitan area)":         "UKF14",  # Nottingham
    "Tyneside conurbation":                   "UKC23",  # Tyneside
    "Portsmouth (metropolitan area)":         "UKJ31",  # Portsmouth
    "Brighton and Hove (metropolitan area)":  "UKJ21",  # Brighton and Hove
    "Southampton (metropolitan area)":        "UKJ32",  # Southampton
    "Reading (metropolitan area)":            "UKJ11",  # Reading
    "Stoke-on-Trent (metropolitan area)":     "UKG22",  # Stoke-on-Trent
    "Preston (metropolitan area)":            "UKD46",  # Preston
    "Blackpool (metropolitan area)":          "UKD48",  # Blackpool
    "Middlesbrough":                          "UKC14",  # Middlesbrough
    "Sunderland":                             "UKC24",  # Sunderland
    "Southend-on-Sea (metropolitan area)":    "UKH34",  # Southend-on-Sea
    "Coventry":                               "UKG34",  # Coventry
    "Luton":                                  "UKH23",  # Luton
    "Warrington":                             "UKD36",  # Warrington
    "Derby":                                  "UKF11",  # Derby
    "Northampton":                            "UKF21",  # Northamptonshire
    "Peterborough":                           "UKH12",  # Peterborough
    "Plymouth":                               "UKK41",  # Plymouth
    "Blackburn with Darwen":                  "UKD44",  # Blackburn with Darwen
    "Bradford":                               "UKE41",  # Bradford
    "Kingston-upon-Hull":                     "UKE11",  # Kingston upon Hull
    "Swindon":                                "UKK14",  # Swindon
    "Dundee City":                            "UKM31",  # Dundee City
    "Aberdeen":                               "UKM50",  # Aberdeen City
    "Cambridge":                              "UKH11",  # Cambridge
    "Oxford":                                 "UKJ14",  # Oxford
    "York":                                   "UKE21",  # York
    "Exeter":                                 "UKK42",  # Exeter
    "Gloucester":                             "UKK13",  # Gloucester
    "Norwich":                                "UKH14",  # Norwich
    "Ipswich":                                "UKH34",  # Ipswich
    "Lincoln":                                "UKF30",  # Lincolnshire
    "Carlisle":                               "UKD13",  # Carlisle
    "Newport":                                "UKL23",  # Newport
    "Swansea":                                "UKL21",  # Swansea
    "Wrexham":                                "UKL13",  # Wrexham
    "North East Lincolnshire":               "UKE13",
    "Thurrock":                               "UKH34",
    "Medway":                                 "UKJ22",
    "Doncaster":                              "UKE31",
    "Rotherham":                              "UKE32",
    "Barnsley":                               "UKE31",
    "Wakefield":                              "UKE43",
    "Kirklees":                               "UKE43",
    "Halton":                                 "UKD36",
    "Dartington":                             "UKK42",
    "Darlington":                             "UKC13",
    "Hartlepool":                             "UKC12",
    "Stockton-on-Tees":                       "UKC14",
    "Hyndburn":                               "UKD45",
    "Burnley":                                "UKD43",
    "Waveney":                                "UKH15",
    "Great Yarmouth":                         "UKH14",
    "Eastbourne":                             "UKJ22",
    "Worthing":                               "UKJ22",
    "Torbay":                                 "UKK42",
    "Cheltenham":                             "UKK13",
    "Hastings":                               "UKJ21",
    "Thanet":                                 "UKJ42",
    "Maidstone":                              "UKJ42",
    "Gravesham":                              "UKJ41",
    "Watford":                                "UKH23",
    "St Albans":                              "UKH23",
    "Dacorum":                                "UKH23",
    "Stevenage":                              "UKH24",
    "Harlow":                                 "UKH33",
    "Basildon":                               "UKH34",
    "Chelmsford":                             "UKH34",
    "Colchester":                             "UKH32",
    "Bedford":                                "UKH21",
    "Peterborough":                           "UKH12",
    "Kettering":                              "UKF24",
    "Corby":                                  "UKF24",
    "Rugby":                                  "UKG13",
    "Warwick":                                "UKG13",
    "Nuneaton and Bedworth":                  "UKG13",
    "Tamworth":                               "UKG11",
    "Cannock Chase":                          "UKG11",
    "East Staffordshire":                     "UKG11",
    "Telford and Wrekin":                     "UKG21",
    "Worcester":                              "UKG12",
    "Cheshire West and Chester":              "UKD63",
    "Wycombe":                                "UKJ13",
    "Slough":                                 "UKJ12",
    "Woking":                                 "UKJ25",
    "Guildford":                              "UKJ25",
    "Tunbridge Wells":                        "UKJ42",
    "Ashford":                                "UKJ42",
    "Redditch":                               "UKG12",
    "Derry & Strabane Local Government District": "UKN09",
    "North Lanarkshire (Airdrie/Bellshill/Coatbridge/Motherwell)": "UKM83",
    "Inverclyde (Greenock)":                  "UKM84",
    "Falkirk":                                "UKM77",
    "Mansfield":                              "UKF16",
    "Chesterfield":                           "UKE12",
    "Basingstoke and Deane":                  "UKJ32",
    "Rushmoor (metropolitan area)":           "UKJ32",
    "Bath and North East Somerset":           "UKK12",
    "Milton Keynes":                          "UKJ13",
    "Bracknell Forest":                       "UKJ11",
    "Crawley":                                "UKJ23",
    "Sunderland":                             "UKC24",
    "Middlesbrough":                          "UKC14",

    # ── Encoding-mangled variants (latin1 artefacts in the CSV) ───────────────
    "\x8eilina":                              "SK031",  # Žilina (SK)
    "Paneve\x9eys":                           "LT005",  # Panevėžys (LT)
    "Ko\x9aice":                              "SK042",  # Košice (SK)
    "Pre\x9aov":                              "SK041",  # Prešov (SK)
    "Communauté d'Agglomération de Lens \x96 Liévin": "FRE12",  # Pas-de-Calais
    "Communauté de Communes de l\x92Ouest de la Plaine de France (CCOPF)": "FR108",

    # ── Missing entries ────────────────────────────────────────────────────────
    "Bournemouth (metropolitan area)":        "UKK21",  # Bournemouth (Dorset)
    "Chartres":                               "FRB06",  # Eure-et-Loir
    "Alkmaar":                                "NL327",  # Kop van Noord-Holland
    "Talavera de la Reina":                   "ES422",  # Toledo (ES)
    "Communauté d'Agglomération de Marne et Chantereine": "FR105",  # Seine-Saint-Denis
}

# ── Quick check ───────────────────────────────────────────────────────────────
if __name__ == "__main__":
    print(f"Total cities mapped: {len(city_nuts)}")
    # Show a sample
    sample = list(city_nuts.items())[:10]
    for city, nuts in sample:
        print(f"  {city!r:55s} → {nuts}")
