
class Generador:
    def generadorTituloParrafo(self, titulo, parrafo):
        titulo = "<h1 >" + titulo + "</h1>"
        parrafo = "<p>" + parrafo + "</p>"
        return titulo + parrafo

    def generadorLista(self,Lista):
        codigo =""
        for i in Lista:
            codigo = codigo + "<li >" + i + "</li>"
        return "<ol>" + codigo + "</ol>"

    def generarImagenHTML(self):
        return "<img src=static/img/juan.png ></img>"

    def generadorTabla(self, csvFile):
        tabla = ""
        td = ""
        for i in csvFile:
            tr1 = "<tr>"
            infoJugadores =i.split(",")
            infoJugadores.append("<img src=\"static/img/"+infoJugadores[0]+".png\"></img>")
            for j in infoJugadores:

                td = td + "<td >" + j + "</td>"
            tr2 = "</tr>"

            tabla = tabla + tr1 + td + tr2
            td =""
        return "<table>" + tabla + "</table>"
