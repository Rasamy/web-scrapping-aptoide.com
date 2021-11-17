from bs4 import BeautifulSoup

def check(elt):
	if len(elt)>0:
		return elt.get_text()
	return ""

def getApplicationInfo(page):
	# Parsing page
	soup = BeautifulSoup(page.content, 'html.parser')
	# ---------------- Initialisation des variables ----------------------------------
	app_version=""
	app_date_sortie=""
	app_nbre_download=""
	app_name=""
	app_description=""

	# -------------- Traitement -------------------------------------------------------
	app_name_elt = soup.select_one("div div div div div div div h1")
	app_version_date = soup.select("div.header-desktop__MoreInfoContainer-xc5gow-11  div div div div div",class_="mini-versions__LatestVersion-sc-19sko2j-5 drfVqx")
	app_nbre_download_elt = soup.select_one("section div div div span")
	app_description_elt = soup.select_one("section.section__SectionContainer-lxnmhg-0 div p",{"itemprop":"description"})


	if len(app_version_date)>0 and len(app_version_date)<3:
		app_version = app_version_date[0].get_text()
		app_date_sortie = app_version_date[1].get_text().replace('(','').replace(')','')
		pass

	app_name = check(app_name_elt)
	app_nbre_download = check(app_nbre_download_elt)
	app_description = check(app_description_elt)

	app_info = {"app_name":app_name,"app_version":app_version,"app_nbre_downloads":app_nbre_download,"date_sortie":app_date_sortie,"app_description":app_description}
	return app_info