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


def bt_dang18_p2_b3_c9_hh9(self):
    a = random.choice([6, 8, 10, 12])
    nua_a = a // 2
    r_expr = nua_a * sqrt(2)
    d_expr = a * sqrt(2)
    s_vuong = a**2
    r_sq = 2 * (nua_a**2)
    s_thua_str = str(Decimal(str(3.14 * r_sq - s_vuong)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)).replace('.', ',')
    s_tron_str = str(Decimal(str(3.14 * r_sq)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)).replace('.', ',')

    hinhve = ('''\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (A) at (-1.1,1.1);
\\coordinate (B) at (-1.1,-1.1);
\\coordinate (C) at (1.1,-1.1);
\\coordinate (D) at (1.1,1.1);
\\coordinate (O) at (0,0);
\\draw[line width=1pt, dashed] (O) circle (1.5556);
\\draw[line width=1pt] (A)--(B)--(C)--(D)--cycle;
\\fill (O) circle (1pt) node[below] {$O$};
\\node[below] at (0,-1.1) {$%s\\text{ m}$};
\\end{tikzpicture}
\\end{center}''' % (a))

    noidungcauhoi = ('''Bác An có một mảnh vườn trồng rau hình vuông cạnh $%s\\text{ m}$. Bác muốn lắp đặt duy nhất một đầu béc tưới phun mưa xoay tròn $360^\\circ$ để nước có thể tưới phủ kín toàn bộ diện tích mảnh vườn (kể cả bốn góc vườn). Lấy $\\pi \\approx 3,14$. Xét tính đúng sai của các khẳng định sau:%s''' % (a, hinhve))

    nb_da_1_d = '\\True Để tưới phủ kín toàn bộ mảnh vườn với bán kính phun nhỏ nhất, bác An cần đặt đầu béc tưới tại giao điểm hai đường chéo của mảnh vườn'
    nb_da_1_s = 'Để tưới phủ kín toàn bộ mảnh vườn với bán kính phun nhỏ nhất, bác An cần đặt đầu béc tưới tại trung điểm một cạnh vườn'
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    loigiai_nb_1 = ('''Đường tròn nhỏ nhất bao phủ toàn bộ hình vuông chính là đường tròn ngoại tiếp hình vuông đó, có tâm là giao điểm hai đường chéo.''')

    th_da_1_d = '\\True Bán kính phun tối thiểu của đầu béc tưới phải đạt $%s\\text{ m}$' % (latex(r_expr))
    th_da_1_s = 'Bán kính phun tối thiểu của đầu béc tưới phải đạt $%s\\text{ m}$' % (latex(d_expr))
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    loigiai_th_1 = ('''Độ dài đường chéo mảnh vườn hình vuông là $%s\\text{ m}$. Bán kính đường tròn ngoại tiếp bằng một nửa đường chéo nên $R = %s\\text{ m}$.''' % (latex(d_expr), latex(r_expr)))

    vd_da_1_d = '\\True Diện tích vùng nước phủ tròn tối thiểu là $%s\\text{ m}^2$' % (s_tron_str)
    vd_da_1_s = 'Diện tích vùng nước phủ tròn tối thiểu là $%s\\text{ m}^2$' % (s_vuong)
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    loigiai_vd_1 = ('''Diện tích hình tròn ngoại tiếp mảnh vườn là $S_{\\text{tròn}} = \\pi R^2 \\approx 3,14 \\cdot (%s)^2 = %s\\text{ (m}^2)$.''' % (latex(r_expr), s_tron_str))

    vdc_da_1_d = '\\True Diện tích phần nước tưới phủ ra bên ngoài mảnh vườn là $%s\\text{ m}^2$' % (s_thua_str)
    vdc_da_1_s = 'Diện tích phần nước tưới phủ ra bên ngoài mảnh vườn là $%s\\text{ m}^2$' % (s_tron_str)
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    loigiai_vdc_1 = ('''Diện tích vùng nước tưới ra ngoài mảnh vườn là $S_{\\text{ngoài}} = S_{\\text{tròn}} - S_{\\text{vuông}} = %s - %s = %s\\text{ (m}^2)$.''' % (s_tron_str, s_vuong, s_thua_str))

    # Đưa các lời giải vào danh sách lời giải
    list_nb_2 = [loigiai_nb_1]
    list_th_2 = [loigiai_th_1]
    list_vd_2 = [loigiai_vd_1]
    list_vdc_2 = [loigiai_vdc_1]

    def count_true_answers(answers):
        return sum('\\True' in ans for ans in answers)

    # Lặp đến khi đáp án có từ 1 đến 3 đúng
    while True:
        nb_da_1 = random.choice(list_nb_da_1)
        th_da_1 = random.choice(list_th_da_1)
        vd_da_1 = random.choice(list_vd_da_1)
        vdc_da_1 = random.choice(list_vdc_da_1)

        answers = [nb_da_1, th_da_1, vd_da_1, vdc_da_1]
        true_count = count_true_answers(answers)

        if 1 <= true_count <= 3:
            break

    # Gán lại vào list
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

    # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
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
               '\\end{ex}\n \end{minipage}\n\n')
    return content
