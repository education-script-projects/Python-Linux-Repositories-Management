#!/usr/bin/eny python
# -*- coding:utf-8 -*-

import os

def update():
	os.system("apt-get update")

def upgrade():
	os.system("apt-get upgrade")

def install():
	os.system("apt-get install")

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
"""

print islemler_ico

islem = input("Yapılcak işlem numarasını giriniz : ")

if islem == 1:
	update()
if islem == 2:
	upgrade()
if islem == 3:
	install()
