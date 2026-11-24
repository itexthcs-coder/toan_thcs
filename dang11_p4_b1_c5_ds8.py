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


def bt_dang11_p4_b1_c5_ds8(self):
    # Dạng 11: Biện luận tính chất toán học của các đại lượng trong thí nghiệm Vật lí
    lisdang = ['1']
    dang = random.choice(lisdang)

    if dang == '1':
        while True:
            t1 = random.randint(235, 260)
            t2 = random.randint(235, 260)
            t3 = random.randint(235, 260)
            t4 = random.randint(235, 260)
            t5_true = random.randint(235, 255)
            if len({t1, t2, t3, t4, t5_true}) >= 4 and (t1 + t2 + t3 + t4 + t5_true) % 5 == 0:
                break

        def fmt2(v):
            return ("%.2f" % (Decimal(v) / Decimal(100))).replace('.', ',')

        t5_true_str = fmt2(t5_true)
        t5_sai_str = ("%.1f" % (Decimal(t5_true) / Decimal(10))).replace('.', ',')
        day = [fmt2(t1), fmt2(t2), fmt2(t3), t5_sai_str, fmt2(t4)]
        random.shuffle(day)
        day_str = ";\\; ".join(day)

        tb_val = Decimal(t1 + t2 + t3 + t4 + t5_true) / Decimal(500)
        tb_str = ("%.2f" % tb_val).replace('.', ',')

        tikz_mang = (
            "\\begin{center}\n"
            "\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round]\n"
            "\\coordinate (A) at (0,0);\n"
            "\\coordinate (B) at (5,0);\n"
            "\\coordinate (C) at (0,2.2);\n"
            "\\draw[line width=1pt] (A) -- (B) -- (C) -- cycle;\n"
            "\\fill (0.8,1.95) circle (1pt) node[above right] {Viên bi};\n"
            "\\node at (3.7,0.28) {$\\alpha$};\n"
            "\\end{tikzpicture}\n"
            "\\end{center}"
        )

        noidungcauhoi = ('''Trong một thí nghiệm khảo sát sự chuyển động của viên bi lăn trên máng nghiêng có độ dốc thay đổi (minh họa ở hình vẽ dưới đây), học sinh ghi lại: \\textit{Góc nghiêng của máng ($\\alpha$, tính theo độ)}, \\textit{Thời gian viên bi lăn hết máng ($t$, tính theo giây)}, và \\textit{Số lần thử nghiệm thành công ($k$)}.
%s
a) Giải thích vì sao $\\alpha$ và $t$ là các số liệu liên tục, còn $k$ là số liệu rời rạc thông qua khả năng nhận giá trị trong một khoảng.\\\\
b) Nếu trong $5$ lần đo thời gian $t$ thu được dãy: $%s$, hãy chỉ ra giá trị có sai sót (do ghi nhầm vị trí dấu phẩy thập phân), sửa lại cho đúng và tính thời gian lăn trung bình.'''
                         % (tikz_mang, day_str))

        loigiai = ('''\\begin{enumEX}[a)]{1}
\\item Biện luận tính chất các đại lượng:\\\\
- Góc nghiêng $\\alpha$ và thời gian $t$ là các đại lượng đo lường vật lí, có thể nhận giá trị thực tùy ý trong một khoảng nào đó (chẳng hạn $\\alpha$ có thể nhận giá trị bất kì giữa $15^{\\circ}$ và $30^{\\circ}$; $t$ có thể nhận giá trị bất kì giữa $2\\,\\text{s}$ và $3\\,\\text{s}$) nên $\\alpha$ và $t$ là \\textbf{số liệu liên tục}.\\\\
- Số lần thử nghiệm thành công $k$ thu được từ phép đếm nên chỉ nhận các giá trị nguyên không âm ($k \\in \\{0; 1; 2; \\dots\\}$), không thể nhận giá trị nằm giữa hai số tự nhiên liên tiếp nên $k$ là \\textbf{số liệu rời rạc}.
\\item Trong dãy số liệu $%s$, các lần đo đều xấp xỉ $2,5\\,\\text{s}$ nhưng có giá trị $%s$ lớn gấp $10$ lần, đây là sai sót do đặt nhầm dấu phẩy thập phân.\\\\
Sửa giá trị $%s$ thành $%s$, thời gian lăn trung bình của $5$ lần đo là:
$$\\dfrac{%s + %s + %s + %s + %s}{5} = %s\\text{ (giây)}.$$
\\end{enumEX}'''
                   % (day_str, t5_sai_str, t5_sai_str, t5_true_str,
                      fmt2(t1), fmt2(t2), fmt2(t3), fmt2(t4), t5_true_str, tb_str))

    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' + str(noidungcauhoi) + '\n\\loigiai{ \n' + str(loigiai) + '}\n'
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
