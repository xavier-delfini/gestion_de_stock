import connection as dbconnect


class Produits:
    def __init__(self, nom, description="", prix="", quantite=-1, id_categorie=-1):
        self.__nom = nom
        self.__description = description
        self.__prix = prix
        self.__quantite = quantite
        self.__id_categorie = id_categorie
        self.__cursor = dbconnect.db.cursor()

    def selectQuery(self, query, values=""):
        if values=="":
            self.__cursor.execute(query)
            return self.__cursor.fetchall()
        else:
            self.__cursor.execute(query, values)
            return self.__cursor.fetchall()

    def get_Infos(self, nom="", where=False):
        SQL = "SELECT * FROM boutique.produit"
        value = [nom]
        if where!=False or nom!="":
            SQL += " WHERE nom = %s"
            return self.selectQuery(SQL,value)
        else:
            return self.selectQuery(SQL)


a = Produits("a")
print(a.get_Infos())
print(a.get_Infos("Doom Eternal",True))
