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

def bt_dang8_p2_b4_c5_hh9(self):
    def fmt_num(val):
        if isinstance(val, int) or (isinstance(val, float) and val.is_integer()):
            return str(int(val))
        s = ("%.6f" % val).rstrip("0").rstrip(".")
        return s.replace(".", ",")

    def count_true_answers(answers):
        return sum('\\True' in ans for ans in answers)
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)

    if dang == '1':
        # Dạng 8: Vị trí tương đối của cạnh tam giác đều với các đường tròn tâm tại đỉnh và trung điểm cạnh
        bo_so = [
            (4, 4, 3),
            (8, 7, 6),
            (12, 11, 10),
            (16, 14, 13)
        ]
        canh, R_lon, R_nho = random.choice(bo_so)
        nua_canh = canh // 2
        k_ah = canh // 2
        k_mk = canh // 4
        ah_sq = 3 * k_ah * k_ah
        R_lon_sq = R_lon * R_lon
        R_nho_sq = R_nho * R_nho
        r_mk_str = "\\sqrt{3}" if k_mk == 1 else "%s\\sqrt{3}" % fmt_num(k_mk)

        hinh_ve = (
            "\\begin{center}\n"
            "\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n"
            "\\coordinate (B) at (-1.6,0);\n"
            "\\coordinate (C) at (1.6,0);\n"
            "\\coordinate (A) at (0,2.771);\n"
            "\\coordinate (H) at (0,0);\n"
            "\\coordinate (M) at (-0.8,1.386);\n"
            "\\coordinate (K) at (-0.8,0);\n"
            "\\draw[line width=1pt] (A)--(B)--(C)--cycle;\n"
            "\\draw[line width=1pt] (A)--(H);\n"
            "\\draw[line width=1pt] (M) circle (1.386);\n"
            "\\draw[line width=1pt, dashed] (M)--(K);\n"
            "\\draw[line width=1pt] (0,0.2)--(0.2,0.2)--(0.2,0);\n"
            "\\draw[line width=1pt] (-0.8,0.2)--(-0.6,0.2)--(-0.6,0);\n"
            "\\fill (A) circle (1pt) node[above] {$A$};\n"
            "\\fill (B) circle (1pt) node[below left] {$B$};\n"
            "\\fill (C) circle (1pt) node[below right] {$C$};\n"
            "\\fill (H) circle (1pt) node[below] {$H$};\n"
            "\\fill (M) circle (1pt) node[above left] {$M$};\n"
            "\\fill (K) circle (1pt) node[below] {$K$};\n"
            "\\end{tikzpicture}\n"
            "\\end{center}"
        )

        noidungcauhoi = (
            '''Cho tam giác đều $ABC$ cạnh $%s\\text{ cm}$, đường cao $AH$ ($H \\in BC$). Xét vị trí tương đối của đường thẳng $BC$ với các đường tròn tâm $A$ và tâm $M$ ($M$ là trung điểm của $AB$).\n%s'''
            % (fmt_num(canh), hinh_ve)
        )

        # Nhận biết
        nb_da_1_d = '\\True Độ dài đường cao $AH$ bằng $%s\\sqrt{3}\\text{ cm}$' % (fmt_num(k_ah))
        nb_da_1_s = 'Độ dài đường cao $AH$ bằng $%s\\sqrt{2}\\text{ cm}$' % (fmt_num(k_ah))
        list_nb_da_1 = [nb_da_1_d, nb_da_1_s]

        loigiai_nb_1_d = (
            '''Đúng. Trong tam giác đều $ABC$ cạnh $%s\\text{ cm}$, đường cao $AH$ đồng thời là đường trung tuyến nên $BH = \\frac{BC}{2} = \\frac{%s}{2} = %s\\text{ cm}$. \\\\ Áp dụng định lí Pythagore vào tam giác $ABH$ vuông tại $H$, ta có: $AH = \\sqrt{AB^2 - BH^2} = \\sqrt{%s^2 - %s^2} = \\sqrt{%s} = %s\\sqrt{3}\\text{ cm}$.'''
            % (fmt_num(canh), fmt_num(canh), fmt_num(nua_canh), fmt_num(canh), fmt_num(nua_canh), fmt_num(ah_sq), fmt_num(k_ah))
        )
        loigiai_nb_1_s = (
            '''Sai. Trong tam giác đều $ABC$, ta có $BH = \\frac{BC}{2} = %s\\text{ cm}$. \\\\ Áp dụng định lí Pythagore vào tam giác $ABH$ vuông tại $H$, ta có: $AH = \\sqrt{%s^2 - %s^2} = \\sqrt{%s} = %s\\sqrt{3}\\text{ cm}$ (khác $%s\\sqrt{2}\\text{ cm}$).'''
            % (fmt_num(nua_canh), fmt_num(canh), fmt_num(nua_canh), fmt_num(ah_sq), fmt_num(k_ah), fmt_num(k_ah))
        )

        # Thông hiểu
        th_da_1_d = '\\True Đường tròn $(A; %s\\text{ cm})$ cắt đường thẳng $BC$ tại hai điểm phân biệt' % (fmt_num(R_lon))
        th_da_1_s = 'Đường tròn $(A; %s\\text{ cm})$ không giao nhau với đường thẳng $BC$' % (fmt_num(R_lon))
        list_th_da_1 = [th_da_1_d, th_da_1_s]

        loigiai_th_1_d = (
            '''Đúng. Khoảng cách từ tâm $A$ đến đường thẳng $BC$ là $d = AH = %s\\sqrt{3} = \\sqrt{%s}\\text{ cm}$. \\\\ Vì $%s = \\sqrt{%s}$ và $\\sqrt{%s} < \\sqrt{%s}$ nên $d < R$. Do đó đường tròn $(A; %s\\text{ cm})$ cắt đường thẳng $BC$ tại hai điểm phân biệt.'''
            % (fmt_num(k_ah), fmt_num(ah_sq), fmt_num(R_lon), fmt_num(R_lon_sq), fmt_num(ah_sq), fmt_num(R_lon_sq), fmt_num(R_lon))
        )
        loigiai_th_1_s = (
            '''Sai. Khoảng cách từ tâm $A$ đến đường thẳng $BC$ là $d = AH = \\sqrt{%s}\\text{ cm} < %s = \\sqrt{%s}\\text{ cm}$. Vì $d < R$ nên đường tròn $(A; %s\\text{ cm})$ cắt đường thẳng $BC$ tại hai điểm phân biệt.'''
            % (fmt_num(ah_sq), fmt_num(R_lon), fmt_num(R_lon_sq), fmt_num(R_lon))
        )

        # Vận dụng
        vd_da_1_d = '\\True Đường tròn $(A; %s\\text{ cm})$ không giao nhau với đường thẳng $BC$' % (fmt_num(R_nho))
        vd_da_1_s = 'Đường tròn $(A; %s\\text{ cm})$ tiếp xúc với đường thẳng $BC$' % (fmt_num(R_nho))
        list_vd_da_1 = [vd_da_1_d, vd_da_1_s]

        loigiai_vd_1_d = (
            '''Đúng. Khoảng cách từ tâm $A$ đến đường thẳng $BC$ là $d = AH = \\sqrt{%s}\\text{ cm}$, còn bán kính đường tròn là $R = %s = \\sqrt{%s}\\text{ cm}$. \\\\ Vì $\\sqrt{%s} > \\sqrt{%s}$ nên $d > R$. Vậy đường tròn $(A; %s\\text{ cm})$ không giao nhau với đường thẳng $BC$.'''
            % (fmt_num(ah_sq), fmt_num(R_nho), fmt_num(R_nho_sq), fmt_num(ah_sq), fmt_num(R_nho_sq), fmt_num(R_nho))
        )
        loigiai_vd_1_s = (
            '''Sai. Khoảng cách từ $A$ đến $BC$ là $d = \\sqrt{%s}\\text{ cm} > %s = \\sqrt{%s}\\text{ cm}$. Vì $d > R$ nên đường tròn $(A; %s\\text{ cm})$ không giao nhau với đường thẳng $BC$, không phải tiếp xúc.'''
            % (fmt_num(ah_sq), fmt_num(R_nho), fmt_num(R_nho_sq), fmt_num(R_nho))
        )

        # Vận dụng cao
        vdc_da_1_d = '\\True Đường tròn $(M; %s\\text{ cm})$ tiếp xúc với đường thẳng $BC$' % (r_mk_str)
        vdc_da_1_s = 'Đường tròn $(M; %s\\text{ cm})$ cắt đường thẳng $BC$ tại hai điểm phân biệt' % (r_mk_str)
        list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]

        loigiai_vdc_1_d = (
            '''Đúng. Kẻ $MK \\perp BC$ tại $K$. Vì $MK // AH$ (cùng vuông góc với $BC$) và $M$ là trung điểm của $AB$ nên $MK$ là đường trung bình của tam giác $ABH$. \\\\ Suy ra khoảng cách từ tâm $M$ đến đường thẳng $BC$ là $MK = \\frac{1}{2}AH = \\frac{%s\\sqrt{3}}{2} = %s\\text{ cm} = R$. \\\\ Vậy đường tròn $(M; %s\\text{ cm})$ tiếp xúc với đường thẳng $BC$ tại $K$.'''
            % (fmt_num(k_ah), r_mk_str, r_mk_str)
        )
        loigiai_vdc_1_s = (
            '''Sai. Kẻ $MK \\perp BC$ tại $K$, khi đó $MK$ là đường trung bình của tam giác $ABH$ nên $MK = \\frac{1}{2}AH = %s\\text{ cm}$ bằng đúng bán kính đường tròn. Do đó đường tròn $(M; %s\\text{ cm})$ tiếp xúc với $BC$ tại $K$, không cắt $BC$ tại hai điểm.'''
            % (r_mk_str, r_mk_str)
        )

        while True:
            nb_da_1 = random.choice(list_nb_da_1)
            th_da_1 = random.choice(list_th_da_1)
            vd_da_1 = random.choice(list_vd_da_1)
            vdc_da_1 = random.choice(list_vdc_da_1)

            answers = [nb_da_1, th_da_1, vd_da_1, vdc_da_1]
            true_count = count_true_answers(answers)
            if 1 <= true_count <= 3:
                break

        loigiai_nb_1 = loigiai_nb_1_d if nb_da_1 == nb_da_1_d else loigiai_nb_1_s
        loigiai_th_1 = loigiai_th_1_d if th_da_1 == th_da_1_d else loigiai_th_1_s
        loigiai_vd_1 = loigiai_vd_1_d if vd_da_1 == vd_da_1_d else loigiai_vd_1_s
        loigiai_vdc_1 = loigiai_vdc_1_d if vdc_da_1 == vdc_da_1_d else loigiai_vdc_1_s

        list_nb_1 = [nb_da_1]
        list_th_1 = [th_da_1]
        list_vd_1 = [vd_da_1]
        list_vdc_1 = [vdc_da_1]

        list_nb_2 = [loigiai_nb_1]
        list_th_2 = [loigiai_th_1]
        list_vd_2 = [loigiai_vd_1]
        list_vdc_2 = [loigiai_vdc_1]

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

    # Xuất câu trắc nghiệm đúng sai
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n\\choiceTFn \n' +
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
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
