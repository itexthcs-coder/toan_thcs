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

def bt_dang3_p2_b4_c5_hh9(self):
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
        # Dạng 3: Chứng minh đường thẳng là tiếp tuyến của đường tròn đường kính là cạnh bên hình thang vuông
        bo_so = [
            (4, 9, 12, 13),
            (6, 11, 12, 13),
            (5, 15, 24, 26),
            (7, 17, 24, 26),
            (4, 12, 15, 17),
            (6, 14, 15, 17),
            (3, 9, 8, 10),
            (5, 11, 8, 10)
        ]
        AB, CD, AD, BC = random.choice(bo_so)
        CH = CD - AB
        R = BC / 2
        d_val = (AB + CD) / 2
        BC_sai = BC + 2

        hinh_ve = (
            "\\begin{center}\n"
            "\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n"
            "\\coordinate (A) at (0,2.4);\n"
            "\\coordinate (B) at (1.0,2.4);\n"
            "\\coordinate (D) at (0,0);\n"
            "\\coordinate (C) at (2.4,0);\n"
            "\\coordinate (O) at (1.7,1.2);\n"
            "\\coordinate (M) at (0,1.2);\n"
            "\\coordinate (H) at (1.0,0);\n"
            "\\draw[line width=1pt] (O) circle (1.389);\n"
            "\\draw[line width=1pt] (A)--(B)--(C)--(D)--cycle;\n"
            "\\draw[line width=1pt, dashed] (O)--(M) (B)--(H);\n"
            "\\draw[line width=1pt] (0,2.2)--(0.2,2.2)--(0.2,2.4);\n"
            "\\draw[line width=1pt] (0,0.2)--(0.2,0.2)--(0.2,0);\n"
            "\\draw[line width=1pt] (0,1.4)--(0.2,1.4)--(0.2,1.2);\n"
            "\\draw[line width=1pt] (1.0,0.2)--(1.2,0.2)--(1.2,0);\n"
            "\\fill (A) circle (1pt) node[above left] {$A$};\n"
            "\\fill (B) circle (1pt) node[above right] {$B$};\n"
            "\\fill (C) circle (1pt) node[below right] {$C$};\n"
            "\\fill (D) circle (1pt) node[below left] {$D$};\n"
            "\\fill (O) circle (1pt) node[right] {$O$};\n"
            "\\fill (M) circle (1pt) node[left] {$M$};\n"
            "\\fill (H) circle (1pt) node[below] {$H$};\n"
            "\\end{tikzpicture}\n"
            "\\end{center}"
        )

        noidungcauhoi = (
            '''Cho hình thang vuông $ABCD$ ($\\widehat{A} = \\widehat{D} = 90^\\circ$) có đáy nhỏ $AB = %s\\text{ cm}$, đáy lớn $CD = %s\\text{ cm}$ và cạnh bên $AD = %s\\text{ cm}$. Xét đường tròn tâm $O$ đường kính $BC$.\n%s'''
            % (fmt_num(AB), fmt_num(CD), fmt_num(AD), hinh_ve)
        )

        # Nhận biết
        nb_da_1_d = '\\True Độ dài cạnh bên $BC$ bằng $%s\\text{ cm}$' % (fmt_num(BC))
        nb_da_1_s = 'Độ dài cạnh bên $BC$ bằng $%s\\text{ cm}$' % (fmt_num(BC_sai))
        list_nb_da_1 = [nb_da_1_d, nb_da_1_s]

        loigiai_nb_1_d = (
            '''Đúng. Kẻ $BH \\perp CD$ tại $H$. Tứ giác $ABHD$ có $\\widehat{A} = \\widehat{D} = \\widehat{BHD} = 90^\\circ$ nên là hình chữ nhật, suy ra $DH = AB = %s\\text{ cm}$ và $BH = AD = %s\\text{ cm}$. \\\\ Do đó $CH = CD - DH = %s - %s = %s\\text{ cm}$. \\\\ Áp dụng định lí Pythagore vào tam giác $BHC$ vuông tại $H$, ta có: $BC = \\sqrt{BH^2 + CH^2} = \\sqrt{%s^2 + %s^2} = %s\\text{ cm}$.'''
            % (fmt_num(AB), fmt_num(AD), fmt_num(CD), fmt_num(AB), fmt_num(CH), fmt_num(AD), fmt_num(CH), fmt_num(BC))
        )
        loigiai_nb_1_s = (
            '''Sai. Kẻ $BH \\perp CD$ tại $H$, ta tính được $BH = AD = %s\\text{ cm}$ và $CH = CD - AB = %s - %s = %s\\text{ cm}$. \\\\ Áp dụng định lí Pythagore vào tam giác $BHC$ vuông tại $H$, ta có: $BC = \\sqrt{BH^2 + CH^2} = \\sqrt{%s^2 + %s^2} = %s\\text{ cm}$ (khác $%s\\text{ cm}$).'''
            % (fmt_num(AD), fmt_num(CD), fmt_num(AB), fmt_num(CH), fmt_num(AD), fmt_num(CH), fmt_num(BC), fmt_num(BC_sai))
        )

        # Thông hiểu
        th_da_1_d = '\\True Tâm $O$ của đường tròn đường kính $BC$ cách đường thẳng $AD$ một khoảng bằng $%s\\text{ cm}$' % (fmt_num(d_val))
        th_da_1_s = 'Tâm $O$ của đường tròn đường kính $BC$ cách đường thẳng $AD$ một khoảng bằng $%s\\text{ cm}$' % (fmt_num(AD))
        list_th_da_1 = [th_da_1_d, th_da_1_s]

        loigiai_th_1_d = (
            '''Đúng. Kẻ $OM \\perp AD$ tại $M$. Vì $AB \\perp AD$, $CD \\perp AD$ và $OM \\perp AD$ nên $AB // OM // CD$. \\\\ Lại có $O$ là trung điểm của cạnh bên $BC$ nên $M$ là trung điểm của $AD$, suy ra $OM$ là đường trung bình của hình thang $ABCD$. \\\\ Vậy khoảng cách từ $O$ đến $AD$ là $OM = \\frac{AB + CD}{2} = \\frac{%s + %s}{2} = %s\\text{ cm}$.'''
            % (fmt_num(AB), fmt_num(CD), fmt_num(d_val))
        )
        loigiai_th_1_s = (
            '''Sai. Kẻ $OM \\perp AD$ tại $M$, vì $OM$ là đường trung bình của hình thang $ABCD$ nên khoảng cách từ $O$ đến $AD$ là $OM = \\frac{AB + CD}{2} = \\frac{%s + %s}{2} = %s\\text{ cm}$ (khác $%s\\text{ cm}$).'''
            % (fmt_num(AB), fmt_num(CD), fmt_num(d_val), fmt_num(AD))
        )

        # Vận dụng
        vd_da_1_d = '\\True Đường thẳng $AD$ là tiếp tuyến của đường tròn đường kính $BC$'
        vd_da_1_s = 'Đường thẳng $AD$ cắt đường tròn đường kính $BC$ tại hai điểm phân biệt'
        list_vd_da_1 = [vd_da_1_d, vd_da_1_s]

        loigiai_vd_1_d = (
            '''Đúng. Bán kính của đường tròn đường kính $BC$ là $R = \\frac{BC}{2} = \\frac{%s}{2} = %s\\text{ cm}$. \\\\ Vì khoảng cách từ tâm $O$ đến đường thẳng $AD$ là $OM = %s\\text{ cm} = R$ nên đường thẳng $AD$ tiếp xúc với đường tròn $(O; R)$, tức là đường thẳng $AD$ là tiếp tuyến của đường tròn đường kính $BC$.'''
            % (fmt_num(BC), fmt_num(R), fmt_num(d_val))
        )
        loigiai_vd_1_s = (
            '''Sai. Bán kính của đường tròn đường kính $BC$ là $R = \\frac{BC}{2} = %s\\text{ cm}$, bằng đúng khoảng cách $OM = %s\\text{ cm}$ từ tâm $O$ đến đường thẳng $AD$. Do đó đường thẳng $AD$ tiếp xúc với đường tròn tại một điểm duy nhất, không cắt tại hai điểm.'''
            % (fmt_num(R), fmt_num(d_val))
        )

        # Vận dụng cao
        vdc_da_1_d = '\\True Đường thẳng $CD$ cắt đường tròn đường kính $BC$ tại hai điểm phân biệt'
        vdc_da_1_s = 'Đường thẳng $CD$ không giao nhau với đường tròn đường kính $BC$'
        list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]

        loigiai_vdc_1_d = (
            '''Đúng. Điểm $C$ nằm trên đường tròn đường kính $BC$, đồng thời góc $\\widehat{BCD}$ là góc nhọn (do $\\widehat{BCH} < 90^\\circ$ trong tam giác $BHC$ vuông tại $H$) nên $CD$ không vuông góc với bán kính $OC$. Vì vậy đường thẳng $CD$ cắt đường tròn đường kính $BC$ tại hai điểm phân biệt.'''
        )
        loigiai_vdc_1_s = (
            '''Sai. Đường thẳng $CD$ đi qua điểm $C$ nằm trên đường tròn đường kính $BC$ và không vuông góc với bán kính $OC$ nên đường thẳng $CD$ cắt đường tròn tại hai điểm phân biệt.'''
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
