import requests
from typing import Dict, Any
from bs4 import BeautifulSoup

class Scrapweb():
	"""Object scrapweb
	Get mobile application info
	"""

	app_version:str=""
	app_date_sortie:str=""
	app_nbre_download:str=""
	app_name:str=""
	app_description:str=""
	app_info:Dict[str,str]={}

	def __init__(self,link:str):
		self.link=link

	def check(self,elt: Any)->str:
		if len(elt)>0:
			return elt.get_text()
		return ""

	def getApplicationInfo(self)->Dict[str,str]:
		# Get page content
		page = requests.get(self.link,timeout=10)
		# Parsing page
		soup = BeautifulSoup(page.content, 'html.parser')
		# -------------- Traitement -------------------------------------------------------
		app_name_elt = soup.select_one("div div div div div div div h1")
		app_version_date = soup.select("div.header-desktop__MoreInfoContainer-xc5gow-11  div div div div div",class_="mini-versions__LatestVersion-sc-19sko2j-5 drfVqx")
		app_nbre_download_elt = soup.select_one("section div div div span")
		app_description_elt = soup.select_one("section.section__SectionContainer-lxnmhg-0 div p",{"itemprop":"description"})


		if len(app_version_date)>0 and len(app_version_date)<3:
			self.setApp_version(app_version_date[0].get_text())
			self.setApp_date_sortie(app_version_date[1].get_text())
			pass

		self.setApp_name(self.check(app_name_elt))
		self.setApp_nbre_download(self.check(app_nbre_download_elt))
		self.setApp_description(self.check(app_description_elt))
		self.app_info = {"app_name":self.app_name,"app_version":self.app_version,"app_nbre_downloads":self.app_nbre_download,"date_sortie":self.app_date_sortie,"app_description":self.app_description}
		return self.app_info


	"""
		Getters and setters for all object attributs
	"""
	def getApp_version(self)->str:
		return self.app_version

	def setApp_version(self,app_version:str):
		self.app_version = app_version

	def getApp_name(self)->str:
		return self.app_name

	def setApp_name(self,app_name:str):
		self.app_name = app_name

	def getApp_date_sortie(self)->str:
		return self.app_date_sortie

	def setApp_date_sortie(self,app_date_sortie:str):
		self.app_date_sortie = app_date_sortie.replace('(','').replace(')','')

	def getApp_nbre_download(self)->str:
		return self.app_nbre_download

	def setApp_nbre_download(self,app_nbre_download:str):
		self.app_nbre_download = app_nbre_download

	def getApp_description(self)->str:
		return self.app_description

	def setApp_description(self,app_description:str):
		self.app_description = app_description
