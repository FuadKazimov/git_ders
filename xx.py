


qiymetler = {
    "Riyaziyyat": 85,
    "Fizika": 78,
    "Kimya": 90,
    "İngilis dili": 88,
    "Tarix": 76
}
cem = 0
say = 0

for qiymet in qiymetler.values():
    cem += qiymet
    say += 1
orta_qiymet = cem / say
print(f"Telebenin orta qiymeti: {round(orta_qiymet)}")



