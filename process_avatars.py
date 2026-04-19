from PIL import Image
import os

def create_circular_avatar(input_path, output_path, size=80):
    """Corta uma foto em circular"""
    img = Image.open(input_path)
    
    # Redimensionar para quadrado
    img = img.resize((size, size), Image.Resampling.LANCZOS)
    
    # Criar máscara circular
    mask = Image.new('L', (size, size), 0)
    from PIL import ImageDraw
    draw = ImageDraw.Draw(mask)
    draw.ellipse([0, 0, size, size], fill=255)
    
    # Aplicar máscara
    img.putalpha(mask)
    img.save(output_path)
    print(f"✅ Avatar criado: {output_path}")

# Processar as 3 fotos
avatars = [
    ('/home/ubuntu/lp/avatar-mae-1.jpg', '/home/ubuntu/lp/avatar-1.png'),
    ('/home/ubuntu/lp/avatar-mae-2.jpg', '/home/ubuntu/lp/avatar-2.png'),
    ('/home/ubuntu/lp/avatar-mae-3.jpg', '/home/ubuntu/lp/avatar-3.png'),
]

for input_file, output_file in avatars:
    if os.path.exists(input_file):
        create_circular_avatar(input_file, output_file)
    else:
        print(f"⚠️ Arquivo não encontrado: {input_file}")
