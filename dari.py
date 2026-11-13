#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""پایتون دری ۳ — موتور فارسی مستقل، در یک فایل.

این فایل خودش زبان فارسی را می‌خواند (تحلیل‌گر واژه و دستور اختصاصی) و برنامه را
با پایتون واقعی اجرا می‌کند؛ پس همه‌ی کتابخانه‌های پایتون (numpy، pandas، kivy ...) در دسترس است.
هیچ مترجمی، متن انگلیسی‌ای نمی‌سازد: فارسی مستقیم به درخت دستور پایتون تبدیل می‌شود.
دستورهای انگلیسی (print، if ...) مجاز نیستند و خطای فارسی می‌دهند.

اجرا در Pydroid: این فایل را باز کنید و دکمه‌ی زرد را بزنید (منوی فارسی می‌آید).
در ترمینال:
    python dari.py برنامه.py      اجرای برنامه
    python dari.py پوسته          محیط تعاملی
    python dari.py کتابخانه‌ها      فهرست کتابخانه‌ها
    python dari.py نصب numpy      نصب کتابخانه
"""
__version__ = "3.0"
import sys as _s, os as _o
try:
    __file__
except NameError:
    __file__ = _o.path.abspath(_s.argv[0] if _s.argv and _s.argv[0] else "dari.py")
"""جدول‌های واژه: کلمه‌های کلیدی، توابع آماده، متدها و نام کتابخانه‌ها."""

KEYWORDS = {
 "اگر": "if",
 "وگر": "elif",
 "وگرنه": "else",
 "برای": "for",
 "در": "in",
 "مادام": "while",
 "تعریف": "def",
 "برگردان": "return",
 "کلاس": "class",
 "درست": "True",
 "نادرست": "False",
 "هیچ": "None",
 "و": "and",
 "یا": "or",
 "نه": "not",
 "است": "is",
 "وارد": "import",
 "از": "from",
 "به_عنوان": "as",
 "امتحان": "try",
 "خطا": "except",
 "سرانجام": "finally",
 "بشکن": "break",
 "ادامه": "continue",
 "بگذر": "pass",
 "با": "with",
 "بالابر": "raise",
 "سراسری": "global",
 "غیرمحلی": "nonlocal",
 "تولید": "yield",
 "لامبدا": "lambda",
 "حذف": "del",
 "ادعا": "assert",
 "ناهمگام": "async",
 "منتظر": "await"
}

BUILTINS = {
 "چاپ": "print",
 "ورودی": "input",
 "طول": "len",
 "دامنه": "range",
 "عدد_صحیح": "int",
 "عدد_اعشاری": "float",
 "متن": "str",
 "منطقی": "bool",
 "فهرست": "list",
 "چندتایی": "tuple",
 "دیکشنری": "dict",
 "مجموعه": "set",
 "جمع": "sum",
 "بیشینه": "max",
 "کمینه": "min",
 "مرتب": "sorted",
 "وارونه": "reversed",
 "نوع": "type",
 "باز": "open",
 "مطلق": "abs",
 "گرد": "round",
 "توان": "pow",
 "شمارش": "enumerate",
 "نگاشت": "map",
 "فیلتر": "filter",
 "زیپ": "zip",
 "همه": "all",
 "هرکدام": "any",
 "اسکی": "ascii",
 "دودویی": "bin",
 "بایت": "bytes",
 "فراخوانی_پذیر": "callable",
 "نویسه": "chr",
 "فهرست_نام_ها": "dir",
 "خارج_قسمت_باقی": "divmod",
 "ارزیابی": "eval",
 "اجرا_کد": "exec",
 "قالب": "format",
 "مجموعه_ثابت": "frozenset",
 "دریافت_ویژگی": "getattr",
 "دارد_ویژگی": "hasattr",
 "هش": "hash",
 "شانزده_دهی": "hex",
 "شناسه": "id",
 "نمونه_است": "isinstance",
 "زیرکلاس_است": "issubclass",
 "تکرارگر": "iter",
 "بعدی": "next",
 "شیء": "object",
 "هشت_هشتی": "oct",
 "کد_نویسه": "ord",
 "نمایش": "repr",
 "تنظیم_ویژگی": "setattr",
 "برش": "slice",
 "والد": "super",
 "مختلط": "complex",
 "ویژگی_ساز": "property",
 "متد_ایستا": "staticmethod",
 "متد_کلاس": "classmethod",
 "بایت_تغییرپذیر": "bytearray",
 "متغیرهای_محلی": "locals",
 "متغیرهای_سراسری": "globals",
 "استثنا": "Exception",
 "استثنای_پایه": "BaseException",
 "خطای_مقدار": "ValueError",
 "خطای_نوع": "TypeError",
 "خطای_نام": "NameError",
 "خطای_اندیس": "IndexError",
 "خطای_کلید": "KeyError",
 "خطای_تقسیم_بر_صفر": "ZeroDivisionError",
 "خطای_ویژگی": "AttributeError",
 "خطای_وارد_کردن": "ImportError",
 "خطای_سیستم": "OSError",
 "خطای_فایل_پیدا_نشد": "FileNotFoundError",
 "پایان_تکرار": "StopIteration",
 "خطای_اجرا": "RuntimeError",
 "خطای_ادعا": "AssertionError",
 "خطای_پیاده_نشده": "NotImplementedError",
 "خطای_سرریز": "OverflowError",
 "خطای_بازگشت": "RecursionError",
 "خطای_نوشتار": "SyntaxError",
 "خطای_تورفتگی": "IndentationError"
}

METHODS = {
 "اضافه": "append",
 "افزودن_همه": "extend",
 "درج": "insert",
 "بردار": "remove",
 "بردار_آخر": "pop",
 "پاک": "clear",
 "شاخص": "index",
 "شمار": "count",
 "مرتب_کن": "sort",
 "وارونه_کن": "reverse",
 "کپی": "copy",
 "کلیدها": "keys",
 "مقدارها": "values",
 "جفت_ها": "items",
 "بگیر": "get",
 "به_روز": "update",
 "پیش_فرض_بگذار": "setdefault",
 "بزرگ": "upper",
 "کوچک": "lower",
 "حذف_فاصله": "strip",
 "جدا_کن": "split",
 "بچسبان": "join",
 "جایگزین": "replace",
 "پیدا_کن": "find",
 "شروع_با": "startswith",
 "پایان_با": "endswith",
 "قالب_بده": "format",
 "عنوان": "title",
 "رقم_است": "isdigit",
 "حرف_است": "isalpha",
 "افزودن": "add",
 "اجتماع": "union",
 "اشتراک": "intersection",
 "تفاضل": "difference",
 "بخوان": "read",
 "بنویس": "write",
 "خط_بخوان": "readline",
 "خط_ها_را_بخوان": "readlines",
 "ببند": "close",
 "ریشه_دوم": "sqrt",
 "کف": "floor",
 "سقف": "ceil",
 "پی": "pi",
 "سینوس": "sin",
 "کسینوس": "cos",
 "تصادفی_صحیح": "randint",
 "انتخاب_کن": "choice",
 "بر_زن": "shuffle",
 "تصادفی_اعشاری": "random",
 "بخواب": "sleep",
 "زمان_اکنون": "time",
 "امروز": "today",
 "اکنون": "now",
 "جلو": "forward",
 "عقب": "backward",
 "راست": "right",
 "چپ": "left",
 "رنگ": "color",
 "سرعت": "speed",
 "قلم_بالا": "penup",
 "قلم_پایین": "pendown"
}

# (نام انگلیسی، نام فارسی) کتابخانه‌های استاندارد پایتون
STDLIB = [
 [
  "abc",
  "کلاس_انتزاعی"
 ],
 [
  "argparse",
  "آرگومان_خط_فرمان"
 ],
 [
  "array",
  "آرایه"
 ],
 [
  "ast",
  "درخت_نحو"
 ],
 [
  "asyncio",
  "ناهمگام_سازی"
 ],
 [
  "atexit",
  "هنگام_خروج"
 ],
 [
  "base64",
  "بیس_شصت_و_چهار"
 ],
 [
  "bisect",
  "تقسیم_دودویی"
 ],
 [
  "builtins",
  "توابع_آماده"
 ],
 [
  "bz2",
  "فشرده_ساز_بی_زد_دو"
 ],
 [
  "calendar",
  "تقویم"
 ],
 [
  "cmath",
  "ریاضی_مختلط"
 ],
 [
  "cmd",
  "فرمان_تعاملی"
 ],
 [
  "codecs",
  "رمزگذاری_متن"
 ],
 [
  "collections",
  "مجموعه_ها"
 ],
 [
  "colorsys",
  "رنگ_ها"
 ],
 [
  "concurrent",
  "همزمانی"
 ],
 [
  "configparser",
  "پیکربندی"
 ],
 [
  "contextlib",
  "زمینه"
 ],
 [
  "copy",
  "رونوشت"
 ],
 [
  "csv",
  "سی_اس_وی"
 ],
 [
  "ctypes",
  "سی_تایپ"
 ],
 [
  "dataclasses",
  "کلاس_داده"
 ],
 [
  "datetime",
  "تاریخ_زمان"
 ],
 [
  "decimal",
  "اعشاری_دقیق"
 ],
 [
  "difflib",
  "تفاوت_متن"
 ],
 [
  "dis",
  "جداسازی_کد"
 ],
 [
  "doctest",
  "آزمون_مستند"
 ],
 [
  "email",
  "ایمیل"
 ],
 [
  "enum",
  "شمارشی"
 ],
 [
  "errno",
  "کد_خطا"
 ],
 [
  "fnmatch",
  "الگوی_نام_فایل"
 ],
 [
  "fractions",
  "کسرها"
 ],
 [
  "ftplib",
  "اف_تی_پی"
 ],
 [
  "functools",
  "ابزار_توابع"
 ],
 [
  "gc",
  "زباله_روب"
 ],
 [
  "getpass",
  "رمز_ورودی"
 ],
 [
  "gettext",
  "ترجمه_متن"
 ],
 [
  "glob",
  "جستجوی_فایل"
 ],
 [
  "graphlib",
  "گراف"
 ],
 [
  "gzip",
  "جی_زیپ"
 ],
 [
  "hashlib",
  "هش_سازی"
 ],
 [
  "heapq",
  "هرم"
 ],
 [
  "hmac",
  "اچ_مک"
 ],
 [
  "html",
  "اچ_تی_ام_ال"
 ],
 [
  "http",
  "اچ_تی_تی_پی"
 ],
 [
  "imaplib",
  "ایمپ"
 ],
 [
  "importlib",
  "وارد_کردن_پویا"
 ],
 [
  "inspect",
  "بازرسی"
 ],
 [
  "io",
  "ورودی_خروجی"
 ],
 [
  "ipaddress",
  "آدرس_آی_پی"
 ],
 [
  "itertools",
  "تکرارگرها"
 ],
 [
  "json",
  "جیسون"
 ],
 [
  "keyword",
  "کلمات_کلیدی"
 ],
 [
  "linecache",
  "کش_خط"
 ],
 [
  "locale",
  "محلی_سازی"
 ],
 [
  "logging",
  "گزارش_گیری"
 ],
 [
  "lzma",
  "ال_زد_ام_ای"
 ],
 [
  "mailbox",
  "صندوق_نامه"
 ],
 [
  "math",
  "ریاضی"
 ],
 [
  "mimetypes",
  "انواع_فایل"
 ],
 [
  "mmap",
  "نگاشت_حافظه"
 ],
 [
  "multiprocessing",
  "چند_پردازشی"
 ],
 [
  "numbers",
  "اعداد"
 ],
 [
  "operator",
  "عملگرها"
 ],
 [
  "os",
  "سیستم_عامل"
 ],
 [
  "pathlib",
  "مسیر"
 ],
 [
  "pickle",
  "ذخیره_شیء"
 ],
 [
  "pkgutil",
  "بسته_ها"
 ],
 [
  "platform",
  "پلتفرم"
 ],
 [
  "poplib",
  "پاپ"
 ],
 [
  "pprint",
  "چاپ_زیبا"
 ],
 [
  "queue",
  "صف"
 ],
 [
  "random",
  "تصادفی"
 ],
 [
  "re",
  "عبارت_منظم"
 ],
 [
  "sched",
  "زمان_بند"
 ],
 [
  "secrets",
  "رمزهای_امن"
 ],
 [
  "select",
  "انتخاب_ورودی"
 ],
 [
  "shelve",
  "قفسه"
 ],
 [
  "shlex",
  "تجزیه_فرمان"
 ],
 [
  "shutil",
  "ابزار_فایل"
 ],
 [
  "signal",
  "سیگنال"
 ],
 [
  "smtplib",
  "ارسال_ایمیل"
 ],
 [
  "socket",
  "سوکت"
 ],
 [
  "socketserver",
  "سرور_سوکت"
 ],
 [
  "sqlite3",
  "پایگاه_داده"
 ],
 [
  "ssl",
  "اس_اس_ال"
 ],
 [
  "stat",
  "وضعیت_فایل"
 ],
 [
  "statistics",
  "آمار"
 ],
 [
  "string",
  "رشته"
 ],
 [
  "struct",
  "ساختار_بایت"
 ],
 [
  "subprocess",
  "زیرفرایند"
 ],
 [
  "sys",
  "سیستم"
 ],
 [
  "tarfile",
  "تار"
 ],
 [
  "tempfile",
  "فایل_موقت"
 ],
 [
  "textwrap",
  "بسته_بندی_متن"
 ],
 [
  "threading",
  "نخ_ها"
 ],
 [
  "time",
  "زمان"
 ],
 [
  "timeit",
  "زمان_سنج"
 ],
 [
  "tkinter",
  "رابط_تی_کی"
 ],
 [
  "traceback",
  "ردیابی_خطا"
 ],
 [
  "turtle",
  "لاک_پشت"
 ],
 [
  "types",
  "انواع"
 ],
 [
  "typing",
  "نوع_دهی"
 ],
 [
  "unicodedata",
  "یونیکد"
 ],
 [
  "unittest",
  "آزمون_واحد"
 ],
 [
  "urllib",
  "یو_آر_ال"
 ],
 [
  "uuid",
  "شناسه_یکتا"
 ],
 [
  "venv",
  "محیط_مجازی"
 ],
 [
  "warnings",
  "هشدارها"
 ],
 [
  "wave",
  "موج_صدا"
 ],
 [
  "weakref",
  "ارجاع_ضعیف"
 ],
 [
  "webbrowser",
  "مرورگر"
 ],
 [
  "xml",
  "ایکس_ام_ال"
 ],
 [
  "zipfile",
  "فایل_زیپ"
 ],
 [
  "zlib",
  "زد_لیب"
 ],
 [
  "zoneinfo",
  "منطقه_زمانی"
 ],
 [
  "this",
  "ذن_پایتون"
 ]
]

# (نام import، نام فارسی، نام pip) کتابخانه‌های بیرونی که با pip نصب می‌شوند
THIRD_PARTY = [
 [
  "kivy",
  "کیوی",
  "kivy"
 ],
 [
  "numpy",
  "نامپای",
  "numpy"
 ],
 [
  "pandas",
  "پاندا",
  "pandas"
 ],
 [
  "requests",
  "ریکوئست",
  "requests"
 ],
 [
  "flask",
  "فلسک",
  "flask"
 ],
 [
  "django",
  "جنگو",
  "django"
 ],
 [
  "fastapi",
  "فست_ای_پی_آی",
  "fastapi"
 ],
 [
  "uvicorn",
  "یووی_کورن",
  "uvicorn"
 ],
 [
  "jinja2",
  "جینجا",
  "jinja2"
 ],
 [
  "pygame",
  "پایگیم",
  "pygame"
 ],
 [
  "matplotlib",
  "ماتپلات_لیب",
  "matplotlib"
 ],
 [
  "PIL",
  "پیلو",
  "pillow"
 ],
 [
  "scipy",
  "سای_پای",
  "scipy"
 ],
 [
  "sklearn",
  "یادگیری_ماشین",
  "scikit-learn"
 ],
 [
  "bs4",
  "زیبا_سوپ",
  "beautifulsoup4"
 ],
 [
  "selenium",
  "سلنیوم",
  "selenium"
 ],
 [
  "sqlalchemy",
  "اس_کیو_ال_آلکمی",
  "sqlalchemy"
 ],
 [
  "cv2",
  "اوپن_سی_وی",
  "opencv-python"
 ],
 [
  "yt_dlp",
  "یوتیوب_دی_ال",
  "yt-dlp"
 ],
 [
  "PyQt5",
  "پای_کیو_تی",
  "PyQt5"
 ],
 [
  "torch",
  "تورچ",
  "torch"
 ],
 [
  "tensorflow",
  "تنسورفلو",
  "tensorflow"
 ],
 [
  "openpyxl",
  "اکسل",
  "openpyxl"
 ],
 [
  "redis",
  "ردیس",
  "redis"
 ],
 [
  "pytest",
  "پای_تست",
  "pytest"
 ],
 [
  "rich",
  "ریچ",
  "rich"
 ],
 [
  "click",
  "کلیک",
  "click"
 ],
 [
  "arabic_reshaper",
  "اصلاح_حروف",
  "arabic-reshaper"
 ],
 [
  "bidi",
  "جهت_متن",
  "python-bidi"
 ],
 [
  "telebot",
  "تلگرام_بات",
  "pyTelegramBotAPI"
 ],
 [
  "aiohttp",
  "ای_او_اچ_تی_تی_پی",
  "aiohttp"
 ],
 [
  "websockets",
  "وب_سوکت",
  "websockets"
 ],
 [
  "moviepy",
  "فیلم_پای",
  "moviepy"
 ]
]

MODULES = {fa: en for en, fa in STDLIB}
MODULES.update({fa: en for en, fa, _pip in THIRD_PARTY})
PIP_NAMES = {en: pip for en, _fa, pip in THIRD_PARTY}
PERSIAN_OF = {en: fa for fa, en in MODULES.items()}


"""توضیح فارسی برای خطاهای رایج پایتون."""

import re

TITLES = {
    "NameError": "نام یا متغیری استفاده شده که تعریف نشده",
    "SyntaxError": "نوشتار کد اشتباه است",
    "IndentationError": "تورفتگی خط‌ها درست نیست",
    "TabError": "تب و فاصله با هم قاطی شده‌اند",
    "TypeError": "نوع داده‌ها با هم جور نیست",
    "ValueError": "مقدار مناسب نیست",
    "ZeroDivisionError": "تقسیم بر صفر",
    "IndexError": "شماره‌ی خانه از فهرست بیرون است",
    "KeyError": "کلید پیدا نشد",
    "AttributeError": "ویژگی یا تابع وجود ندارد",
    "ImportError": "وارد کردن (import) انجام نشد",
    "ModuleNotFoundError": "کتابخانه نصب نیست",
    "FileNotFoundError": "فایل یا پوشه پیدا نشد",
    "PermissionError": "اجازه‌ی دسترسی نیست",
    "RecursionError": "تابع بی‌پایان خودش را صدا می‌زند",
    "KeyboardInterrupt": "برنامه با کنترل‌سی متوقف شد",
    "OverflowError": "عدد از حد مجاز بزرگ‌تر است",
    "UnicodeDecodeError": "خواندن متن با این رمزگذاری ممکن نیست (encoding='utf-8' را امتحان کنید)",
    "ConnectionError": "اتصال شبکه برقرار نشد",
    "OSError": "خطای سیستم یا فایل",
    "AssertionError": "ادعای برنامه (ادعا) برقرار نبود",
}


def explain(exc):
    """(عنوان، توضیح) فارسی برای یک استثنا برمی‌گرداند."""
    name = type(exc).__name__
    msg = str(exc)
    title = TITLES.get(name) or next((TITLES[b.__name__] for b in type(exc).__mro__ if b.__name__ in TITLES), "خطا در اجرای برنامه")
    detail, m = "", None
    if name == "NameError" and (m := re.search(r"name '(.+?)' is not defined", msg)):
        detail = "«%s» هنوز ساخته نشده یا املایش غلط است. اول به آن مقدار بدهید." % m.group(1)
    elif name == "ZeroDivisionError":
        detail = "تقسیم یا باقی‌مانده بر صفر ممکن نیست."
    elif name == "ValueError" and (m := re.search(r"invalid literal for int\(\) with base 10: (.+)", msg)):
        detail = "%s عدد صحیح نیست و تبدیل نمی‌شود." % m.group(1)
    elif name == "TypeError" and "unsupported operand" in msg:
        detail = "این دو مقدار را نمی‌شود با این عملگر ترکیب کرد (مثلاً جمع کردن عدد با متن). یکی را با متن() یا عدد_صحیح() تبدیل کنید."
    elif name == "TypeError" and "not callable" in msg:
        detail = "چیزی که مثل تابع صدا زده شده تابع نیست. نام متغیر را با نام تابع یکی نکرده باشید."
    elif name == "TypeError" and "argument" in msg:
        detail = "تعداد یا نوع ورودی‌های تابع درست نیست."
    elif name == "IndexError":
        detail = "شماره‌ی خانه از تعداد عضوها بیشتر است. شمارش از ۰ شروع می‌شود."
    elif name == "KeyError":
        detail = "این کلید در دیکشنری نیست: %s" % msg
    elif name == "AttributeError" and (m := re.search(r"'(.+?)' object has no attribute '(.+?)'", msg)):
        detail = "شیء از نوع «%s» ویژگی یا تابعی به نام «%s» ندارد." % (m.group(1), m.group(2))
    elif name == "ModuleNotFoundError" and (m := re.search(r"No module named '([\w.]+)'", msg)):
        detail = "کتابخانه‌ی «%s» نصب نیست. با دستور  farsi install %s  نصبش کنید." % (m.group(1), m.group(1).split(".")[0])
    elif name in ("SyntaxError", "IndentationError", "TabError"):
        detail = "پرانتز، دو نقطه (:)، نقل‌قول و تورفتگی همان خط و خط قبلش را بررسی کنید."
    elif name == "FileNotFoundError":
        detail = "مسیر فایل را بررسی کنید: %s" % (getattr(exc, "filename", None) or msg)
    return title, detail




import ast
import re
import linecache
import importlib.abc
import importlib.machinery
import traceback

# ===================== جدول‌های کمکی موتور =====================
KWARGS = {"پایان": "end", "جداکننده": "sep", "کلید": "key", "وارونه": "reverse", "فایل": "file", "حالت": "mode",
          "رمزگذاری": "encoding", "شروع": "start", "پیش_فرض": "default", "پایه": "base", "فاصله": "indent"}
DUNDER = {"ساز": "__init__", "متن_شیء": "__str__", "نمایش_شیء": "__repr__", "طول_شیء": "__len__",
          "دریافت_عضو": "__getitem__", "تنظیم_عضو": "__setitem__", "حذف_عضو": "__delitem__", "فراخوانی": "__call__",
          "ورود_به_بلوک": "__enter__", "خروج_از_بلوک": "__exit__", "تکرارگر_شیء": "__iter__", "بعدی_شیء": "__next__",
          "برابر_است": "__eq__", "جمع_شیء": "__add__", "شامل_است": "__contains__", "کمتر_است": "__lt__",
          "هش_شیء": "__hash__", "نابود": "__del__"}
_ALL_BUILTINS = dict(BUILTINS)
_ALL_BUILTINS.update(DUNDER)
_ENG_SKIP = {"id", "type", "format", "hash", "object", "vars", "dir", "license", "credits", "copyright", "help", "exit", "quit",
             "Ellipsis", "NotImplemented"}
ENGLISH_KW = {}
for _fa, _en in KEYWORDS.items():
    ENGLISH_KW.setdefault(_en, _fa)
ENGLISH_BI = {}
for _fa, _en in BUILTINS.items():
    if not _en.startswith("_") and _en not in _ENG_SKIP:
        ENGLISH_BI.setdefault(_en, _fa)
TABLES = {"KEYWORDS": KEYWORDS, "BUILTINS": _ALL_BUILTINS, "METHODS": METHODS, "MODULES": MODULES, "KWARGS": KWARGS,
          "ENGLISH_KW": ENGLISH_KW, "ENGLISH_BI": ENGLISH_BI}


# ===================== موتور: تحلیل‌گر واژه‌ها (Lexer) =====================
# کد فارسی را مستقیماً به نشانه (token) تبدیل می‌کند. هیچ متن انگلیسی‌ای ساخته نمی‌شود.

ZWNJ = "\u200c"
_DIG = str.maketrans("۰۱۲۳۴۵۶۷۸۹٠١٢٣٤٥٦٧٨٩", "01234567890123456789")


class DariSyntaxError(Exception):
    """خطای نوشتاری فارسی با جای دقیق."""
    def __init__(self, title, detail="", line=0, col=0, length=1):
        Exception.__init__(self, title)
        self.title, self.detail, self.line, self.col, self.length = title, detail, line, col, length


class Tok:
    __slots__ = ("t", "v", "line", "col", "eline", "ecol")

    def __init__(self, t, v, line, col, eline=None, ecol=None):
        self.t, self.v, self.line, self.col = t, v, line, col
        self.eline = line if eline is None else eline
        self.ecol = col + len(v) if ecol is None else ecol

    def __repr__(self):
        return "Tok(%s,%r,%d:%d)" % (self.t, self.v, self.line, self.col)


_STR_RE = re.compile(r"""([rRbBuUfF]{0,2})(\"\"\"|'''|"|')""")
_NAME_RE = re.compile(r"[^\W\d][\w\u200c\u200d]*")
_NUM_RE = re.compile(
    r"0[xX][0-9a-fA-F_]+|0[oO][0-7_]+|0[bB][01_]+|"
    r"(?:\d[\d_]*(?:\.[\d_]*)?|\.\d[\d_]*)(?:[eE][+-]?\d[\d_]*)?[jJ]?")
_OPS3 = ("**=", "//=", ">>=", "<<=", "...")
_OPS2 = ("**", "//", ">>", "<<", "<=", ">=", "==", "!=", "->", ":=", "+=", "-=", "*=", "/=", "%=", "@=", "&=", "|=", "^=")
_OPS1 = "+-*/%@&|^~<>()[]{},:.;="
_CLOSE = {")": "(", "]": "[", "}": "{"}
_OPEN_FA = {"(": "پرانتز «(»", "[": "کروشه «[»", "{": "آکولاد «{»"}
_BAD_QUOTES = {"\u201c": "“", "\u201d": "”", "\u2018": "‘", "\u2019": "’", "«": "«", "»": "»"}


def tokenize(src, keywords, english_kw, strict=True):
    """keywords: نام فارسی ← کلیدواژه؛ english_kw: مجموعه‌ی کلیدواژه‌های انگلیسی (ممنوع در حالت فقط‌فارسی)."""
    src = src.replace("\r\n", "\n").replace("\r", "\n")
    if src.startswith("\ufeff"):
        src = src[1:]
    toks = []
    i, n, line, ls = 0, len(src), 1, 0
    indents = [0]
    brackets = []
    bol = True
    while i < n:
        if bol and not brackets:
            j, w = i, 0
            while j < n and src[j] in " \t":
                w = w + (8 - w % 8) if src[j] == "\t" else w + 1
                j += 1
            if j >= n:
                i = n
                break
            if src[j] == "\n":
                i, line = j + 1, line + 1
                ls = i
                continue
            if src[j] == "#":
                k = src.find("\n", j)
                if k < 0:
                    i = n
                    break
                i, line = k + 1, line + 1
                ls = i
                continue
            if src[j] == "\\" and src[j + 1:j + 2] == "\n":
                i, line = j + 2, line + 1
                ls = i
                continue
            if w > indents[-1]:
                indents.append(w)
                toks.append(Tok("INDENT", "", line, 0, line, j - i))
            else:
                while w < indents[-1]:
                    indents.pop()
                    toks.append(Tok("DEDENT", "", line, 0, line, 0))
                if w != indents[-1]:
                    raise DariSyntaxError("تورفتگی نادرست", "تورفتگی این خط با هیچ بلوک قبلی هم‌تراز نیست. خط‌های هر بلوک باید دقیقاً به یک اندازه بروند تو (معمولاً ۴ فاصله).", line, 0, max(j - i, 1))
            i = j
            bol = False
        c = src[i]
        col = i - ls
        if c == "\n":
            if brackets:
                i, line = i + 1, line + 1
                ls = i
                continue
            toks.append(Tok("NEWLINE", "", line, col, line, col + 1))
            i, line = i + 1, line + 1
            ls = i
            bol = True
            continue
        if c in " \t":
            i += 1
            continue
        if c == "#":
            k = src.find("\n", i)
            i = n if k < 0 else k
            continue
        if c == "\\" and src[i + 1:i + 2] == "\n":
            i, line = i + 2, line + 1
            ls = i
            continue
        m = _STR_RE.match(src, i)
        if m:
            q = m.group(2)
            j = m.end()
            sl, sc = line, col
            cl, cls_ = line, ls
            closed = False
            while j < n:
                ch = src[j]
                if ch == "\\":
                    if src[j + 1:j + 2] == "\n":
                        cl += 1
                        cls_ = j + 2
                    j += 2
                    continue
                if src.startswith(q, j):
                    closed = True
                    break
                if ch == "\n":
                    if len(q) == 1:
                        break
                    cl += 1
                    cls_ = j + 1
                j += 1
            if not closed:
                raise DariSyntaxError("نقل‌قول بسته نشده", "این رشته با %s شروع شده ولی تا آخر خط (یا فایل) بسته نشده. آخرش همان نقل‌قول را بگذارید." % q, sl, sc, max(len(src[i:j].split("\n")[0]), 1))
            j += len(q)
            toks.append(Tok("STR", src[i:j], sl, sc, cl, j - cls_))
            line, ls = cl, cls_
            i = j
            continue
        if c in _BAD_QUOTES:
            raise DariSyntaxError("نقل‌قول نامعتبر", "از نقل‌قول فارسی یا هوشمند «%s» استفاده شده. برای رشته فقط از \" یا ' ساده استفاده کنید." % c, line, col, 1)
        m = _NUM_RE.match(src, i) if (c.isdigit() or (c == "." and src[i + 1:i + 2].isdigit())) else None
        if m:
            txt = m.group(0)
            j = m.end()
            if j < n and (src[j].isalpha() or src[j] == "_"):
                raise DariSyntaxError("عدد و حرف چسبیده", "بعد از عدد «%s» بلافاصله حرف آمده. بین عدد و نام فاصله یا عملگر بگذارید." % txt, line, col, j - i + 1)
            toks.append(Tok("NUM", txt.translate(_DIG), line, col, line, col + len(txt)))
            i = j
            continue
        m = _NAME_RE.match(src, i)
        if m:
            nm = m.group(0)
            if nm in keywords:
                toks.append(Tok("KW", keywords[nm], line, col, line, col + len(nm)))
            else:
                if strict and nm in english_kw:
                    raise DariSyntaxError("دستور انگلیسی مجاز نیست", "«%s» انگلیسی است. در پایتون دری بنویسید: «%s»." % (nm, english_kw[nm]), line, col, len(nm))
                toks.append(Tok("NAME", nm, line, col, line, col + len(nm)))
            i = m.end()
            continue
        if c == "،":
            toks.append(Tok("OP", ",", line, col, line, col + 1))
            i += 1
            continue
        if c == "؛":
            toks.append(Tok("OP", ";", line, col, line, col + 1))
            i += 1
            continue
        op = None
        if src.startswith(_OPS3, i):
            op = src[i:i + 3]
        elif src.startswith(_OPS2, i):
            op = src[i:i + 2]
        elif c in _OPS1:
            op = c
        if op is None:
            raise DariSyntaxError("نویسه‌ی ناشناخته", "نویسه‌ی «%s» در برنامه معنی ندارد. اگر داخل رشته است، دورش نقل‌قول بگذارید." % c, line, col, 1)
        if op in "([{":
            brackets.append((op, line, col))
        elif op in ")]}":
            if not brackets:
                raise DariSyntaxError("بسته‌شدن اضافه", "«%s» بسته شده ولی بازی برایش نبوده. آن را بردارید یا قبلش بازکننده بگذارید." % op, line, col, 1)
            o, ol, oc = brackets.pop()
            if o != _CLOSE[op]:
                raise DariSyntaxError("پرانتز یا کروشه اشتباه بسته شده", "%s در خط %d باز شده ولی با «%s» بسته شده." % (_OPEN_FA[o], ol, op), line, col, 1)
        toks.append(Tok("OP", op, line, col, line, col + len(op)))
        i += len(op)
    if brackets:
        o, ol, oc = brackets[-1]
        raise DariSyntaxError("%s بسته نشده" % _OPEN_FA[o].split(" ")[0], "%s در این خط باز شده و تا آخر برنامه بسته نشده. جفتش را بگذارید." % _OPEN_FA[o], ol, oc, 1)
    if toks and toks[-1].t not in ("NEWLINE", "DEDENT", "INDENT"):
        toks.append(Tok("NEWLINE", "", line, i - ls, line, i - ls))
    while len(indents) > 1:
        indents.pop()
        toks.append(Tok("DEDENT", "", line, 0, line, 0))
    toks.append(Tok("EOF", "", line, 0, line, 0))
    return toks


# ===================== موتور: تحلیل‌گر دستور (Parser) =====================
# توکن‌های فارسی را مستقیماً به درخت دستور پایتون (AST) تبدیل می‌کند.

_LISTF = {"body", "orelse", "finalbody", "handlers", "decorator_list", "targets", "names", "bases", "keywords",
          "args", "posonlyargs", "kwonlyargs", "kw_defaults", "defaults", "elts", "keys", "values", "ops",
          "comparators", "generators", "ifs", "items", "type_params", "type_ignores"}
_BINOP = {"+": ast.Add, "-": ast.Sub, "*": ast.Mult, "/": ast.Div, "//": ast.FloorDiv, "%": ast.Mod, "@": ast.MatMult,
          "**": ast.Pow, "<<": ast.LShift, ">>": ast.RShift, "|": ast.BitOr, "^": ast.BitXor, "&": ast.BitAnd}
_CMP = {"<": ast.Lt, ">": ast.Gt, "==": ast.Eq, ">=": ast.GtE, "<=": ast.LtE, "!=": ast.NotEq}
_AUG = {"+=": ast.Add, "-=": ast.Sub, "*=": ast.Mult, "/=": ast.Div, "//=": ast.FloorDiv, "%=": ast.Mod, "@=": ast.MatMult,
        "**=": ast.Pow, "<<=": ast.LShift, ">>=": ast.RShift, "|=": ast.BitOr, "^=": ast.BitXor, "&=": ast.BitAnd}
_END_TOK = ("NEWLINE", "EOF", "DEDENT", "INDENT")
_BUILTIN_KW_CALLEES = {"print", "sorted", "open", "max", "min", "sum", "enumerate", "round", "int", "bytes", "zip"}


class Parser:
    def __init__(self, source, tables, filename="<farsi>", strict=True):
        self.src = source.replace("\r\n", "\n").replace("\r", "\n")
        self.lines = self.src.split("\n")
        self.T = tables  # KEYWORDS, BUILTINS, METHODS, MODULES, KWARGS, ENGLISH_KW, ENGLISH_BI
        self.strict = strict
        self.toks = tokenize(self.src, tables["KEYWORDS"], tables["ENGLISH_KW"], strict)
        self.p = 0
        self.fname = filename

    # ---------- ابزار ----------
    def bcol(self, line, col):
        try:
            return len(self.lines[line - 1][:col].encode("utf-8"))
        except IndexError:
            return col

    def N(self, cls, a, b=None, **kw):
        """ساخت گره با جای دقیق: a = نشانه‌ی شروع، b = آخرین نشانه‌ی مصرف‌شده."""
        for f in cls._fields:
            if f not in kw:
                kw[f] = [] if f in _LISTF else (ast.Load() if f == "ctx" else None)
        n = cls(**kw)
        if b is None:
            b = self.toks[self.p - 1] if self.p > 0 else a
        n.lineno, n.col_offset = a.line, self.bcol(a.line, a.col)
        n.end_lineno, n.end_col_offset = b.eline, self.bcol(b.eline, b.ecol)
        if (n.end_lineno, n.end_col_offset) < (n.lineno, n.col_offset):
            n.end_lineno, n.end_col_offset = n.lineno, n.col_offset
        return n

    @property
    def tok(self):
        return self.toks[self.p]

    def peek(self, k=1):
        return self.toks[min(self.p + k, len(self.toks) - 1)]

    def adv(self):
        t = self.toks[self.p]
        if t.t != "EOF":
            self.p += 1
        return t

    def is_op(self, v):
        t = self.toks[self.p]
        return t.t == "OP" and t.v == v

    def is_kw(self, v):
        t = self.toks[self.p]
        return t.t == "KW" and t.v == v

    def accept_op(self, v):
        return self.adv() if self.is_op(v) else None

    def accept_kw(self, v):
        return self.adv() if self.is_kw(v) else None

    def err(self, title, detail="", tok=None, length=None):
        t = tok or self.tok
        if length is None:
            length = 1 if t.t in _END_TOK else max(t.ecol - t.col, 1)
        raise DariSyntaxError(title, detail, t.line, t.col, length)

    def persian_of(self, t):
        if t.t == "KW":
            for fa, en in self.T["KEYWORDS"].items():
                if en == t.v:
                    return fa
        return t.v

    def desc(self, t):
        return {"NEWLINE": "پایان خط", "EOF": "پایان برنامه", "INDENT": "تورفتگی اضافه", "DEDENT": "پایان بلوک"}.get(t.t) or "«%s»" % self.persian_of(t)

    def prev(self):
        return self.toks[self.p - 1] if self.p else self.tok

    def expect_op(self, v, what=None):
        if self.is_op(v):
            return self.adv()
        t = self.tok
        if v == ":":
            self.err("«:» جا افتاده", "بعد از این دستور باید دو نقطه «:» بیاید. به‌جای آن %s آمده است." % self.desc(t),
                     self.prev() if t.t in _END_TOK else t)
        self.err("انتظار %s بود" % (what or "«%s»" % v), "به‌جای آن %s آمده است." % self.desc(t), t)

    def expect_kw(self, v):
        if self.is_kw(v):
            return self.adv()
        self.err("انتظار «%s» بود" % self.persian_of(Tok("KW", v, 0, 0)), "به‌جای آن %s آمده است." % self.desc(self.tok))

    def map_name(self, nm):
        return self.T["BUILTINS"].get(nm) or nm

    def check_english(self, t):
        if self.strict and t.v in self.T["ENGLISH_BI"]:
            raise DariSyntaxError("دستور انگلیسی مجاز نیست",
                                  "«%s» انگلیسی است. در پایتون دری بنویسید: «%s»." % (t.v, self.T["ENGLISH_BI"][t.v]),
                                  t.line, t.col, len(t.v))

    def name(self, what="نام"):
        t = self.tok
        if t.t != "NAME":
            self.err("انتظار %s بود" % what, "به‌جای آن %s آمده است." % self.desc(t))
        self.adv()
        return t

    def attr_name(self, nm):
        T = self.T
        if nm in T["METHODS"]:
            return T["METHODS"][nm]
        b = T["BUILTINS"].get(nm)
        if b and b.startswith("__"):
            return b
        return nm

    # ---------- برنامه ----------
    def parse_module(self):
        body = []
        while self.tok.t != "EOF":
            if self.tok.t == "NEWLINE":
                self.adv()
                continue
            if self.tok.t == "INDENT":
                self.err("تورفتگی بی‌جا", "این خط تورفتگی دارد ولی دستوری با «:» قبلش نیست. تورفتگی را بردارید.")
            if self.tok.t == "DEDENT":
                self.adv()
                continue
            body.extend(self.statement())
        return ast.Module(body=body, type_ignores=[])

    def block(self, what="این دستور"):
        if self.tok.t == "NEWLINE":
            self.adv()
            if self.tok.t != "INDENT":
                self.err("بعد از «:» تورفتگی لازم است",
                         "خط بعدی باید حدود ۴ فاصله بروید تو (داخل بلوک %s)." % what, self.tok, 1)
            self.adv()
            body = []
            while self.tok.t not in ("DEDENT", "EOF"):
                if self.tok.t == "NEWLINE":
                    self.adv()
                    continue
                if self.tok.t == "INDENT":
                    self.err("تورفتگی بی‌جا", "این خط بیشتر از خط قبلی رفته تو ولی دستوری با «:» قبلش نیست.")
                body.extend(self.statement())
            if self.tok.t == "DEDENT":
                self.adv()
            if not body:
                self.err("بلوک خالی", "داخل بلوک حداقل یک دستور بنویسید (اگر چیزی نمی‌خواهید «بگذر»).")
            return body
        return self.simple_line()

    def statement(self):
        t = self.tok
        if t.t == "KW":
            k = t.v
            f = {"if": self.if_stmt, "while": self.while_stmt, "for": self.for_stmt, "def": self.def_stmt,
                 "class": self.class_stmt, "try": self.try_stmt, "with": self.with_stmt}.get(k)
            if f:
                return [f()]
            if k == "async":
                return [self.async_stmt()]
            if k in ("elif", "else", "except", "finally"):
                under = {"elif": "«اگر»", "else": "«اگر»، «برای» یا «مادام»", "except": "«امتحان»", "finally": "«امتحان»"}[k]
                self.err("«%s» بی‌جا" % self.persian_of(t),
                         "«%s» باید درست زیر %s و هم‌تراز با آن بیاید." % (self.persian_of(t), under))
        if t.t == "OP" and t.v == "@":
            return [self.decorated()]
        return self.simple_line()

    def simple_line(self):
        out = [self.small_stmt()]
        while self.accept_op(";"):
            if self.tok.t == "NEWLINE":
                break
            out.append(self.small_stmt())
        if self.tok.t == "NEWLINE":
            self.adv()
        elif self.tok.t not in ("EOF", "DEDENT"):
            t = self.tok
            hint = " شاید بین دو چیز عملگر یا کامای «،» جا افتاده." if t.t in ("NAME", "NUM", "STR") else ""
            self.err("دستور درست تمام نشد", "بعد از کامل شدن دستور %s آمده است.%s" % (self.desc(t), hint))
        return out

    # ---------- دستورهای ساده ----------
    def at_end(self):
        t = self.tok
        return t.t in ("NEWLINE", "EOF", "DEDENT") or (t.t == "OP" and t.v == ";")

    def small_stmt(self):
        t = self.tok
        if t.t == "KW":
            k = t.v
            if k == "pass":
                self.adv()
                return self.N(ast.Pass, t)
            if k == "break":
                self.adv()
                return self.N(ast.Break, t)
            if k == "continue":
                self.adv()
                return self.N(ast.Continue, t)
            if k == "return":
                self.adv()
                v = None if self.at_end() else self.testlist_star()
                return self.N(ast.Return, t, value=v)
            if k == "raise":
                self.adv()
                ex = cause = None
                if not self.at_end():
                    ex = self.test()
                    if self.accept_kw("from"):
                        cause = self.test()
                return self.N(ast.Raise, t, exc=ex, cause=cause)
            if k in ("global", "nonlocal"):
                self.adv()
                names = [self.name().v]
                while self.accept_op(","):
                    names.append(self.name().v)
                return self.N(ast.Global if k == "global" else ast.Nonlocal, t, names=[self.map_name(x) for x in names])
            if k == "del":
                self.adv()
                tg = [self.target_expr(ast.Del())]
                while self.accept_op(","):
                    if self.at_end():
                        break
                    tg.append(self.target_expr(ast.Del()))
                return self.N(ast.Delete, t, targets=tg)
            if k == "assert":
                self.adv()
                a = self.test()
                msg = self.test() if self.accept_op(",") else None
                return self.N(ast.Assert, t, test=a, msg=msg)
            if k == "import":
                return self.import_stmt()
            if k == "from":
                return self.from_stmt()
        # دستور چاپ بدون پرانتز:  چاپ "سلام", x
        if t.t == "NAME" and self.T["BUILTINS"].get(t.v) == "print":
            n1 = self.peek()
            if n1.line == t.line and (n1.t in ("STR", "NUM", "NAME")
                                      or (n1.t == "KW" and n1.v in ("True", "False", "None", "not", "lambda", "await"))
                                      or (n1.t == "OP" and n1.v in ("[", "{", "-", "~"))):
                self.adv()
                args = [self.test_or_star()]
                while self.accept_op(","):
                    if self.at_end():
                        break
                    args.append(self.test_or_star())
                fn = self.N(ast.Name, t, t, id="print", ctx=ast.Load())
                call = self.N(ast.Call, t, func=fn, args=args, keywords=[])
                return self.N(ast.Expr, t, value=call)
        return self.expr_stmt()

    def test_or_star(self):
        if self.is_op("*"):
            s = self.adv()
            v = self.bitor()
            return self.N(ast.Starred, s, value=v, ctx=ast.Load())
        return self.test()

    def expr_stmt(self):
        t = self.tok
        first = self.testlist_star()
        if self.is_op(":") and isinstance(first, (ast.Name, ast.Attribute, ast.Subscript)):
            self.adv()
            ann = self.test()
            val = self.test() if self.accept_op("=") else None
            self.set_ctx(first, ast.Store(), t)
            return self.N(ast.AnnAssign, t, target=first, annotation=ann, value=val, simple=1 if isinstance(first, ast.Name) else 0)
        if self.tok.t == "OP" and self.tok.v in _AUG:
            op = self.adv().v
            self.set_ctx(first, ast.Store(), t, aug=True)
            val = self.yield_expr() if self.is_kw("yield") else self.testlist_star()
            return self.N(ast.AugAssign, t, target=first, op=_AUG[op](), value=val)
        if self.is_op("="):
            targets = [first]
            val = None
            while self.accept_op("="):
                val = self.yield_expr() if self.is_kw("yield") else self.testlist_star()
                if self.is_op("="):
                    targets.append(val)
            for tg in targets:
                self.set_ctx(tg, ast.Store(), t)
            return self.N(ast.Assign, t, targets=targets, value=val)
        return self.N(ast.Expr, t, value=first)

    def set_ctx(self, node, ctx, tok, aug=False):
        if isinstance(node, (ast.Name, ast.Attribute, ast.Subscript)):
            node.ctx = ctx
            if isinstance(node, ast.Name) and isinstance(ctx, ast.Store) and node.id in ("True", "False", "None"):
                self.err("نمی‌شود به این مقدار چیزی داد", "درست، نادرست و هیچ ثابت‌اند.", tok)
        elif isinstance(node, (ast.Tuple, ast.List)) and not aug:
            node.ctx = ctx
            for e in node.elts:
                self.set_ctx(e, ctx, tok)
        elif isinstance(node, ast.Starred) and not aug:
            node.ctx = ctx
            self.set_ctx(node.value, ctx, tok)
        else:
            what = {"Call": "نتیجه‌ی صدا زدن یک تابع", "Constant": "یک مقدار ثابت", "BinOp": "یک عبارت حسابی",
                    "Compare": "یک مقایسه"}.get(type(node).__name__, "این عبارت")
            raise DariSyntaxError("نمی‌شود به این چیزی داد",
                                  "سمت چپ علامت «=» باید نام متغیر (یا عضوی از فهرست) باشد، نه %s. اگر منظورتان مقایسه است «==» بنویسید." % what,
                                  tok.line, tok.col, 1)

    def target_expr(self, ctx):
        t = self.tok
        e = self.bitor_star()
        self.set_ctx(e, ctx, t)
        return e

    def bitor_star(self):
        if self.is_op("*"):
            s = self.adv()
            return self.N(ast.Starred, s, value=self.bitor(), ctx=ast.Load())
        return self.bitor()

    def target_list(self):
        t = self.tok
        first = self.bitor_star()
        if self.is_op(","):
            elts = [first]
            while self.accept_op(","):
                if self.is_kw("in") or self.is_op("="):
                    break
                elts.append(self.bitor_star())
            first = self.N(ast.Tuple, t, elts=elts)
        self.set_ctx(first, ast.Store(), t)
        return first

    # ---------- وارد کردن ----------
    def dotted(self):
        parts = [self.name("نام کتابخانه").v]
        while self.is_op(".") and self.peek().t == "NAME":
            self.adv()
            parts.append(self.adv().v)
        return parts

    def map_module(self, parts):
        M = self.T["MODULES"]
        full = ".".join(parts)
        if full in M:
            return M[full]
        return ".".join(M.get(p, p) for p in parts)

    def import_stmt(self):
        t = self.adv()
        names = []
        while True:
            st = self.tok
            parts = self.dotted()
            real = self.map_module(parts)
            asn = None
            if self.accept_kw("as"):
                asn = self.name().v
            elif real != ".".join(parts) and len(parts) == 1:
                asn = parts[0]  # وارد ریاضی  ←  ماژول math با نام ریاضی
            names.append(self.N(ast.alias, st, name=real, asname=asn))
            if not self.accept_op(","):
                break
        return self.N(ast.Import, t, names=names)

    def from_stmt(self):
        t = self.adv()
        level = 0
        while self.is_op(".") or self.is_op("..."):
            level += len(self.adv().v)
        mod = None
        if self.tok.t == "NAME":
            mod = self.map_module(self.dotted())
        elif level == 0:
            self.err("انتظار نام کتابخانه بود", "بعد از «از» نام کتابخانه بیاید؛ مثلاً  از ریاضی وارد ریشه_دوم")
        self.expect_kw("import")
        names = []
        if self.is_op("*"):
            s = self.adv()
            names.append(self.N(ast.alias, s, name="*", asname=None))
        else:
            paren = bool(self.accept_op("("))
            while True:
                st = self.name("نام")
                orig = st.v
                real = self.T["METHODS"].get(orig) or self.T["BUILTINS"].get(orig) or orig
                asn = None
                if self.accept_kw("as"):
                    asn = self.name().v
                elif real != orig:
                    asn = orig
                names.append(self.N(ast.alias, st, name=real, asname=asn))
                if not self.accept_op(","):
                    break
                if paren and self.is_op(")"):
                    break
            if paren:
                self.expect_op(")")
        return self.N(ast.ImportFrom, t, module=mod, names=names, level=level)

    # ---------- دستورهای مرکب ----------
    def if_stmt(self):
        t = self.adv()
        test = self.namedexpr()
        self.expect_op(":")
        body = self.block("«اگر»")
        orelse = []
        if self.is_kw("elif"):
            orelse = [self.if_stmt()]
        elif self.is_kw("else"):
            self.adv()
            self.expect_op(":")
            orelse = self.block("«وگرنه»")
        return self.N(ast.If, t, self.prev(), test=test, body=body, orelse=orelse)

    def while_stmt(self):
        t = self.adv()
        test = self.namedexpr()
        self.expect_op(":")
        body = self.block("«مادام»")
        orelse = []
        if self.is_kw("else"):
            self.adv()
            self.expect_op(":")
            orelse = self.block("«وگرنه»")
        return self.N(ast.While, t, self.prev(), test=test, body=body, orelse=orelse)

    def for_stmt(self, is_async=False, start=None):
        t = start or self.tok
        self.adv()
        target = self.target_list()
        if not self.is_kw("in"):
            self.err("«در» جا افتاده", "بعد از متغیر حلقه باید «در» بیاید؛ مثلاً  برای i در دامنه(5):")
        self.adv()
        it = self.testlist_star()
        self.expect_op(":")
        body = self.block("«برای»")
        orelse = []
        if self.is_kw("else"):
            self.adv()
            self.expect_op(":")
            orelse = self.block("«وگرنه»")
        return self.N(ast.AsyncFor if is_async else ast.For, t, self.prev(), target=target, iter=it, body=body,
                      orelse=orelse, type_comment=None)

    def params(self, closer, allow_ann):
        posonly, args, defaults, kwonly, kwdef = [], [], [], [], []
        vararg = kwarg = None
        seen_star = False
        seen = set()
        while not (self.is_op(closer) if closer else self.is_op(":")):
            if self.is_op("/"):
                self.adv()
                posonly, args = args, []
            elif self.is_op("**"):
                self.adv()
                nt = self.name("نام پارامتر")
                ann = self.test() if allow_ann and self.accept_op(":") else None
                kwarg = self.N(ast.arg, nt, nt, arg=self.map_name(nt.v), annotation=ann)
            elif self.is_op("*"):
                self.adv()
                seen_star = True
                if self.tok.t == "NAME":
                    nt = self.adv()
                    ann = self.test() if allow_ann and self.accept_op(":") else None
                    vararg = self.N(ast.arg, nt, nt, arg=self.map_name(nt.v), annotation=ann)
            else:
                nt = self.name("نام پارامتر")
                nm = self.map_name(nt.v)
                if nm in seen:
                    self.err("نام پارامتر تکراری", "پارامتر «%s» دو بار آمده." % nt.v, nt)
                seen.add(nm)
                ann = self.test() if allow_ann and self.accept_op(":") else None
                a = self.N(ast.arg, nt, nt, arg=nm, annotation=ann)
                dv = self.test() if self.accept_op("=") else None
                if seen_star:
                    kwonly.append(a)
                    kwdef.append(dv)
                else:
                    args.append(a)
                    if dv is not None:
                        defaults.append(dv)
                    elif defaults:
                        self.err("پارامتر بدون مقدار بعد از پارامتر مقدارداد",
                                 "پارامترهایی که مقدار پیش‌فرض دارند باید آخر فهرست بیایند.", nt)
            if not self.accept_op(","):
                break
        return ast.arguments(posonlyargs=posonly, args=args, vararg=vararg, kwonlyargs=kwonly, kw_defaults=kwdef,
                             kwarg=kwarg, defaults=defaults)

    def def_stmt(self, decos=None, is_async=False, start=None):
        t = start or self.tok
        self.adv()
        nt = self.name("نام تابع")
        self.expect_op("(")
        a = self.params(")", True)
        self.expect_op(")")
        ret = self.test() if self.accept_op("->") else None
        self.expect_op(":")
        body = self.block("تابع «%s»" % nt.v)
        cls = ast.AsyncFunctionDef if is_async else ast.FunctionDef
        return self.N(cls, t, self.prev(), name=self.map_name(nt.v), args=a, body=body, decorator_list=decos or [],
                      returns=ret, type_comment=None)

    def class_stmt(self, decos=None):
        t = self.adv()
        nt = self.name("نام کلاس")
        bases, kws = [], []
        if self.accept_op("("):
            bases, kws = self.call_args(None)
            self.expect_op(")")
        self.expect_op(":")
        body = self.block("کلاس «%s»" % nt.v)
        return self.N(ast.ClassDef, t, self.prev(), name=self.map_name(nt.v), bases=bases, keywords=kws, body=body,
                      decorator_list=decos or [])

    def decorated(self):
        decos = []
        while self.is_op("@"):
            self.adv()
            decos.append(self.namedexpr())
            if self.tok.t == "NEWLINE":
                self.adv()
        if self.is_kw("def"):
            return self.def_stmt(decos)
        if self.is_kw("class"):
            return self.class_stmt(decos)
        if self.is_kw("async") and self.peek().t == "KW" and self.peek().v == "def":
            s = self.adv()
            return self.def_stmt(decos, True, s)
        self.err("بعد از «@» باید «تعریف» یا «کلاس» بیاید")

    def async_stmt(self):
        s = self.adv()
        if self.is_kw("def"):
            return self.def_stmt(None, True, s)
        if self.is_kw("for"):
            return self.for_stmt(True, s)
        if self.is_kw("with"):
            return self.with_stmt(True, s)
        self.err("بعد از «ناهمگام» باید تعریف، برای یا با بیاید")

    def try_stmt(self):
        t = self.adv()
        self.expect_op(":")
        body = self.block("«امتحان»")
        handlers, orelse, final = [], [], []
        while self.is_kw("except"):
            ht = self.adv()
            typ = nm = None
            if not self.is_op(":"):
                typ = self.test()
                if self.accept_kw("as"):
                    nm = self.map_name(self.name().v)
                elif self.is_op(","):
                    self.err("چند نوع خطا را داخل پرانتز بنویسید", "مثلاً  خطا (خطای_مقدار, خطای_نوع):")
            self.expect_op(":")
            hb = self.block("«خطا»")
            handlers.append(self.N(ast.ExceptHandler, ht, self.prev(), type=typ, name=nm, body=hb))
        if self.is_kw("else"):
            if not handlers:
                self.err("«وگرنه» بدون «خطا»", "بعد از «امتحان» اول باید «خطا» بیاید.")
            self.adv()
            self.expect_op(":")
            orelse = self.block("«وگرنه»")
        if self.is_kw("finally"):
            self.adv()
            self.expect_op(":")
            final = self.block("«سرانجام»")
        if not handlers and not final:
            self.err("«امتحان» بدون «خطا» یا «سرانجام»",
                     "بعد از بلوک «امتحان» حتماً «خطا» یا «سرانجام» بیاید.", t)
        return self.N(ast.Try, t, self.prev(), body=body, handlers=handlers, orelse=orelse, finalbody=final)

    def with_stmt(self, is_async=False, start=None):
        t = start or self.tok
        self.adv()
        items = []
        while True:
            ctx = self.test()
            v = self.target_expr(ast.Store()) if self.accept_kw("as") else None
            items.append(ast.withitem(context_expr=ctx, optional_vars=v))
            if not self.accept_op(","):
                break
        self.expect_op(":")
        body = self.block("«با»")
        return self.N(ast.AsyncWith if is_async else ast.With, t, self.prev(), items=items, body=body, type_comment=None)

    # ---------- عبارت‌ها ----------
    def list_end(self):
        t = self.tok
        return (t.t in ("NEWLINE", "EOF", "DEDENT")
                or (t.t == "OP" and t.v in ("=", ")", "]", "}", ":", ";"))
                or (t.t == "KW" and t.v == "in"))

    def testlist_star(self):
        t = self.tok
        first = self.test_or_star()
        if self.is_op(","):
            elts = [first]
            while self.accept_op(","):
                if self.list_end():
                    break
                elts.append(self.test_or_star())
            return self.N(ast.Tuple, t, elts=elts)
        return first

    def yield_expr(self):
        t = self.adv()
        if self.accept_kw("from"):
            return self.N(ast.YieldFrom, t, value=self.test())
        v = None
        if not self.at_end() and not (self.tok.t == "OP" and self.tok.v in (")", "]", "}")):
            v = self.testlist_star()
        return self.N(ast.Yield, t, value=v)

    def namedexpr(self):
        t = self.tok
        if t.t == "NAME" and self.peek().t == "OP" and self.peek().v == ":=":
            self.adv()
            self.adv()
            v = self.test()
            tgt = self.N(ast.Name, t, t, id=self.map_name(t.v), ctx=ast.Store())
            return self.N(ast.NamedExpr, t, target=tgt, value=v)
        return self.test()

    def test(self):
        t = self.tok
        if t.t == "KW" and t.v == "lambda":
            self.adv()
            a = self.params(None, False)
            self.expect_op(":")
            body = self.test()
            return self.N(ast.Lambda, t, args=a, body=body)
        e = self.or_test()
        if self.is_kw("if"):
            self.adv()
            cond = self.or_test()
            if not self.is_kw("else"):
                self.err("«وگرنه» جا افتاده", "عبارت شرطی باید این شکل باشد:  مقدار۱ اگر شرط وگرنه مقدار۲")
            self.adv()
            other = self.test()
            return self.N(ast.IfExp, t, test=cond, body=e, orelse=other)
        return e

    def or_test(self):
        t = self.tok
        e = self.and_test()
        if self.is_kw("or"):
            vals = [e]
            while self.accept_kw("or"):
                vals.append(self.and_test())
            return self.N(ast.BoolOp, t, op=ast.Or(), values=vals)
        return e

    def and_test(self):
        t = self.tok
        e = self.not_test()
        if self.is_kw("and"):
            vals = [e]
            while self.accept_kw("and"):
                vals.append(self.not_test())
            return self.N(ast.BoolOp, t, op=ast.And(), values=vals)
        return e

    def not_test(self):
        t = self.tok
        if self.is_kw("not"):
            self.adv()
            return self.N(ast.UnaryOp, t, op=ast.Not(), operand=self.not_test())
        return self.comparison()

    def comparison(self):
        t = self.tok
        left = self.bitor()
        ops, comps = [], []
        while True:
            k = self.tok
            if k.t == "OP" and k.v in _CMP:
                self.adv()
                op = _CMP[k.v]()
            elif k.t == "KW" and k.v == "in":
                self.adv()
                op = ast.In()
            elif k.t == "KW" and k.v == "not" and self.peek().t == "KW" and self.peek().v == "in":
                self.adv()
                self.adv()
                op = ast.NotIn()
            elif k.t == "KW" and k.v == "is":
                self.adv()
                if self.is_kw("not"):
                    self.adv()
                    op = ast.IsNot()
                else:
                    op = ast.Is()
            else:
                break
            ops.append(op)
            comps.append(self.bitor())
        if ops:
            return self.N(ast.Compare, t, left=left, ops=ops, comparators=comps)
        return left

    def _binlevel(self, sub, opset):
        t = self.tok
        left = sub()
        while self.tok.t == "OP" and self.tok.v in opset:
            op = self.adv().v
            right = sub()
            left = self.N(ast.BinOp, t, left=left, op=_BINOP[op](), right=right)
        return left

    def bitor(self):
        return self._binlevel(self.bitxor, ("|",))

    def bitxor(self):
        return self._binlevel(self.bitand, ("^",))

    def bitand(self):
        return self._binlevel(self.shift, ("&",))

    def shift(self):
        return self._binlevel(self.arith, ("<<", ">>"))

    def arith(self):
        return self._binlevel(self.term, ("+", "-"))

    def term(self):
        return self._binlevel(self.factor, ("*", "/", "//", "%", "@"))

    def factor(self):
        t = self.tok
        if t.t == "OP" and t.v in ("+", "-", "~"):
            self.adv()
            operand = self.factor()
            op = {"+": ast.UAdd, "-": ast.USub, "~": ast.Invert}[t.v]()
            return self.N(ast.UnaryOp, t, op=op, operand=operand)
        return self.power()

    def power(self):
        t = self.tok
        base = self.await_expr()
        if self.is_op("**"):
            self.adv()
            exp = self.factor()
            return self.N(ast.BinOp, t, left=base, op=ast.Pow(), right=exp)
        return base

    def await_expr(self):
        t = self.tok
        if t.t == "KW" and t.v == "await":
            self.adv()
            return self.N(ast.Await, t, value=self.primary())
        return self.primary()

    def primary(self):
        t = self.tok
        e = self.atom()
        while True:
            k = self.tok
            if k.t == "OP" and k.v == ".":
                self.adv()
                nt = self.tok
                if nt.t != "NAME":
                    self.err("بعد از «.» باید نام بیاید", "به‌جای آن %s آمده است." % self.desc(nt))
                self.adv()
                e = self.N(ast.Attribute, t, attr=self.attr_name(nt.v), value=e, ctx=ast.Load())
            elif k.t == "OP" and k.v == "(":
                self.adv()
                args, kws = self.call_args(e)
                if not self.is_op(")"):
                    self.err("«)» جا افتاده",
                             "پرانتز صدا زدن تابع در خط %d بسته نشده؛ به‌جای «)» %s آمده است. شاید کامای «،» جا افتاده." % (k.line, self.desc(self.tok)))
                self.adv()
                e = self.N(ast.Call, t, func=e, args=args, keywords=kws)
            elif k.t == "OP" and k.v == "[":
                self.adv()
                sl = self.subscript()
                self.expect_op("]")
                e = self.N(ast.Subscript, t, value=e, slice=sl, ctx=ast.Load())
            else:
                break
        return e

    def subscript(self):
        t = self.tok
        first = self.slice_item()
        if self.is_op(","):
            elts = [first]
            while self.accept_op(","):
                if self.is_op("]"):
                    break
                elts.append(self.slice_item())
            return self.N(ast.Tuple, t, elts=elts)
        return first

    def slice_item(self):
        t = self.tok
        lower = upper = step = None
        if not self.is_op(":"):
            e = self.test_or_star() if self.is_op("*") else self.namedexpr()
            if not self.is_op(":"):
                return e
            lower = e
        self.expect_op(":")
        if not (self.is_op(":") or self.is_op("]") or self.is_op(",")):
            upper = self.test()
        if self.accept_op(":"):
            if not (self.is_op("]") or self.is_op(",")):
                step = self.test()
        return self.N(ast.Slice, t, lower=lower, upper=upper, step=step)

    def kw_ok(self, callee):
        if callee is None:
            return False
        if isinstance(callee, ast.Name):
            return callee.id in _BUILTIN_KW_CALLEES
        return isinstance(callee, ast.Attribute)

    def call_args(self, callee):
        args, kws = [], []
        mapkw = self.kw_ok(callee)
        while not self.is_op(")"):
            t = self.tok
            if self.is_op("*"):
                self.adv()
                args.append(self.N(ast.Starred, t, value=self.test(), ctx=ast.Load()))
            elif self.is_op("**"):
                self.adv()
                kws.append(self.N(ast.keyword, t, arg=None, value=self.test()))
            elif t.t == "NAME" and self.peek().t == "OP" and self.peek().v == "=":
                self.adv()
                self.adv()
                nm = self.T["KWARGS"].get(t.v, t.v) if mapkw else t.v
                kws.append(self.N(ast.keyword, t, arg=nm, value=self.test()))
            else:
                e = self.namedexpr()
                if self.is_kw("for") or (self.is_kw("async") and self.peek().v == "for"):
                    e = self.N(ast.GeneratorExp, t, elt=e, generators=self.comp_for())
                args.append(e)
            if not self.accept_op(","):
                break
        return args, kws

    def comp_for(self):
        gens = []
        while self.is_kw("for") or (self.is_kw("async") and self.peek().t == "KW" and self.peek().v == "for"):
            is_async = 0
            if self.is_kw("async"):
                self.adv()
                is_async = 1
            self.adv()
            target = self.target_list()
            if not self.is_kw("in"):
                self.err("«در» جا افتاده", "در فهرست‌سازی بعد از متغیر باید «در» بیاید.")
            self.adv()
            it = self.or_test()
            ifs = []
            while self.is_kw("if"):
                self.adv()
                ifs.append(self.or_test())
            gens.append(ast.comprehension(target=target, iter=it, ifs=ifs, is_async=is_async))
        return gens

    def atom(self):
        t = self.tok
        k = t.t
        if k == "NAME":
            self.adv()
            self.check_english(t)
            return self.N(ast.Name, t, t, id=self.map_name(t.v), ctx=ast.Load())
        if k == "NUM":
            self.adv()
            try:
                v = ast.literal_eval(t.v)
            except (ValueError, SyntaxError):
                raise DariSyntaxError("عدد نادرست", "«%s» عدد معتبری نیست." % t.v, t.line, t.col, len(t.v))
            return self.N(ast.Constant, t, t, value=v, kind=None)
        if k == "STR":
            return self.strings()
        if k == "KW":
            if t.v in ("True", "False", "None"):
                self.adv()
                return self.N(ast.Constant, t, t, value={"True": True, "False": False, "None": None}[t.v], kind=None)
            if t.v == "lambda":
                return self.test()
            if t.v == "yield":
                return self.yield_expr()
            self.err("این‌جا «%s» جایش نیست" % self.persian_of(t), "در این جای عبارت یک مقدار یا نام لازم بود.")
        if k == "OP":
            if t.v == "(":
                return self.paren()
            if t.v == "[":
                return self.list_atom()
            if t.v == "{":
                return self.dict_atom()
            if t.v == "...":
                self.adv()
                return self.N(ast.Constant, t, t, value=Ellipsis, kind=None)
        if k in ("NEWLINE", "EOF", "DEDENT"):
            self.err("عبارت ناقص است", "این خط ناتمام مانده؛ بعد از عملگر یا کاما باید مقداری بیاید.", self.prev())
        self.err("این‌جا %s جایش نیست" % self.desc(t), "در این جای عبارت یک مقدار یا نام لازم بود. پرانتز و کاماها را بررسی کنید.")

    def is_comp(self):
        return self.is_kw("for") or (self.is_kw("async") and self.peek().t == "KW" and self.peek().v == "for")

    def paren(self):
        t = self.adv()
        if self.is_op(")"):
            self.adv()
            return self.N(ast.Tuple, t, elts=[])
        if self.is_kw("yield"):
            e = self.yield_expr()
            self.expect_op(")")
            return e
        first = self.test_or_star() if self.is_op("*") else self.namedexpr()
        if self.is_comp():
            gens = self.comp_for()
            self.expect_op(")")
            return self.N(ast.GeneratorExp, t, elt=first, generators=gens)
        if self.is_op(","):
            elts = [first]
            while self.accept_op(","):
                if self.is_op(")"):
                    break
                elts.append(self.test_or_star() if self.is_op("*") else self.namedexpr())
            self.expect_op(")")
            return self.N(ast.Tuple, t, elts=elts)
        if not self.is_op(")"):
            self.err("«)» جا افتاده",
                     "پرانتز باز شده در خط %d بسته نشده؛ به‌جای «)» %s آمده است. شاید کامای «،» جا افتاده." % (t.line, self.desc(self.tok)))
        self.adv()
        return first

    def list_atom(self):
        t = self.adv()
        if self.is_op("]"):
            self.adv()
            return self.N(ast.List, t, elts=[])
        first = self.test_or_star() if self.is_op("*") else self.namedexpr()
        if self.is_comp():
            gens = self.comp_for()
            self.expect_op("]")
            return self.N(ast.ListComp, t, elt=first, generators=gens)
        elts = [first]
        while self.accept_op(","):
            if self.is_op("]"):
                break
            elts.append(self.test_or_star() if self.is_op("*") else self.namedexpr())
        if not self.is_op("]"):
            self.err("«]» جا افتاده",
                     "کروشه‌ی باز شده در خط %d بسته نشده؛ به‌جای «]» %s آمده است. شاید بین دو مقدار کامای «،» جا افتاده." % (t.line, self.desc(self.tok)))
        self.adv()
        return self.N(ast.List, t, elts=elts)

    def dict_atom(self):
        t = self.adv()
        if self.is_op("}"):
            self.adv()
            return self.N(ast.Dict, t, keys=[], values=[])
        keys, vals = [], []
        is_set = False
        first = True
        while not self.is_op("}"):
            if self.is_op("**"):
                self.adv()
                keys.append(None)
                vals.append(self.bitor())
            else:
                k = self.test_or_star() if self.is_op("*") else self.namedexpr()
                if first and not self.is_op(":"):
                    is_set = True
                if is_set:
                    if first and self.is_comp():
                        gens = self.comp_for()
                        self.expect_op("}")
                        return self.N(ast.SetComp, t, elt=k, generators=gens)
                    keys.append(k)
                else:
                    self.expect_op(":")
                    v = self.test()
                    if first and self.is_comp():
                        gens = self.comp_for()
                        self.expect_op("}")
                        return self.N(ast.DictComp, t, key=k, value=v, generators=gens)
                    keys.append(k)
                    vals.append(v)
            first = False
            if not self.accept_op(","):
                break
        if not self.is_op("}"):
            self.err("«}» جا افتاده",
                     "آکولاد باز شده در خط %d بسته نشده؛ به‌جای «}» %s آمده است. شاید بین دو مقدار کامای «،» جا افتاده." % (t.line, self.desc(self.tok)))
        self.adv()
        if is_set:
            return self.N(ast.Set, t, elts=keys)
        return self.N(ast.Dict, t, keys=keys, values=vals)

    # ---------- رشته‌ها ----------
    def strings(self):
        t0 = self.tok
        parts = []
        any_f = False
        is_bytes = None
        while self.tok.t == "STR":
            s = self.adv()
            m = re.match(r"([rRbBuUfF]*)(\"\"\"|'''|\"|')", s.v)
            prefix, q = m.group(1).lower(), m.group(2)
            body = s.v[m.end():len(s.v) - len(q)]
            if ("b" in prefix) != bool(is_bytes) and is_bytes is not None:
                self.err("بایت و متن را نمی‌شود به هم چسباند", "", s)
            is_bytes = "b" in prefix
            if is_bytes:
                try:
                    parts.append(("c", ast.literal_eval(s.v)))
                except Exception:
                    raise DariSyntaxError("رشته‌ی بایت نادرست", "", s.line, s.col, len(s.v))
            elif "f" in prefix:
                any_f = True
                parts.extend(self.fstring_parts(body, "r" in prefix, s))
            else:
                try:
                    parts.append(("c", ast.literal_eval(prefix.replace("f", "") + q + body + q)))
                except SyntaxError:
                    raise DariSyntaxError("رشته‌ی نادرست", "نوشتار این رشته مشکل دارد (مثلاً «\\» در جای نامناسب).", s.line, s.col, len(s.v))
        last = self.prev()
        if not any_f:
            v = b"".join(p[1] for p in parts) if is_bytes else "".join(p[1] for p in parts)
            return self.N(ast.Constant, t0, last, value=v, kind=None)
        vals, buf = [], ""
        for p in parts:
            if p[0] == "c":
                buf += p[1]
            else:
                if buf:
                    vals.append(self.N(ast.Constant, t0, last, value=buf, kind=None))
                    buf = ""
                vals.append(p[1])
        if buf:
            vals.append(self.N(ast.Constant, t0, last, value=buf, kind=None))
        return self.N(ast.JoinedStr, t0, last, values=vals)

    def fstring_parts(self, body, raw, tok):
        out, lit = [], []
        i, n = 0, len(body)

        def flush():
            if lit:
                txt = "".join(lit)
                if not raw and "\\" in txt:
                    try:
                        txt = ast.literal_eval('"""' + txt.replace('"""', '\\"\\"\\"') + '"""')
                    except Exception:
                        pass
                out.append(("c", txt))
                lit.clear()

        while i < n:
            c = body[i]
            if c == "{":
                if body[i + 1:i + 2] == "{":
                    lit.append("{")
                    i += 2
                    continue
                flush()
                depth, j, instr = 0, i + 1, None
                while j < n:
                    ch = body[j]
                    if instr:
                        if ch == instr:
                            instr = None
                    elif ch in "\"'":
                        instr = ch
                    elif ch in "([{":
                        depth += 1
                    elif ch in ")]":
                        depth -= 1
                    elif ch == "}":
                        if depth == 0:
                            break
                        depth -= 1
                    elif ch in "!:" and depth == 0 and not (ch == "!" and body[j + 1:j + 2] == "="):
                        break
                    j += 1
                expr_raw = body[i + 1:j]
                expr_src = expr_raw.strip()
                dbg = False
                if expr_src.endswith("=") and not expr_src.endswith(("==", "!=", "<=", ">=")):
                    dbg = True
                    lit.append(expr_raw)
                    flush()
                    expr_src = expr_src[:-1].strip()
                conv, spec = -1, None
                if j < n and body[j] == "!":
                    conv = ord(body[j + 1]) if j + 1 < n else -1
                    j += 2
                if j < n and body[j] == ":":
                    k, d = j + 1, 0
                    while k < n:
                        if body[k] == "{":
                            d += 1
                        elif body[k] == "}":
                            if d == 0:
                                break
                            d -= 1
                        k += 1
                    sp = self.fstring_parts(body[j + 1:k], raw, tok)
                    j = k
                    sv = [self.N(ast.Constant, tok, tok, value=p[1], kind=None) if p[0] == "c" else p[1] for p in sp]
                    spec = self.N(ast.JoinedStr, tok, tok, values=sv)
                if dbg and conv == -1 and spec is None:
                    conv = 114
                if j >= n or body[j] != "}":
                    raise DariSyntaxError("آکولاد در رشته‌ی f بسته نشده", "داخل رشته‌ی f، «{» باز شده ولی «}» ندارد. برای نوشتن خود آکولاد دو تا بنویسید: {{", tok.line, tok.col, 1)
                if not expr_src:
                    raise DariSyntaxError("عبارت خالی در رشته‌ی f", "بین { و } باید نام یا عبارتی باشد.", tok.line, tok.col, 1)
                sub = Parser("(" + expr_src + ")", self.T, self.fname, self.strict)
                try:
                    e = sub.paren()
                    if sub.tok.t not in ("NEWLINE", "EOF"):
                        sub.err("عبارت درست تمام نشد")
                except DariSyntaxError as ex:
                    raise DariSyntaxError(ex.title, (ex.detail + " " if ex.detail else "") + "(داخل رشته‌ی f)", tok.line, tok.col, 1)
                _relocate(e, tok)
                out.append(("e", self.N(ast.FormattedValue, tok, tok, value=e, conversion=conv, format_spec=spec)))
                i = j + 1
                continue
            if c == "}":
                if body[i + 1:i + 2] == "}":
                    lit.append("}")
                    i += 2
                    continue
                raise DariSyntaxError("«}» تنها در رشته‌ی f", "برای نوشتن خود «}» دو تا بنویسید: }}", tok.line, tok.col, 1)
            lit.append(c)
            i += 1
        flush()
        return out


def _relocate(node, tok):
    for n in ast.walk(node):
        if hasattr(n, "lineno"):
            n.lineno = n.end_lineno = tok.line
            n.col_offset = 0
            n.end_col_offset = 1


STRICT = True  # حالت «فقط فارسی»: دستور انگلیسی خطا می‌دهد


def parse_source(source, filename="<farsi>", strict=None):
    """کد فارسی ← درخت دستور پایتون. خطای نوشتاری را با DariSyntaxError برمی‌گرداند."""
    tree = Parser(source, TABLES, filename, STRICT if strict is None else strict).parse_module()
    ast.fix_missing_locations(tree)
    return tree


def compile_source(source, filename="<farsi>", strict=None, mode="exec"):
    tree = parse_source(source, filename, strict)
    if mode == "single":
        tree = ast.Interactive(body=tree.body)
    return compile(tree, filename, mode)


_SOURCES = {}


def register_source(filename, source):
    """تا پایتون هنگام نمایش خطا بتواند خط‌های برنامه را نشان بدهد."""
    _SOURCES[filename] = source.split("\n")
    linecache.cache[filename] = (len(source), None, source.splitlines(True), filename)


class _DariLoader(importlib.machinery.SourceFileLoader):
    """ماژول‌های فارسی هم‌پوشه‌ی برنامه (وارد ماژول_من) با همین موتور خوانده می‌شوند."""

    def source_to_code(self, data, path, *, _optimize=-1):
        text = importlib.util.decode_source(data)
        if re.search(r"[\u0600-\u06FF]", text):
            register_source(path, text)
            try:
                return compile(parse_source(text, path), path, "exec", dont_inherit=True, optimize=_optimize)
            except DariSyntaxError as e:
                raise SyntaxError("%s (خط %d): %s" % (e.title, e.line, e.detail), (path, e.line, e.col + 1, ""))
        return super().source_to_code(data, path, _optimize=_optimize)


class _DariFinder(importlib.abc.MetaPathFinder):
    def __init__(self, folder):
        self.folder = folder

    def find_spec(self, name, path=None, target=None):
        if "." in name:
            return None
        spec = importlib.machinery.PathFinder.find_spec(name, [self.folder])
        if spec is None or not isinstance(spec.loader, importlib.machinery.SourceFileLoader):
            return None
        spec.loader = _DariLoader(spec.loader.name, spec.loader.path)
        return spec


"""اجرای برنامه و گزارش خطای فارسی."""

import os
import sys


def _line_of(filename, n):
    ls = _SOURCES.get(filename)
    if ls and 1 <= n <= len(ls):
        return ls[n - 1]
    return ""


def report_syntax(e, source, filename):
    ls = source.replace("\r\n", "\n").split("\n")
    print("", file=sys.stderr)
    print("❗ خطای نوشتاری: %s  (خط %d، ستون %d)" % (e.title, e.line, e.col + 1), file=sys.stderr)
    if 1 <= e.line <= len(ls):
        text = ls[e.line - 1]
        print("   " + text, file=sys.stderr)
        print("   " + " " * len(text[:e.col]) + "^" * max(min(e.length, max(len(text) - e.col, 1)), 1), file=sys.stderr)
        part = text[e.col:e.col + e.length].strip()
        if part:
            print("   جای اشتباه: «%s»" % part, file=sys.stderr)
    if e.detail:
        print("   %s" % e.detail, file=sys.stderr)


def report_error(exc, tb, filename):
    """گزارش خطای اجرا: فقط خط‌های خود برنامه، با توضیح فارسی."""
    sys.stdout.flush()
    frames = []
    t = tb
    while t is not None:
        if t.tb_frame.f_code.co_filename == filename:
            frames.append((t.tb_lineno, t.tb_frame.f_code.co_name))
        t = t.tb_next
    title, detail = explain(exc)
    last = frames[-1][0] if frames else getattr(exc, "lineno", None)
    print("", file=sys.stderr)
    print("❗ %s%s" % (title, " (خط %d)" % last if last else ""), file=sys.stderr)
    if frames:
        text = _line_of(filename, frames[-1][0]).strip()
        if text:
            print("   %d:  %s" % (frames[-1][0], text), file=sys.stderr)
        if len(frames) > 1:
            path = " ← ".join("%s (خط %d)" % ("برنامه" if fn == "<module>" else "تابع " + fn, ln) for ln, fn in reversed(frames))
            print("   مسیر: %s" % path, file=sys.stderr)
    if detail:
        print("   %s" % detail, file=sys.stderr)
    msg = "%s: %s" % (type(exc).__name__, exc)
    print("   پیام فنی: %s" % msg.strip(), file=sys.stderr)


def run_source(source, filename="<farsi>", argv=None, strict=None):
    """کد فارسی را می‌خواند و اجرا می‌کند. کد خروج را برمی‌گرداند."""
    full = os.path.abspath(filename) if os.path.exists(filename) else filename
    script_dir = os.path.dirname(full) if os.path.exists(full) else os.getcwd()
    old_argv, old_path, old_meta = sys.argv[:], sys.path[:], sys.meta_path[:]
    sys.argv = [filename] + list(argv or [])
    sys.path.insert(0, script_dir)
    sys.meta_path.insert(0, _DariFinder(script_dir))
    register_source(full, source)
    glob = {"__name__": "__main__", "__file__": full, "__builtins__": __builtins__}
    try:
        try:
            code_obj = compile_source(source, full, strict)
        except DariSyntaxError as e:
            report_syntax(e, source, full)
            return 1
        exec(code_obj, glob)
        return 0
    except SystemExit as e:
        return e.code if isinstance(e.code, int) else (0 if e.code is None else 1)
    except KeyboardInterrupt:
        print("\n(متوقف شد)", file=sys.stderr)
        return 130
    except BaseException as exc:  # noqa: BLE001
        report_error(exc, exc.__traceback__, full)
        return 1
    finally:
        sys.argv, sys.path[:], sys.meta_path[:] = old_argv, old_path, old_meta


def run_file(path, argv=None, strict=None):
    try:
        with open(path, "r", encoding="utf-8-sig") as f:
            source = f.read()
    except OSError as e:
        print("فایل باز نشد: %s" % e, file=sys.stderr)
        return 2
    return run_source(source, path, argv, strict)


"""دستورهای خط فرمان:  farsi اجرا | کتابخانه‌ها | نصب | حذف | محیط | پوسته | پروژه"""

import code
import importlib.util
import os
import subprocess
import sys


ENV_DIR = ".farsi_env"
THIS_FILE = os.path.abspath(__file__)

ALIASES = {
    "run": "run", "اجرا": "run",
    "libs": "libs", "کتابخانه‌ها": "libs", "کتابخانه_ها": "libs",
    "install": "install", "نصب": "install",
    "uninstall": "uninstall", "حذف": "uninstall",
    "env": "env", "محیط": "env",
    "shell": "shell", "پوسته": "shell",
    "new": "new", "پروژه": "new",
    "version": "version", "نسخه": "version",
    "help": "help", "راهنما": "help",
}

HELP = """پایتون دری %s: زبان فارسی مستقل روی موتور واقعی پایتون

  farsi فایل.py                اجرای یک برنامه (همان  farsi اجرا فایل.py)
        --آزاد                 دستور انگلیسی هم مجاز باشد (پیش‌فرض: فقط فارسی)
  farsi کتابخانه‌ها            فهرست کتابخانه‌ها با نام فارسی و انگلیسی و وضعیت نصب
        --نصب‌شده | --نصب‌نشده | --جستجو متن
  farsi نصب نام                نصب کتابخانه با pip (نام فارسی یا انگلیسی)، مثلاً  farsi نصب کیوی
  farsi حذف نام                حذف کتابخانه
  farsi محیط ساختن             ساخت محیط جدا (venv) برای همین پروژه در پوشه‌ی .farsi_env
  farsi پروژه نام              ساخت پوشه‌ی پروژه با main.py و محیط جدا
  farsi پوسته                  محیط تعاملی (هر خط را می‌نویسید و نتیجه را می‌بینید)
  farsi نسخه

اگر پوشه‌ی .farsi_env هست، نصب و اجرا داخل همان محیط انجام می‌شود.
""" % __version__


def find_env(start=None):
    d = os.path.abspath(start or os.getcwd())
    while True:
        cand = os.path.join(d, ENV_DIR)
        if os.path.isdir(cand):
            return cand
        parent = os.path.dirname(d)
        if parent == d:
            return None
        d = parent


def env_python(env):
    for sub in ("bin/python", "Scripts/python.exe"):
        p = os.path.join(env, *sub.split("/"))
        if os.path.exists(p):
            return p
    return None


def project_python(start=None):
    env = find_env(start)
    return (env_python(env) if env else None) or sys.executable


def resolve(name):
    """نام فارسی یا انگلیسی را به (نام import، نام pip یا None برای استاندارد) تبدیل می‌کند."""
    en = MODULES.get(name, name)
    std = {e for e, _ in STDLIB}
    if en in std:
        return en, None
    return en, PIP_NAMES.get(en, en)


def is_installed(en, python=None):
    if python and python != sys.executable:
        r = subprocess.run([python, "-c", "import importlib.util,sys;sys.exit(0 if importlib.util.find_spec(%r) else 1)" % en], capture_output=True)
        return r.returncode == 0
    try:
        return importlib.util.find_spec(en) is not None
    except (ImportError, ValueError):
        return False


def cmd_run(args):
    if not args:
        print("نام فایل را بنویسید:  farsi اجرا برنامه.py")
        return 2
    path, rest = args[0], args[1:]
    env = find_env(os.path.dirname(os.path.abspath(path)))
    py = env_python(env) if env else None
    if py and os.path.abspath(py) != os.path.abspath(sys.executable):
        e = dict(os.environ)
        e["PYTHONIOENCODING"] = "utf-8"
        return subprocess.call([py, THIS_FILE, "run", path] + rest, env=e)
    return run_file(path, rest)


def cmd_libs(args):
    only, query = None, None
    i = 0
    while i < len(args):
        a = args[i]
        if a in ("--نصب‌شده", "--installed"):
            only = True
        elif a in ("--نصب‌نشده", "--missing"):
            only = False
        elif a in ("--جستجو", "--search") and i + 1 < len(args):
            query = args[i + 1].lower()
            i += 1
        i += 1
    py = project_python()
    rows = [(e, f, "استاندارد") for e, f in STDLIB] + [(e, f, "pip") for e, f, _p in THIRD_PARTY]
    known = {r[0] for r in rows}
    for name in sorted(getattr(sys, "stdlib_module_names", ())):
        if not name.startswith("_") and name not in known:
            rows.append((name, "—", "استاندارد"))
    out, yes = [], 0
    for en, fa, kind in sorted(rows):
        ok = is_installed(en, py)
        yes += ok
        if only is not None and ok != only:
            continue
        if query and query not in en.lower() and query not in fa:
            continue
        out.append((en, fa, kind, ok))
    w = max([len(r[0]) for r in out] + [10])
    print("%-*s  %-24s %-10s %s" % (w, "English", "فارسی", "نوع", "وضعیت"))
    for en, fa, kind, ok in out:
        print("%-*s  %-24s %-10s %s" % (w, en, fa, kind, "✔ نصب‌شده" if ok else "✘ نصب‌نشده"))
    print("\nنصب‌شده: %d   نصب‌نشده: %d   (پایتون: %s)" % (yes, len(rows) - yes, py))
    return 0


def cmd_install(args, remove=False):
    if not args:
        print("نام کتابخانه را بنویسید:  farsi نصب کیوی")
        return 2
    py = project_python()
    code_ = 0
    for name in args:
        en, pip = resolve(name)
        if pip is None:
            if remove:
                print("«%s» کتابخانه‌ی استاندارد است و حذف نمی‌شود." % name)
            elif is_installed(en, py):
                print("«%s» (%s) کتابخانه‌ی استاندارد است و همین حالا همراه پایتون هست." % (name, en))
            else:
                print("«%s» استاندارد است ولی روی این پایتون نیست. روی لینوکس: sudo apt install python3-tk  (برای tkinter)  |  در ترموکس: pkg install python-tkinter" % en)
                code_ = 1
            continue
        cmd = [py, "-m", "pip", "uninstall", "-y", pip] if remove else [py, "-m", "pip", "install", pip]
        print("→ " + " ".join(cmd))
        r = subprocess.call(cmd)
        code_ = code_ or r
    return code_


def cmd_env(args):
    sub = args[0] if args else "ساختن"
    if sub in ("ساختن", "create", "ساخت"):
        import venv
        target = os.path.join(os.getcwd(), ENV_DIR)
        print("ساخت محیط جدا در", target)
        venv.EnvBuilder(with_pip=True, clear=False).create(target)
        print("آماده شد. از این به بعد «farsi نصب ...» داخل همین محیط نصب می‌کند.")
        return 0
    if sub in ("مسیر", "path"):
        env = find_env()
        print(env or "محیطی ساخته نشده")
        return 0
    print("farsi محیط ساختن | farsi محیط مسیر")
    return 2


def cmd_new(args):
    if not args:
        print("نام پروژه را بنویسید:  farsi پروژه فروشگاه")
        return 2
    name = args[0]
    os.makedirs(name, exist_ok=True)
    main_py = os.path.join(name, "main.py")
    if not os.path.exists(main_py):
        with open(main_py, "w", encoding="utf-8") as f:
            f.write('# برنامه‌ی من\nنام = ورودی("اسم شما؟ ")\nچاپ("سلام", نام)\n')
    print("پروژه ساخته شد:", name)
    print("برای محیط جدا:  cd %s  &&  farsi محیط ساختن" % name)
    print("برای اجرا:      farsi %s" % os.path.join(name, "main.py"))
    return 0


def _needs_more(src):
    try:
        tokenize(src, KEYWORDS, ENGLISH_KW, False)
    except DariSyntaxError as e:
        return "بسته نشده" in e.title and "نقل" not in e.title
    return False


def cmd_shell(_args):
    print("پایتون دری %s (پایتون %s)" % (__version__, sys.version.split()[0]))
    print("مثال:  چاپ(\"سلام\")     برای خروج بنویسید: خروج")
    ns = {"__name__": "__main__", "__builtins__": __builtins__}
    buf = []
    n = 0
    while True:
        try:
            line = input("... " if buf else ">>> ")
        except EOFError:
            print()
            break
        except KeyboardInterrupt:
            print()
            buf = []
            continue
        if not buf and line.strip() in ("خروج", "خروج()", "exit", "exit()"):
            break
        buf.append(line)
        src = "\n".join(buf)
        if line.strip() == "" and len(buf) == 1:
            buf = []
            continue
        if line.strip() != "" and (_needs_more(src) or line.rstrip().endswith(":") or (len(buf) > 1)):
            continue
        n += 1
        fname = "<پوسته %d>" % n
        register_source(fname, src)
        try:
            co = compile_source(src, fname, None, "single")
            exec(co, ns)
        except DariSyntaxError as e:
            report_syntax(e, src, fname)
        except SystemExit:
            break
        except KeyboardInterrupt:
            print("\n(متوقف شد)")
        except BaseException as exc:  # noqa: BLE001
            report_error(exc, exc.__traceback__, fname)
        buf = []
    return 0


SAMPLE = """# اولین برنامه‌ی من
نام = ورودی("نام شما؟ ")
چاپ("سلام", نام)
برای i در دامنه(1, 4):
    چاپ("شماره", i)
"""


def _is_self(p):
    try:
        with open(p, encoding="utf-8") as f:
            t = f.read(400)
            return "پایتون دری ۳" in t or "پایتون دری — یک فایل" in t
    except Exception:
        return False


def _menu():
    """بدون آرگومان (مثلاً دکمه‌ی زرد پایدروید): فهرست برنامه‌ها را نشان می‌دهد."""
    me = os.path.abspath(__file__)
    dirs = []
    for d in (os.getcwd(), os.path.dirname(me), os.path.expanduser("~"),
              "/sdcard/Download", "/storage/emulated/0/Download",
              "/sdcard/Documents", "/sdcard", "/storage/emulated/0"):
        if d and os.path.isdir(d) and d not in dirs:
            dirs.append(d)
    found, seen = [], set()
    for d in dirs:
        try:
            names = sorted(os.listdir(d))
        except OSError:
            continue
        for n in names:
            p = os.path.join(d, n)
            try:
                key = os.path.realpath(p)
            except OSError:
                key = p
            if (n.endswith(".py") and os.path.isfile(p) and key not in seen
                    and os.path.abspath(p) != me and not _is_self(p)):
                seen.add(key)
                found.append(p)
    found = found[:30]
    print("پایتون دری %s" % __version__)
    while True:
        print("\nبرنامه‌ی فارسی را انتخاب کنید:\n")
        for i, p in enumerate(found, 1):
            print("  %d) %s" % (i, p))
        if not found:
            print("  (هنوز برنامه‌ی فارسی‌ای پیدا نشد)")
        print("\n  ۱۰۰) ساختن و اجرای یک برنامه‌ی نمونه")
        print("  0) پوسته (محیط تعاملی)")
        print("  یا مسیر کامل فایل را بنویسید")
        try:
            a = input("\nشماره یا مسیر: ").strip()
        except EOFError:
            return 0
        a = a.translate(str.maketrans("۰۱۲۳۴۵۶۷۸۹", "0123456789"))
        if a == "0":
            return cmd_shell([])
        if a == "100":
            p = os.path.join(os.path.dirname(me), "سلام.py")
            try:
                with open(p, "w", encoding="utf-8") as f:
                    f.write(SAMPLE)
            except OSError:
                p = os.path.join(os.getcwd(), "سلام.py")
                with open(p, "w", encoding="utf-8") as f:
                    f.write(SAMPLE)
            print("ساخته شد:", p)
            return cmd_run([p])
        if a.isdigit() and 1 <= int(a) <= len(found):
            return cmd_run([found[int(a) - 1]])
        if a and os.path.isfile(a):
            return cmd_run([a])
        print("\n❗ «%s» شماره‌ی درست یا فایل موجود نیست. دوباره امتحان کنید." % a)


def main(argv=None):
    global STRICT
    argv = list(sys.argv[1:] if argv is None else argv)
    if "--آزاد" in argv:
        STRICT = False
        argv = [a for a in argv if a != "--آزاد"]
    if not argv:
        return _menu()
    if argv[0] in ("-h", "--help"):
        print(HELP)
        return 0
    cmd = ALIASES.get(argv[0])
    if cmd is None:
        return cmd_run(argv)  # farsi فایل.py
    rest = argv[1:]
    if cmd == "run":
        return cmd_run(rest)
    if cmd == "libs":
        return cmd_libs(rest)
    if cmd == "install":
        return cmd_install(rest)
    if cmd == "uninstall":
        return cmd_install(rest, remove=True)
    if cmd == "env":
        return cmd_env(rest)
    if cmd == "new":
        return cmd_new(rest)
    if cmd == "shell":
        return cmd_shell(rest)
    if cmd == "version":
        print("پایتون فارسی", __version__)
        return 0
    print(HELP)
    return 0


if __name__ == "__main__":
    sys.exit(main())
