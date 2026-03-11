#!/usr/bin/env python3
"""Color converter — RGB, HSL, HSV, HEX, CMYK."""
import sys, colorsys
def hex_to_rgb(h):
    h = h.lstrip('#')
    return tuple(int(h[i:i+2], 16) for i in (0, 2, 4))
def rgb_to_hex(r, g, b): return f"#{r:02x}{g:02x}{b:02x}"
def rgb_to_hsl(r, g, b):
    h, l, s = colorsys.rgb_to_hls(r/255, g/255, b/255)
    return round(h*360), round(s*100), round(l*100)
def rgb_to_cmyk(r, g, b):
    if r==g==b==0: return 0,0,0,100
    c,m,y = 1-r/255, 1-g/255, 1-b/255
    k = min(c,m,y); return round((c-k)/(1-k)*100), round((m-k)/(1-k)*100), round((y-k)/(1-k)*100), round(k*100)
if __name__ == "__main__":
    color = sys.argv[1] if len(sys.argv) > 1 else "#3498db"
    r, g, b = hex_to_rgb(color)
    h, s, l = rgb_to_hsl(r, g, b)
    c, m, y, k = rgb_to_cmyk(r, g, b)
    hsv = colorsys.rgb_to_hsv(r/255, g/255, b/255)
    print(f"HEX:  {rgb_to_hex(r,g,b)}")
    print(f"RGB:  ({r}, {g}, {b})")
    print(f"HSL:  ({h}°, {s}%, {l}%)")
    print(f"HSV:  ({round(hsv[0]*360)}°, {round(hsv[1]*100)}%, {round(hsv[2]*100)}%)")
    print(f"CMYK: ({c}%, {m}%, {y}%, {k}%)")
