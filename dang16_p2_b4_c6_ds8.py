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




def bt_dang16_p2_b4_c6_ds8(self):
    # Dạng 16: Bài toán tài chính – Vay ngân hàng trả góp mua nhà (Vận dụng tr.22 & Bài 6.30 SGK)
    von_ty = random.choice([1.2, 1.8, 2.4])
    von_tr = int(round(von_ty * 1000))
    von_chia_12 = von_tr // 12
    
    y1 = 48
    r1_pct = random.choice([6, 9, 12])
    r1_dec = Rational(r1_pct, 100)
    x1 = Rational(von_tr, y1) + von_chia_12 * r1_dec
    
    y2 = 120
    x2 = (von_tr // 120) + 5
    chenh_lech = x2 * y2 - von_tr
    
    nb_da_1_d = '\\True Số tiền bác Châu phải trả mỗi tháng được tính theo công thức $x = \\frac{%s}{y} + %sr$.' % (von_tr, von_chia_12)
    nb_da_1_s = 'Số tiền bác Châu phải trả mỗi tháng được tính theo công thức $x = \\frac{%s}{y} + %sr$.' % (von_tr, von_tr)
    loigiai_nb_1 = """Tiền gốc hằng tháng là $\\frac{%s}{y}$ (triệu đồng), lãi suất tháng là $\\frac{r}{12}$ nên tiền lãi hằng tháng là $%s \\cdot \\frac{r}{12} = %sr$ (triệu đồng). Vậy $x = \\frac{%s}{y} + %sr$.""" % (
        von_tr, von_tr, von_chia_12, von_tr, von_chia_12
    )
    
    th_da_1_d = '\\True Công thức biểu thị lãi suất năm $r$ theo $x$ và $y$ là $r = \\frac{xy - %s}{%sy}$.' % (von_tr, von_chia_12)
    th_da_1_s = 'Công thức biểu thị lãi suất năm $r$ theo $x$ và $y$ là $r = \\frac{xy + %s}{%sy}$.' % (von_tr, von_chia_12)
    loigiai_th_1 = """Từ $x = \\frac{%s}{y} + %sr \\Rightarrow %sr = x - \\frac{%s}{y} = \\frac{xy - %s}{y} \\Rightarrow r = \\frac{xy - %s}{%sy}$.""" % (
        von_tr, von_chia_12, von_chia_12, von_tr, von_tr, von_tr, von_chia_12
    )
    
    vd_da_1_d = '\\True Nếu trả góp mỗi tháng $%s$ triệu đồng trong vòng $4$ năm ($48$ tháng) thì lãi suất năm của khoản vay này là $%s\\%%$.' % (latex(x1), r1_pct)
    vd_da_1_s = 'Nếu trả góp mỗi tháng $%s$ triệu đồng trong vòng $4$ năm ($48$ tháng) thì lãi suất năm của khoản vay này là $%s\\%%$.' % (latex(x1), r1_pct + 2)
    loigiai_vd_1 = """Thay $x = %s, y = 48$ vào công thức tính $r$, ta được $r = \\frac{%s \\cdot 48 - %s}{%s \\cdot 48} = %s = %s\\%%$.""" % (
        latex(x1), latex(x1), von_tr, von_chia_12, float(r1_dec), r1_pct
    )
    
    vdc_da_1_d = '\\True Nếu mỗi tháng bác Châu trả $%s$ triệu đồng trong $10$ năm ($120$ tháng) thì tổng số tiền thực tế bác phải trả chênh lệch $%s$ triệu đồng so với khoản vay ban đầu.' % (x2, chenh_lech)
    vdc_da_1_s = 'Nếu mỗi tháng bác Châu trả $%s$ triệu đồng trong $10$ năm ($120$ tháng) thì tổng số tiền thực tế bác phải trả chênh lệch $%s$ triệu đồng so với khoản vay ban đầu.' % (x2, chenh_lech - 100)
    loigiai_vdc_1 = """Tổng số tiền bác Châu phải trả trong $10$ năm ($120$ tháng) là $%s \\cdot 120 = %s$ (triệu đồng), chênh lệch so với khoản vay ban đầu là $%s - %s = %s$ (triệu đồng).""" % (
        x2, x2 * y2, x2 * y2, von_tr, chenh_lech
    )
    
    while True:
        nb_da_1 = random.choice([nb_da_1_d, nb_da_1_s])
        th_da_1 = random.choice([th_da_1_d, th_da_1_s])
        vd_da_1 = random.choice([vd_da_1_d, vd_da_1_s])
        vdc_da_1 = random.choice([vdc_da_1_d, vdc_da_1_s])
        answers = [nb_da_1, th_da_1, vd_da_1, vdc_da_1]
        if 1 <= sum('\\True' in ans for ans in answers) <= 3:
            break
            
    noidungcauhoi = ("""Bác Châu vay ngân hàng $%s$ tỉ đồng ($%s$ triệu đồng) để mua nhà theo hình thức trả góp. Số tiền bác Châu phải trả mỗi tháng bao gồm tiền gốc hằng tháng (bằng số tiền gốc chia đều cho số tháng vay) và tiền lãi hằng tháng (bằng số tiền gốc nhân với lãi suất tháng). Gọi $r$ là lãi suất năm (viết dưới dạng số thập phân), $x$ (triệu đồng) là số tiền phải trả mỗi tháng và $y$ (tháng) là số tháng vay. Xét tính đúng sai của các khẳng định sau:"""
                     % (str(von_ty).replace('.', '{,}'), von_tr))
                     
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' + str(noidungcauhoi) + '\n' +
               '\\choiceTFn \n' +
               '{' + str(nb_da_1) + '}\n' +
               '{' + str(th_da_1) + '}\n' +
               '{' + str(vd_da_1) + '}\n' +
               '{' + str(vdc_da_1) + '}\n' +
               '\\loigiai{ \n' +
               '\\begin{enumEX}[a)]{1} \n' +
               '\\item ' + str(loigiai_nb_1) + '\n' +
               '\\item ' + str(loigiai_th_1) + '\n' +
               '\\item ' + str(loigiai_vd_1) + '\n' +
               '\\item ' + str(loigiai_vdc_1) + '\n' +
               '\\end{enumEX}} \n' +
               '\\end{ex}\n \\end{minipage}\n\n')
    return content
