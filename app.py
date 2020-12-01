from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from Main_ui import Ui_Form
from http.client import HTTPSConnection
from json import loads

######################################################

app = QtWidgets.QApplication(sys.argv)
Form = QtWidgets.QWidget()
ui = Ui_Form()
ui.setupUi(Form)
Form.show()

######################################################

def Weather():
	key    = '833e43f3e6eab9ec137f016d1b46f923'
	domain = 'api.openweathermap.org'
	endpoint_current = f'/data/2.5/weather?q={ui.copy_text()}&appid={key}&units=metric&lang=ru'
	connection = HTTPSConnection( domain )
	connection.request('GET', endpoint_current )
	response   = connection.getresponse()
	data       = loads( response.read() )
	cod        = data['cod']
	if data['cod'] == 200:
		temp       = data['main']['temp']
		wind       = data['wind']['speed']
		weather    = data['weather'][0]['description']
		location   = data['name']
			
		ui.server_https.setText( str(cod) )
		ui.lineEdit.setText( str(location) )
		ui.lineEdit_3.setText( str(weather) )
		ui.lineEdit_2.setText( str(wind) )
		ui.lineEdit_5.setText( str(temp) )
		ui.server_https.setText( str(cod) )
	elif data['cod'] == '404':
		ui.lineEdit.setText( str(cod) )
		ui.lineEdit_3.setText( str(cod) )
		ui.lineEdit_2.setText( str(cod) )
		ui.lineEdit_5.setText( str(cod) )
		ui.server_https.setText( str(cod) )

######################################################

ui.pushButton.clicked.connect( Weather )

sys.exit(app.exec_())

#                      создал MRDroks                    #