<p align="center">
    <img src="logo.png" width="150" alt="انجام تکنیک‌های پردازش تصویر با OpenCV">
</p>

<p align="center" style="font-size: 16px; font-family: Tahoma, Arial, sans-serif; color: #555;">
    پردازش تصویر با OpenCV
</p>
<br>
<br>

### مراحل نصب و اجرای مستقل پروژه ها :
<br>


### رفتن به فولدر برنامه
    cd D:\firedetection
### ساخت محیط مجازی
    python -m venv fire
### فعال کردن محیط مجازی
    .\fire\Scripts\activate
### نصب کتابخانه مورد نیاز
    pip install numpy opencv-python tensorflow matplotlib
### ساخت فایل نیازمندیهای پروژه
    pip freeze > requirements.txt
### نصب نیازمندی های پروژه در صورت نیاز به صورت یکجا
    pip install -r requirements.txt
### اجرای برنامه
    python main.py
### غیرفعال کردن محیط مجازی برنامه
    deactivate
