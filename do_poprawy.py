from PIL import Image, ImageDraw, ImageFont

def text_img_modul(text, filename, font_size=20, image_size=(1200, 400), bg_color=(255, 239, 204), text_color=(0, 0, 0)):
    # Tworzenie nowego obrazu
    image = Image.new('RGB', image_size, bg_color)
    draw = ImageDraw.Draw(image)

    # Użycie czcionki
    font = ImageFont.truetype("/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf", font_size)

    # Podział tekstu na linie
    lines = text.split('\n')
    y_text = 50  # Początkowa pozycja Y dla tekstu

    for line in lines:
        # Obliczanie pozycji tekstu
        text_width, text_height = draw.textsize(line, font=font)
        position = ((image_size[0] - text_width) // 2, y_text)
        draw.text(position, line, fill=text_color, font=font)
        y_text += text_height + 10  # Przesunięcie Y dla następnej linii

    # Zapis obrazu do pliku
    image.save(filename)
    print(f"Obraz zapisany jako {filename}")

# Tekst do dodania
text = """Cześć! Nazywam się Kamil Pietrucha i jestem absolwentem matematyki na Uniwersytecie Rzeszowskim.
Zapraszam wszystkich uczniów szkół podstawowych i ponadpodstawowych na korepetycje z matematyki.
Oferuję: indywidualne podejście do każdego ucznia, pomoc w zrozumieniu trudnych zagadnień,
przygotowanie do sprawdzianów, egzaminów i matury. Zajęcia w przyjaznej atmosferze.
Dostępne są lekcje: stacjonarne w Rzeszowie, online, dostosowane do Twoich potrzeb.
Cena: 60 zł za 60 minut. Chętnie pomogę Ci osiągnąć lepsze wyniki w nauce i zrozumieć matematykę.
Skontaktuj się ze mną już dziś! Tel.: 881 258 636 Facebook: Matematyka Kamil Pietrucha"""

# Wywołanie funkcji
text_img_modul(text, "korepetycje_kamil.png", font_size=18)