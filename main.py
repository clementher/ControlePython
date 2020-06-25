# Zone 1 ## zone pour les fonctions
# exercice 00 (la fonction est definie dans cette zone)
def exempleHello (msg):
    return "bonjour {}, comment allez-vous ?".format(msg)


###### exercice 01
def makeDico_A7(filename, sep):
   print("Creation d'un dictionnaire a partir du fichier 'dns.txt' avec '80' entrees")
   f = open(filename, "r")

   dico = {}
   
   for i in range(0,80):
     resol = f.readline().split(sep)
     dico[resol[0]] = resol[1].replace("\n","")
     
   return dico

###### exercice 02
def verifUrl_B3(url):
  decode = url.count(".")

  if decode == 1:
    str = url.split(".")
    x, y = str

    if len(y) <= 3:
      return True

    else:
      print("url mal formee")
      return False

  else:
    print("url mal formee")
    return False

###### exercice 03
def getTLD_O8(url):
  if verifUrl_B3(url):
    str = url.split(".")
    x, y = str
    return y
  else:
    print("TDL mal formee")
    return False

###### exercice 04
def VerifTLD_W5(tldOk, tld):
  for x in tldOk:
    if tld==x:
      return True

  print("TLD Absente")
  return False
      
  

###### exercice 05
    

###### exercice 06


# Zone 2 ## zone pour les classes
###### exercice 07


###### exercice 08


###### exercice 09
    

# Zone 3 ## zone pour les tests des fonctions

def main() :
  from re import split
	###### exercice 00 (la fonction est appelee dans cette zone afin de confirmer son fonctionnement) 
  print("exercice 00 #######################")
  salutations = exempleHello("Michel")
  print(salutations)
  print(salutations.split(sep=" "))

	###### exercice 01
  print("exercice 01 #######################")
  resolDns = makeDico_A7("dns.txt", ",")
  print(resolDns)

	###### exercice 02
  print("exercice 02 #######################")
  result = verifUrl_B3("microsoft.com")
  print(result)

	###### exercice 03
  print("exercice 03 #######################")
  result = getTLD_O8("microsoft.com")
  print(result)


	###### exercice 04
  print("exercice 04 #######################")
  result = VerifTLD_W5(['fr', 'com', 'net'], "com")

	###### exercice 05
  print("exercice 05 #######################")


	###### exercice 06
  print("exercice 06 #######################")

	# Zone 4 ## zone pour les tests de la classe

	###### exercice 07
  print("exercice 07 #######################")


	###### exercice 08
  print("exercice 08 #######################")


	###### exercice 09
  print("exercice 09 #######################")
	
	###### exercice 10
  print("exercice 10 #######################")

if __name__=="__main__":
	print("main()")
	main()