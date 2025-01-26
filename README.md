<p align="center">
    <img src="logo.png" width="200" alt="OpenCV انجام تکنیک های پردازش تصویر با">
</p>


### مراحل نصب و اجرای مستقل پروژه ها :



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
