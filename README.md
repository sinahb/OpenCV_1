# OpenCV_1
انجام تکنیک های پردازش تصویر با Opencv روی تصاویر

مراحل نصب و اجرای مستقل پروژه ها :
رفتن به فولدر برنامه
cd D:\firedetection
ساخت محیط مجازی
python -m venv fire
فعال کردن محیط مجازی
.\fire\Scripts\activate
نصب کتابخانه مورد نیاز
pip install numpy opencv-python tensorflow matplotlib
ساخت فایل نیازمندیهای پروژه
pip freeze > requirements.txt
نصب نیازمندیهای پروژه در صورت نیاز به صورت یکجا
pip install -r requirements.txt
اجرای برنامه
python main.py
غیرفعال کردن محیط مجازی برنامه
deactivate
