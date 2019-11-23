def limpaFloat(palavra):

    palavraStr = str(palavra)
    if (palavraStr.find(',') != -1):
        # Encontrou vírgula
        palavraLimpa = palavraStr.replace(",", "")
        numero = float(palavraLimpa)
    else:
        # Não encontrou vírgula
        numero = float(palavra)

    return numero

