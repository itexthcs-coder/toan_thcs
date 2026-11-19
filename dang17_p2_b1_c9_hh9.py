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


def bt_dang17_p2_b1_c9_hh9(self):
    goc_AOB = random.choice([90, 100, 110, 120, 130])
    goc_lon = goc_AOB // 2
    cung_lon = 360 - goc_AOB
    goc_nho = cung_lon // 2

    hinh_ve = (
        '\\begin{center}\n'
        '\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n'
        '\\coordinate (O) at (0,0);\n'
        '\\coordinate (A) at (215:2);\n'
        '\\coordinate (B) at (325:2);\n'
        '\\coordinate (M) at (105:2);\n'
        '\\coordinate (N) at (270:2);\n'
        '\\draw[line width=1pt] (O) circle (2cm);\n'
        '\\draw[line width=1pt] (A)--(O)--(B) (A)--(M)--(B);\n'
        '\\draw[line width=1pt, dashed] (A)--(N)--(B);\n'
        '\\fill (O) circle (1pt) node[below] {$O$};\n'
        '\\fill (A) circle (1pt) node[left] {$A$};\n'
        '\\fill (B) circle (1pt) node[right] {$B$};\n'
        '\\fill (M) circle (1pt) node[above] {$M$};\n'
        '\\fill (N) circle (1pt) node[below] {$N$};\n'
        '\\end{tikzpicture}\n'
        '\\end{center}'
    )

    noidungcauhoi = (
        'Để giúp tàu thuyền tránh bãi đá ngầm nằm trong vùng giới hạn bởi đường tròn $(O)$, người ta đặt hai ngọn hải đăng tại $A$ và $B$ trên đường tròn sao cho góc ở tâm $\\widehat{AOB} = %s^\\circ$ như hình vẽ. Khi tàu ở vị trí $M$ trên biển, thuyền trưởng đo góc nhìn $\\widehat{AMB}$ tới hai ngọn hải đăng.\n%s'
        % (goc_AOB, hinh_ve)
    )

    nb_da_1_d = '\\True Nếu tàu đi đúng trên ranh giới cung lớn $AB$ của đường tròn $(O)$ thì góc đo được $\\widehat{AMB} = %s^\\circ$' % (goc_lon)
    nb_da_1_s = 'Nếu tàu đi đúng trên ranh giới cung lớn $AB$ của đường tròn $(O)$ thì góc đo được $\\widehat{AMB} = %s^\\circ$' % (goc_AOB)
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    loigiai_nb_1 = 'Khi $M$ nằm trên cung lớn $AB$ của đường tròn $(O)$, $\\widehat{AMB}$ là góc nội tiếp chắn cung nhỏ $AB$ nên $\\widehat{AMB} = \\dfrac{1}{2}\\widehat{AOB} = \\dfrac{%s^\\circ}{2} = %s^\\circ$.' % (goc_AOB, goc_lon)
    list_nb_2 = [loigiai_nb_1]

    th_da_1_d = '\\True Nếu tàu đi trên cung nhỏ $AB$ tại vị trí $N$ thì góc đo được $\\widehat{ANB} = %s^\\circ$' % (goc_nho)
    th_da_1_s = 'Nếu tàu đi trên cung nhỏ $AB$ tại vị trí $N$ thì góc đo được $\\widehat{ANB} = %s^\\circ$' % (goc_lon)
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    loigiai_th_1 = 'Số đo cung lớn $AB$ bằng $360^\\circ - %s^\\circ = %s^\\circ$. Khi $N$ nằm trên cung nhỏ $AB$, góc nội tiếp $\\widehat{ANB}$ chắn cung lớn $AB$ nên $\\widehat{ANB} = \\dfrac{1}{2} \\cdot %s^\\circ = %s^\\circ$.' % (goc_AOB, cung_lon, cung_lon, goc_nho)
    list_th_2 = [loigiai_th_1]

    vd_da_1_d = '\\True Khi tàu nằm ở bên ngoài đường tròn $(O)$ về phía cung lớn $AB$ thì góc $\\widehat{AMB}$ luôn nhỏ hơn $%s^\\circ$' % (goc_lon)
    vd_da_1_s = 'Khi tàu nằm ở bên ngoài đường tròn $(O)$ về phía cung lớn $AB$ thì góc $\\widehat{AMB}$ luôn lớn hơn $%s^\\circ$' % (goc_lon)
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    loigiai_vd_1 = 'Khi $M$ nằm ngoài đường tròn $(O)$ về phía cung lớn $AB$, gọi $K$ là giao điểm của $AM$ với cung lớn $AB$, ta có $\\widehat{AKB} = %s^\\circ$ là góc ngoài của $\\triangle KMB$ nên $\\widehat{AMB} < \\widehat{AKB} = %s^\\circ$.' % (goc_lon, goc_lon)
    list_vd_2 = [loigiai_vd_1]

    vdc_da_1_d = '\\True Để tàu đi an toàn bên ngoài vùng nguy hiểm đường tròn $(O)$, thuyền trưởng cần giữ cho góc nhìn $\\widehat{AMB} < %s^\\circ$' % (goc_lon)
    vdc_da_1_s = 'Để tàu đi an toàn bên ngoài vùng nguy hiểm đường tròn $(O)$, thuyền trưởng cần giữ cho góc nhìn $\\widehat{AMB} > %s^\\circ$' % (goc_lon)
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    loigiai_vdc_1 = 'Vì khi tàu ở trên đường tròn thì $\\widehat{AMB} = %s^\\circ$, ở bên trong đường tròn thì $\\widehat{AMB} > %s^\\circ$, và ở bên ngoài đường tròn thì $\\widehat{AMB} < %s^\\circ$ nên điều kiện an toàn là $\\widehat{AMB} < %s^\\circ$.' % (goc_lon, goc_lon, goc_lon, goc_lon)
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

    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
               '\\choiceTFn \n'
               '{' + str(shuffled_answers_nb[0]) + '}\n'
               '{' + str(shuffled_answers_th[0]) + '}\n'
               '{' + str(shuffled_answers_vd[0]) + '}\n'
               '{' + str(shuffled_answers_vdc[0]) + '}\n'
               '\\loigiai{ \n'
               '\\begin{enumEX}[a)]{1} \n'
               '\\item ' + str(shuffled_solutions_nb[0]) + '\n'
               '\\item ' + str(shuffled_solutions_th[0]) + '\n'
               '\\item ' + str(shuffled_solutions_vd[0]) + '\n'
               '\\item ' + str(shuffled_solutions_vdc[0]) + '\n'
               '\\end{enumEX}} \n'
               '\\end{ex}\n \\end{minipage}\n\n')
    return content
