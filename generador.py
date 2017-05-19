
class Generador:
    def generadorTituloParrafo(self, tirulo, parrafo):
        titulo = "<h1 >" + titulo + "</h1>"
        parrafo = "<p>" + parrado + "</p>"
        return tirulo + parrafo

    def generadorLista(self,Lista):
        codigo =""
        for i in Lista:
            codigo = codigo + "<li >" + i + "</li>"
        return "<ol>" + codigo + "</ol>"

    def generadorTabla(self, listaTabla):
        tabla = ""
        td = ""
        for i in listaTabla:
            tr1 = "<tr>"
            for j in i.split(","):
                td = td + "<td >" + j + "</td>"
            tr2 = "</tr>"

            tabla = tabla + tr1 + td + tr2
            td =""
        return "<table>" + tabla + "</table>"
