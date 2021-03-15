import pyshorteners

url = input("Enter url: ")

print("Url after shortening", pyshorteners.Shortener().tinyurl.short(url))