#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os

def update():
	os.system("apt-get update")

def upgrade():
	os.system("apt-get upgrade")

def install():
	os.system("apt-get install")
	
def autoremove():
	os.system("apt-get autoremove")

repositories_management_ico = """
############################################################
#    PYTHON - Repositories Management - GH0ST S0FTWARE     #
############################################################ 
#                       CONTACT                            #
############################################################
#               DEVELOPER : İSMAİL TAŞDELEN                #
#          Mail Address : pentestdatabase@gmail.com        #
#   LINKEDIN : https://www.linkedin.com/in/ismailtasdelen  #
#              Whatsapp : + 90 534 295 94 31               #
############################################################
"""

print repositories_management_ico

islemler_ico = """
(1) Repositories Update
(2) Repositories Upgrade
(3) Repositories Install
(4) Repositories Autoremove
"""

print islemler_ico

islem = input("Yapılcak işlem numarasını giriniz : ")

if islem == 1:
	update()
	
elif islem == 2:
	upgrade()
	
elif islem == 3:
	install()

elif islem == 4:
	autoremove()
