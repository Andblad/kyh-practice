"""
så om du har en for loop som tar ut quiz-frågor,
så är det inte mer jobb än att lägga in fel svar i en  lista, eller två.
"""


frågor = {'prompt': 'fråga', 'rightAnswer': '1', 'wrongAnswers': ['2', '3', '4']}
rätt_fråga_svar_ls = []
fråga_ls = []
rätt_svar_ls = []

"""
Om du vill göra som jag har gjort:
"""

for fråga in frågor:
    lista_m_svar = [fråga['rightAnswer']
    for a in fråga['wrongAnswers']:
        lista_m_svar.append(a)
    # mixar ihop det
    sv = input()
    # När användare svarat körs följande:
    # det är rad 29 och 30 som är viktiga här.
    try:
        if int(sv) == (lista_m_svar.index(fråga['rightAnswer']) + 1):
            print("Rätt!")
        else:
            print(f"Fel, rätt svar är {lista_m_svar.index(fråga['rightAnswer']) + 1}: {fråga['rightAnswer']}")
            t = fråga['prompt'], fråga['rightAnswer']
            rätt_fråga_svar_ls.append(t)

"""
Om du vill göra som Daniel:
"""
for fråga in frågor:
    lista_m_svar = [fråga['rightAnswer']
    for a in fråga['wrongAnswers']:
        lista_m_svar.append(a)
    # mixar ihop det
    # och printar ut.
    sv = input()
    # När användare svarat körs följande:
    # Det är rad 49 och 50 som är viktiga här.
    try:
        if int(sv) == (lista_m_svar.index(fråga['rightAnswer']) + 1):
            print("Rätt!")
        else:
            print(f"Fel, rätt svar är {lista_m_svar.index(fråga['rightAnswer']) + 1}: {fråga['rightAnswer']}")
        fråga_ls = fråga['prompt']
        rätt_svar_ls = fråga['rightAnswer']

"""
Om du kan implementera någon av dessa metoder
kommer du bara behöva printa i slutet.
"""

#pritna för  rätt_fråga_svar_ls:
for i in rätt_svar_ls:
    print(f" Fråga : {rätt_svar_ls[i][0]}, Rätt svar :{rätt_svar_ls[i][1]} ")
# vi kör det genom en for loop för att komma åt alla tupler i listan,
# sedan går vi in i dom genom [0] och [1], där första elementet är frågan, andra är svaret.

# för att printa två listor:
for i in fråga_ls,rätt_svar_ls:
    print(f" Fråga : {fråga_ls[i]}, Rätt svar : {rätt_svar_ls[i]}")
# Här behöver vi inte tänka på att gå in i tupler,
# utan behöver bara skriva ut i den ordning som det ligger i listorna.

"""
Båda dessa metoder kräver att du skapar en lista
innan du kör en for-loop som printar ut frågor, tar användar data och övrigt.
"""