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


def bt_dang11_p2_b1_c10_hh9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        r_nho = random.choice([3, 6])
        r_lon = 2 * r_nho
        h_thang = random.choice([4, 5, 7])
        h_nho = h_thang
        h_lon = 2 * h_thang
        v_nho = ((r_nho ** 2) * h_nho) // 3
        v_lon = ((r_lon ** 2) * h_lon) // 3
        v_cut = v_lon - v_nho

        noidungcauhoi = ('''Cho hình thang vuông $ABCD$ ($\\widehat{A} = \\widehat{D} = 90^\\circ$) có đáy nhỏ $AB = %s\\text{ cm}$, đáy lớn $CD = %s\\text{ cm}$ và cạnh bên $AD = %s\\text{ cm}$. Quay hình thang vuông $ABCD$ một vòng quanh cạnh $AD$ cố định ta được một hình nón cụt (phần còn lại của hình nón lớn đỉnh $S$ khi cắt bỏ đi hình nón nhỏ đỉnh $S$ ở phía trên bởi mặt phẳng song song với đáy, như hình vẽ). Xét tính đúng sai của các khẳng định sau:
\\begin{center}
\\begin{tikzpicture}[scale=0.85, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (S) at (0,3.6);
\\coordinate (A) at (0,1.8);
\\coordinate (B) at (1,1.8);
\\coordinate (D) at (0,0);
\\coordinate (C) at (2,0);
\\draw[line width=1pt] (0,1.8) ellipse (1 and 0.25);
\\draw[line width=1pt] (-2,0) arc (180:360:2 and 0.4);
\\draw[line width=1pt, dashed] (2,0) arc (0:180:2 and 0.4);
\\draw[line width=1pt] (-1,1.8)--(-2,0) (1,1.8)--(2,0);
\\draw[line width=1pt, dashed] (-1,1.8)--(S)--(1,1.8) (S)--(D)--(C) (A)--(B);
\\fill (S) circle (1pt) node[above] {$S$};
\\fill (A) circle (1pt) node[left] {$A$};
\\fill (B) circle (1pt) node[right] {$B$};
\\fill (D) circle (1pt) node[below] {$D$};
\\fill (C) circle (1pt) node[right] {$C$};
\\end{tikzpicture}
\\end{center}'''
                         % (r_nho, r_lon, h_thang))

        nb_da_1_d = '\\True Hình nón lớn ban đầu có bán kính đáy $R = %s\\text{ cm}$ và chiều cao $h_{\\text{lớn}} = %s\\text{ cm}$' % (r_lon, h_lon)
        nb_da_1_s = 'Hình nón lớn ban đầu có bán kính đáy $R = %s\\text{ cm}$ và chiều cao $h_{\\text{lớn}} = %s\\text{ cm}$' % (r_lon, h_thang)
        list_nb_da_1 = [nb_da_1_d, nb_da_1_s]

        loigiai_nb_1 = ('''Kéo dài $AD$ và $BC$ cắt nhau tại $S$. Vì $AB // CD$ và $AB = %s = \\frac{1}{2}CD$ nên $AB$ là đường trung bình của $\\Delta SDC$, suy ra $SA = AD = %s\\text{ cm}$ và $SD = %s\\text{ cm}$. Vậy hình nón lớn có $R = CD = %s\\text{ cm}$ và $h_{\\text{lớn}} = SD = %s\\text{ cm}$.''' % (r_nho, h_thang, h_lon, r_lon, h_lon))
        list_nb_2 = [loigiai_nb_1]

        th_da_1_d = '\\True Hình nón nhỏ bị cắt bỏ ở phía trên có bán kính đáy $r = %s\\text{ cm}$ và chiều cao $h_{\\text{nhỏ}} = %s\\text{ cm}$' % (r_nho, h_nho)
        th_da_1_s = 'Hình nón nhỏ bị cắt bỏ ở phía trên có bán kính đáy $r = %s\\text{ cm}$ và chiều cao $h_{\\text{nhỏ}} = %s\\text{ cm}$' % (r_nho, h_lon)
        list_th_da_1 = [th_da_1_d, th_da_1_s]

        loigiai_th_1 = ('''Hình nón nhỏ ở phía trên có bán kính đáy $r = AB = %s\\text{ cm}$ và chiều cao $h_{\\text{nhỏ}} = SA = %s\\text{ cm}$.''' % (r_nho, h_nho))
        list_th_2 = [loigiai_th_1]

        vd_da_1_d = '\\True Thể tích của hình nón lớn gấp $8$ lần thể tích của hình nón nhỏ'
        vd_da_1_s = 'Thể tích của hình nón lớn gấp $4$ lần thể tích của hình nón nhỏ'
        list_vd_da_1 = [vd_da_1_d, vd_da_1_s]

        loigiai_vd_1 = ('''Ta có $V_{\\text{lớn}} = \\frac{1}{3}\\pi \\cdot %s^2 \\cdot %s = %s\\pi\\text{ (cm}^3\\text{)}$ và $V_{\\text{nhỏ}} = \\frac{1}{3}\\pi \\cdot %s^2 \\cdot %s = %s\\pi\\text{ (cm}^3\\text{)}$. Suy ra $\\frac{V_{\\text{lớn}}}{V_{\\text{nhỏ}}} = \\frac{%s\\pi}{%s\\pi} = 8$.''' % (r_lon, h_lon, v_lon, r_nho, h_nho, v_nho, v_lon, v_nho))
        list_vd_2 = [loigiai_vd_1]

        vdc_da_1_d = '\\True Thể tích của khối tròn xoay tạo thành khi quay hình thang $ABCD$ quanh $AD$ bằng $%s\\pi\\text{ cm}^3$' % (v_cut)
        vdc_da_1_s = 'Thể tích của khối tròn xoay tạo thành khi quay hình thang $ABCD$ quanh $AD$ bằng $%s\\pi\\text{ cm}^3$' % (v_lon)
        list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]

        loigiai_vdc_1 = ('''Thể tích hình nón cụt tạo thành là: $V = V_{\\text{lớn}} - V_{\\text{nhỏ}} = %s\\pi - %s\\pi = %s\\pi\\text{ (cm}^3\\text{)}$.''' % (v_lon, v_nho, v_cut))
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
               '\\begin{ex}\n' + str(noidungcauhoi) + '\n' +
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
