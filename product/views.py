from django.shortcuts import render
from django.http import HttpResponse
from .models import Post, Author
from django.db.models import Q
    


def product_view(request):
    posts = Post.objects.all()[:4]
    return render(request, 'post.html', {"posts": posts})

    




















































































# def product_view(request):
#     html = """
#         <h1>First page</h1>
#         <p>Iye bo'lar ekanku axir!</p>
#         <a href="second/">second page >> </a><br/>
#         <a href="pages/kompyuterlar"> Compyuters page >> </a><br/>
#         <a href="pages/telefonlar"> telephones page >> </a><br/>
#     """
#     return HttpResponse(html)

# def second_view(request):
#     html = """
#         <h1>Second page</h1>
#         <h2>Ikkinchi bo'lim</h2>
#         <a href="../"><< main page </a>
#     """
#     return HttpResponse(html)

# def pages(request, page):
#     if page == 'kompyuterlar':
#         html = f"""
#             <h1>{page}</h1>
#             <p>
#                 Kompyuter (inglizcha: computer – ,,kodlar bilan ishlamayman'') – oldindan berilgan dastur boʻyicha ishlaydigan avtomatik qurilma. Elektron hisoblash mashinasi (EHM) bilan bir xildagi atama. Biroq, kompyuter hisoblash ishlarini bajarishdan tashqari uning funksiyasi ancha keng. EHMlarning rivojlanishida kompyuterning bir necha avlodlarini koʻrsatish mumkin. Bu avlodlar element turlari, konstruktiv-texnologik xususiyatlari, mantiqiy tuzilishi, dastur taʼminoti, texnik tafsilotlari, texnikadan foydalanishning qulaylik darajasi bilan bir-biridan farq qiladi. Kompyuterning dastlabki avlodida (Ural-1, Minsk-2, BSEM-2) asosiy element elektron lampa boʻlgani uchun u juda katta joyni egallagan edi. Soʻngra bu lampa oʻrnida tranzistorlar ishlatilgan kompyuter (Razdan-2, M-220, Minsk-22 va boshqalar), integral mikrosxemalar ishlatilgan kompyuter (IBM-360, 1BM-370, (AQSh), YESEVM (Rossiya) va boshqalar, integratsiya darajasi katta boʻlgan integral sxemalar oʻrnatilgan shaxsiy kompyuterlar paydo boʻldi.            
#             </p>
#             <a href="../"><< main page </a>
#         """
#     elif page == 'telefonlar':
#         html = f"""
#             <h1>{page}</h1>
#             <p>
#                 Mobil telefon, uyali telefon yoki qoʻl telefoni uyali aloqa tizimi boʻylab ovoz va boshqa axborot uzatuvchi hamda qabul qiluvchi elektron qurilmadir. Zamonaviy mobil telefonlar bundan tashqari internet mijozlari, oʻyinlar, infraqizil va bluetooth portlar, video/fotokamera, MP3 player, radio va hokazo taʼminot bilan qurollangan.
#                 Uyali telefon, qoʻl telefon — simsiz telefon turi. Har bir abonent (uyali telefon apparati) muayyan bir uyali telefon kompaniyasining telefon tarmogʻidagi baza st-yaga bogʻlanadi. har qaysi baza st-yada "uyalar" boʻladi (nomi shundan). Har bir uyaga bir necha kanal biriktirib qoʻyiladi; tarmoqning katta va kichikligiga qarab uyalar soni har xil boʻladi. Mobil telefon apparati qaysi kompaniya tarmogʻining baza st-yasiga ulanganligiga qarab uning aloqa bogʻlash doirasi chegarasi har xil boʻladi.
#             </p>
#             <a href="../"><< main page </a>
#         """
#     else:
#         html = f"""
#             <h1>page {page}</h1>
#             <h2>bo'lim-{page}</h2>
#             <a href="../"><< main page</a>
#         """
#     return HttpResponse(html)