import random
sak = ['lampa','tandborste','kudde','bord','lampa']
väg = 'beställas på posten','laddas ner','köpas på ica','lånas på bilioteket','hämtas på din vårdcentral'
nat = ['svenskar','tyskar','danskar','norrmän','finnländare']
sjukdom = ['corronavirus','vattkoppor','röda hund','förkylning','HIV']
koms = ['komma nära','chatta med','åka bil med','äta middiga med','bråka med']
namn = ['Bill Gates', 'Harry Potter','Nalle Puh','alla världens kvinnor','Gustav Vasa']
org = ['Svenska institutet för inre säkerhet, SIIS', 'Folkhälsomyndigheten,FHM','Gothia Towers Svenska Mässan AB','Volvo lastvagnar','Googel']
ort = ['Ludvika', 'Staffanstorp', 'Allecante','Östra Strande, Halmstad','Stockholm']
tyck = ['Vi','Du','Jag','Ni','Dom']
gora = ['ät en trevlig middag iställt','spela spel','strunta i att göra nått liknade','dansa limbo','låta någon med bättre mandat ta i den frågan kanske']
position = ['chef','städare','medarbetare','okänd postion','tomte-imitatör']
def main():
    x = random.randint(0,4)
    y = random.randint(0 ,4)

    print(f"En {random.choice(sak)} som kan {random.choice(väg)} ska varna {random.choice(nat)} som  {random.choice(koms)} någon som smittats av {random.choice(sjukdom)} .")
    print(f"- {random.choice(tyck)} tycker att vi i {random.choice(ort)} borde {random.choice(gora)}, säger {random.choice(namn)}, {random.choice(position)} för {random.choice(org)}.")


if __name__ == '__main__':
    main()