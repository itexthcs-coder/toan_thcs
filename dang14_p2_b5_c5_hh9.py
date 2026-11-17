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


def bt_dang14_p2_b5_c5_hh9(self):
    def fmt(val):
        return str(val).replace('.', ',')

    k = random.randint(1, 3)
    R = 5 * k
    kc_tam = 6 * k
    nua_day = 4 * k
    day_chung = 8 * k

    tikz_code = (
"""\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (O1) at (0,0);
\\coordinate (O2) at (2.3,0);
\\coordinate (O3) at (4.6,0);
\\coordinate (O4) at (1.15,-1.0);
\\coordinate (O5) at (3.45,-1.0);
\\draw[line width=1pt] (O1) circle (1cm);
\\draw[line width=1pt] (O2) circle (1cm);
\\draw[line width=1pt] (O3) circle (1cm);
\\draw[line width=1pt] (O4) circle (1cm);
\\draw[line width=1pt] (O5) circle (1cm);
\\fill (O1) circle (1pt) node[above] {$O_1$};
\\fill (O2) circle (1pt) node[above] {$O_2$};
\\fill (O3) circle (1pt) node[above] {$O_3$};
\\fill (O4) circle (1pt) node[below] {$O_4$};
\\fill (O5) circle (1pt) node[below] {$O_5$};
\\end{tikzpicture}
\\end{center}"""
    )

    noidungcauhoi = ("""Biểu tượng Thế vận hội Olympic gồm $5$ vòng tròn bằng nhau bán kính $R = %s\\text{ cm}$ đan xen vào nhau, chia làm hai hàng: hàng trên gồm $3$ vòng tròn tâm $O_1$ (Xanh dương), $O_2$ (Đen), $O_3$ (Đỏ) thẳng hàng và nằm ngoài nhau; hàng dưới gồm $2$ vòng tròn tâm $O_4$ (Vàng), $O_5$ (Xanh lục) thẳng hàng và nằm ngoài nhau. Mỗi vòng tròn hàng dưới đều cắt hai vòng tròn liền kề ở hàng trên.
%s""" % (fmt(R), tikz_code))

    # Nhận biết
    nb_da_1_d = '\\True Khoảng cách giữa tâm $O_1$ (Xanh dương) và tâm $O_2$ (Đen) phải lớn hơn $%s\\text{ cm}$' % (fmt(2 * R))
    nb_da_1_s = 'Khoảng cách giữa tâm $O_1$ (Xanh dương) và tâm $O_2$ (Đen) phải bằng $%s\\text{ cm}$' % (fmt(2 * R))
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]

    loigiai_nb_1 = ("""Vì hai vòng tròn $(O_1; R)$ và $(O_2; R)$ nằm ngoài nhau nên khoảng cách giữa hai tâm thỏa mãn $O_1O_2 > R + R = %s + %s = %s\\text{ cm}$.""" % (fmt(R), fmt(R), fmt(2 * R)))

    # Thông hiểu
    th_da_1_d = '\\True Khoảng cách giữa tâm $O_4$ (Vàng) và tâm $O_2$ (Đen) phải nhỏ hơn $%s\\text{ cm}$' % (fmt(2 * R))
    th_da_1_s = 'Khoảng cách giữa tâm $O_4$ (Vàng) và tâm $O_2$ (Đen) phải lớn hơn $%s\\text{ cm}$' % (fmt(2 * R))
    list_th_da_1 = [th_da_1_d, th_da_1_s]

    loigiai_th_1 = ("""Vì vòng tròn $(O_4; R)$ cắt vòng tròn $(O_2; R)$ nên $0 < O_2O_4 < R + R = %s\\text{ cm}$.""" % (fmt(2 * R)))

    # Vận dụng
    vd_da_1_d = '\\True Vòng tròn $(O_1)$ (Xanh dương) và vòng tròn $(O_5)$ (Xanh lục) là hai đường tròn nằm ngoài nhau'
    vd_da_1_s = 'Vòng tròn $(O_1)$ (Xanh dương) và vòng tròn $(O_5)$ (Xanh lục) là hai đường tròn tiếp xúc ngoài'
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]

    loigiai_vd_1 = ("""Trong biểu tượng chuẩn Olympic, vòng tròn Xanh dương $(O_1)$ nằm ngoài cùng bên trái và vòng tròn Xanh lục $(O_5)$ nằm lệch hẳn về phía bên phải, không có điểm chung nào nên chúng là hai đường tròn nằm ngoài nhau.""")

    # Vận dụng cao
    vdc_da_1_d = '\\True Nếu khoảng cách giữa tâm $O_4$ (Vàng) và tâm $O_1$ (Xanh dương) là $%s\\text{ cm}$ thì độ dài dây cung chung của hai vòng tròn này bằng $%s\\text{ cm}$' % (fmt(kc_tam), fmt(day_chung))
    vdc_da_1_s = 'Nếu khoảng cách giữa tâm $O_4$ (Vàng) và tâm $O_1$ (Xanh dương) là $%s\\text{ cm}$ thì độ dài dây cung chung của hai vòng tròn này bằng $%s\\text{ cm}$' % (fmt(kc_tam), fmt(nua_day))
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]

    loigiai_vdc_1 = ("""Hai đường tròn $(O_1; %s\\text{ cm})$ và $(O_4; %s\\text{ cm})$ bằng nhau nên đường nối tâm $O_1O_4$ cắt dây chung tại trung điểm $H$ của cả hai đoạn. Ta có $O_1H = \\frac{O_1O_4}{2} = %s\\text{ cm}$. \\\\ Nửa độ dài dây cung chung bằng $\\sqrt{R^2 - O_1H^2} = \\sqrt{%s^2 - %s^2} = %s\\text{ cm}$. Vậy độ dài dây cung chung bằng $2 \\cdot %s = %s\\text{ cm}$.""" % (fmt(R), fmt(R), fmt(kc_tam // 2), fmt(R), fmt(kc_tam // 2), fmt(nua_day), fmt(nua_day), fmt(day_chung)))

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
