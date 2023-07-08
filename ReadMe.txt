Poniższy kod wykonuje symulację ruchu trzech ciał w układzie trójwymiarowym, uwzględniając siłę grawitacyjną między nimi. Oto opis, jak działa poszczególne części kodu:

Importowanie bibliotek:
scipy - biblioteka do obliczeń naukowych i numerycznych.
matplotlib - biblioteka do tworzenia wykresów i wizualizacji danych.
numpy - biblioteka do manipulacji i obliczeń na macierzach i wektorach.

Definiowanie stałych i parametrów:
G - stała grawitacji.
m_nd, r_nd, v_nd, t_nd - wartości skalujące używane do przeliczenia jednostek na jednostki niemiarowe.
K1, K2 - stałe używane do obliczania pochodnych i przekształcania jednostek.
m1, m2, m3 - masy trzech ciał.
r1, r2, r3 - początkowe wektory położeń trzech ciał.
v1, v2, v3 - początkowe wektory prędkości trzech ciał.

Obliczanie środka masy:
Obliczanie współrzędnych środka masy trzech ciał na podstawie mas i położeń.

Definiowanie równań ruchu:
Funkcja ThreeBodyEquations oblicza pochodne położeń i prędkości trzech ciał zgodnie z równaniami ruchu opisanymi w kodzie.
Wykorzystuje stałe, masy ciał oraz aktualne położenia i prędkości jako argumenty.

Przygotowanie warunków początkowych i przedziału czasowego:
Tworzenie tablicy init_params zawierającej początkowe wartości położeń i prędkości.
Spłaszczanie tablicy init_params do postaci jednowymiarowej.
Definiowanie time_span jako przedział czasowy, w którym będzie wykonywana symulacja.

Wykonywanie symulacji:
Wywołanie funkcji odeint z modułu scipy.integrate w celu rozwiązania równań ruchu.
Przekazanie funkcji ThreeBodyEquations, warunków początkowych i przedziału czasowego jako argumentów.

Zapisywanie rozwiązania pozycji:
Przypisanie wynikowych położeń do osobnych tablic r1_sol, r2_sol, r3_sol.

Wizualizacja wyników:
Tworzenie figury i osi 3D przy użyciu biblioteki matplotlib.
Rysowanie trajektorii ruchu trzech ciał w przestrzeni 3D.
Dodawanie punktów końcowych reprezentujących trzy ciała.
Ustalanie etykiet, tytułu i legendy wykresu.
Wyświetlanie wykresu z wynikami.

Tworzenie animacji:
Tworzenie figury i osi 3D dla animacji.
Inicjalizowanie punktów reprezentujących trzy ciała na początkowych pozycjach.
Definiowanie funkcji Animate, która aktualizuje pozycje ciał i rysuje trajektorie w kolejnych krokach animacji.
Wywołanie funkcji animation.FuncAnimation w celu utworzenia animacji.
Wyświetlanie animacji.
Kod realizuje symulację ruchu trzech ciał z wykorzystaniem numerycznej integracji równań ruchu oraz wizualizuje wyniki w postaci wykresów 3D oraz animacji.