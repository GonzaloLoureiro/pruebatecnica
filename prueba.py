import os
import json

def main():
    path = "/Users/pgonzalo/Desktop/pruebatecnica/"

    respuesta = {'auth_module': {},
                'content_module': {}}
    parteb = {'auth_module': {},
                'content_module': {}}
    lista = []

    def primera(param):
        if not aux['provider'][param] in respuesta[param]:
                respuesta[param][aux['provider'][param]] = ['./' + file]
        else:
                respuesta[param][aux['provider'][param]].append('./' + file)

    def segunda(auth, content):
        if not aux['provider'][auth] in parteb[auth] and not aux['provider'][content] in parteb[content]:
                parteb[auth][aux['provider'][auth]] = ['./' + file]
                parteb[content][aux['provider'][content]] = ['./' + file]
        elif not aux['provider'][auth] in parteb[auth] and aux['provider'][content] in parteb[content]:
                parteb[auth][aux['provider'][auth]] = ['./' + file]
                parteb[content][aux['provider'][content]] = ['./' + file]    
        elif not aux['provider'][content] in parteb[content] and aux['provider'][auth] in parteb[auth]:
                parteb[content][aux['provider'][content]] = ['./' + file]
                parteb[auth][aux['provider'][auth]] = ['./' + file]

    for file in os.listdir(path):
        with open(path + file) as otro:
            aux = json.load(otro)
            primera('auth_module')
            primera('content_module')
            segunda('auth_module', 'content_module')
            
    for arc in parteb['auth_module'].values():
        lista.append(arc[0])
    for arch in parteb['content_module'].values():
        if not arch[0] in lista:
            lista.append(arch[0])

    with open('final.json', 'w') as f:
        json.dump('Parte A:', f)
        f.write('\n')
        json.dump(respuesta, f, indent=2)
        f.write('\n')
        json.dump('Parte B:', f)
        f.write('\n')
        json.dump(lista, f)

if __name__ == "__main__":
    main()

    


    