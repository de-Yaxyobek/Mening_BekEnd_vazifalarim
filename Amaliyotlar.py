# # Ro'yhatdan o'tish
# print("\t<<<<< KIRIDIT PANELI >>>>>")
# print("\tYahyobek kiridit bank tizimiga xush kelibsiz.")

# ism = str(input("\t<<< Ismingiz nima? >>> ").title())

# print(f"\tAssalomu alaykum {ism}.")
# print("Bizda shu tariflar bor: ")
# print(f"\nBizda umumiy mablag' 15_000_000 so'm pul bor.Sizga shu mablag'dan ko'p pul bera olmaymiz.")
# print("foiz: 35%")
# print("Agar 1-2 kunga kechiktirilsa: 10% qo'shiladi!")

# kiridit = int(input("Qancha kridit olmoqchisiz?  "))
# if kiridit <= 100_000:
#     print("Bunday oz pul bera olmaymiz! ")
# elif kiridit >= 100_000:
#     print("Davom ettiring")
#     if 15_00_000> kiridit >= 0:
#         print("Rahmat kiriditingiz hozir beriladi yana davom ettiring.")
#     else:
#         print("Bunaqa katta mablag' bizda yo'q.")
#     oylar = int(input("Kiriditni necha oyga olmoqchisiz?   "))
#     print(f"Kiriditni oyiga {kiridit / oylar} qilib bo'lib to'laysiz.")


#     mablag = 15_000_000
#     foiz = 1.5 * kiridit
#     kechiktirilsa = kiridit * 1.5 + 250_000
#     kech_berilsa = str(input("Kridit vaqtidan o'tib, kechikib kettimi? (ha \ yo'q)     "))
#     if kech_berilsa == "ha":
#         print(f"Sizning kiriditngiz 1-2 kunga kechiksa: {kechiktirilsa} qilib qaytarasiz!")
#         print("Rahmat yana kelib turing")
#     else:
#         print("Kirdit olganingiz uchun rahmat yana kelib turing.")

#         print("\n\t <<<<< TO'LOV QILISH PANELI: >>>>>")
#     tolash = str(input("Kriditga to'lov qilmoqchimisiz? (ha \ yo'q)  ").lower())
#     if tolash == 'ha':
#         a = int(input(" <<< Qancha bul to'lamoqchisiz? >>>  "))
#         if a == kiridit:
#             print("Rahmat")
#         else:
#             print("Yana to'layvering. Rahmat. ")
#     else:
#         print("\nQachon kiriditni to'laysiz? ")
#         print("<<<<<< HURMAT BILAN YAHYOBEK KIRIDIT BANK TIZIMI >>>>>> ")