class Generador:

    def generadorTituloParrafo(self, titulo, parrafo):
        titulo = "<h1>" + titulo + "</h1>"
        parrafo = "<p>" + parrafo + "</p>"
        return titulo + parrafo

    def nombre(self, file):
        for k in file:
            for l in k.split(","):
                print (l)