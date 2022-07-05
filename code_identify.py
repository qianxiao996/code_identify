import re
import urllib.parse
import qdarkstyle
from threading import Thread
import requests
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import *
import  base64, json, time, sys
import frozen_dir
SETUP_DIR = frozen_dir.app_path()
sys.path.append(SETUP_DIR)
import web
from ui.main import Ui_MainWindow
import easyocr
import muggle_ocr
import ddddocr

# muggle_ocr_obj = muggle_ocr.SDK(model_type=muggle_ocr.ModelType.Captcha)
muggle_ocr_obj = muggle_ocr.SDK(conf_path="./lib/captcha.yaml")
ddddocr_obj = ddddocr.DdddOcr()
easyocr_obj = easyocr.Reader(['en'], gpu=False)  # need to run only once to load model into memory


class MyApplication(web.application):
    def run(self, port=8080, *middleware):
        func = self.wsgifunc(*middleware)
        return web.httpserver.runsimple(func, ('0.0.0.0', port))


class MainWindows(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindows, self).__init__(parent)
        self.Ui = Ui_MainWindow()
        self.Ui.setupUi(self)
        self.setWindowIcon(QtGui.QIcon('./main.ico'))
        self.Ui.comboBox_type.currentIndexChanged.connect(self.change_comboBox_type)  # comboBox事件选中触发刷新
        self.Ui.pushButton_start.clicked.connect(self.get_code)
        self.Ui.tableWidget_result.verticalHeader().setDefaultSectionSize(50)
        self.Ui.tableWidget_result.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.Ui.tableWidget_result.horizontalHeader().setSectionResizeMode(0, QHeaderView.Interactive)
        self.Ui.pushButton_web.clicked.connect(self.web_server)
        self.webapp = MyApplication(urls, globals())

        self.Ui.pushButton_path.clicked.connect(self.bendi_code)

    def web_server(self):
        if self.Ui.pushButton_web.text() == "开启WEB接口":
            t1 = Thread(target=self.gogog_Webapi, args=())
            t1.start()
            import socket
            sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sk.settimeout(1)
            i = 3
            error = ''
            while i:
                try:
                    sk.connect(('127.0.0.1', 9090))
                    self.Ui.pushButton_web.setText("关闭服务")
                    box = QtWidgets.QMessageBox(window)
                    box.warning(self, "Success", "服务开启成功！\n访问地址:http://0.0.0.0:9090" + error)
                    return
                except Exception as e:
                    error = str(e)
                sk.close()
            box = QtWidgets.QMessageBox(window)
            box.warning(self, "Error", "服务开启失败！" + error)
        else:
            self.webapp.stop()
            self.Ui.pushButton_web.setText("开启WEB接口")

    def gogog_Webapi(self):
        try:
            self.webapp.run(port=9090)
        except:
            pass

    def change_comboBox_type(self):
        panduan_type = self.Ui.comboBox_type.currentText()
        if panduan_type == "Response Data":
            self.Ui.lineEdit_type_text.setEnabled(False)
        elif panduan_type == "JSON Match":
            self.Ui.lineEdit_type_text.setEnabled(True)
            self.Ui.lineEdit_type_text.setText('response')
        else:
            self.Ui.lineEdit_type_text.setEnabled(True)

    def get_response_text(self, content):
        match_text = self.Ui.lineEdit_type_text.text()
        comboBox_type = self.Ui.comboBox_type.currentText()
        if comboBox_type == "Response":
            return content
        elif comboBox_type == "Re Match":
            try:
                match_Result = re.findall(match_text, content)
                if match_Result:
                    match_Result = match_Result[0]
            except:
                match_Result = ""
                box = QtWidgets.QMessageBox(window)
                box.warning(self, "Error", "数据匹配失败！")
                return None
            return match_Result
        elif comboBox_type == "JSON Match":
            try:
                response = json.loads(content)
            except:
                box = QtWidgets.QMessageBox(window)
                box.warning(self, "Error", "返回数据不是json")
                return None
            content = eval(match_text)
            return content



        else:
            return content

    def get_code(self):
        try:
            url = self.Ui.lineEdit_url.text()
            if not url:
                return
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36 by qianxiao996",
                "Referer": url
            }
            r = requests.get(url, headers=headers, timeout=3,verify=False)
            try:
                content = self.get_response_text(r.content.decode('ISO-8859-1'))
            except Exception as e:
                print(e)
                box = QtWidgets.QMessageBox(window)
                box.warning(self, "Error", "获取图像失败！")
                return
            if content:
                try:
                    content = self.image_decode(content)
                except:
                    box = QtWidgets.QMessageBox(window)
                    box.warning(self, "Error", "解码失败！")
                    return
                photo = QPixmap()
                photo.loadFromData(content.encode('ISO-8859-1'))
                self.Ui.label_code_result.setPixmap(photo)
                self.Ui.label_code_result.setScaledContents(True)  # 让图片自适应label大小
                type = self.Ui.comboBox.currentText()
                code_result = self.code_identify(type, content.encode('ISO-8859-1'))
                aaa_time = time.strftime("%H:%M:%S", time.localtime())
                self.add_table(aaa_time, str(content), code_result, '本地识别')
                self.Ui.plainTextEdit_log.appendPlainText(aaa_time + ":" + code_result)
            else:
                self.Ui.label_code_result.setText("获取图片失败！")
        except:
            pass
    def image_decode(self, content):
        decode_type = self.Ui.comboBox_encode.currentText()
        if decode_type == "无":
            return content
        elif decode_type == "Base64":
            return (base64.b64decode(content.strip().replace(' ', '').replace('\r', '').replace('\n', ''))).decode('ISO-8859-1')
        elif decode_type == "Hex":
            content = content.replace('0x', '').replace('0X', '')
            result_text = str(bytes.fromhex(content), encoding='ISO-8859-1')
            return result_text
        elif decode_type == "二进制":
            content = str(hex(int(content, 2)))
            content = content.replace('0x', '').replace('0X', '')
            result_text = str(bytes.fromhex(content), encoding='ISO-8859-1')
            return result_text
        else:
            return content

    def add_table(self, aaa_time, content, code_result, type):
        label_code_result = QtWidgets.QLabel()
        label_code_result.setMinimumSize(QtCore.QSize(100, 30))
        photo = QPixmap()
        photo.loadFromData(content.encode('ISO-8859-1'))
        label_code_result.setPixmap(photo)
        row = self.Ui.tableWidget_result.rowCount()  # 获取行数
        self.Ui.tableWidget_result.insertRow(row)
        now_time = QTableWidgetItem(aaa_time)
        # img_item  = QTableWidgetItem(label_code_result)
        code_result_item = QTableWidgetItem(code_result)
        type_item = QTableWidgetItem(type)
        self.Ui.tableWidget_result.setItem(row, 0, now_time)
        self.Ui.tableWidget_result.setCellWidget(row, 1, label_code_result)  # self → Ui_form
        self.Ui.tableWidget_result.setItem(row, 2, code_result_item)
        self.Ui.tableWidget_result.setItem(row, 3, type_item)

    def code_identify(self, type, content):
        try:
            result = ''
            if type == "ddddocr":
                result = ddddocr_obj.classification(content)
            elif type == "Muggle Ocr":
                result = muggle_ocr_obj.predict(image_bytes=content)
            elif type == "Easyocr":
                result = easyocr_obj.readtext(content, detail=0)
                result = ''.join(result)
                # print(result)
                result = list(filter(str.isalnum, result))
                result = ''.join(result)
        except Exception as e:
            result = "识别失败," + str(e)
        return result

    def bendi_code(self):
        filename = self.file_open(r"Image Files (*.jpg);;Image Files (*.png);;Image Files (*.jpeg);;All files(*.*)")
        if filename:
            f = open(filename, 'rb')
            image_Dada = f.read()
            f.close()
            if image_Dada:
                type = self.Ui.comboBox.currentText()
                code_result = self.code_identify(type, image_Dada)
                aaa_time = time.strftime("%H:%M:%S", time.localtime())
                self.add_table(aaa_time, image_Dada.decode('ISO-8859-1'), code_result, '本地图片')
                self.Ui.plainTextEdit_log.appendPlainText(aaa_time + ":" + code_result)

    # 文件打开对话框
    def file_open(self, type):
        try:
            fileName, selectedFilter = QFileDialog.getOpenFileName(self, (r"选择图片文件"), '', type)
            return (fileName)  # 返回文件路径
        except:
            return None


urls = (
    '/', 'index',
    '/ddddocr/base64', 'ddddocr_base64',
    '/easyocr/base64', 'easyocr_base64',
    '/muggle_ocr/base64', 'muggle_ocr_base64',

)


class index:
    def GET(self):
        web.header("Content-Type", "text/html; charset=UTF-8")
        render = web.template.render("templates")
        return render.index()


class ddddocr_base64:
    def POST(self):
        web.header("Content-Type", "text/json")
        data1 = web.data()
        try:
            data_json = json.loads(data1)
        except:
            return {'status': '0', 'result': "json数据解析错误"}
        img_b64 = data_json.get('image')
        img_b64 = urllib.parse.unquote(img_b64)  # 对字符串进行url解码
        x = base64.b64decode(img_b64)
        code = MainWindows().code_identify("ddddocr", x)
        return {'status': '1', 'result': code}


class easyocr_base64:
    def POST(self):
        web.header("Content-Type", "text/json")
        data1 = web.data()
        try:
            data_json = json.loads(data1)
        except:
            return {'status': '0', 'result': "json数据解析错误"}
        img_b64 = data_json.get('image')
        img_b64 = urllib.parse.unquote(img_b64)  # 对字符串进行url解码
        x = base64.b64decode(img_b64)
        code = MainWindows().code_identify("Easyocr", x)
        return {'status': '1', 'result': code}


class muggle_ocr_base64:
    def POST(self):
        web.header("Content-Type", "text/json")
        data1 = web.data()
        try:
            data_json = json.loads(data1)
        except:
            return {'status': '0', 'result': "json数据解析错误"}
        img_b64 = data_json.get('image')
        img_b64 = urllib.parse.unquote(img_b64)  # 对字符串进行url解码
        x = base64.b64decode(img_b64)
        code = MainWindows().code_identify("Muggle Ocr", x)
        return {'status': '1', 'result': code}


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    # app.setStyleSheet(qdarkstyle.load_stylesheet(qt_api='pyqt5'))
    # app.setStyleSheet(qdarkstyle.load_stylesheet(qt_api='pyqt5', palette=LightPalette()))

    window = MainWindows()
    # f=open('./qss/white.qss', 'r',encoding='utf-8')
    # qssStyle= f.read()
    # window.setStyleSheet(qssStyle)
    window.show()
    sys.exit(app.exec_())
