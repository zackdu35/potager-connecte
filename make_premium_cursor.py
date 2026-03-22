from PIL import Image, ImageDraw, ImageFilter
import math

def draw_polygon(draw, polygon, fill, outline, width=1):
    draw.polygon(polygon, fill=fill, outline=outline, width=width)

def make_cursor():
    # Large canvas for smooth drawing then downscale
    scale = 4
    img = Image.new('RGBA', (32*scale, 32*scale), (0,0,0,0))
    
    # Base polygon for a sleek modern arrow
    # Tip at (4,4), Right tip at (24, 13), inner corner at (15, 15), bottom tip at (20, 25), inner notch at (15, 27), left ankle at (10, 17), bottom left at (3, 22)
    poly = [
        (4*scale, 4*scale),
        (22*scale, 12*scale),
        (14*scale, 14*scale),
        (18*scale, 24*scale),
        (14*scale, 26*scale),
        (10*scale, 16*scale),
        (3*scale, 21*scale)
    ]
    
    # 1. Glow layer
    glow = Image.new('RGBA', (32*scale, 32*scale), (0,0,0,0))
    glow_draw = ImageDraw.Draw(glow)
    glow_draw.polygon(poly, fill=(16, 185, 129, 255))
    glow = glow.filter(ImageFilter.GaussianBlur(radius=3*scale))
    
    # 2. Add glow twice for intensity
    img.paste(glow, (0, int(2*scale)), glow)
    
    # 3. Arrow main body (Dark sleak interior)
    main = Image.new('RGBA', (32*scale, 32*scale), (0,0,0,0))
    main_draw = ImageDraw.Draw(main)
    main_draw.polygon(poly, fill=(15, 23, 42, 255), outline=(16, 185, 129, 255), width=int(1.5*scale))
    
    # Compose
    img.paste(main, (0,0), main)
    
    # Resize down
    final = img.resize((32, 32), Image.Resampling.LANCZOS)
    final.save('/Users/zaccharie/Documents/gift papa/docs/assets/cursor.png')

def make_pointer():
    scale = 4
    img = Image.new('RGBA', (32*scale, 32*scale), (0,0,0,0))

    # A sleek hand pointer representation or a smaller sleek arrow? Let's just create a highly styled hand.
    # Actually, a glowing hand pointer. I will use a high quality hand SVG, rasterize it.
    pass

make_cursor()
print("Done base cursor")
