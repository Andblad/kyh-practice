#Uppgift 28, 36, 37, 39, 40, 42, 43 (enhetstester och funktioner)
#Uppgift 36 (moduler)

#upg28
#Nedan ser ni 2 enhetstester för konvertering mellan olika enheter.
#Spara testerna i en fil kallad "test_conversions.py".
#Utöka "requirements.txt" med en rad som innehåller "pytest" - detta är ett mycket populärt verktyg för att köra automatiska tester i Python.

# test_conversions.py
from conversions import m_to_mm, cm_to_m

def test_conversion_from_meters_to_mm():
    expected = 1000
    got = m_to_mm(m=1)
    assert expected == got

def test_cm_to_m():
    expected = 2
    got = cm_to_m(cm=200)
    assert expected == got

#28.1 Implementera funktionerna m_to_mm och cm_to_m i en ny modul conversions.py.
#28.2 Lägg till några fler tester för m_to_mm med andra värden, så att ni är helt
   #  säkra på att funktionerna fungerar som de ska!
#28.3 Skriv 2 tester för en ny funktion mm_to_m (som inte finns än).
#28.4 Implementera funktionen conversions.mm_to_m!
#28.5 Skriv tillräckligt många tester för att ni ska känna att ni litar på en funktion
    # som konverterar från Fahrenheit till Celsius. Hur många tester räcker? Diskutera!
