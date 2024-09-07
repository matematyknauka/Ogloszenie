from PIL import Image, ImageDraw, ImageFont

def text_img_modul(text, filename, font_size=20, image_size=(400, 200), bg_color=(255, 239, 204), text_color=(0, 0, 0)): # Podać tylko dwie zmienne.
    # Tworzenie nowego obrazu
    image = Image.new('RGB', image_size, bg_color)
    draw = ImageDraw.Draw(image)

    # Use a different font that's available in your system
    font = ImageFont.truetype("/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf", font_size)

    # Obliczanie pozycji tekstu
    text_width, text_height = draw.textsize(text, font=font)
    position = ((image_size[0] - text_width) // 2, (image_size[1] - text_height) // 2)

    # Rysowanie tekstu na obrazie
    draw.text(position, text, fill=text_color, font=font)
    draw.text((0, 0, 0), text, fill=text_color, font=font)

    # Zapis obrazu do pliku
    image.save(filename)
    print(f"Obraz zapisany jako {filename}")