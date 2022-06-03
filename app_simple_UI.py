from ReservationScripts.Scripts import *
# -----------------------------------------------------------------------------#
# Select Restuarant
# -----------------------------------------------------------------------------#
print("輸入定位餐廳代號：")
print("\t1: 旭集")
print("\t2: 饗饗")
print("\t3: 饗食天堂")
print("\t4: 茶六")
print("\t5: 涮乃葉")
print("\t6: Mo-Mo Paradise")
print("\t7: Will's Teppanyaki")
selection = str(input("(1-7):"))
# -----------------------------------------------------------------------------#
# Initiate
# -----------------------------------------------------------------------------#
if selection == "1":
    crawler = Sunrise()
elif selection == "2":
    crawler = InParadise()
elif selection == "3":
    crawler = Paradise()
elif selection == "4":
    crawler = Tea6()    
elif selection == "5":
    crawler = SyaBuYo()
elif selection == "6":
    crawler = MoMoParadise()
elif selection == "7":
    crawler = WillsTeppanyaki()
# -----------------------------------------------------------------------------#
# dump REQUIREMENT_INFO.txt for editing
# -----------------------------------------------------------------------------#
crawler.dump_required_info()
print("'REQUIREMENT_INFO.txt' has been created, please modify the INFO then save the file.")
print(" press Enter when done...")
input()
# -----------------------------------------------------------------------------#
# read INFO.txt
# -----------------------------------------------------------------------------#
crawler.read_info()
# -----------------------------------------------------------------------------#
# start when
# -----------------------------------------------------------------------------#
print('When should it begin to crawl? in the format of YYYY-mm-dd_HH:mm (ex. 2022-06-24_20:20)')
print('(Press Enter to start immediately.)')
start_when = str(input(":"))
if start_when == '':
    crawler.run()
else:
    crawler.run(start_when=start_when)
