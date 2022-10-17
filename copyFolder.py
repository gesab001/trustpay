import json
import os
import shutil

source_dir = os.path.join(r"C:\Users\giova\Desktop\trustpay", "nzd")

f = open("currencyCodes.json", "r", encoding="utf8")
jsondata = json.loads(f.read())
del jsondata["currencyCodes"]["NZD"]
for currency in jsondata["currencyCodes"]:
  print(currency)
  currencyfolder = currency.lower()
  currencySymbol = jsondata["currencySymbols"][currency]["symbol"]
  dest_dir = os.path.join(r"C:\Users\giova\Desktop\trustpay", currencyfolder)
  try:
    shutil.rmtree(dest_dir)
  except: 
    print(dest_dir + " does not exist")
    shutil.copytree(source_dir, dest_dir)
    source_file = os.path.join(r"C:\Users\giova\Desktop\trustpay", currencyfolder, "paypal.html")
    f = open(source_file)
    html = f.read()
    f.close()
    html = html.replace("NZD", currency)
    html = html.replace("$", currencySymbol)
    print(html)
    with open(source_file, "w", encoding="utf8") as writer:
      writer.write(html)
    