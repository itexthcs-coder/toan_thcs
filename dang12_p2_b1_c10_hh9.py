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


def bt_dang12_p2_b1_c10_hh9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        k = random.choice([1, 2])
        r1 = 3 * k
        h1 = 4 * k
        l1 = 5 * k
        r2 = 6 * k
        h2 = 8 * k
        v1 = ((r1 ** 2) * h1) // 3
        v2 = ((r2 ** 2) * h2) // 3
        v_tong = v1 + v2

        noidungcauhoi = ('''Cho hình phẳng $ABCD$ gồm hai tam giác vuông $\\Delta ABE$ vuông tại $A$ ($AB = %s\\text{ cm}$, $AE = %s\\text{ cm}$) và $\\Delta DCE$ vuông tại $D$ ($DC = %s\\text{ cm}$, $DE = %s\\text{ cm}$) như hình vẽ, trong đó $A, E, D$ thẳng hàng. Quay hình $ABCD$ quanh đường thẳng $AD$ một vòng. Xét tính đúng sai của các khẳng định sau:
\\begin{center}
\\begin{tikzpicture}[scale=0.85, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (A) at (0,2.6);
\\coordinate (B) at (-1.2,2.6);
\\coordinate (E) at (0,1.6);
\\coordinate (D) at (0,0);
\\coordinate (C) at (2.2,0);
\\draw[line width=1pt] (B)--(A)--(D)--(C)--(B);
\\draw[line width=1pt] (-0.22,2.6)--(-0.22,2.38)--(0,2.38);
\\draw[line width=1pt] (0,0.22)--(0.22,0.22)--(0.22,0);
\\fill (A) circle (1pt) node[right] {$A$};
\\fill (B) circle (1pt) node[left] {$B$};
\\fill (E) circle (1pt) node[right] {$E$};
\\fill (D) circle (1pt) node[left] {$D$};
\\fill (C) circle (1pt) node[right] {$C$};
\\end{tikzpicture}
\\end{center}'''
                         % (r1, h1, r2, h2))

        nb_da_1_d = '\\True Khối tròn xoay tạo thành gồm hai hình nón chung đỉnh $E$'
        nb_da_1_s = 'Khối tròn xoay tạo thành là một hình trụ có chiều cao bằng $AD$'
        list_nb_da_1 = [nb_da_1_d, nb_da_1_s]

        loigiai_nb_1 = ('''Khi quay hình $ABCD$ quanh $AD$ một vòng, tam giác vuông $ABE$ tạo thành hình nón đỉnh $E$ ở phía trên và tam giác vuông $DCE$ tạo thành hình nón đỉnh $E$ ở phía dưới. Vậy khối tròn xoay gồm hai hình nón chung đỉnh $E$.''')
        list_nb_2 = [loigiai_nb_1]

        th_da_1_d = '\\True Hình nón phía trên có bán kính đáy $r_1 = %s\\text{ cm}$ và độ dài đường sinh $l_1 = %s\\text{ cm}$' % (r1, l1)
        th_da_1_s = 'Hình nón phía trên có bán kính đáy $r_1 = %s\\text{ cm}$ và độ dài đường sinh $l_1 = %s\\text{ cm}$' % (h1, l1)
        list_th_da_1 = [th_da_1_d, th_da_1_s]

        loigiai_th_1 = ('''Hình nón phía trên có bán kính đáy $r_1 = AB = %s\\text{ cm}$, chiều cao $h_1 = AE = %s\\text{ cm}$ nên độ dài đường sinh là $l_1 = BE = \\sqrt{%s^2 + %s^2} = %s\\text{ (cm)}$.''' % (r1, h1, r1, h1, l1))
        list_th_2 = [loigiai_th_1]

        vd_da_1_d = '\\True Thể tích của hình nón phía dưới bằng $%s\\pi\\text{ cm}^3$' % (v2)
        vd_da_1_s = 'Thể tích của hình nón phía dưới bằng $%s\\pi\\text{ cm}^3$' % (3 * v2)
        list_vd_da_1 = [vd_da_1_d, vd_da_1_s]

        loigiai_vd_1 = ('''Hình nón phía dưới có $r_2 = DC = %s\\text{ cm}$, $h_2 = DE = %s\\text{ cm}$ nên thể tích là: $V_2 = \\frac{1}{3}\\pi r_2^2 h_2 = \\frac{1}{3}\\pi \\cdot %s^2 \\cdot %s = %s\\pi\\text{ (cm}^3\\text{)}$.''' % (r2, h2, r2, h2, v2))
        list_vd_2 = [loigiai_vd_1]

        vdc_da_1_d = '\\True Tổng thể tích của hình tạo thành khi quay hình $ABCD$ quanh $AD$ bằng $%s\\pi\\text{ cm}^3$' % (v_tong)
        vdc_da_1_s = 'Tổng thể tích của hình tạo thành khi quay hình $ABCD$ quanh $AD$ bằng $%s\\pi\\text{ cm}^3$' % (v2 - v1)
        list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]

        loigiai_vdc_1 = ('''Thể tích hình nón phía trên là $V_1 = \\frac{1}{3}\\pi \\cdot %s^2 \\cdot %s = %s\\pi\\text{ (cm}^3\\text{)}$. Tổng thể tích khối tròn xoay là: $V = V_1 + V_2 = %s\\pi + %s\\pi = %s\\pi\\text{ (cm}^3\\text{)}$.''' % (r1, h1, v1, v1, v2, v_tong))
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
