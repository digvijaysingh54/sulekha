from PIL import Image, ImageDraw
import os

# Create images folder path
images_folder = r"c:\Users\Digvijay\OneDrive\Documents\sulekha\images"

# Make sure images folder exists
os.makedirs(images_folder, exist_ok=True)

def create_beach_image(filepath, width=1200, height=800):
    """Create an attractive beach-themed image"""
    img = Image.new('RGB', (width, height))
    draw = ImageDraw.Draw(img, 'RGBA')
    
    # Sky gradient (light blue to lighter blue)
    for y in range(height // 2):
        ratio = y / (height // 2)
        r = int(135 + (200 - 135) * ratio)
        g = int(206 + (230 - 206) * ratio)
        b = int(235 + (250 - 235) * ratio)
        draw.line([(0, y), (width, y)], fill=(r, g, b))
    
    # Ocean gradient (deeper blue to lighter blue)
    for y in range(height // 2, height):
        ratio = (y - height // 2) / (height // 2)
        r = int(70 + (240 - 70) * ratio)
        g = int(130 + (248 - 130) * ratio)
        b = int(180 + (255 - 180) * ratio)
        draw.line([(0, y), (width, y)], fill=(r, g, b))
    
    # Add some wave details
    for x in range(0, width, 100):
        draw.ellipse([x, height // 2 - 10, x + 80, height // 2 + 30], 
                     fill=(255, 255, 255, 80))
    
    # Add sand
    draw.rectangle([0, height * 0.55, width, height * 0.7], 
                   fill=(238, 214, 175))
    
    # Add sun/glow
    sun_x, sun_y = width * 0.15, height * 0.15
    draw.ellipse([sun_x - 80, sun_y - 80, sun_x + 80, sun_y + 80], 
                 fill=(255, 200, 87, 200))
    draw.ellipse([sun_x - 60, sun_y - 60, sun_x + 60, sun_y + 60], 
                 fill=(255, 220, 130, 180))
    
    img.save(filepath, 'JPEG', quality=95)
    print(f"✓ Created: {os.path.basename(filepath)}")

def create_temple_image(filepath, width=1200, height=800):
    """Create an attractive temple-themed image"""
    img = Image.new('RGB', (width, height))
    draw = ImageDraw.Draw(img, 'RGBA')
    
    # Sky with golden hour colors
    for y in range(height):
        ratio = y / height
        r = int(255 - (50 * ratio))
        g = int(180 - (80 * ratio))
        b = int(100 - (30 * ratio))
        draw.line([(0, y), (width, y)], fill=(r, g, b))
    
    # Ground
    draw.rectangle([0, height * 0.6, width, height], fill=(139, 110, 75))
    
    # Temple silhouette (simplified triangular shape)
    temple_x = width // 2
    temple_base_y = height * 0.6
    
    # Main temple structure
    points = [
        (temple_x - 150, temple_base_y),
        (temple_x + 150, temple_base_y),
        (temple_x + 100, temple_base_y - 200),
        (temple_x, temple_base_y - 300),
        (temple_x - 100, temple_base_y - 200)
    ]
    draw.polygon(points, fill=(180, 100, 60))
    
    # Add dome top (golden)
    dome_x, dome_y = temple_x, temple_base_y - 310
    draw.ellipse([dome_x - 40, dome_y - 60, dome_x + 40, dome_y + 20], 
                 fill=(255, 200, 80))
    
    # Add spiritual glow
    draw.ellipse([dome_x - 80, dome_y - 100, dome_x + 80, dome_y + 60], 
                 fill=(255, 200, 100, 100))
    
    # Add decorative elements
    for i in range(5):
        x = width * 0.2 + i * width * 0.15
        y = temple_base_y - 150
        draw.ellipse([x - 15, y - 15, x + 15, y + 15], fill=(200, 100, 50))
    
    img.save(filepath, 'JPEG', quality=95)
    print(f"✓ Created: {os.path.basename(filepath)}")

def create_nature_image(filepath, width=1200, height=800):
    """Create an attractive nature/hills image"""
    img = Image.new('RGB', (width, height))
    draw = ImageDraw.Draw(img, 'RGBA')
    
    # Sky gradient (morning/misty)
    for y in range(height):
        ratio = y / height
        r = int(200 - (50 * ratio))
        g = int(220 - (80 * ratio))
        b = int(240 - (60 * ratio))
        draw.line([(0, y), (width, y)], fill=(r, g, b))
    
    # Mountains (layered)
    # Back mountain
    mountain1_points = [(0, height * 0.5), (width * 0.3, height * 0.2), (width * 0.6, height * 0.5)]
    draw.polygon(mountain1_points, fill=(100, 140, 100))
    
    # Front mountain
    mountain2_points = [(width * 0.2, height * 0.55), (width * 0.7, height * 0.35), (width, height * 0.55)]
    draw.polygon(mountain2_points, fill=(80, 120, 80))
    
    # Ground
    draw.rectangle([0, height * 0.55, width, height], fill=(120, 180, 100))
    
    # Add trees (simple triangles)
    for x in [width * 0.15, width * 0.4, width * 0.75, width * 0.9]:
        y_base = height * 0.55
        # Tree top
        tree_points = [(x - 30, y_base), (x + 30, y_base), (x, y_base - 80)]
        draw.polygon(tree_points, fill=(60, 100, 60))
        # Tree trunk
        draw.rectangle([x - 8, y_base - 30, x + 8, y_base], fill=(101, 67, 33))
    
    # Add sun rays/glow
    sun_x, sun_y = width * 0.15, height * 0.2
    draw.ellipse([sun_x - 50, sun_y - 50, sun_x + 50, sun_y + 50], 
                 fill=(255, 200, 100, 150))
    
    img.save(filepath, 'JPEG', quality=95)
    print(f"✓ Created: {os.path.basename(filepath)}")

def create_spiritual_image(filepath, width=1200, height=800):
    """Create a spiritual/meditation themed image"""
    img = Image.new('RGB', (width, height))
    draw = ImageDraw.Draw(img, 'RGBA')
    
    # Meditation/spiritual gradient (purples and blues)
    for y in range(height):
        ratio = y / height
        r = int(100 + (50 * ratio))
        g = int(100 + (50 * ratio))
        b = int(200 - (50 * ratio))
        draw.line([(0, y), (width, y)], fill=(r, g, b))
    
    # Lotus pond area
    draw.rectangle([0, height * 0.5, width, height], fill=(50, 100, 80))
    
    # Water reflection
    for i in range(5):
        y = height * 0.5 + i * 30
        draw.line([(0, y), (width, y)], fill=(30, 80, 60, 100))
    
    # Lotus flowers (circles)
    lotus_positions = [(width * 0.2, height * 0.65), (width * 0.5, height * 0.7), 
                       (width * 0.8, height * 0.65), (width * 0.35, height * 0.55)]
    for lx, ly in lotus_positions:
        # Petals
        draw.ellipse([lx - 40, ly - 40, lx + 40, ly + 40], fill=(200, 150, 200))
        # Center
        draw.ellipse([lx - 15, ly - 15, lx + 15, ly + 15], fill=(255, 200, 100))
    
    # Moon in sky
    moon_x, moon_y = width * 0.85, height * 0.15
    draw.ellipse([moon_x - 60, moon_y - 60, moon_x + 60, moon_y + 60], 
                 fill=(240, 240, 220))
    
    # Stars
    import random
    random.seed(42)
    for _ in range(20):
        star_x = random.randint(0, width)
        star_y = random.randint(0, int(height * 0.4))
        draw.ellipse([star_x - 3, star_y - 3, star_x + 3, star_y + 3], 
                     fill=(255, 255, 200))
    
    img.save(filepath, 'JPEG', quality=95)
    print(f"✓ Created: {os.path.basename(filepath)}")

# Create all images
print("🎨 Creating attractive travel and hobbies images...")
print()

create_beach_image(os.path.join(images_folder, "beach-sunset.jpg"))
create_temple_image(os.path.join(images_folder, "temple-golden-hour.jpg"))
create_nature_image(os.path.join(images_folder, "nature-mountains.jpg"))
create_spiritual_image(os.path.join(images_folder, "spiritual-meditation.jpg"))

print()
print("✨ All images created successfully!")
print("📸 Location: c:\\Users\\Digvijay\\OneDrive\\Documents\\sulekha\\images\\")
