from varasto import Varasto

def print_varasto(mehua, olutta):
    print(f"Luonnin jälkeen:\n"
    f"Mehuvarasto: {mehua}\n"
    f"Olutvarasto: {olutta}\n"

    "Olut getterit:\n"
    f"saldo = {olutta.saldo}\n"
    f"tilavuus = {olutta.tilavuus}\n"
    f"paljonko_mahtuu = {olutta.paljonko_mahtuu()}\n"

    "Mehu setterit:\n"
    f"Lisätään 50.7")
    mehua.lisaa_varastoon(50.7)
    print(f"Mehuvarasto: {mehua}\n"
    "Otetaan 3.14")
    mehua.ota_varastosta(3.14)
    print(f"Mehuvarasto: {mehua}\n"

    "Virhetilanteita:\n"
    "Varasto(-100.0);")
    huono = Varasto(-100.0)
    print(f"{huono}\n"

    "Varasto(100.0, -50.7)")
    huono = Varasto(100.0, -50.7)
    print(f"{huono}\n"

    f"Olutvarasto: {olutta}\n"
    "olutta.lisaa_varastoon(1000.0)")
    olutta.lisaa_varastoon(1000.0)
    print(f"Olutvarasto: {olutta}\n"

    f"Mehuvarasto: {mehua}\n"
    "mehua.lisaa_varastoon(-666.0)")
    mehua.lisaa_varastoon(-666.0)
    print(f"Mehuvarasto: {mehua}\n"

    f"Olutvarasto: {olutta}\n"
    "olutta.ota_varastosta(1000.0)")


def main():
    mehua = Varasto(100.0)
    olutta = Varasto(100.0, 20.2)

    print_varasto(mehua, olutta)

    saatiin = olutta.ota_varastosta(1000.0)
    print(f"saatiin {saatiin}\n"
    f"Olutvarasto: {olutta}\n"

    f"Mehuvarasto: {mehua}\n"
    "mehua.otaVarastosta(-32.9)")
    saatiin = mehua.ota_varastosta(-32.9)
    print(f"saatiin {saatiin}\n"
    f"Mehuvarasto: {mehua}")
 

if __name__ == "__main__":
    main()
