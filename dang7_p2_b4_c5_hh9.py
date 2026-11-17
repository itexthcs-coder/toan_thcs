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

def bt_dang7_p2_b4_c5_hh9(self):
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
        # Dạng 7: Đường tròn tiếp xúc với bốn cạnh của hình thoi
        bo_so = [
            (6, 8, 10),
            (3, 4, 5),
            (12, 16, 20),
            (9, 12, 15),
            (15, 20, 25),
            (18, 24, 30)
        ]
        OA, OB, canh = random.choice(bo_so)
        AC = 2 * OA
        BD = 2 * OB
        BD_sai = BD + 2
        OH = round((OA * OB) / canh, 4)
        OH_sq = round(OH * OH, 6)
        R_lon = round(OH + 0.5, 4)

        hinh_ve = (
            "\\begin{center}\n"
            "\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n"
            "\\coordinate (O) at (0,0);\n"
            "\\coordinate (A) at (-1.5,0);\n"
            "\\coordinate (C) at (1.5,0);\n"
            "\\coordinate (B) at (0,2.0);\n"
            "\\coordinate (D) at (0,-2.0);\n"
            "\\coordinate (H) at (-0.96,1.28);\n"
            "\\draw[line width=1pt] (A)--(B)--(C)--(D)--cycle;\n"
            "\\draw[line width=1pt] (A)--(C) (B)--(D);\n"
            "\\draw[line width=1pt] (O) circle (1.2);\n"
            "\\draw[line width=1pt, dashed] (O)--(H);\n"
            "\\fill (O) circle (1pt) node[below right] {$O$};\n"
            "\\fill (A) circle (1pt) node[left] {$A$};\n"
            "\\fill (C) circle (1pt) node[right] {$C$};\n"
            "\\fill (B) circle (1pt) node[above] {$B$};\n"
            "\\fill (D) circle (1pt) node[below] {$D$};\n"
            "\\fill (H) circle (1pt) node[above left] {$H$};\n"
            "\\end{tikzpicture}\n"
            "\\end{center}"
        )

        noidungcauhoi = (
            '''Cho hình thoi $ABCD$ có cạnh bằng $%s\\text{ cm}$ và đường chéo $AC = %s\\text{ cm}$. Gọi $O$ là giao điểm của hai đường chéo $AC$ và $BD$.\n%s'''
            % (fmt_num(canh), fmt_num(AC), hinh_ve)
        )

        # Nhận biết
        nb_da_1_d = '\\True Độ dài đường chéo $BD$ bằng $%s\\text{ cm}$' % (fmt_num(BD))
        nb_da_1_s = 'Độ dài đường chéo $BD$ bằng $%s\\text{ cm}$' % (fmt_num(BD_sai))
        list_nb_da_1 = [nb_da_1_d, nb_da_1_s]

        loigiai_nb_1_d = (
            '''Đúng. Trong hình thoi $ABCD$, hai đường chéo $AC$ và $BD$ vuông góc với nhau tại trung điểm $O$ của mỗi đường. \\\\ Ta có $OA = \\frac{AC}{2} = \\frac{%s}{2} = %s\\text{ cm}$. \\\\ Áp dụng định lí Pythagore vào tam giác $OAB$ vuông tại $O$, ta có: $OB = \\sqrt{AB^2 - OA^2} = \\sqrt{%s^2 - %s^2} = %s\\text{ cm}$. \\\\ Vậy độ dài đường chéo $BD = 2 \\cdot OB = 2 \\cdot %s = %s\\text{ cm}$.'''
            % (fmt_num(AC), fmt_num(OA), fmt_num(canh), fmt_num(OA), fmt_num(OB), fmt_num(OB), fmt_num(BD))
        )
        loigiai_nb_1_s = (
            '''Sai. Trong hình thoi $ABCD$, ta có $OA = \\frac{AC}{2} = %s\\text{ cm}$ và $AC \\perp BD$ tại $O$. \\\\ Áp dụng định lí Pythagore vào tam giác $OAB$ vuông tại $O$, ta có $OB = \\sqrt{%s^2 - %s^2} = %s\\text{ cm}$, suy ra $BD = 2 \\cdot OB = %s\\text{ cm}$ (khác $%s\\text{ cm}$).'''
            % (fmt_num(OA), fmt_num(canh), fmt_num(OA), fmt_num(OB), fmt_num(BD), fmt_num(BD_sai))
        )

        # Thông hiểu
        th_da_1_d = '\\True Khoảng cách từ $O$ đến bốn cạnh của hình thoi đều bằng nhau và bằng $%s\\text{ cm}$' % (fmt_num(OH))
        th_da_1_s = 'Khoảng cách từ $O$ đến bốn cạnh của hình thoi đều bằng nhau và bằng $%s\\text{ cm}$' % (fmt_num(R_lon))
        list_th_da_1 = [th_da_1_d, th_da_1_s]

        loigiai_th_1_d = (
            '''Đúng. Kẻ đường cao $OH$ của tam giác $OAB$ vuông tại $O$ ($H \\in AB$). Ta có $OH \\cdot AB = OA \\cdot OB \\Rightarrow OH = \\frac{OA \\cdot OB}{AB} = \\frac{%s \\cdot %s}{%s} = %s\\text{ cm}$. \\\\ Vì giao điểm $O$ của hai đường chéo hình thoi nằm trên các đường phân giác của bốn góc hình thoi nên $O$ cách đều cả bốn cạnh của hình thoi một khoảng bằng $%s\\text{ cm}$.'''
            % (fmt_num(OA), fmt_num(OB), fmt_num(canh), fmt_num(OH), fmt_num(OH))
        )
        loigiai_th_1_s = (
            '''Sai. Kẻ đường cao $OH$ của tam giác $OAB$ vuông tại $O$, ta tính được $OH = \\frac{OA \\cdot OB}{AB} = \\frac{%s \\cdot %s}{%s} = %s\\text{ cm}$. Vì $O$ cách đều bốn cạnh của hình thoi nên khoảng cách từ $O$ đến mỗi cạnh là $%s\\text{ cm}$ (khác $%s\\text{ cm}$).'''
            % (fmt_num(OA), fmt_num(OB), fmt_num(canh), fmt_num(OH), fmt_num(OH), fmt_num(R_lon))
        )

        # Vận dụng
        vd_da_1_d = '\\True Đường tròn $(O; %s\\text{ cm})$ nhận cả bốn đường thẳng $AB$, $BC$, $CD$, $DA$ làm tiếp tuyến' % (fmt_num(OH))
        vd_da_1_s = 'Đường tròn $(O; %s\\text{ cm})$ tiếp xúc với cả bốn cạnh của hình thoi $ABCD$' % (fmt_num(R_lon))
        list_vd_da_1 = [vd_da_1_d, vd_da_1_s]

        loigiai_vd_1_d = (
            '''Đúng. Vì khoảng cách từ tâm $O$ đến cả bốn đường thẳng $AB$, $BC$, $CD$, $DA$ đều bằng $%s\\text{ cm} = R$ nên đường tròn $(O; %s\\text{ cm})$ tiếp xúc với cả bốn đường thẳng đó, tức là nhận cả bốn đường thẳng làm tiếp tuyến.'''
            % (fmt_num(OH), fmt_num(OH))
        )
        loigiai_vd_1_s = (
            '''Sai. Khoảng cách từ tâm $O$ đến mỗi cạnh của hình thoi là $d = %s\\text{ cm} < R = %s\\text{ cm}$ nên đường tròn $(O; %s\\text{ cm})$ cắt mỗi đường thẳng chứa cạnh của hình thoi tại hai điểm phân biệt, không phải tiếp xúc.'''
            % (fmt_num(OH), fmt_num(R_lon), fmt_num(R_lon))
        )

        # Vận dụng cao
        vdc_da_1_d = '\\True Nếu đường tròn $(O; %s\\text{ cm})$ tiếp xúc với $AB$ tại $H$ thì $HA \\cdot HB = %s\\text{ cm}^2$' % (fmt_num(OH), fmt_num(OH_sq))
        vdc_da_1_s = 'Nếu đường tròn $(O; %s\\text{ cm})$ tiếp xúc với $AB$ tại $H$ thì $H$ là trung điểm của $AB$' % (fmt_num(OH))
        list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]

        loigiai_vdc_1_d = (
            '''Đúng. Khi đường tròn $(O; %s\\text{ cm})$ tiếp xúc với $AB$ tại $H$ thì $OH \\perp AB$ tại $H$ và $OH = %s\\text{ cm}$. \\\\ Trong tam giác $OAB$ vuông tại $O$ có đường cao $OH$, ta có $HA \\cdot HB = OH^2 = (%s)^2 = %s\\text{ cm}^2$.'''
            % (fmt_num(OH), fmt_num(OH), fmt_num(OH), fmt_num(OH_sq))
        )
        loigiai_vdc_1_s = (
            '''Sai. Khi đường tròn $(O; %s\\text{ cm})$ tiếp xúc với $AB$ tại $H$ thì $OH$ là đường cao của tam giác vuông $OAB$. Vì $OA = %s\\text{ cm} \\neq OB = %s\\text{ cm}$ nên tam giác $OAB$ không cân tại $O$, do đó chân đường cao $H$ không trùng với trung điểm của $AB$.'''
            % (fmt_num(OH), fmt_num(OA), fmt_num(OB))
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
