from morse_code_converter import MorseCodeConverter



on = True
converter = MorseCodeConverter()


while on:
    choice = input("Vuoi codificare un messaggio in linguaggio morse o decodificare un messaggio dal linguaggio morse?(Le barre verticali indicano gli spazi tra le parole e gli slash quelli tra le lettere)\n Scrivi 'codifica' o 'decodifica': ")
    if choice == "codifica":
        mess_da_cod = input("Inserisci il messaggio che vuoi codificare in linguaggio morse: ")
        print(converter.convert_to_morse(mess_da_cod))
    elif choice == "decodifica":
        mess_da_decod = input("Inserisci il messaggio che vuoi codificare in testo: ")
        print(converter.convert_to_text(mess_da_decod))
    else:
        print("scelta non valida")
    keep_on = input("Vuoi continuare a usare il programma?\n Scrivi 'si' o 'no': ")
    if keep_on == "no":
        on = False