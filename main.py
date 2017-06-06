import cherrypy,os
from generador import Generador
from template import Template


class goodAndDevil(object):
    @cherrypy.expose
    def index(self):

        miGenerador = Generador()
        file = open("lista.csv","r")
        #Con estas lineas obtengo la plantilla
        miTemplate = Template()
        pagina=miTemplate.TEMPLATE
        pagina = pagina.replace("[ CONT1 ]", miGenerador.generadorTituloParrafo("Game Score","")  )
        pagina = pagina.replace("[ CONT2 ]", miGenerador.generadorTabla(file))
        # pagina = pagina.replace("[ CONT3 ]", miGenerador.generarImagenHTML())


        return pagina

if __name__ == '__main__':
    conf = {
        '/': {
            'tools.sessions.on': True,
            'tools.staticdir.root': os.path.abspath(os.getcwd())
        },
        '/static': {
            'tools.staticdir.on': True,
            'tools.staticdir.dir': './public'
        }
    }
    cherrypy.config.update({'server.socket_host': '127.0.0.1', })
    cherrypy.config.update({'server.socket_port': int(os.environ.get('PORT', '5000')), })
    cherrypy.quickstart(goodAndDevil(), '/', conf)