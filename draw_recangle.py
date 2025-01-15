from PIL import Image, ImageDraw

def draw_rectangle_on_image(image_path, x, y, width, height):
    # باز کردن تصویر
    img = Image.open(image_path)

    # ایجاد یک شیء برای رسم
    draw = ImageDraw.Draw(img)

    # کشیدن کادر
    draw.rectangle([x, y, x + width, y + height], outline="red", width=3)

    # نمایش تصویر
    img.show()

# مشخصات کادر: (مختصات، عرض، ارتفاع)
image_path = "D:/screenshots/screenshot_029.png"  # مسیر تصویر
x = 200  # مختصات X
y = 00  # مختصات Y
width = 480  # عرض کادر
height = 700  # ارتفاع کادر

# فراخوانی تابع
draw_rectangle_on_image(image_path, x, y, width, height)
