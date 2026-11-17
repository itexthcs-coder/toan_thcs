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

def bt_dang18_p2_b2_c5_hh9(self):
    R = random.choice([50, 60, 70, 80])
    dk = 2 * R
    rong = dk - 5
    dai = dk + 10

    noidungcauhoi = ('''Một xưởng mộc cần cắt một mặt bàn hình tròn tâm $O$, bán kính $R = %s\\text{ cm}$ từ một tấm gỗ hình chữ nhật có chiều rộng $%s\\text{ cm}$ và chiều dài $%s\\text{ cm}$. Trên mặt bàn tròn này, người thợ dự định gắn một thanh nẹp thẳng dài $%s\\sqrt{2}\\text{ cm}$ nối hai điểm $A, B$ nằm trên mép bàn (như hình vẽ).
    \\begin{center}
    \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
    \\coordinate (O) at (0,0);
    \\coordinate (A) at (45:1.8);
    \\coordinate (B) at (135:1.8);
    \\draw[line width=1pt] (O) circle (1.8);
    \\draw[line width=1pt] (A)--(B);
    \\draw[line width=1pt, dashed] (O)--(A) (O)--(B);
    \\fill (O) circle (1pt) node[below] {$O$};
    \\fill (A) circle (1pt) node[above right] {$A$};
    \\fill (B) circle (1pt) node[above left] {$B$};
    \\end{tikzpicture}
    \\end{center}''' % (R, rong, dai, R))

    nb_da_1_d = '\\True Độ dài dây cung lớn nhất của mặt bàn hình tròn là $%s\\text{ cm}$' % (dk)
    nb_da_1_s = 'Độ dài dây cung lớn nhất của mặt bàn hình tròn là $%s\\text{ cm}$' % (R)
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    loigiai_nb_1 = ('''Đường kính mặt bàn hình tròn là $2R = 2 \\cdot %s = %s\\text{ cm}$, đây chính là độ dài dây cung lớn nhất của mặt bàn.''' % (R, dk))
    list_nb_2 = [loigiai_nb_1]

    th_da_1_d = '\\True Tấm gỗ hình chữ nhật nói trên không đủ kích thước để cắt nguyên vẹn mặt bàn hình tròn bán kính $%s\\text{ cm}$' % (R)
    th_da_1_s = 'Tấm gỗ hình chữ nhật nói trên đủ kích thước để cắt nguyên vẹn mặt bàn hình tròn bán kính $%s\\text{ cm}$' % (R)
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    loigiai_th_1 = ('''Để cắt nguyên vẹn mặt bàn hình tròn có đường kính $%s\\text{ cm}$, cả chiều dài và chiều rộng của tấm gỗ đều phải không nhỏ hơn $%s\\text{ cm}$. \\\\ Vì chiều rộng tấm gỗ là $%s\\text{ cm} < %s\\text{ cm}$ nên không đủ kích thước để cắt nguyên vẹn mặt bàn.''' % (dk, dk, rong, dk))
    list_th_2 = [loigiai_th_1]

    vd_da_1_d = '\\True Góc ở tâm $\\widehat{AOB}$ tạo bởi hai đầu thanh nẹp có số đo bằng $90^\\circ$'
    vd_da_1_s = 'Góc ở tâm $\\widehat{AOB}$ tạo bởi hai đầu thanh nẹp có số đo bằng $60^\\circ$'
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    loigiai_vd_1 = ('''Xét tam giác $OAB$ có $OA^2 + OB^2 = %s^2 + %s^2 = 2 \\cdot %s^2 = (%s\\sqrt{2})^2 = AB^2$. \\\\ Theo định lí Pythagore đảo, tam giác $OAB$ vuông tại $O$, do đó $\\widehat{AOB} = 90^\\circ$.''' % (R, R, R, R))
    list_vd_2 = [loigiai_vd_1]

    vdc_da_1_d = '\\True Phần mép bàn cong nhỏ giới hạn bởi hai đầu thanh nẹp là một cung tròn có số đo bằng $90^\\circ$'
    vdc_da_1_s = 'Phần mép bàn cong nhỏ giới hạn bởi hai đầu thanh nẹp là một cung tròn có số đo bằng $270^\\circ$'
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    loigiai_vdc_1 = ('''Góc ở tâm $\\widehat{AOB} = 90^\\circ$ chắn cung nhỏ $\\overparen{AB}$ nên phần mép bàn cong nhỏ giới hạn bởi hai đầu thanh nẹp có số đo bằng $90^\\circ$ (còn $270^\\circ$ là số đo cung lớn).''')
    list_vdc_2 = [loigiai_vdc_1]

    def count_true_answers(answers):
        return sum('\\True' in ans for ans in answers)

    while True:
        nb_da_1 = random.choice(list_nb_da_1)
        th_da_1 = random.choice(list_th_da_1)
        vd_da_1 = random.choice(list_vd_da_1)
        vdc_da_1 = random.choice(list_vdc_da_1)
        answers = [nb_da_1, th_da_1, vd_da_1, vdc_da_1]
        true_count = count_true_answers(answers)
        if 1 <= true_count <= 3:
            break

    list_nb_1 = [nb_da_1]
    list_th_1 = [th_da_1]
    list_vd_1 = [vd_da_1]
    list_vdc_1 = [vdc_da_1]

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
