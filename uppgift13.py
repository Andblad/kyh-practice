import random

väg = 'beställas på posten','laddas ner','köpas på ica','lånas på bilioteket','hämtas på din vårdcentral'
nat = ['svensk','tysk','dansk','norman','finnländare']
sjukdom = ['corronavirus','vattkoppor','röda hund','förkylning','HIV']
koms = ['komma nära','chatta med','åka bil med','äta middiga med','bråka med']




def main(väg,nat,sjukdom,koms,):
    x = random.randint(1, 4)

    print(f"En app som kan {väg[x]} ska varna {nat[x]} som någon {random.choices(koms)} som smittats av {random.choices(sjukdom)} .")
    print(f"- Du tycker att vi i Helsingland borde strunta i att göra något liknande, säger Jonathan, chef för Svenska institutetför inre säkerhet, SIIS.")


if __name__ == '__main__':
    main(väg,nat,sjukdom,koms,)