#!/usr/bin/env python3
"""color_convert — Color space conversion (RGB/HSL/HSV/HEX/CMYK). Zero deps."""
import sys

def hex_to_rgb(h):
    h = h.lstrip('#')
    return tuple(int(h[i:i+2], 16) for i in (0, 2, 4))

def rgb_to_hex(r, g, b):
    return f"#{r:02x}{g:02x}{b:02x}"

def rgb_to_hsl(r, g, b):
    r, g, b = r/255, g/255, b/255
    mx, mn = max(r,g,b), min(r,g,b)
    l = (mx + mn) / 2
    if mx == mn:
        h = s = 0
    else:
        d = mx - mn
        s = d / (2 - mx - mn) if l > 0.5 else d / (mx + mn)
        if mx == r: h = (g - b) / d + (6 if g < b else 0)
        elif mx == g: h = (b - r) / d + 2
        else: h = (r - g) / d + 4
        h /= 6
    return round(h*360), round(s*100), round(l*100)

def rgb_to_hsv(r, g, b):
    r, g, b = r/255, g/255, b/255
    mx, mn = max(r,g,b), min(r,g,b)
    v = mx
    s = 0 if mx == 0 else (mx - mn) / mx
    if mx == mn: h = 0
    elif mx == r: h = (g - b) / (mx - mn) % 6
    elif mx == g: h = (b - r) / (mx - mn) + 2
    else: h = (r - g) / (mx - mn) + 4
    return round(h*60) % 360, round(s*100), round(v*100)

def rgb_to_cmyk(r, g, b):
    if r == g == b == 0: return 0, 0, 0, 100
    c, m, y = 1-r/255, 1-g/255, 1-b/255
    k = min(c, m, y)
    return round((c-k)/(1-k)*100), round((m-k)/(1-k)*100), round((y-k)/(1-k)*100), round(k*100)

def ansi_color(r, g, b, text=" ██ "):
    return f"\033[48;2;{r};{g};{b}m{text}\033[0m"

def main():
    colors = [("#ff6b6b","Coral"), ("#4ecdc4","Teal"), ("#45b7d1","Sky"),
              ("#f7dc6f","Gold"), ("#8e44ad","Purple"), ("#2ecc71","Emerald")]
    print("Color Converter:\n")
    print(f"  {'Name':<10} {'HEX':<10} {'RGB':<15} {'HSL':<15} {'HSV':<15} {'CMYK':<20}")
    for hex_val, name in colors:
        r, g, b = hex_to_rgb(hex_val)
        hsl = rgb_to_hsl(r, g, b)
        hsv = rgb_to_hsv(r, g, b)
        cmyk = rgb_to_cmyk(r, g, b)
        swatch = ansi_color(r, g, b)
        print(f"  {name:<10} {hex_val:<10} ({r},{g},{b}){'':>4} "
              f"({hsl[0]}°,{hsl[1]}%,{hsl[2]}%){'':>2} "
              f"({hsv[0]}°,{hsv[1]}%,{hsv[2]}%){'':>2} "
              f"({cmyk[0]},{cmyk[1]},{cmyk[2]},{cmyk[3]}) {swatch}")

if __name__ == "__main__":
    main()
