# 🏪 POS Telegram Bot - Firebird 2.5 x64

Oshxona POS sistemasi uchun owner hisobotlarini ko'rsatadigan Telegram bot.

## 🚀 O'rnatish

### 1. Repository klonlash
```bash
git clone https://github.com/rebelclub/pos_bot.git
cd pos_bot
```

### 2. Python virtual environment yaratish
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# yoki
venv\Scripts\activate  # Windows
```

### 3. Dependencies o'rnatish
```bash
pip install -r requirements.txt
```

### 4. Firebird driver o'rnatish

**Windows:**
- [Firebird Client](https://firebirdsql.org/en/firebird-2-5/) yuklab oling va o'rnating

**Linux:**
```bash
sudo apt-get install firebird-dev
```

### 5. .env fayl sozlash

`.env.example` faylini `.env` ga nusxalang va o'z ma'lumotlaringizni kiriting:

```bash
cp .env.example .env
nano .env
```

**Kerakli ma'lumotlar:**
- `BOT_TOKEN` - [@BotFather](https://t.me/BotFather) dan oling
- `OWNER_ID` - O'z Telegram ID [@userinfobot](https://t.me/userinfobot)
- `DB_*` - Firebird baza ma'lumotlari

### 6. Database strukturasini moslash

⚠️ **MUHIM:** `database/firebird_db.py` faylidagi SQL query'larni o'z bazangiz strukturasiga moslashtirishingiz kerak!

Bazangizda quyidagi jadvallar bo'lishi kerak (yoki o'xshash):
- `SALES` (buyurtmalar)
- `SALES_ITEMS` (buyurtma detallari)
- `PRODUCTS` (mahsulotlar)
- `EMPLOYEES` (xodimlar)
- `INVENTORY` (inventar)

### 7. Botni ishga tushirish

```bash
python main.py
```

## 📊 Funksiyalar

- ✅ Kunlik/Haftalik/Oylik savdo hisobotlari
- ✅ Real-time joriy smena ma'lumotlari
- ✅ TOP mahsulotlar (10, 20, 50)
- ✅ Xodimlar statistikasi
- ✅ Inventar va kam qolgan tovarlar
- ✅ Naqd/Karta to'lovlar statistikasi
- ✅ Owner-only access (xavfsizlik)

## 🔒 Xavfsizlik

Faqat `.env` faylidagi `OWNER_ID` ga ega foydalanuvchi botdan foydalana oladi.

## 📝 Muammolar

Agar muammo yuzaga kelsa:
1. Firebird baza ulanishini tekshiring
2. `.env` fayldagi ma'lumotlarni tekshiring
3. SQL query'lar baza strukturasiga moslashtirilganligini tekshiring
4. Log fayllarni ko'rib chiqing

## 📞 Yordam

Savollar bo'lsa, issue oching yoki contact qiling.

## 📄 License

MIT License