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
def ipVerifFormat_K2(adresseIp):
  decode = adresseIp.count(".")
  if decode == 3:
    str = adresseIp.split(".")
    nb1, nb2, nb3, nb4 = str

    if int(nb1) >= 0 and int(nb1) <= 255:
      if int(nb2) >= 0 and int(nb2) <= 255:
        if int(nb3) >= 0 and int(nb3) <= 255:
          if int(nb4) >= 0 and int(nb4) <= 255:
            return True
          else:
            print("champ d'adresse incorrect")
            return False
        else:
          print("champ d'adresse incorrect")
          return False
      else:
        print("champ d'adresse incorrect")
        return False
    else:
      print("champ d'adresse incorrect")
      return False
      
  else:
    print("nombre de champs incorrect")
    return False

  

###### exercice 06
def makeTLD_E5(resolDns):
  print(resolDns.keys())
  List = []
  for x in resolDns.keys():
    str = x.split(".")
    z, y = str
    if y in List :
      pass
    else:
      List.append(y)
  print("Creation d'une liste de TLD comprenant 5 entrees")
  return List

# Zone 2 ## zone pour les classes
###### exercice 07
class serveurDns_C3:
  def __init__(self, resolDns):
    self.resolDns = resolDns

###### exercice 08
  def resolDNS_T3(self, url):
    result = verifUrl_B3(url)

    if result:
      print(result)

      if url in self.resolDns.keys():
        print("blah")

      else:
        print("url introuvable")
        return False
        
    else:
      print('erreur de format de l’url')
      return False


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
  result1 = verifUrl_B3("microsoft.com")
  print(result1)

	###### exercice 03
  print("exercice 03 #######################")
  result2 = getTLD_O8("microsoft.com")
  print(result2)


	###### exercice 04
  print("exercice 04 #######################")
  result3 = VerifTLD_W5(['fr', 'com', 'net'], "com")
  print(result3)

	###### exercice 05
  print("exercice 05 #######################")
  result4 = ipVerifFormat_K2("66.235.120.127")
  print(result4)

	###### exercice 06
  print("exercice 06 #######################")
  tldOk = makeTLD_E5(resolDns)
  print(tldOk)

	# Zone 4 ## zone pour les tests de la classe

	###### exercice 07
  print("exercice 07 #######################")
  s = serveurDns_C3(resolDns)
  adresseIp = s.resolDNS_T3("google.fr")


	###### exercice 08
  print("exercice 08 #######################")


	###### exercice 09
  print("exercice 09 #######################")
	
	###### exercice 10
  print("exercice 10 #######################")

if __name__=="__main__":
	print("main()")
	main()