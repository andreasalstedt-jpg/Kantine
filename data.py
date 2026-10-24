"""Laget av Claude"""
varer =[
    {"navn": "Monster",       "pris": "40kr", "bilde": "https://bilder.ngdata.no/5060751216070/kmh/large.jpg"},
    {"navn": "iskaffe",        "pris": "35kr", "bilde": "https://bilder.ngdata.no/7038010003820/meny/large.jpg"},
    {"navn": "Te",            "pris": "30kr", "bilde": "https://www.twinings.no/download.ashx?galleryrequest=image,/content/images/products/,F12002-earl-grey-25p.jpg,600,400,,,true,true,false,false"},
    {"navn": "Cola",          "pris": "28kr", "bilde": "https://engrosnett.no/image/kalde-drikker/mineralvann/5108675-5108675.jpg?v=639263683640030000"},
    {"navn": "Farris",        "pris": "27kr", "bilde": "https://farris.no/wp-content/uploads/2026/06/farris-frus.jpg"},
    {"navn": "Appelsinjuice", "pris": "32kr", "bilde": "https://www.lunsj.no/25668-large_default/raa-appelsinjuice-kaldpresset-1l-synnove.jpg"},
    {"navn": "Eplejuice",     "pris": "32kr", "bilde": "https://images.matinfo.no/images/large/202307071056027770_809.jpg"},
    {"navn": "Vann",          "pris": "20kr", "bilde": "https://bilder.ngdata.no/7044610874876/meny/large.jpg"},
    {"navn": "Melk",          "pris": "25kr", "bilde": "https://www.skolelyst.no/_next/image?url=%2F_next%2Fstatic%2Fmedia%2F198.33-o4gugh_me8.png&w=3840&q=75"},
    {"navn": "Smoothie",     "pris": "25kr", "bilde": "https://bilder.ngdata.no/7040518520334/meny/large.jpg"},


    {"navn": "Kanelboller",  "pris": "40kr", "bilde": "https://bilder.ngdata.no/7041614003332/kmh/large.jpg"},
    {"navn": "Skolebrød",   "pris": "40kr", "bilde": "https://images.matinfo.no/images/large/201712181319370299_07072047920071.jpg"},
    {"navn": "Wienerbrød",  "pris": "42kr", "bilde": "https://www.mesterbakeren.no/wp-content/uploads/importedmedia/2025/03/7029161128067_main.jpg"},
    {"navn": "Croissant",   "pris": "36kr", "bilde": "https://www.kinsarvik.no/cdn/shop/files/3115550171_BA100006.jpg?v=1768390174&width=480"},
    {"navn": "Rundstykke",  "pris": "18kr", "bilde": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRGyb_kNRD9Fv3zLKNpRWh_XtX1axB8YMYMxZNU_iIS092Diz4FICUBoXnT&s=10"},
    {"navn": "Baguette",    "pris": "30kr", "bilde": "https://www.mesterbakeren.no/wp-content/uploads/importedmedia/2025/03/7029161131272_main.jpg"},
    {"navn": "Vaffel",      "pris": "35kr", "bilde": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQQh6y3r8CIwWWOnLs9SjMzsfTXNqkEG-DMDPhZj8d3ICPR_QhKzaLfDKw&s=10"},
    {"navn": "Muffins",     "pris": "34kr", "bilde": "https://images2.europris.no/produkter/vw800/216153/216153_main.webp"},
    {"navn": "Brownie",     "pris": "38kr", "bilde": "https://foodora.dhmedia.io/image/product-information-management/6797a3bb288832006fd18f59.png?height=480"},
    {"navn": "Cookie",     "pris": "25kr", "bilde": "https://marutham.no/wp-content/uploads/2024/05/9vFU3I_1716454826_12463_0_0_pck-600x600.jpg"},


    {"navn": "Potetgull",      "pris": "32kr", "bilde": "https://bilder.ngdata.no/7050122304343/meny/large.jpg"},
    {"navn": "Popcorn",        "pris": "28kr", "bilde": "https://images2.europris.no/produkter/vw800/192587/192587_main.webp"},
    {"navn": "Nøtteblanding",  "pris": "40kr", "bilde": "https://www.sesum.no/_next/image?url=https%3A%2F%2Fglpowwptzbokwtkbsnko.supabase.co%2Fstorage%2Fv1%2Fobject%2Fpublic%2Fproduct-images%2F9249.jpg&w=1920&q=75"},
    {"navn": "Peanøtter",      "pris": "25kr", "bilde": "https://bilder.ngdata.no/7039317008679/meny/large.jpg"},
    {"navn": "Sjokoladebar",   "pris": "22kr", "bilde": "https://bilder.ngdata.no/7040110569908/meny/large.jpg"},
]

meny = [
    {"dag": "Mandag", "navn": "Nuggets", "pris": "60kr", "bilde": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR_Rs3ty8N214Au8crMVeF20N_Oed2_UGcx78-dJ9ENUiw6xlJHP1JLqJA&s=10",
     "beskrivelse": "Sprø kyllingnuggets servert med pommes frites og dipp."},
    {"dag": "Tirsdag", "navn": "Ertestuing", "pris": "100kr", "bilde": "https://images.matprat.no/xqrjx7e6s8-VerticalRelated__w=392/ertestuing_2.jpg",
     "beskrivelse": "Kremet ertestuing, en varm og mettende klassiker."},
    {"dag": "Onsdag", "navn": "Smalahove", "pris": "10kr", "bilde": "https://thumb.wikimedia.org/wikipedia/commons/thumb/5/5f/Smalahove_klar.JPG/250px-Smalahove_klar.JPG?utm_source=no.wikipedia.org&utm_campaign=parser&utm_content=thumbnail",
     "beskrivelse": "Tradisjonell vestlandsrett med kokt poteter og kålrabistappe."},
    {"dag": "Torsdag", "navn": "Butter chicken", "pris": "70kr", "bilde": "https://cdn.apartmenttherapy.info/image/upload/f_jpg,q_auto:eco,c_fill,g_auto,w_1500,ar_4:3/k%2FPhoto%2FRecipes%2F2024-12-butter-chicken%2Fbutter-chicken-323",
     "beskrivelse": "Mør kylling i mild, kremet tomatsaus med ris og nanbrød."},
    {"dag": "Fredag", "navn": "Pizza", "pris": "50kr", "bilde": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS1ncOxFNm6f_pTvK6unyxTQmfHu0syYMEYmFHVgAZiW827B4X19Fy00hA&s=10",
     "beskrivelse": "Fredagspizza med ost og skinke, rett fra ovnen."},
]
     
     
     
     

