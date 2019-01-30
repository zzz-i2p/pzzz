# -*- coding: utf-8 -*-
##

import os
import sys

from core.core import *
from time import sleep as timeout


def main():
	banner()
	print "   [01] Сбор Информации"
	print "   [02] Сканер Уязвимостей"
	print "   [03] Стресс-Тестирование"
	print "   [04] Пароль Атаки"
	print "   [05] Веб-Хакинга"
	print "   [06] Инструменты Эксплуатации"
	print "   [07] Sniffing & Spoofing"
	print "   [08] Другие\n"
	print "   [10] Выход\n"
	zzz = raw_input("$zzz ")

	if zzz == "1" or zzz == "01":
		print "\n    [01] Nmap"
		print "    [02] Red Hawk"
		print "    [03] D-Tect"
		print "    [04] sqlmap"
		print "    [05] Infoga"
		print "    [06] ReconDog"
		print "    [07] AndroZenmap"
		print "    [08] sqlmate"
		print "    [09] AstraNmap"
		print "    [10] WTF"
		print "    [11] Easymap"
		print "    [12] BlackBox"
		print "    [13] XD3v"
		print "    [14] Crips"
		print "    [15] SIR"
		print "    [16] EvilURL"
		print "    [17] Striker"
		print "    [18] Xshell"
		print "    [19] OWScan"
		print "    [20] OSIF"
		print "    [21] Devploit"
		print "    [22] Namechk"
		print "    [23] AUXILE"
		print "    [24] inther"
		print "    [25] GINF\n"
		print "    [00] Главное меню\n"
		infogathering = raw_input("$zzz ")
if infogathering == "01" or infogathering == "1":
			nmap()
		elif infogathering == "02" or infogathering == "2":
			red_hawk()
		elif infogathering == "03" or infogathering == "3":
			dtect()
		elif infogathering == "04" or infogathering == "4":
			sqlmap()
		elif infogathering == "05" or infogathering == "5":
			infoga()
		elif infogathering == "06" or infogathering == "6":
			reconDog()
		elif infogathering == "07" or infogathering == "7":
			androZenmap()
		elif infogathering == "08" or infogathering == "8":
			sqlmate()
		elif infogathering == "09" or infogathering == "9":
			astraNmap()
		elif infogathering == "10":
			wtf()
		elif infogathering == "11":
			easyMap()
		elif infogathering == "12":
			blackbox()
		elif infogathering == "13":
			xd3v()
		elif infogathering == "14":
			crips()
		elif infogathering == "15":
			sir()
		elif infogathering == "16":
			evilURL()
		elif infogathering == "17":
			striker()
		elif infogathering == "18":
			xshell()
		elif infogathering == "19":
			owscan()
		elif infogathering == "20":
			osif()
		elif infogathering == "21":
			devploit()
		elif infogathering == "22":
			namechk()
		elif infogathering == "23":
			auxile()
		elif infogathering == "24":
			inther()
		elif infogathering == "25":
			ginf()
		elif infogathering == "00" or infogathering == "0":
			restart_program()
		else:
			print "\nОшибка: неверный ввод"
			timeout(2)
			restart_program()

elif zzz == "10":
		sys.exit()
	
	else:
		print "\nERROR: Wrong Input"
		timeout(2)
		restart_program()

if __name__ == "__main__":
	main()

