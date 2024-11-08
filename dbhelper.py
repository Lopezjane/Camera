from sqlite3 import connect,Row

database:str = "students.db"

def getprocess(sql:str)->list:pass
def postprocess(sql:str)->bool:
    db:object = connect(database)
    cursor:object = db.cursor()
    cursor.execute(sql)
    db.commit()
    db.close()
    return True if cursor.rowcount>0 else False


def add_record(table:str,**kwargs)->bool:
    keys:list = list(kwargs.keys())
    values:list = list(kwargs.values())
    fld:str = "`,`".join(keys)
    val:str = "','".join(values)
    sql:str = f"INSERT INTO `{table}`(`{fld}`) VALUES('{val}')"
    return postprocess(sql)