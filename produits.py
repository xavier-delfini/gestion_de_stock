import _mysql_connector
class Produits:
    def __init__(self,nom,description="",prix="",quantite=-1,id_categorie=-1):
        __nom=nom
        __description=description
        __prix=prix
        __quantite=quantite
        __id_categorie=id_categorie
    def get_Infos(self,nom):