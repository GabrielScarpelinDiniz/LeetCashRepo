def interpret(command):
    palavra = ""
    resposta = ""
    for letra in command:
        palavra+=letra
        if palavra=="G":
            resposta+="G"
            palavra = ""
        elif palavra=="()":
            resposta+="o"
            palavra = ""
        elif palavra=="(al)":
            resposta+="al"
            palavra = ""
    return resposta

print(interpret("G()(al))"))
        