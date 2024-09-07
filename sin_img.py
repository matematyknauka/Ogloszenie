def run():
    import matplotlib.pyplot as plt  # Importujemy moduł Matplotlib do rysowania wykresów
    import numpy as np  # Importujemy NumPy do obliczeń numerycznych

    # Generowanie wykresu funkcji sinus
    x = np.linspace(-2 * np.pi, 2 * np.pi, 100)  # Tworzymy 100 punktów od -2π do 2π
    y = np.sin(x)  # Obliczamy wartości funkcji sinus dla tych punktów

    plt.figure(figsize=(7, 4))  # Ustawiamy rozmiar wykresu
    plt.plot(x, y, color='blue', linewidth=2)  # Rysujemy wykres funkcji sinus
    plt.fill_between(x, y, color='skyblue', alpha=0.5)  # Wypełniamy obszar pod wykresem
    plt.axhline(0, color='black', linewidth=0.5, linestyle='--')  # Dodajemy poziomą linię na osi X
    plt.axvline(0, color='black', linewidth=0.5, linestyle='--')  # Dodajemy pionową linię na osi Y
    plt.title('Wykres funkcji sinus', fontsize=14, fontweight='bold')  # Dodajemy tytuł wykresu
    plt.xlabel('x', fontsize=12)  # Etykieta osi X
    plt.ylabel('sin(x)', fontsize=12)  # Etykieta osi Y
    plt.grid(color='gray', linestyle='--', linewidth=0.5)  # Dodajemy siatkę do wykresu

    # Zapisywanie wykresu jako obraz
    plt.savefig('wykres_sinus.png', transparent=True)  # Zapisujemy wykres jako plik PNG z przezroczystym tłem
    plt.show()  # Wyświetlamy wykres
