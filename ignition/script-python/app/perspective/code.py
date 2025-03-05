def navigate(page=None, name=None, url=None, view=None, viewParams={}):
	if page is not None:
		system.perspective.navigate(page=page)
	elif view is not None:
		system.perspective.navigate(view=view,params=viewParams)
	elif url is not None:
		system.perspective.navigate(url=url)
	else:
		pass
		
def navigateToPage(page=None, name=None):
	navigate(page=page,name=name)
	
def navigateToUrl(url=None):
	navigate(url=url)

def navigateToView(view=None, viewParams={}):
	navigate(view=view,viewParams=viewParams)
	
