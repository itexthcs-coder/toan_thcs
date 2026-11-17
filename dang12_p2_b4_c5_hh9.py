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

def bt_dang12_p2_b4_c5_hh9(self):
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
        # Dạng 12: Tiếp tuyến chung của hai đường tròn bằng nhau trong truyền động cơ khí (Dây curoa)
        R = random.choice([8, 10, 12, 15, 18, 20])
        L = random.choice([40, 50, 60, 75, 80])
        L_sai = L - R

        hinh_ve = (
            "\\begin{center}\n"
            "\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n"
            "\\coordinate (O1) at (-1.8,0);\n"
            "\\coordinate (O2) at (1.8,0);\n"
            "\\coordinate (A) at (-1.8,1.0);\n"
            "\\coordinate (B) at (1.8,1.0);\n"
            "\\draw[line width=1pt] (O1) circle (1.0);\n"
            "\\draw[line width=1pt] (O2) circle (1.0);\n"
            "\\draw[line width=1pt] (-1.8,1.0)--(1.8,1.0);\n"
            "\\draw[line width=1pt] (-1.8,-1.0)--(1.8,-1.0);\n"
            "\\draw[line width=1pt] (O1)--(A) (O2)--(B);\n"
            "\\draw[line width=1pt, dashed] (O1)--(O2);\n"
            "\\draw[line width=1pt] (-1.8,0.8)--(-1.6,0.8)--(-1.6,1.0);\n"
            "\\draw[line width=1pt] (1.8,0.8)--(1.6,0.8)--(1.6,1.0);\n"
            "\\fill (O1) circle (1pt) node[below] {$O_1$};\n"
            "\\fill (O2) circle (1pt) node[below] {$O_2$};\n"
            "\\fill (A) circle (1pt) node[above] {$A$};\n"
            "\\fill (B) circle (1pt) node[above] {$B$};\n"
            "\\end{tikzpicture}\n"
            "\\end{center}"
        )

        noidungcauhoi = (
            '''Trong một hệ thống truyền động cơ khí, hai bánh đà hình tròn có cùng bán kính $R = %s\\text{ cm}$ đặt cách nhau một khoảng giữa hai tâm là $O_1O_2 = %s\\text{ cm}$. Một dây curoa căng thẳng tiếp xúc với cả hai bánh đà tại hai tiếp điểm $A \\in (O_1)$ và $B \\in (O_2)$ nằm cùng một phía đối với đường nối tâm $O_1O_2$.\n%s'''
            % (fmt_num(R), fmt_num(L), hinh_ve)
        )

        # Nhận biết
        nb_da_1_d = '\\True Hai bán kính $O_1A$ và $O_2B$ cùng vuông góc với đoạn dây curoa thẳng $AB$'
        nb_da_1_s = 'Hai bán kính $O_1A$ và $O_2B$ tạo với đoạn dây curoa thẳng $AB$ một góc $60^\\circ$'
        list_nb_da_1 = [nb_da_1_d, nb_da_1_s]

        loigiai_nb_1_d = (
            '''Đúng. Vì đường thẳng $AB$ tiếp xúc với đường tròn $(O_1)$ tại $A$ và tiếp xúc với đường tròn $(O_2)$ tại $B$ nên theo tính chất của tiếp tuyến, hai bán kính $O_1A$ và $O_2B$ cùng vuông góc với đoạn dây curoa thẳng $AB$.'''
        )
        loigiai_nb_1_s = (
            '''Sai. Theo tính chất của tiếp tuyến, tiếp tuyến của đường tròn vuông góc với bán kính đi qua tiếp điểm nên $O_1A \\perp AB$ và $O_2B \\perp AB$ (góc tạo bởi chúng bằng $90^\\circ$, không phải $60^\\circ$).'''
        )

        # Thông hiểu
        th_da_1_d = '\\True Khoảng cách từ tâm $O_1$ đến đường thẳng chứa đoạn dây curoa $AB$ bằng $%s\\text{ cm}$' % (fmt_num(R))
        th_da_1_s = 'Khoảng cách từ tâm $O_1$ đến đường thẳng chứa đoạn dây curoa $AB$ bằng $%s\\text{ cm}$' % (fmt_num(2 * R))
        list_th_da_1 = [th_da_1_d, th_da_1_s]

        loigiai_th_1_d = (
            '''Đúng. Vì $O_1A \\perp AB$ tại $A$ nên khoảng cách từ tâm $O_1$ đến đường thẳng $AB$ chính là độ dài bán kính $O_1A = R = %s\\text{ cm}$.'''
            % (fmt_num(R))
        )
        loigiai_th_1_s = (
            '''Sai. Vì đường thẳng $AB$ tiếp xúc với $(O_1; %s\\text{ cm})$ tại $A$ nên $O_1A \\perp AB$ và khoảng cách từ $O_1$ đến $AB$ bằng bán kính $R = %s\\text{ cm}$ (khác $%s\\text{ cm}$).'''
            % (fmt_num(R), fmt_num(R), fmt_num(2 * R))
        )

        # Vận dụng
        vd_da_1_d = '\\True Tứ giác $O_1ABO_2$ là một hình chữ nhật'
        vd_da_1_s = 'Tứ giác $O_1ABO_2$ là một hình thang cân nhưng không phải hình chữ nhật'
        list_vd_da_1 = [vd_da_1_d, vd_da_1_s]

        loigiai_vd_1_d = (
            '''Đúng. Ta có $O_1A \\perp AB$ và $O_2B \\perp AB$ nên $O_1A // O_2B$. \\\\ Lại có $O_1A = O_2B = R = %s\\text{ cm}$ nên tứ giác $O_1ABO_2$ là hình bình hành. \\\\ Hình bình hành $O_1ABO_2$ có một góc vuông ($\\widehat{O_1AB} = 90^\\circ$) nên là một hình chữ nhật.'''
            % (fmt_num(R))
        )
        loigiai_vd_1_s = (
            '''Sai. Vì $O_1A // O_2B$ (cùng vuông góc với $AB$) và $O_1A = O_2B = R$, kết hợp với $\\widehat{O_1AB} = 90^\\circ$ nên tứ giác $O_1ABO_2$ là một hình chữ nhật.'''
        )

        # Vận dụng cao
        vdc_da_1_d = '\\True Độ dài phần dây curoa thẳng $AB$ giữa hai tiếp điểm bằng $%s\\text{ cm}$' % (fmt_num(L))
        vdc_da_1_s = 'Độ dài phần dây curoa thẳng $AB$ giữa hai tiếp điểm bằng $%s\\text{ cm}$' % (fmt_num(L_sai))
        list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]

        loigiai_vdc_1_d = (
            '''Đúng. Vì tứ giác $O_1ABO_2$ là hình chữ nhật nên hai cạnh đối bằng nhau: $AB = O_1O_2 = %s\\text{ cm}$.'''
            % (fmt_num(L))
        )
        loigiai_vdc_1_s = (
            '''Sai. Vì tứ giác $O_1ABO_2$ là hình chữ nhật nên độ dài phần dây curoa thẳng $AB = O_1O_2 = %s\\text{ cm}$ (khác $%s\\text{ cm}$).'''
            % (fmt_num(L), fmt_num(L_sai))
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
