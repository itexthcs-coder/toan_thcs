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


def bt_dang16_p2_b3_c9_hh9(self):
    nua_rong, cao, ban_kinh = random.choice([(3, 4, 5), (4, 3, 5), (6, 8, 10), (5, 12, 13)])
    rong = 2 * nua_rong
    chieu_dai_thep = str(Decimal(str(3.14 * ban_kinh)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)).replace('.', ',')
    chu_vi_ca_tron = str(Decimal(str(2 * 3.14 * ban_kinh)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)).replace('.', ',')

    hinhve = ('''\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (O) at (0,0);
\\coordinate (M) at (-2.5,0);
\\coordinate (N) at (2.5,0);
\\coordinate (A) at (-1.5,0);
\\coordinate (B) at (1.5,0);
\\coordinate (C) at (1.5,2);
\\coordinate (D) at (-1.5,2);
\\draw[line width=1pt] (N) arc (0:180:2.5);
\\draw[line width=1pt] (M)--(N);
\\draw[line width=1pt] (A)--(D)--(C)--(B);
\\fill (O) circle (1pt) node[below] {$O$};
\\node[above] at (0,2) {$%s\\text{ m}$};
\\node[left] at (-1.5,1) {$%s\\text{ m}$};
\\end{tikzpicture}
\\end{center}''' % (rong, cao))

    noidungcauhoi = ('''Một người thợ cơ khí muốn dựng một khung cổng hình chữ nhật có chiều rộng $%s\\text{ m}$ và chiều cao $%s\\text{ m}$, phía bên ngoài khung cổng được bao bọc bởi một vòm thép uốn cong dạng nửa đường tròn đi qua hai đỉnh phía trên của khung chữ nhật và nhận đường thẳng chứa chân cổng làm đường kính. Lấy $\\pi \\approx 3,14$. Xét tính đúng sai của các khẳng định sau:%s''' % (rong, cao, hinhve))

    nb_da_1_d = '\\True Tâm của nửa đường tròn vòm cổng là trung điểm của đoạn thẳng nối hai chân cổng'
    nb_da_1_s = 'Tâm của nửa đường tròn vòm cổng là giao điểm hai đường chéo khung cổng chữ nhật'
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    loigiai_nb_1 = ('''Do tính đối xứng của khung cổng hình chữ nhật và đường thẳng chứa chân cổng là đường kính nên tâm $O$ của nửa đường tròn là trung điểm của đoạn thẳng nối hai chân cổng.''')

    th_da_1_d = '\\True Bán kính của nửa đường tròn vòm cổng bằng $%s\\text{ m}$' % (ban_kinh)
    th_da_1_s = 'Bán kính của nửa đường tròn vòm cổng bằng $%s\\text{ m}$' % (nua_rong + cao)
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    loigiai_th_1 = ('''Khoảng cách từ tâm $O$ đến mỗi chân cổng là $\\dfrac{%s}{2} = %s\\text{ (m)}$. Áp dụng định lí Pythagore, bán kính của nửa đường tròn là $R = \\sqrt{%s^2 + %s^2} = %s\\text{ (m)}$.''' % (rong, nua_rong, nua_rong, cao, ban_kinh))

    vd_da_1_d = '\\True Chiều cao tối đa tính từ mặt đất lên đỉnh cao nhất của vòm cổng là $%s\\text{ m}$' % (ban_kinh)
    vd_da_1_s = 'Chiều cao tối đa tính từ mặt đất lên đỉnh cao nhất của vòm cổng là $%s\\text{ m}$' % (2 * ban_kinh)
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    loigiai_vd_1 = ('''Vì đường kính của nửa đường tròn nằm trên mặt đất nên chiều cao tối đa từ mặt đất lên đỉnh vòm cổng chính bằng bán kính $R = %s\\text{ m}$.''' % (ban_kinh))

    vdc_da_1_d = '\\True Chiều dài đoạn thép cần dùng để uốn khung nửa đường tròn đó xấp xỉ $%s\\text{ m}$' % (chieu_dai_thep)
    vdc_da_1_s = 'Chiều dài đoạn thép cần dùng để uốn khung nửa đường tròn đó xấp xỉ $%s\\text{ m}$' % (chu_vi_ca_tron)
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    loigiai_vdc_1 = ('''Chiều dài đoạn thép uốn thành nửa đường tròn bán kính $R = %s\\text{ m}$ là $C_{\\text{nửa}} = \\pi R \\approx 3,14 \\cdot %s = %s\\text{ (m)}$.''' % (ban_kinh, ban_kinh, chieu_dai_thep))

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
