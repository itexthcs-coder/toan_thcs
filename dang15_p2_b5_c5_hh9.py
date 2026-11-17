import sys
from PyQt5.QtWidgets import QApplication, QColorDialog, QMainWindow, QSplitter, QTreeWidget, QSpacerItem, QSizePolicy, QTreeWidgetItem, QCheckBox, QFileDialog, QVBoxLayout, QTextEdit, QPushButton, QWidget, QLabel, QLineEdit, QDialog, QAction, QMessageBox, QScrollBar, QHeaderView, QMenu, QGridLayout
from sympy import *
from sympy.abc import x
import sympy as sp
from sympy import symbols,sqrt,evaluate,Subs,latex, Rational, expand, simplify, integrate
import random
import math
from sympy import Rational
from fractions import Fraction as frac
from random import randint
from PyQt5.QtGui import QTextCursor
from PyQt5.QtGui import QFont
import hashlib
import uuid
import os
from sympy import symbols, Eq, solve
import numpy as np
from PyQt5.QtGui import QIcon
from math import factorial
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QTextDocument
from subprocess import run, CalledProcessError
import shutil
from PyQt5.QtWidgets import QProgressBar
from docx import Document
from PyQt5 import QtGui
import re
import pandas as pd
from PyQt5.QtGui import QPixmap
import subprocess
import platform
import json
from decimal import Decimal, ROUND_HALF_UP
from PyQt5.QtWidgets import QComboBox, QPushButton, QVBoxLayout, QWidget
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QSpinBox, QTreeWidget, QTreeWidgetItem, QCheckBox, QTextEdit, QPushButton, QHBoxLayout
from random import randint, choice, shuffle
from sympy import latex
from fractions import Fraction
from collections import Counter
from random import sample
import shutil
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt
import qrcode
import json
import glob
import os
import platform
import subprocess
import hashlib
import base64
from datetime import datetime, timedelta
from PyQt5.QtWidgets import (QApplication, QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox)
from sympy import symbols, solve, Lt
#from PyQt5.QtWebEngineWidgets import QWebEngineView
#from PyQt5.QtCore import QUrl
#from sympy import latex
import re
import pyperclip
import warnings
warnings.filterwarnings("ignore", category=FutureWarning)

import google.generativeai as genai
from sympy.abc import x, y, z, t
import sys
import os
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QFileDialog, QMessageBox
)
from pdf2image import convert_from_path
from math import degrees
import openpyxl
from openpyxl import Workbook
from openpyxl.styles import Alignment, Font
from openpyxl.utils import get_column_letter
from sympy import simplify, collect
from itertools import combinations
import itertools
from PyQt5.QtCore import QSettings
import sys
import os
import platform
import subprocess
import hashlib
import time
from datetime import datetime, timedelta
# Bổ sung các widget và core cho Splash Screen
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QDialog, QLabel, QLineEdit, 
    QPushButton, QComboBox, QCheckBox, QTextEdit, QVBoxLayout, 
    QHBoxLayout, QGridLayout, QMessageBox, QColorDialog,
    QSplashScreen, QProgressBar  # <-- BỔ SUNG 2 CÁI NÀY
)
from PyQt5.QtCore import Qt, QSettings, QThread, pyqtSignal  # <-- BỔ SUNG QThread, pyqtSignal
from PyQt5.QtGui import QIcon, QPixmap, QFont
from PyQt5.QtGui import QFont, QBrush, QColor
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QSplitter, QTreeWidget, QTreeWidgetItem, QTextEdit, QLabel, 
    QSpacerItem, QSizePolicy, QStackedWidget, QPushButton, QCheckBox, QSpinBox,
    QScrollArea  # <-- Thêm mục này vào đây
)
from PyQt5.QtWidgets import QCheckBox
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtCore import Qt, QPropertyAnimation, pyqtProperty
from functools import wraps
import re
import uuid
import json, base64
from datetime import datetime
from nacl.signing import VerifyKey
from nacl.encoding import HexEncoder
from nacl.exceptions import BadSignatureError
### CÔNG CỤ
import sys
import numpy as np
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QDialog, 
    QVBoxLayout, QHBoxLayout, QTabWidget, QWidget, 
    QLabel, QSlider, QDoubleSpinBox, QGroupBox
)
from PyQt5.QtCore import Qt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from mpl_toolkits.mplot3d import Axes3D  # Cần cho 3D


def bt_dang15_p2_b5_c5_hh9(self):
    def fmt(val):
        if isinstance(val, float):
            s = str(round(val, 4)).rstrip('0').rstrip('.')
            return s.replace('.', ',')
        return str(val).replace('.', ',')

    R_mt = 16
    r_mt = 15
    d_khuyen = round(random.choice([0.4, 0.6, 0.8]), 1)

    noidungcauhoi = ("""Khi Mặt Trăng đi qua giữa Trái Đất và Mặt Trời, đĩa tròn Mặt Trăng che khuất đĩa tròn Mặt Trời tạo ra hiện tượng nhật thực. Giả sử tại thời điểm quan sát từ Trái Đất, đĩa Mặt Trời có bán kính biểu kiến là $R = %s'$ (phút cung), đĩa Mặt Trăng có bán kính biểu kiến là $r = %s'$ ($r < R$ trong trường hợp nhật thực hình khuyên), và khoảng cách giữa hai tâm đĩa là $d$.""" % (fmt(R_mt), fmt(r_mt)))

    # Nhận biết
    nb_da_1_d = '\\True Khi hiện tượng nhật thực một phần diễn ra, viền của đĩa Mặt Trăng và đĩa Mặt Trời là hai đường tròn cắt nhau'
    nb_da_1_s = 'Khi hiện tượng nhật thực một phần diễn ra, viền của đĩa Mặt Trăng và đĩa Mặt Trời là hai đường tròn tiếp xúc ngoài'
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]

    loigiai_nb_1 = ("""Trong giai đoạn nhật thực một phần, đĩa Mặt Trăng che lấp một phần đĩa Mặt Trời nên biên giới hai đĩa tròn giao nhau tại đúng $2$ điểm, tức là hai đường tròn cắt nhau ($R - r < d < R + r$).""")

    # Thông hiểu
    th_da_1_d = '\\True Khoảnh khắc đĩa Mặt Trăng bắt đầu chạm vào mép ngoài của đĩa Mặt Trời (tiếp xúc lần 1) ứng với $d = %s\'$' % (fmt(R_mt + r_mt))
    th_da_1_s = 'Khoảnh khắc đĩa Mặt Trăng bắt đầu chạm vào mép ngoài của đĩa Mặt Trời (tiếp xúc lần 1) ứng với $d = %s\'$' % (fmt(R_mt - r_mt))
    list_th_da_1 = [th_da_1_d, th_da_1_s]

    loigiai_th_1 = ("""Thời điểm bắt đầu nhật thực (tiếp xúc lần 1) tương ứng với vị trí hai đường tròn tiếp xúc ngoài nên $d = R + r = %s + %s = %s'$.""" % (fmt(R_mt), fmt(r_mt), fmt(R_mt + r_mt)))

    # Vận dụng
    vd_da_1_d = '\\True Khi $d = %s\'$, toàn bộ đĩa Mặt Trăng nằm gọn bên trong đĩa Mặt Trời mà không chạm viền (nhật thực hình khuyên)' % (fmt(d_khuyen))
    vd_da_1_s = 'Khi $d = %s\'$, đĩa Mặt Trăng và đĩa Mặt Trời tiếp xúc trong với nhau' % (fmt(d_khuyen))
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]

    loigiai_vd_1 = ("""Ta có $R - r = %s - %s = %s'$. Vì $d = %s' < %s'$ nên $d < R - r$, đường tròn đĩa Mặt Trời đựng đường tròn đĩa Mặt Trăng (không có điểm chung).""" % (fmt(R_mt), fmt(r_mt), fmt(R_mt - r_mt), fmt(d_khuyen), fmt(R_mt - r_mt)))

    # Vận dụng cao
    vdc_da_1_d = '\\True Nếu tại một địa điểm, hai tâm đĩa Mặt Trời và Mặt Trăng trùng khít nhau ($d = 0$) khi $r < R$, ta thu được hình ảnh hai đường tròn đồng tâm'
    vdc_da_1_s = 'Nếu hai tâm đĩa Mặt Trời và Mặt Trăng trùng khít nhau ($d = 0$) khi $r < R$, ta thu được hiện tượng nhật thực toàn phần che kín hoàn toàn Mặt Trời'
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]

    loigiai_vdc_1 = ("""Khi hai tâm trùng nhau ($d = 0$) và hai bán kính khác nhau ($r < R$), hai đường tròn là hai đường tròn đồng tâm (trường hợp đặc biệt của hai đường tròn đựng nhau), tạo thành vòng sáng hình khuyên xung quanh Mặt Trăng.""")

    def count_true_answers(answers):
        return sum('\\True' in ans for ans in answers)

    while True:
        nb_da_1 = random.choice(list_nb_da_1)
        th_da_1 = random.choice(list_th_da_1)
        vd_da_1 = random.choice(list_vd_da_1)
        vdc_da_1 = random.choice(list_vdc_da_1)
        answers = [nb_da_1, th_da_1, vd_da_1, vdc_da_1]
        if 1 <= count_true_answers(answers) <= 3:
            break

    list_nb_1, list_nb_2 = [nb_da_1], [loigiai_nb_1]
    list_th_1, list_th_2 = [th_da_1], [loigiai_th_1]
    list_vd_1, list_vd_2 = [vd_da_1], [loigiai_vd_1]
    list_vdc_1, list_vdc_2 = [vdc_da_1], [loigiai_vdc_1]

    combined_nb = list(zip(list_nb_1, list_nb_2))
    combined_th = list(zip(list_th_1, list_th_2))
    combined_vd = list(zip(list_vd_1, list_vd_2))
    combined_vdc = list(zip(list_vdc_1, list_vdc_2))

    random.shuffle(combined_nb)
    random.shuffle(combined_th)
    random.shuffle(combined_vd)
    random.shuffle(combined_vdc)

    shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)
    shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
    shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
    shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)

    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n' +
               '\\choiceTFn \n' +
               '{' + str(shuffled_answers_nb[0]) + '}\n' +
               '{' + str(shuffled_answers_th[0]) + '}\n' +
               '{' + str(shuffled_answers_vd[0]) + '}\n' +
               '{' + str(shuffled_answers_vdc[0]) + '}\n' +
               '\\loigiai{ \n' +
               '\\begin{enumEX}[a)]{1} \n' +
               '\\item ' + str(shuffled_solutions_nb[0]) + '\n' +
               '\\item ' + str(shuffled_solutions_th[0]) + '\n' +
               '\\item ' + str(shuffled_solutions_vd[0]) + '\n' +
               '\\item ' + str(shuffled_solutions_vdc[0]) + '\n' +
               '\\end{enumEX}} \n' +
               '\\end{ex}\n \\end{minipage}\n\n')
    return content
