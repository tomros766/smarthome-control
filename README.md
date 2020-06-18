# Python 2020
## Informacje ogólne
### Temat Projektu
##### System sterowania inteligentnym domem
### Autor
##### Tomasz Rosiek
## Funkcjonalność
Aplikacja generuje pilota sterującego inteligentnym domem na podstawie pliku konfiguracyjnego *config.json*. Obsługuje urządzenia dwustanowe, takie jak alarm, rolety czy żarówki, a także te o stanie "liczbowym", jak urządzenia sterujące temperaturą czy wilgotnością powietrza.
Pokoje podzielone są na zakładki, każdy z nich posiada własny zestaw przycisków.
## Aspekt techniczny
Aplikacja została napisana w języku Python, korzysta z biblioteki paho-mqtt oraz tkinter. 
Wszystkie komunikaty zdefiniowane w pliku konfiguracyjnym są przesyłane do brokera MQTT, którego adres definiuje się w panelu logowania. Wysyłane komunikaty mają (w przypadku urządzeń dwustanowych) flagę *retained* ustawioną na **True**, dlatego jest możliwe odczytanie stanu początkowego (zakładając, że nie istnieją inne urządzenia wysyłające komunikaty bez tej flagi).
Interfejs graficzny został opracowany za pomocą tkinter.
### Kod
#### main.py
Główny plik projektu, wczytuje plik konfiguracyjny i uruchamia aplikację.
#### room.py
Plik definiuje klasę Room, pośredniczy w publikowaniu komunikatów przez swoje odpowiednie opcje (przyciski)
#### room_option.py
Plik definiuje klasę RoomOption, w praktyce mechanizm pojedynczego przycisku. Obsługuje publikacje komunikatów przez klienta oraz zmianę własnego stanu.
#### gui/login.py
Plik definiuje klasę Login, zawierającą okno i mechanizm logowania. Oprócz obsługi interfejsu graficznego, wysyła do rodzica wprowadzone dane logowania (ID klienta oraz adres brokera MQTT).
#### gui/home.py
Plik definiuje klasę Home, zawierającą okno z zakładkami poszczególnych pokoi. Odpowiada za tworzenie okien dla odpowiednich pokoi.
#### gui/room_frame.py
Plik definiuje klasę RoomFrame, odpowiadającą za wygląd pojedynczej zakładki (pokoju). Na podstawie otrzymanego pokoju, rozmieszcza przyciski oraz przypina funkcje reagujące na ich kliknięcia (wywołuje funkcję publikacji wiadomości dla danego pokoju)
#### gui/gui.py
Plik definiuje klasę App, odpowiadającą za zmianę pomiędzy ekranem Login i Home oraz  obsługę klienta MQTT: połączenie oraz subskrypcja, która wraz z funkcją callbackową *on_message* pozwala pilotowi na odczytanie stanu początkowego 
### Instalacja zależności
#### wymagania:
  * Python 3.*
  * narzędzie pip (nie wymagane, jeśli masz zainstalowaną bibliotekę paho-mqtt)
  * Dostęp do brokera MQTT
 #### instalacja
 Z głównego folderu projektu wykonaj polecenie
 `pip install -r requirements.txt`
 ### Plik konfiguracyjny
 Plik konfiguracyjny *config.json* posiada następującą strukturę:
 
 ![Struktura JSON](https://github.com/tomros766/smarthome-control/blob/master/img/config.png "struktura pliku JSON")
 
 Plik jest tablicą zakładek (pokoi), z których każda posiada nazwę oraz tablicę przycisków. Pojedynczy przycisk posiada nazwę opcji, pozycję na pilocie, temat i treść publikowanej wiadomości oraz flagę informującą czy jest to urządzenie dwustanowe czy o wartości liczbowej. W przypadku urządzenia dwustanowego pola *message_one* oraz *message_two* oznaczają odpowiednie stany, w przypadku urządzenia z wartością liczbową, wiadomości te oznaczają odpowiendio podniesienie i obniżenie wartości (jest to istotne ze względu na dobór ikon, po dokonaniu odpowiednich zmian w pliku
 *gui/room_frame.py* zastrzeżenie to przestaje mieć znaczenie).
