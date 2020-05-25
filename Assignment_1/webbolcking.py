website_list = ['www.netflix.com', 'www.spotify.com', 'www.hbo.com', 'www.facebook.com']
blocked = False
import webbrowser

website = input ('Enter the website : ')
for i in website_list :
    if website == i :
        blocked = True
        print ("The website is blocked!!")
if blocked == False :
   # webbrowser.open_new_tab(website)
	print("This Website is not Blocked")
