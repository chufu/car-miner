import argparse
from pyquery import PyQuery as pq

#parser = argparse.ArgumentParser(description = "fetch car data")
#parser.add_argument('url', metavar = 'URL', help = 'Url to mobile.de')
#parser.add_argument('-x',metavar = 'Proxy', help = 'Http-Proxy credentials: user:Password@url:port')
#
#args = parser.parse_args()
#
#d = pq(url = args.url)
#car_descrptors = d('.cBox-body, .cBox-body--resultitem, .rbt-reg, .rbt-no-top').children("a")
#car_headers = car_descriptors("a.result-item.link--muted.no--text--decoration")
#links = [h.attr("href") for h in car_headers.items("a")]
#
fieldnames = ["Fahzeugnummer", "Kilometerstand", "Hubraum", "Leistung", "Kraftstoffart", "GGetrieb", "Erstzulassung", "Anzahl der Fahrzeughalter", "HU", "Klimatisierung", "Einparkhilfe", "Farbe", "Bluetooth", "Bordcomputer", "CD-Spieler", "Elektr. Fensterheber", "Elektr. Seitenspiegel", "Elektr. Sitzeinstellung", "Freisprecheinrichtung", "Head-Up Display", "Isofix (Kindersitzbefestigung)", "MP3-Schnittstelle", "Multifunktionslenkrad", "Navigationssystem", "Regensensor", "Schiebedach", "Servolenkung", "Sitzbelüftung", "Sitzheizung", "Skisack", "Standheizung", "Start/Stopp-Automatik", "Tempomat", "Tuner/Radio", "Zentralverriegelung", "ESP", "Servolenkung", "Tagfahrlicht", "Garantie", "Partikelfilter"]

with open('cars.csv', 'w') as csvfile:
  writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
  writer.writeheader()

#for link in links:
l = pq(filename="C:\Users\egrn\projects\car_miner\single_car.htm")

features = ' '.join([f.html() for f in l("#rbt-features").items("p")])

with open('cars.csv', 'a') as csvfile:
  writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
  writer.writerow({"Fahzeugnummer": l(""),
    "Kilometerstand": l("#rbt-mileage-l").html(),
    "Hubraum": l("#rbt-cubicCapacity-v").html(),
    "Leistung": l("#rbt-power-v").html(),
    "Kraftstoffart": l("#rbt-fuel-v").html(),
    "Getriebe": l("#rbt-transmission-v").html(),
    "Erstzulassung": l("#rbt-firstRegistration-v").html(),
    "Anzahl der Fahrzeughalter": l("#rbt-numberOfPreviousOwners-v").html(),
    "HU": l("#rbt-hu-v").html(),
    "Klimatisierung": l("#rbt-climatisation-v").html(),
    "Einparkhilfe": l("#rbt-parkAssists-v").html(),
    "Farbe": l("#rbt-color-v").html(),

    "Bluetooth": "1" if features.find("Bluetooth") != -1 else "0",
    "Bordcomputer": "1" if features.find("Bordcomputer") != -1 else "0",
    "CD-Spieler": "1" if features.find("CD-Spieler") != -1 else "0",
    "Elektr. Fensterheber": "1" if features.find("Elektr. Fensterheber") != -1 else "0",
    "Elektr. Seitenspiegel": "1" if features.find("Elektr. Seitenspiegel") != -1 else "0",
    "Elektr. Sitzeinstellung": "1" if features.find("Elektr. Sitzeinstellung") != -1 else "0",
    "Freisprecheinrichtung": "1" if features.find("Freisprecheinrichtung") != -1 else "0",
    "Head-Up Display": "1" if features.find("Head-Up Display") != -1 else "0",
    "Isofix (Kindersitzbefestigung)": "1" if features.find("Isofix (Kindersitzbefestigung)") != -1 else "0",
    "MP3-Schnittstelle": "1" if features.find("MP3-Schnittstelle") != -1 else "0",
    "Multifunktionslenkrad": "1" if features.find("Multifunktionslenkrad") != -1 else "0",
    "Navigationssystem": "1" if features.find("Navigationssystem") != -1 else "0",
    "Regensensor": "1" if features.find("Regensensor") != -1 else "0",
    "Schiebedach": "1" if features.find("Schiebedach") != -1 else "0",
    "Servolenkung": "1" if features.find("Servolenkung") != -1 else "0",
    "Sitzbelüftung": "1" if features.find("Sitzbelüftung") != -1 else "0",
    "Sitzheizung": "1" if features.find("Sitzheizung") != -1 else "0",
    "Skisack": "1" if features.find("Skisack") != -1 else "0",
    "Standheizung": "1" if features.find("Standheizung") != -1 else "0",
    "Start/Stopp-Automatik": "1" if features.find("Start/Stopp-Automatik") != -1 else "0",
    "Tempomat": "1" if features.find("Tempomat") != -1 else "0",
    "Tuner/Radio": "1" if features.find("Tuner/Radio") != -1 else "0",
    "Zentralverriegelung": "1" if features.find("Zentralverriegelung") != -1 else "0",

    "Partikelfilter": "1" if features.find("Partikelfilter") != -1 else "0",
    "ESP": "1" if features.find("ESP") != -1 else "0",
    "Servolenkung": "1" if features.find("Servolenkung") != -1 else "0",
    "Tagfahrlicht": "1" if features.find("Tagfahrlicht") != -1 else  "0",

    "Garantie": "1" if features.find("Garantie") != -1 else "0",
  })
