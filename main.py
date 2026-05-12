import flet as ft
import requests
from datetime import datetime

def main(page: ft.Page):
    page.title = "مواقيت الصلاة"
    page.rtl = True
    page.theme_mode = ft.ThemeMode.LIGHT
    page.bgcolor = "#E0F2F1"

    city, country = "Cairo", "Egypt" # غير مدينتك هنا

    try:
        url = f"http://api.aladhan.com/v1/timingsByCity?city={city}&country={country}"
        data = requests.get(url).json()
        timings = data['data']['timings']
        hijri = data['data']['date']['hijri']['date']
    except:
        timings, hijri = {}, "شغل النت"

    prayers_ar = {'Fajr':'الفجر', 'Dhuhr':'الظهر', 'Asr':'العصر', 'Maghrib':'المغرب', 'Isha':'العشاء'}

    page.add(
        ft.Column([
            ft.Text("🕌 مواقيت الصلاة", size=28, weight=ft.FontWeight.BOLD),
            ft.Text(f"{city} - {hijri}", size=14),
            ft.Divider(),
            *[ft.Card(content=ft.Container(
                content=ft.Row([
                    ft.Text(prayers_ar[p], size=20, weight=ft.FontWeight.W_600),
                    ft.Text(t, size=20, color="#00796B"),
                ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
                padding=15
            )) for p, t in timings.items() if p in prayers_ar]
        ], spacing=10)
    )

ft.app(target=main)
