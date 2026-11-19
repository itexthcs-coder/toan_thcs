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


def bt_dang20_p2_b2_c8_ds9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)

    if dang == '1':
        noidungcauhoi = ('''Ở đậu Hà Lan, allele trội $A$ quy định hạt vàng, allele lặn $a$ quy định hạt xanh; allele trội $B$ quy định hạt trơn, allele lặn $b$ quy định hạt nhăn. Thực hiện phép lai giữa hai cây đậu đều có kiểu gene dị hợp hai cặp gene $(Aa, Bb) \\times (Aa, Bb)$. Cây con nhận ngẫu nhiên một giao tử từ bố và một giao tử từ mẹ.''')

        bang_mau = '''\\begin{center}
\\begin{tabular}{|c|c|c|c|c|}
\\hline
Bố $\\backslash$ Mẹ & $(A, B)$ & $(A, b)$ & $(a, B)$ & $(a, b)$ \\\\
\\hline
$(A, B)$ & $(AA, BB)$ & $(AA, Bb)$ & $(Aa, BB)$ & $(Aa, Bb)$ \\\\
\\hline
$(A, b)$ & $(AA, bB)$ & $(AA, bb)$ & $(Aa, bB)$ & $(Aa, bb)$ \\\\
\\hline
$(a, B)$ & $(aA, BB)$ & $(aA, Bb)$ & $(aa, BB)$ & $(aa, Bb)$ \\\\
\\hline
$(a, b)$ & $(aA, bB)$ & $(aA, bb)$ & $(aa, bB)$ & $(aa, bb)$ \\\\
\\hline
\\end{tabular}
\\end{center}'''

        nb_da_1_d = '\\True Mỗi cây bố và cây mẹ đều tạo ra $4$ loại giao tử đồng khả năng là $(A, B); (A, b); (a, B); (a, b)$, nên không gian mẫu có $16$ phần tử'
        nb_da_1_s = 'Mỗi cây bố và cây mẹ đều tạo ra $2$ loại giao tử đồng khả năng, nên không gian mẫu có $4$ phần tử'
        list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
        loigiai_nb_1 = ('''Ta lập bảng tổ hợp giao tử của cây bố và cây mẹ:%sCây bố cho $4$ loại giao tử $(A, B); (A, b); (a, B); (a, b)$ và cây mẹ cũng cho $4$ loại giao tử như vậy, suy ra $n(\\Omega) = 4 \\cdot 4 = 16$.''' % (bang_mau))

        th_da_1_d = '\\True Xác suất để cây con có kiểu hình hạt vàng và trơn là $\\dfrac{9}{16}$'
        th_da_1_s = 'Xác suất để cây con có kiểu hình hạt vàng và trơn là $\\dfrac{3}{4}$'
        list_th_da_1 = [th_da_1_d, th_da_1_s]
        loigiai_th_1 = ('''Cây con có hạt vàng và trơn khi có ít nhất một allele $A$ ($3$ cách tổ hợp: $AA, Aa, aA$) và ít nhất một allele $B$ ($3$ cách tổ hợp: $BB, Bb, bB$), nên có $3 \\cdot 3 = 9$ kết quả thuận lợi.\\\\
Vậy xác suất cần tìm là $\\dfrac{9}{16}$.''')

        vd_da_1_d = '\\True Xác suất để cây con có kiểu hình hạt xanh và nhăn là $\\dfrac{1}{16}$'
        vd_da_1_s = 'Xác suất để cây con có kiểu hình hạt xanh và nhăn là $\\dfrac{1}{8}$'
        list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
        loigiai_vd_1 = ('''Cây con có hạt xanh và nhăn khi nhận giao tử $(a, b)$ từ cả bố và mẹ, có $1$ kết quả thuận lợi.\\\\
Vậy xác suất cần tìm là $\\dfrac{1}{16}$.''')

        vdc_da_1_d = '\\True Xác suất để cây con mang một tính trạng trội và một tính trạng lặn là $\\dfrac{3}{8}$'
        vdc_da_1_s = 'Xác suất để cây con mang một tính trạng trội và một tính trạng lặn là $\\dfrac{1}{4}$'
        list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
        loigiai_vdc_1 = ('''Cây con có hạt vàng, nhăn có $3 \\cdot 1 = 3$ kết quả; cây con có hạt xanh, trơn có $1 \\cdot 3 = 3$ kết quả. Tổng cộng có $6$ kết quả thuận lợi.\\\\
Vậy xác suất cần tìm là $\\dfrac{6}{16} = \\dfrac{3}{8}$.''')

        def count_true_answers(answers):
            return sum('\\True' in ans for ans in answers)

        while True:
            nb_da_1 = random.choice(list_nb_da_1)
            th_da_1 = random.choice(list_th_da_1)
            vd_da_1 = random.choice(list_vd_da_1)
            vdc_da_1 = random.choice(list_vdc_da_1)
            answers = [nb_da_1, th_da_1, vd_da_1, vdc_da_1]
            if 1 <= count_true_answers(answers) <= 3:
                break

        list_nb_1, list_th_1, list_vd_1, list_vdc_1 = [nb_da_1], [th_da_1], [vd_da_1], [vdc_da_1]
        list_nb_2, list_th_2, list_vd_2, list_vdc_2 = [loigiai_nb_1], [loigiai_th_1], [loigiai_vd_1], [loigiai_vdc_1]

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
