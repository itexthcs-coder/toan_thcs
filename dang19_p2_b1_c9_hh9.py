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


def bt_dang19_p2_b1_c9_hh9(self):
    MN = random.choice([12, 16, 20, 24])
    cung_MP = random.choice([40, 50, 60])
    cung_NQ = random.choice([50, 60, 70])
    cung_PQ = 180 - cung_MP - cung_NQ
    goc_PMQ = cung_PQ // 2
    goc_MIP = (cung_MP + cung_NQ) // 2

    hinh_ve = (
        '\\begin{center}\n'
        '\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n'
        '\\coordinate (O) at (0,0);\n'
        '\\coordinate (M) at (-2.4,0);\n'
        '\\coordinate (N) at (2.4,0);\n'
        '\\coordinate (P) at (130:2.4);\n'
        '\\coordinate (Q) at (65:2.4);\n'
        '\\coordinate (I) at (intersection of M--Q and N--P);\n'
        '\\draw[line width=1pt] (2.4,0) arc (0:180:2.4cm) -- cycle;\n'
        '\\draw[line width=1pt] (M)--(P)--(N) (M)--(Q)--(N);\n'
        '\\fill (O) circle (1pt) node[below] {$O$};\n'
        '\\fill (M) circle (1pt) node[left] {$M$};\n'
        '\\fill (N) circle (1pt) node[right] {$N$};\n'
        '\\fill (P) circle (1pt) node[above left] {$P$};\n'
        '\\fill (Q) circle (1pt) node[above right] {$Q$};\n'
        '\\fill (I) circle (1pt) node[below] {$I$};\n'
        '\\end{tikzpicture}\n'
        '\\end{center}'
    )

    noidungcauhoi = (
        'Một vòm cầu trang trí có dạng nửa đường tròn tâm $O$, đường kính $MN = %s\\text{ m}$. Trên vòm cầu người ta gắn hai điểm neo cáp treo $P$ và $Q$ (theo thứ tự $M, P, Q, N$) sao cho $\\text{sđ}\\overparen{MP} = %s^\\circ$ và $\\text{sđ}\\overparen{NQ} = %s^\\circ$. Hai thanh giằng chéo $MQ$ và $NP$ cắt nhau tại điểm $I$ như hình vẽ.\n%s'
        % (MN, cung_MP, cung_NQ, hinh_ve)
    )

    nb_da_1_d = '\\True Góc nội tiếp $\\widehat{MPN}$ và góc nội tiếp $\\widehat{MQN}$ đều bằng $90^\\circ$'
    nb_da_1_s = 'Góc nội tiếp $\\widehat{MPN}$ và góc nội tiếp $\\widehat{MQN}$ đều bằng $60^\\circ$'
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    loigiai_nb_1 = 'Vì $MN$ là đường kính của nửa đường tròn $(O)$ nên $\\widehat{MPN}$ và $\\widehat{MQN}$ là các góc nội tiếp chắn nửa đường tròn, suy ra $\\widehat{MPN} = \\widehat{MQN} = 90^\\circ$.'
    list_nb_2 = [loigiai_nb_1]

    th_da_1_d = '\\True Số đo cung $PQ$ ở đỉnh vòm bằng $%s^\\circ$' % (cung_PQ)
    th_da_1_s = 'Số đo cung $PQ$ ở đỉnh vòm bằng $%s^\\circ$' % (180 - cung_PQ)
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    loigiai_th_1 = 'Nửa đường tròn có số đo bằng $180^\\circ$ nên $\\text{sđ}\\overparen{PQ} = 180^\\circ - (\\text{sđ}\\overparen{MP} + \\text{sđ}\\overparen{NQ}) = 180^\\circ - (%s^\\circ + %s^\\circ) = %s^\\circ$.' % (cung_MP, cung_NQ, cung_PQ)
    list_th_2 = [loigiai_th_1]

    vd_da_1_d = '\\True Góc $\\widehat{PMQ}$ tạo bởi hai dây cáp $MP$ và $MQ$ bằng $%s^\\circ$' % (goc_PMQ)
    vd_da_1_s = 'Góc $\\widehat{PMQ}$ tạo bởi hai dây cáp $MP$ và $MQ$ bằng $%s^\\circ$' % (cung_PQ)
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    loigiai_vd_1 = 'Góc nội tiếp $\\widehat{PMQ}$ chắn cung $PQ$ nên $\\widehat{PMQ} = \\dfrac{1}{2}\\text{sđ}\\overparen{PQ} = \\dfrac{1}{2} \\cdot %s^\\circ = %s^\\circ$.' % (cung_PQ, goc_PMQ)
    list_vd_2 = [loigiai_vd_1]

    vdc_da_1_d = '\\True Góc $\\widehat{MIP}$ tạo bởi hai thanh giằng chéo tại điểm giao $I$ có số đo bằng $%s^\\circ$' % (goc_MIP)
    vdc_da_1_s = 'Góc $\\widehat{MIP}$ tạo bởi hai thanh giằng chéo tại điểm giao $I$ có số đo bằng $%s^\\circ$' % (180 - goc_MIP)
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    loigiai_vdc_1 = 'Xét $\\triangle IMN$, góc $\\widehat{MIP}$ là góc ngoài tại đỉnh $I$ nên $\\widehat{MIP} = \\widehat{IMN} + \\widehat{INM} = \\dfrac{1}{2}\\text{sđ}\\overparen{NQ} + \\dfrac{1}{2}\\text{sđ}\\overparen{MP} = \\dfrac{%s^\\circ + %s^\\circ}{2} = %s^\\circ$.' % (cung_NQ, cung_MP, goc_MIP)
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
