import datetime
from datetime import date




def initializeaza_pachet(id, data_inceput, data_sfarsit, destinatie, pret):

    dictionar_pachete = {"id": id,
                         "data de început a calatoriei": data_inceput,
                         "data de sfarsit a calatoriei": data_sfarsit,
                         "destinatie": destinatie,
                         "pret": pret}
    return dictionar_pachete

def get_id(pachet):
    return pachet["id"]

def get_data_inceput(pachet):
    return pachet["data de început a calatoriei"]

def get_data_sfarsit(pachet):
    return pachet["data de sfarsit a calatoriei"]

def get_destinatie(pachet):
    return pachet["destinatie"]

def get_pret(pachet):
    return pachet["pret"]


def set_id(pachet, id_nou):
    pachet["id"] = id_nou

def set_data_inceperii(pachet, data_noua):
    pachet["data de început a calatoriei"] = data_noua
def set_data_sfarsit(pachet, data_noua):
    pachet["data de sfarsit a calatoriei"] = data_noua

def set_destinatie(pachet, destinatie_noua):
    pachet["destinatie"] = destinatie_noua

def set_pret(pachet, pret_nou):
    pachet["pret"] = pret_nou

def aranjeaza_lista(pachet):
    string = ""
    string = string+"Pachet id = " + str(get_id(pachet))+"\n"
    string = string + "Data de inceput = "+str(get_data_inceput(pachet))+"\n"
    string = string + "Data de sfarsit = "+str(get_data_sfarsit(pachet))+"\n"
    string = string + "Destinatia = "+str(get_destinatie(pachet))+"\n"
    string = string + "Pret = "+str(get_pret(pachet))+"\n"
    return string

def lista_pachete_precompletata():
    lista_pachete=[]
    pachet1 = initializeaza_pachet(1, "2023-07-15", "2023-07-20", "Spania", 100)
    pachet2 = initializeaza_pachet(2, "2023-3-18", "2023-3-20", "Romania", 50)
    pachet3 = initializeaza_pachet(3, "2023-4-1", "2023-4-11", "Bulgaria", 150)
    lista_pachete.append(pachet1)
    lista_pachete.append(pachet2)
    lista_pachete.append(pachet3)
    return lista_pachete

#OPERATII#

def modifica_pachet(lista_pachete, id, data_inceput, data_sfarsit, locatie, pret):
    valori_sterse = []
    for i in range(len(lista_pachete)):
        pachet_curent = lista_pachete[i]
        if get_id(pachet_curent) == id:
            set_data_inceperii(pachet_curent, data_inceput)
            set_data_sfarsit(pachet_curent, data_sfarsit)
            set_destinatie(pachet_curent, locatie)
            set_pret(pachet_curent, pret)
            adauga_pachet_istoric(lista_pachete, len(lista_pachete))
            valori_sterse.append([i, lista_pachete[i]])
    print(ui_tipareste_pachete(lista_pachete))
    adauga_pachet_istoric(undo_modificare, valori_sterse)


def copiaza_lista(lista_pachete):
    copie_lista = []
    for pachet in lista_pachete:
        copie_pachet = initializeaza_pachet(get_id(pachet), get_data_inceput(pachet), get_data_sfarsit(pachet), get_destinatie(pachet), get_pret(pachet))
        copie_lista.append(copie_pachet)
    return copie_lista

def adauga_pachet_in_lista(lista_pachete, indice):
    valori_sterse = []
    id1 = indice
    for i in range(id1-1, len(lista_pachete)):
        id_nou = get_id((lista_pachete[i]))+1
        set_id(lista_pachete[i], id_nou)
    data_inceput1 = input("Introduceti data de inceput sub forma YYYY-MM-DD:")
    data_sfarsit1 = input("Introduceti data de sfarsit sub forma YYYY-MM-DD:")
    destinatie1 = input("Introduceti destinatie:")
    pret1 = input("Introduceti pret:")
    pachet_nou = initializeaza_pachet(id1, data_inceput1, data_sfarsit1, destinatie1, pret1)
    valori_sterse.append([indice, pachet_nou])
    lista_pachete.insert(indice-1, pachet_nou)
    print(ui_tipareste_pachete(lista_pachete))
    adauga_pachet_istoric(undo_adaugare, valori_sterse)
    return lista_pachete

def adauga_pachet_istoric(tip_actiune, val):
   istoric_actiuni.append([tip_actiune, val])


def sterge_pachet_destinatie_aleasa(lista_pachete, destinatie_aleasa):
    valori_sterse = []
    for i in range(len(lista_pachete)-1, -1, -1):
        pachet_curent = lista_pachete[i]
        if get_destinatie(pachet_curent) == destinatie_aleasa:
            valori_sterse.append([i, lista_pachete[i]])
            lista_pachete.remove(pachet_curent)
    adauga_pachet_istoric(undo_stergere_dupa_destinatie, valori_sterse)
    print(ui_tipareste_pachete(lista_pachete))

def stergere_pachet_pe_durata_de_zile(lista_pachete, durata_zile):

    valori_sterse = []
    for i in range(len(lista_pachete)-1, -1, -1):
        pachet_curent = lista_pachete[i]
        data_inceput_pachet = get_data_inceput(pachet_curent)
        year, month, day = map(int, data_inceput_pachet.split('-'))
        data1 = datetime.date(year, month, day)
        data_sfarsit_pachet = get_data_sfarsit(pachet_curent)
        year, month, day = map(int, data_sfarsit_pachet.split('-'))
        data2 = datetime.date(year, month, day)
        diferenta= data2-data1
        if diferenta.days < durata_zile:
          valori_sterse.append([i, lista_pachete[i]])
          lista_pachete.remove(pachet_curent)
    adauga_pachet_istoric(undo_stergere_dupa_durata_zile, valori_sterse)
    return lista_pachete


def stergere_pachete_dupa_pret(lista_pachete, suma_aleasa):
    valori_sterse = []
    for i in range(len(lista_pachete) - 1, -1, -1):
        pachet_curent = lista_pachete[i]
        pret_curent = get_pret(pachet_curent)
        if pret_curent > suma_aleasa:
            valori_sterse.append([i, lista_pachete[i]])
            lista_pachete.remove(pachet_curent)
    print(ui_tipareste_pachete(lista_pachete))
    adauga_pachet_istoric(undo_stergere_dupa_pret, valori_sterse)


def exista_id(lista_mea, id):
    for i in range(len(lista_mea)):
        pachet_curent = lista_mea[i]
        if get_id(pachet_curent) == id:
            return True
    return False

def exista_destinatie(lista_mea, destinatie):
    for i in range(len(lista_mea)):
        pachet_curent = lista_mea[i]
        if get_destinatie(pachet_curent) == destinatie:
            return True
    return False

def exista_data_sfarsit(lista_mea, data_sfarsit):
    for i in range(len(lista_mea)):
        pachet_curent = lista_mea[i]
        if get_data_sfarsit(pachet_curent) == data_sfarsit:
            return True
    return False

def exista_data_inceput(lista_mea, data_inceput):
    for i in range(len(lista_mea)):
        pachet_curent = lista_mea[i]
        if get_data_inceput(pachet_curent) == data_inceput:
            return True
    return False


def tipareste_pachete_care_pp_sejur(lista_mea, data_inceput_sejur, data_sfarsit_sejur):
    print("Pachetele care presupun sejur din intervalul dat sunt:")
    for i in range(len(lista_mea)-1, -1, -1):
       pachet_curent = lista_mea[i]
       if get_data_inceput(pachet_curent) >= data_inceput_sejur and get_data_sfarsit(pachet_curent) <= data_sfarsit_sejur:
           print(aranjeaza_lista(pachet_curent))

def tipareste_pachet_dupa_perioada_ord_cresc(lista_mea, data_inceput_sejur, data_sfarsit_sejur):
    print("Pachetele disponibile in perioada citita sunt (in ordine crescatoare a pretului):")
    for i in range(0, len(lista_mea)):
       pachet_curent = lista_mea[i]
       for j in range(i+1, len(lista_mea)):
           pachet_curent1 = lista_mea[j]
           if get_pret(pachet_curent) >= get_pret(pachet_curent1):
               pachet_curent, pachet_curent1 = pachet_curent1, pachet_curent

    for k in range(0, len(lista_mea)):
       pachet_curent2 = lista_mea[k]
       if get_data_inceput(pachet_curent2) >= data_inceput_sejur and get_data_sfarsit(pachet_curent2) <= data_sfarsit_sejur:
           print(aranjeaza_lista(pachet_curent2))

def tipareste_media_pret_pt_destinatie(lista_mea, destinatie_data):
    nr_elemente=0
    sum=0
    for i in range(len(lista_mea)-1, -1, -1):
       pachet_curent = lista_mea[i]
       if get_destinatie(pachet_curent) == destinatie_data:
           nr_elemente+=1
           sum = sum+ get_pret(pachet_curent)
    print("Media de pret pentru", destinatie_data, "este", sum/nr_elemente)

def tipareste_pachet_dupa_destinatie_si_pret(lista_mea, destinatie_data, pret_dat):
    for i in range(len(lista_mea)-1, -1, -1):
        pachet_curent = lista_mea[i]
        if get_destinatie(pachet_curent) == destinatie_data and get_pret(pachet_curent) < pret_dat:
           print(aranjeaza_lista(pachet_curent))

def tipareste_pachet_dupa_data_sfarsit(lista_mea, data_sfarsit_sejur):
    for i in range(len(lista_mea)):
        pachet_curent = lista_mea[i]
        if get_data_sfarsit(pachet_curent) == data_sfarsit_sejur:
          print(aranjeaza_lista(pachet_curent))

def tipareste_nr_oferte_pt_destinatie(lista_mea, destinatie_data):
    nr_oferte = 0
    for i in range(len(lista_mea)):
        pachet_curent = lista_mea[i]
        if get_destinatie(pachet_curent) == destinatie_data:
          nr_oferte+=1
    print("Numarul de oferte pentru", destinatie_data, "este", nr_oferte)

def tipareste_nr_oferte_dupa_interval_pret(lista_mea, interval1, interval2):
    nr_oferte = 0
    for i in range(len(lista_mea)):
        pachet_curent = lista_mea[i]
        if get_pret(pachet_curent)<=interval2 and get_pret(pachet_curent) >= interval1:
          nr_oferte+=1
          print(aranjeaza_lista(pachet_curent))
    if nr_oferte != 0:
        print("Numarul de oferte in intervalul", interval1, "si", interval2, " este:", nr_oferte)
        print("\n")
    else:
        print("Nu exista pachete in intervalul dat!")

def eliminare_oferte_dupa_pret_si_destinatie(lista_mea, destinatie_data, pret_dat):
    valori_sterse = []
    for i in range(len(lista_mea)-1, -1, -1):
        pachet_curent = lista_mea[i]
        if get_destinatie(pachet_curent) != destinatie_data and get_pret(pachet_curent) > pret_dat:
           valori_sterse.append([i, lista_mea[i]])
           lista_mea.remove(pachet_curent)
    print("Lista de oferte dupa eliminare: ")
    print(ui_tipareste_pachete(lista_mea))
    adauga_pachet_istoric(undo_eliminare_dupa_pret_si_destinatie, valori_sterse)


def eliminare_oferte_dupa_luna_data(lista_pachete, luna_data):
    valori_sterse = []
    for i in range(len(lista_pachete)-1, -1, -1):
        pachet_curent = lista_pachete[i]
        data_inceput_pachet = get_data_inceput(pachet_curent)
        year, month, day = map(int, data_inceput_pachet.split('-'))
        data1 = datetime.date(year, month, day)
        data11= data1.month
        data_sfarsit_pachet = get_data_sfarsit(pachet_curent)
        year, month, day = map(int, data_sfarsit_pachet.split('-'))
        data2 = datetime.date(year,month, day)
        data22 = data2.month
        if luna_data == data11 or luna_data == data22:
          valori_sterse.append([i, lista_pachete[i]])
          lista_pachete.remove(pachet_curent)
    adauga_pachet_istoric(undo_stergere_dupa_durata_zile, valori_sterse)
    return lista_pachete

istoric_actiuni = []
undo_adaugare = 'a'
undo_modificare = 'm'
undo_stergere_dupa_destinatie= 's1'
undo_stergere_dupa_pret = 's2'
undo_stergere_dupa_durata_zile = 's3'
undo_eliminare_dupa_pret_si_destinatie = 's4'
undo_pt_eliminare_dupa_luna = 's5'


def undo_pt_stergere_dupa_destinatie(lista_pachete, val):
    for stergeri in val:
        index = stergeri[0]
        element = stergeri[1]
        lista_pachete.insert(index, element)
    return lista_pachete

def undo_pt_stergere_dupa_durata_zile(lista_pachete, val):
    for stergeri in val:
        index = stergeri[0]
        element = stergeri[1]
        lista_pachete.insert(index, element)
    return lista_pachete

def undo_pt_stergere_dupa_pret(lista_pachete, val):
    for stergeri in val:
        index =  stergeri[0]
        element = stergeri[1]
        lista_pachete.insert(index, element)
    return lista_pachete

def undo_pt_eliminare_dupa_pret_si_destinatie(lista_pachete, val):
    for stergeri in val:
        index = stergeri[0]
        element = stergeri[1]
        lista_pachete.insert(index, element)
    return lista_pachete

def undo_pt_eliminare_dupa_luna_data(lista_pachete, val):
    for stergeri in val:
        index = stergeri[0]
        element = stergeri[1]
        lista_pachete.insert(index, element)
    return lista_pachete


def undo_pt_adaugare(lista_pachete, val):
    for stergeri in val:
        index = stergeri[0]
        element = stergeri[1]
        lista_pachete.remove(index, element)
    return lista_pachete


def undo_pt_modifica_pachet(lista_pachete, val):
    for stergeri in val:
        index = stergeri[0]
        element = stergeri[1]
        lista_pachete.remove(index, element)
    return lista_pachete

def wrapper_modificare(lista_pachete, id, data_inceput, data_sfarsit, destinatie, pret):
    copie_lista = copiaza_lista(lista_pachete)
    if exista_id(lista_pachete, id):
        modifica_pachet(lista_pachete, id, data_inceput, data_sfarsit, destinatie, pret)
        lista_undo[:] = copie_lista

def undo_ultima_actiune(lista_pachete):
    if len(istoric_actiuni) == 0:
        print("Istoricul actiunilor este gol\n")
        return lista_pachete
    ultima_actiune = len(istoric_actiuni) - 1
    tip_actiune, val = istoric_actiuni[ultima_actiune][0], istoric_actiuni[ultima_actiune][1]
    if tip_actiune == undo_adaugare:
        lista_pachete = undo_pt_adaugare(lista_pachete, val)
    elif tip_actiune == undo_modificare:
        lista_pachete = undo_pt_modifica_pachet(lista_pachete, val)
    elif tip_actiune == undo_stergere_dupa_destinatie:
        lista_pachete = undo_pt_stergere_dupa_destinatie(lista_pachete, val)
    elif tip_actiune == undo_stergere_dupa_pret:
        lista_pachete = undo_pt_stergere_dupa_pret(lista_pachete, val)
    elif tip_actiune == undo_stergere_dupa_durata_zile:
        lista_pachete = undo_pt_stergere_dupa_durata_zile(lista_pachete, val)
    elif tip_actiune == undo_eliminare_dupa_pret_si_destinatie:
        lista_pachete = undo_pt_eliminare_dupa_pret_si_destinatie(lista_pachete, val)
    elif tip_actiune == undo_pt_eliminare_dupa_luna:
        lista_pachete = undo_pt_eliminare_dupa_luna_data(lista_pachete, val)
    istoric_actiuni.pop(ultima_actiune)
    print(ui_tipareste_pachete(lista_pachete))

def ui_tipareste_pachete(lista_mea):
    if len(lista_mea) == 0:
        print("Lista e goala!")
    else:
       for i in range(len(lista_mea)):
          pachet_curent = lista_mea[i]
          print(aranjeaza_lista(pachet_curent))

def ui_adauga_pachet(lista_pachete):
  try:
     id = int(input("Introduceti id:"))
     if exista_id(lista_pachete, id) is True:
       print("Id deja existent!")
     else:
       data_inceput = input("Introduceti data de inceput sub forma YYYY-MM-DD:")
       data_sfarsit = input("Introduceti data de sfarsit sub forma YYYY-MM-DD:")
       destinatie = input("Introduceti destinatie:")
       pret = int(input("Introduceti pret:"))
       pachet_nou = initializeaza_pachet(id, data_inceput, data_sfarsit, destinatie, pret)
       lista_pachete.append(pachet_nou)
       return lista_pachete
  except:
      print("Date incorecte! Reincercati!")

def ui_modifica_pachet(lista_pachete):
    id = int(input("Introduceti id-ul pachetuluilui pe care vreti sa il modificati:"))
    data_inceput_noua = input("Introduceti data de inceput pe care vreti sa o modificati")
    data_sfarsit_noua = input("Introduceti data de sfarsit pe care vreti sa o modificati:")
    locatie_noua = input("Introduceti locatia pe care doriti sa o modificati")
    pret_nou = input("Introduceti pretul pe care doriti sa il modificati:")
    modifica_pachet(lista_pachete, id, data_inceput_noua, data_sfarsit_noua, locatie_noua, pret_nou)

def  ui_adauga_pachet_in_lista(lista_pachete):
    indice = int(input("Introduceti id-ul pachetului:"))
    print(adauga_pachet_in_lista(lista_pachete, indice))

def ui_tipareste_pachet_dupa_destinatie_si_pret(lista_pachete):
    destinatie_data=input("Dati destinatia:")
    pret_dat=int(input("Dati pret:"))
    if exista_destinatie(lista_pachete, destinatie_data) is True:
        tipareste_pachet_dupa_destinatie_si_pret(lista_pachete, destinatie_data, pret_dat)
    else:
        print("NU exista pachet cu aceasta destinatie si acest pret!")
        print("\n")


def ui_eliminare_oferte_dupa_pret_si_destinatie(lista_pachete):
    destinatie_data = input("Dati destinatia:")
    pret_dat = int(input("Dati pret:"))
    eliminare_oferte_dupa_pret_si_destinatie(lista_pachete, destinatie_data, pret_dat)

def ui_eliminare_oferte_dupa_luna_data(lista_pachete):
    luna_data = int(input("Dati luna:"))
    eliminare_oferte_dupa_luna_data(lista_pachete, luna_data)

def ui_tipareste_nr_oferte_pt_destinatie(lista_pachete):
    destinatie_data = input("Dati destinatia:")
    if exista_destinatie(lista_pachete, destinatie_data) is True:
        tipareste_nr_oferte_pt_destinatie(lista_pachete, destinatie_data)
    else:
        print("NU exista pachet cu aceasta destinatie!")
        print("\n")

def ui_tipareste_media_pret_pt_destinatie(lista_pachete):
    destinatie_data = input("Dati destinatia:")
    if exista_destinatie(lista_pachete, destinatie_data) is True:
        tipareste_media_pret_pt_destinatie(lista_pachete, destinatie_data)
    else:
        print("NU exista pachet cu aceasta destinatie!")
        print("\n")


def ui_tipareste_dupa_pp_sejur(lista_pachete):
    data_inceput_sejur = input("Introduceti data de inceput sub forma YYYY-MM-DD:")
    data_sfarsit_sejur = input("Introduceti data de sfarsit sub forma YYYY-MM-DD:")
    tipareste_pachete_care_pp_sejur(lista_pachete, data_inceput_sejur, data_sfarsit_sejur)

def ui_tipareste_pachet_dupa_perioada_ord_cresc(lista_pachete):
    data_inceput_sejur = input("Introduceti data de inceput sub forma YYYY-MM-DD:")
    data_sfarsit_sejur = input("Introduceti data de sfarsit sub forma YYYY-MM-DD:")
    tipareste_pachet_dupa_perioada_ord_cresc(lista_pachete, data_inceput_sejur, data_sfarsit_sejur)


def ui_tipareste_pachet_dupa_data_sfarsit(lista_pachete):
    data_sfarsit_sejur = input("Introduceti data de sfarsit sub forma YYYY-MM-DD:")
    if exista_data_sfarsit(lista_pachete, data_sfarsit_sejur) is True:
        tipareste_pachet_dupa_data_sfarsit(lista_pachete, data_sfarsit_sejur)
    else:
        print("NU exista pachet cu aceasta data de sfarsit a calatoriei!")
        print("\n")

def ui_tipareste_nr_oferte_dupa_interval_pret(lista_pachete):
    interval1 = int(input("Dati primul capat al intervalului:"))
    interval2 = int(input("Dati al doilea capat al intervalului:"))
    tipareste_nr_oferte_dupa_interval_pret(lista_pachete, interval1, interval2)


def ui_sterge_pachet_destinatie_aleasa(lista_pachete):
    destinatie_aleasa = input("Alegeti destinatia pentru care doriti sa stergeti pachetul:")
    if exista_destinatie(lista_pachete, destinatie_aleasa) is True:
        sterge_pachet_destinatie_aleasa(lista_pachete, destinatie_aleasa)
    else:
        print("Pachet inexistent!")

def ui_stergere_pachet_pe_durata_de_zile(lista_pachete):
    durata_zile = int(input("Introduceti durata de zile:"))
    stergere_pachet_pe_durata_de_zile(lista_pachete, durata_zile)

def ui_stergere_pachete_dupa_pret(lista_pachete):
    suma_aleasa = int(input("Introduceti suma aleasa:"))
    stergere_pachete_dupa_pret(lista_pachete, suma_aleasa)


def program():
    lista_pachete = lista_pachete_precompletata()
    lista_undo = []
    while True:
      print("Bine ai venit la aplicatia Python care te va ajuta cu gestiunea pachetelor de călătorie oferite de o agenție de turism!")
      print("\n")
      print("Introduceti tipul de comanda pe care il doriti:")
      print("\n")
      print("1. Optiuni de adaugare ")
      print("2. Optiuni de stergere")
      print("3. Optiuni de cautare")
      print("4. Optiuni de rapoarte")
      print("5. Optiuni de filtrare")
      print("6. Optiuni de undo")
      print("7. Exit")
      print("\n")

      option = int(input("Introduceti tipul de comanda dorita:"))
      print("\n")

      if option == 1:
          print("a. Adaugă pachet de călătorie:")
          print("b. Modifică pachet de călătorie:")
          print("c. Adauga pachet in lista:")
          print("\n")
          option_new= input("Introduceti urmatoarea comanda:")
          if option_new == "a":
              ui_adauga_pachet(lista_pachete)
          elif option_new == "b":
              ui_modifica_pachet(lista_pachete)
          elif option_new == "c":
              ui_adauga_pachet_in_lista(lista_pachete)

      elif option == 2:
          print("a. Ștergerea tuturor pachetelor de călătorie disponibile pentru o destinație dată")
          print("b. Ștergerea tuturor pachetelor de călătorie care au o durată mai scurtă decât un număr de zile dat")
          print("c. Ștergerea tuturor pachetelor de călătorie care au prețul mai mare decât o sumă dată")
          print("\n")
          option_new=input("Introduceti urmatoarea comanda:")
          if option_new == "a":
             ui_sterge_pachet_destinatie_aleasa(lista_pachete)
          elif option_new == "b":
              ui_stergere_pachet_pe_durata_de_zile(lista_pachete)
          elif option_new == "c":
              ui_stergere_pachete_dupa_pret(lista_pachete)

      elif option == 3:
          print("a. Tipărirea pachetelor de călătorie care presupun un sejur într-un interval dat. ")
          print("b. Tipărirea pachetelor de călătorie cu o destinație dată și cu preț mai mic decât o sumă dată.")
          print("c. Tipărirea pachetelor de călătorie cu o anumită dată de sfârșit. ")
          print("d. Tipareste oferte")
          print("\n")
          option_new = input("Introduceti urmatoarea comanda:")
          if option_new == "a":
              ui_tipareste_dupa_pp_sejur(lista_pachete)
          elif option_new == "b":
              ui_tipareste_pachet_dupa_destinatie_si_pret(lista_pachete)
          elif option_new == "c":
              ui_tipareste_pachet_dupa_data_sfarsit(lista_pachete)
          elif option_new =="d":
              ui_tipareste_pachete(lista_pachete)


      elif option == 4:
          print("a. Tipărirea numărului de oferte pentru o destinație dată.")
          print("b. Tipărirea tuturor pachetelor disponibile într-o anumită perioadă citită de la tastatură în ordinea crescătoare a prețului.")
          print("c. Tipărirea mediei de preț pentru o destinație dată")
          print("d. Tiparirea ofertelor, nr de oferte, unde pretul ofertelor se afla intr-un interval dat. ")
          print("\n")
          option_new = input("Introduceti urmatoarea comanda:")
          if option_new == "a":
              ui_tipareste_nr_oferte_pt_destinatie(lista_pachete)
          elif option_new == "b":
             ui_tipareste_pachet_dupa_perioada_ord_cresc(lista_pachete)
          elif option_new == "c":
              ui_tipareste_media_pret_pt_destinatie(lista_pachete)
          elif option_new == "d":
              ui_tipareste_nr_oferte_dupa_interval_pret(lista_pachete)

      elif option == 5:
          print("a. Eliminarea ofertelor care au un preț mai mare decât cel dat și o destinație diferită de cea citită de la tastatură.")
          print("b. Eliminarea ofertelor în care sejurul presupune zile dintr-o anumită lună.")
          print("\n")
          option_new = input("Introduceti urmatoarea comanda:")
          if option_new == "a":
              ui_eliminare_oferte_dupa_pret_si_destinatie(lista_pachete)
          elif option_new == "b":
              ui_eliminare_oferte_dupa_luna_data(lista_pachete)


      elif option == 6:
          print("a. Refacerea ultimei operații.")
          print("\n")
          option_new = input("Introduceti urmatoarea comanda:")
          if option_new == "a":
            undo_ultima_actiune(lista_pachete)

      elif option == 7:
          break

      else:
          print("Comanda invalida! Reincercati!")

def test():

    lista_pachete = [{'id': 1, 'data de început a calatoriei': '2023-07-15', 'data de sfarsit a calatoriei': '2023-12-4', 'destinatie': 'Spania', 'pret': 100}, {'id': 2, 'data de început a calatoriei': '2023-3-18', 'data de sfarsit a calatoriei': '2023-3-20', 'destinatie': 'Romania', 'pret': 50}, {'id': 3, 'data de început a calatoriei': '2023-4-14', 'data de sfarsit a calatoriei': '2023-5-14', 'destinatie': 'Bulgaria', 'pret': 150}]
    assert lista_pachete[0] == {'id': 1, 'data de început a calatoriei': '2023-07-15', 'data de sfarsit a calatoriei': '2023-12-4', 'destinatie': 'Spania', 'pret': 100}
    assert get_destinatie(lista_pachete[0]) == "Spania"
    assert initializeaza_pachet( 4, "2023-08-20", "2023-08-25", "Franta", 250) == {"id": 4, "data de început a calatoriei":"2023-08-20", "data de sfarsit a calatoriei":"2023-08-25", "destinatie": "Franta", "pret": 250}
    modifica_pachet(lista_pachete,1,"2023-08-20","2023-08-25","Franta",250)
    print (lista_pachete)
    assert (lista_pachete == [{'id': 1, 'data de început a calatoriei': '2023-08-20', 'data de sfarsit a calatoriei': '2023-08-25', 'destinatie': 'Franta', 'pret': 250}, {'id': 2, 'data de început a calatoriei': '2023-3-18', 'data de sfarsit a calatoriei': '2023-3-20', 'destinatie': 'Romania', 'pret': 50}, {'id': 3, 'data de început a calatoriei': '2023-4-14', 'data de sfarsit a calatoriei': '2023-5-14', 'destinatie': 'Bulgaria', 'pret': 150}])
    sterge_pachet_destinatie_aleasa(lista_pachete, "Bulgaria")
    print(lista_pachete)
    assert (lista_pachete==[{'id': 1, 'data de început a calatoriei': '2023-08-20', 'data de sfarsit a calatoriei': '2023-08-25', 'destinatie': 'Franta', 'pret': 250}, {'id': 2, 'data de început a calatoriei': '2023-3-18', 'data de sfarsit a calatoriei': '2023-3-20', 'destinatie': 'Romania', 'pret': 50}])
    stergere_pachet_pe_durata_de_zile(lista_pachete, 5)
    print(lista_pachete)
    assert([{'id': 1, 'data de început a calatoriei': '2023-08-20', 'data de sfarsit a calatoriei': '2023-08-25', 'destinatie': 'Franta', 'pret': 250}])
    stergere_pachete_dupa_pret(lista_pachete, 100)
    print(lista_pachete)
    assert (lista_pachete == [])
    print("Testele au trecut!")

test()
program()