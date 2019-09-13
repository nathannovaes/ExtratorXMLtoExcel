
#Verifica o fornecedor
def encontraFornecedor(produto):

  if produto.find('AGROINCA') != -1 or produto.find('Agroinca') != -1:
      return 'Agroinca'
  elif produto.find('THEREZOPOLIS') != -1 or produto.find('SUL AMERICANA') != -1:
      return 'Arbor'
  elif produto.find('BARILLA') != -1 or produto.find('Barilla') != -1 or produto.find('SFOGLIE') != -1:
      return 'Barilla'
  elif produto.find('BONAFONT') != -1 or produto.find('Bonafont') != -1:
      return 'Bonafont'
  elif produto.find('CASA MADEIRA') != -1 or produto.find('Casa Madeira') != -1:
      return 'Casa Madeira'
  elif produto.find('CERPA') != -1 or produto.find('Cerpa') != -1:
      return 'Cerpa'
  elif produto.find('DGOIAS') != -1 or produto.find('DGoias') != -1 or produto.find("D'GOIAS") != -1:
      return 'DGoias'
  elif produto.find('DORI') != -1 or produto.find('Dori') != -1:
      return 'Dori'
  elif produto.find('GOES') != -1 or produto.find('Goes') != -1:
      return 'Goes'
  elif produto.find('VEDETT') != -1 or produto.find('FAXE') != -1:
      return 'Interfood'
  elif produto.find('HEMMER') != -1 or produto.find('Hemmer') != -1:
      return 'Hemmer'
  elif produto.find('JUXX') != -1 or produto.find('Juxx') != -1:
      return 'Juxx'
  elif produto.find('KELCO') != -1 or produto.find('PIPICAT') != -1 or produto.find(' KEL') != -1 or produto.find('Kelco') != -1 or produto.find('Pipicat') != -1:
      return 'Kelco'
  elif produto.find('MASTIG') != -1 or produto.find('Mastig') != -1:
      return 'Mastig'
  elif produto.find('NESTLE') != -1 or produto.find('LOURENCO') != -1 or produto.find('PERRIER') != -1 or produto.find('Nestle') != -1 or produto.find('Lourenco') != -1 or produto.find('Perrier') != -1 or produto.find('PELLEGRINO') != -1 or produto.find('Pellegrino') != -1 or produto.find(' VITAL') != -1:
      return 'Nestle'
  elif produto.find('NUTRY') != -1 or produto.find('Nutry') != -1 or produto.find('NUTRIBOM') != -1:
      return 'Nutry'
  elif produto.find('PRATA') != -1 or produto.find('Prata') != -1:
      return 'Prata'
  elif produto.find(' RIO ') != -1 or produto.find(' Rio ') != -1:
      return 'Rio'
  elif produto.find('ACQUISSIMA') != -1 or produto.find('Acquissima') != -1:
      return 'Socorro'
  elif produto.find('TRADIPET') != -1 or produto.find('Tradipet') != -1:
      return 'Tradipet'
  elif produto.find('CONCHA') != -1 or produto.find('Concha') != -1 or produto.find('DIABLO') != -1:
      return 'CYT'
  else:
      return 'Fornecedor não encontrado'


