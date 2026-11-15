# Radar 360 — Android MVP 0.1

To jest działający szkielet aplikacji Android (Java + WebView + Leaflet). Zawiera:
- mapę OpenStreetMap z centrum startowym Elbląg,
- rzeczywiste pobieranie danych samolotów z OpenSky (jeśli API jest dostępne),
- rzeczywistą pogodę z Open-Meteo,
- trzęsienia ziemi z publicznego feedu USGS,
- warstwy i zakładki dla statków, dróg, dronów, pożarów, kolei i zdarzeń,
- listę źródeł i jawne oznaczenie modułów, które wymagają dalszej integracji.

## Jak zbudować APK
1. Zainstaluj Android Studio (bezpłatne).
2. Otwórz folder `Radar360` jako projekt.
3. Poczekaj na synchronizację Gradle i instalację Android SDK 35.
4. Wybierz Build > Build Bundle(s) / APK(s) > Build APK(s).
5. APK znajdziesz w `app/build/outputs/apk/debug/app-debug.apk`.

## Ważne ograniczenia MVP
- To projekt źródłowy, nie skompilowany APK.
- OpenSky ma limity, a dostępność API może się zmieniać.
- AISStream wymaga klucza i najlepiej pośredniczącego backendu. Nie umieszczaj prywatnego klucza w publicznym APK.
- Ruch drogowy, IMGW/RSO, PAŻP, pożary NASA FIRMS, kolej i publiczne komunikaty służb wymagają osobnych, zweryfikowanych integracji.
- Nie ma publicznego, legalnego i kompletnego feedu do śledzenia wszystkich radiowozów, karetek, funkcjonariuszy lub dronów.
- Dane nie są usługą alarmową. W nagłych sytuacjach dzwoń pod 112.

## Prywatność i koszty
Aplikacja nie wysyła lokalizacji telefonu. Startuje na stałym obszarze mapy. Nie ma konta ani własnego serwera. Korzysta z usług zewnętrznych, które mogą stosować limity i warunki użycia.


## Automatyczne zbudowanie APK bez Android Studio
W projekcie dodano GitHub Actions (`.github/workflows/build-apk.yml`).
1. Utwórz repozytorium na GitHub i wgraj zawartość tego folderu.
2. Otwórz zakładkę Actions w repozytorium.
3. Uruchom workflow „Build Radar 360 APK” (Run workflow), jeśli nie uruchomił się po push.
4. Po zakończeniu otwórz wykonane zadanie i pobierz artefakt `Radar360-debug-apk`.
5. Rozpakuj pobrany artefakt na telefonie i zainstaluj `app-debug.apk`.

To jest debug APK do testów, podpisany kluczem debug. Do publikacji w Google Play potrzebny będzie osobny klucz release.
