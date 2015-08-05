import math
from PIL import Image

width = 512
height = 512
image = Image.new("RGB", (width, height))

# Params (xa < xb & ya < yb)
xa = -1.5
xb = -0.75
ya = 0.0
yb = 0.75
iterations = 256

for ky in range(height):
  for kx in range(width):
    x = xa + (xb - xa) * kx / (width - 1)
    y = ya + (yb - ya) * ky / (height - 1)
    for i in range(iterations):
      try:
        e = math.exp(-0.5 * math.pi * y)
        p = math.pi * x / 2
        x = e * math.cos(p)
        y = e * math.sin(p)
      except:
        break
      if math.hypot(x, y) > 100:
        break
    image.putpixel((kx, ky), (i, i, i))

# Done!
image.save("tetration.png")
