from flask import Flask, session, render_template, request, redirect, url_for
from flaskext.mysql import MySQL
import pymysql

app = Flask(__name__)
app.secret_key = "cairocoders-ednalan"

mysql = MySQL()

app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'testingdb'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

@app.route('/productos')
def productos():
    return render_template("productos.html")

@app.route('/registro')
def registro():
    return render_template("registro.html")

@app.route('/login')
def login():
    return render_template("login.html")

@app.route('/inicio_correcto')
def inicio_correcto():
    return render_template("inicio_correcto.html")

@app.route('/inicio_incorrecto')
def inicio_incorrecto():
    return render_template("inicio_incorrecto.html")

@app.route('/usuarios', methods=['POST'])
def usuarios():
    if request.method == 'POST':
        aux_Correo = request.form['correo']
        aux_Contrasena = request.form['contrasena']
        conn = pymysql.connect(host='localhost', user='root', passwd='', db='agenda' )
        cursor = conn.cursor()
        cursor.execute('insert into registro (correo,contrasena) values (%s, %s)',(aux_Correo, aux_Contrasena))
        conn.commit()
    return redirect(url_for('home'))

@app.route('/iniciar_sesion', methods=['POST'])
def iniciar_sesion():
    if request.method == 'POST':
        aux_Correo = request.form['correo']
        aux_Contrasena = request.form['contrasena']
        conn = pymysql.connect(host='localhost', user='root', passwd='', db='agenda')
        cursor = conn.cursor()
        cursor.execute('select * from registro where correo=%s and contrasena=%s', (aux_Correo, aux_Contrasena))
        dato = cursor.fetchone()
    try:
        if aux_Correo and aux_Contrasena in dato:
           return render_template("inicio_correcto.html")
    except:
           return redirect(url_for('inicio_incorrecto'))

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/clases')
def clases():
    return render_template("clases.html")

@app.route('/nuestraempresa')
def nuestraempresa():
    return render_template("nuestraempresa.html")

@app.route('/servicios')
def servicios():
    return render_template("servicios.html")

@app.route('/contacto')
def contacto():
    return render_template("contacto.html")

@app.route('/crud')
def crud():
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='agenda', port=3306 )
    cursor = conn.cursor()
    cursor.execute('select id, correo, comentarios from comenta order by id')
    datos = cursor.fetchall()
    return render_template("crud.html", comentarios = datos)

@app.route('/editar/<string:id>')
def editar(id):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='agenda', port=3306 )
    cursor = conn.cursor()
    cursor.execute('select id, correo, comentarios from comenta where id = %s', (id))
    dato  = cursor.fetchall()
    return render_template("editar.html", comentar=dato[0])

@app.route('/editar_comenta/<string:id>',methods=['POST'])
def editar_comenta(id):
    if request.method == 'POST':
        corr=request.form['correo']
        come=request.form['comentarios']
        conn = pymysql.connect(host='localhost', user='root', passwd='', db='agenda', port=3306 )
        cursor = conn.cursor()
        cursor.execute('update comenta set correo=%s, comentarios=%s where id=%s', (corr,come,id))
        conn.commit()
    return redirect(url_for('crud'))

@app.route('/borrar/<string:id>')
def borrar(id):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='agenda', port=3306 )
    cursor = conn.cursor()
    cursor.execute('delete from comenta where id = {0}'.format(id))
    conn.commit()
    return redirect(url_for('crud'))

@app.route('/insertar')
def insertar():
    return render_template("insertar.html")

@app.route('/agrega_comenta', methods=['POST'])
def agrega_comenta():
    if request.method == 'POST':
        aux_Correo = request.form['correo']
        aux_Comentarios = request.form['comentarios']
        conn = pymysql.connect(host='localhost', user='root', passwd='', db='agenda', port=3306 )
        cursor = conn.cursor()
        cursor.execute('insert into comenta (correo,comentarios) values (%s, %s)',(aux_Correo, aux_Comentarios))
        conn.commit()
    return redirect(url_for('crud'))

###FUNCIONES PARA CLASE

@app.route('/registroclase')
def registroclase():
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='agenda' )
    cursor = conn.cursor()
    cursor.execute('select idclase, nomclase from clases order by idclase')
    datos = cursor.fetchall()
    return render_template("registroclase.html", clase=datos, dat=' ')

@app.route('/registroclase_fdetalle/<string:idC>', methods=['GET'])
def registroclase_fdetalle(idC):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='agenda')
    cursor = conn.cursor()

    cursor.execute('select idclase, nomclase from clases order by idclase')
    datos = cursor.fetchall()

    cursor.execute('select idclase,nomclase,nomprofesor,horario,precio,instru from clases where idclase = %s', (idC))
    dato = cursor.fetchall()

    datos = cursor.fetchall()
    return render_template("registroclase.html", clase = datos, dat=dato[0])

@app.route('/registroclase_borrar/<string:idC>')
def registroclase_borrar(idC):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='agenda')
    cursor = conn.cursor()
    cursor.execute('delete from clases where idclase = %s',(idC))
    conn.commit()
    return redirect(url_for('clases'))

@app.route('/registroclase_agregar')
def registroclase_agregar():
    return render_template("registroclase_agr.html")

@app.route('/registroclase_fagrega', methods=['POST'])
def registroclase_fagrega():
    if request.method == 'POST':
        nomcla = request.form['nomclase']
        nompro = request.form['nomprofesor']
        hora = request.form['horario']
        pre = request.form['precio']
        inst = request.form['instru']
        conn = pymysql.connect(host='localhost', user='root', passwd='', db='agenda' )
        cursor = conn.cursor()
        cursor.execute('insert into clases (nomclase,nomprofesor,horario,precio,instru) values (%s,%s,%s,%s,%s)',(nomcla,nompro,hora,pre,inst))
        conn.commit()
    return redirect(url_for('clases'))


@app.route('/registroclase_editar/<string:idC>')
def registroclase_editar(idC):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='agenda')
    cursor = conn.cursor()
    cursor.execute('select idclase,nomclase,nomprofesor,horario,precio,instru from clases where idclase = %s', (idC))
    dato = cursor.fetchall()
    return render_template("registroclase_edi.html", dat=dato[0])

@app.route('/registroclase_fedita/<string:idC>', methods=['POST'])
def registroclase_fedita(idC):
    if request.method == 'POST':
        nomcla = request.form['nomclase']
        nompro = request.form['nomprofesor']
        hora = request.form['horario']
        pre = request.form['precio']
        inst = request.form['instru']
        
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='agenda')
    cursor = conn.cursor()
    cursor.execute('update clases set nomclase = %s, nomprofesor = %s, horario = %s, precio = %s, instru = %s where idclase = %s', (nomcla, nompro, hora, pre, inst, idC))
    conn.commit()
    return redirect(url_for('clases'))

###FUNCIONES PARA PRODUCTO

@app.route('/registroproductos')
def registroproductos():
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='agenda' )
    cursor = conn.cursor()
    cursor.execute('select idproducto, nomproducto from productos order by idproducto')
    datos = cursor.fetchall()
    return render_template("registroproductos.html", producto=datos, dat=' ')

@app.route('/registroproductos_fdetalle/<string:idP>', methods=['GET'])
def registroproductos_fdetalle(idP):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='agenda')
    cursor = conn.cursor()

    cursor.execute('select idproducto, nomproducto from productos order by idproducto')
    datos = cursor.fetchall()

    cursor.execute('select idproducto,nomproducto,folio,caracteristicas,nomprovedor,exportado,precio from productos where idproducto = %s', (idP))
    dato = cursor.fetchall()

    datos = cursor.fetchall()
    return render_template("registroproductos.html", producto = datos, dat=dato[0])

@app.route('/registroproductos_borrar/<string:idP>')
def registroproductos_borrar(idP):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='agenda')
    cursor = conn.cursor()
    cursor.execute('delete from productos where idproducto = %s',(idP))
    conn.commit()
    return redirect(url_for('productos'))

@app.route('/registroproductos_agregar')
def registroproductos_agregar():
    return render_template("registroproductos_agr.html")

@app.route('/registroproductos_fagrega', methods=['POST'])
def registroproductos_fagrega():
    if request.method == 'POST':
        nompro = request.form['nomproducto']
        fol = request.form['folio']
        carac = request.form['caracteristicas']
        nomprov = request.form['nomprovedor']
        exp = request.form['exportado']
        pre = request.form['precio']
        conn  = pymysql.connect(host='localhost', user='root', passwd='', db='agenda' )
        cursor = conn.cursor()
        cursor.execute('insert into productos (nomproducto,folio,caracteristicas,nomprovedor,exportado,precio) values (%s,%s,%s,%s,%s,%s)',(nompro,fol,carac,nomprov,exp,pre))
        conn.commit()
    return redirect(url_for('productos'))


@app.route('/registroproductos_editar/<string:idP>')
def registroproductos_editar(idP):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='agenda')
    cursor = conn.cursor()
    cursor.execute('select idproducto,nomproducto,folio,caracteristicas,nomprovedor,exportado,precio from productos where idproducto = %s', (idP))
    dato = cursor.fetchall()
    return render_template("registroproductos_edi.html", dat=dato[0])

@app.route('/registroproductos_fedita/<string:idP>', methods=['POST'])
def registroproductos_fedita(idP):
    if request.method == 'POST':
        nompro = request.form['nomproducto']
        fol = request.form['folio']
        carac = request.form['caracteristicas']
        nomprov = request.form['nomprovedor']
        exp = request.form['exportado']
        pre = request.form['precio']
        
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='agenda')
    cursor = conn.cursor()
    cursor.execute('update productos set nomproducto = %s, folio = %s, caracteristicas = %s, nomprovedor = %s, exportado = %s, precio = %s where idproducto = %s', (nompro, fol, carac, nomprov, exp, pre, idP))
    conn.commit()
    return redirect(url_for('productos'))

if __name__ == "__main__":
    app.run(debug=True)