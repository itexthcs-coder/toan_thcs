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

def bt_dang13_p2_b2_c5_hh9(self):
    k = random.choice([2, 3, 4])
    R = 5 * k
    nua_AB = 4 * k
    AB = 8 * k
    OH = 3 * k
    chieu_cao = R - OH

    noidungcauhoi = ('''Một cây cầu đi bộ có nhịp vòm dạng một cung tròn $\\overparen{AB}$ thuộc đường tròn tâm $O$, bán kính $R = %s\\text{ m}$. Mặt sàn cầu nằm ngang đóng vai trò là dây cung $AB$ dài $%s\\text{ m}$ (như hình vẽ).
    \\begin{center}
    \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
    \\coordinate (O) at (0,0);
    \\coordinate (A) at (143:2.0);
    \\coordinate (B) at (37:2.0);
    \\coordinate (H) at (0,1.2);
    \\coordinate (M) at (0,2.0);
    \\draw[line width=1pt] (B) arc (37:143:2.0);
    \\draw[line width=1pt] (A)--(B);
    \\draw[line width=1pt, dashed] (O)--(A) (O)--(B) (O)--(M);
    \\fill (O) circle (1pt) node[below] {$O$};
    \\fill (A) circle (1pt) node[left] {$A$};
    \\fill (B) circle (1pt) node[right] {$B$};
    \\fill (H) circle (1pt) node[below right] {$H$};
    \\fill (M) circle (1pt) node[above] {$M$};
    \\end{tikzpicture}
    \\end{center}''' % (R, AB))

    nb_da_1_d = '\\True Khoảng cách từ tâm $O$ của đường tròn đến mặt sàn cầu $AB$ bằng $%s\\text{ m}$' % (OH)
    nb_da_1_s = 'Khoảng cách từ tâm $O$ của đường tròn đến mặt sàn cầu $AB$ bằng $%s\\text{ m}$' % (nua_AB)
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    loigiai_nb_1 = ('''Gọi $H$ là trung điểm của $AB$ thì $OH \\perp AB$ và $AH = \\dfrac{AB}{2} = \\dfrac{%s}{2} = %s\\text{ m}$. \\\\ Áp dụng định lí Pythagore trong tam giác $OHA$ vuông tại $H$: $OH = \\sqrt{OA^2 - AH^2} = \\sqrt{%s^2 - %s^2} = %s\\text{ m}$.''' % (AB, nua_AB, R, nua_AB, OH))
    list_nb_2 = [loigiai_nb_1]

    th_da_1_d = '\\True Chiều cao thông thủy lớn nhất từ mặt sàn cầu $AB$ lên đến đỉnh vòm cung là $%s\\text{ m}$' % (chieu_cao)
    th_da_1_s = 'Chiều cao thông thủy lớn nhất từ mặt sàn cầu $AB$ lên đến đỉnh vòm cung là $%s\\text{ m}$' % (OH)
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    loigiai_th_1 = ('''Đỉnh vòm cung là điểm chính giữa $M$ của cung nhỏ $\\overparen{AB}$. \\\\ Chiều cao thông thủy lớn nhất từ mặt sàn cầu lên đỉnh vòm là $MH = OM - OH = %s - %s = %s\\text{ m}$.''' % (R, OH, chieu_cao))
    list_th_2 = [loigiai_th_1]

    vd_da_1_d = '\\True Nếu gọi $\\widehat{AOB} = 2\\alpha$ thì $\\sin \\alpha = 0,8$'
    vd_da_1_s = 'Nếu gọi $\\widehat{AOB} = 2\\alpha$ thì $\\sin \\alpha = 0,6$'
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    loigiai_vd_1 = ('''Trong tam giác $OHA$ vuông tại $H$, ta có $\\widehat{AOH} = \\alpha$ và $\\sin \\alpha = \\dfrac{AH}{OA} = \\dfrac{%s}{%s} = 0,8$.''' % (nua_AB, R))
    list_vd_2 = [loigiai_vd_1]

    vdc_da_1_d = '\\True Số đo của cung tròn $\\overparen{AB}$ tạo nên vòm cầu lớn hơn $90^\\circ$'
    vdc_da_1_s = 'Số đo của cung tròn $\\overparen{AB}$ tạo nên vòm cầu nhỏ hơn $90^\\circ$'
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    loigiai_vdc_1 = ('''Vì $\\sin \\alpha = 0,8 > \\dfrac{\\sqrt{2}}{2} = \\sin 45^\\circ$ nên $\\alpha > 45^\\circ$. \\\\ Suy ra số đo cung nhỏ $\\overparen{AB}$ bằng $\\widehat{AOB} = 2\\alpha > 90^\\circ$.''')
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
               '\\end{ex}\n \\end{minipage}\n\n')
    return content
