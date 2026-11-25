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
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QDialog, QLabel, QLineEdit, 
    QPushButton, QComboBox, QCheckBox, QTextEdit, QVBoxLayout, 
    QHBoxLayout, QGridLayout, QMessageBox, QColorDialog,
    QSplashScreen, QProgressBar
)
from PyQt5.QtCore import Qt, QSettings, QThread, pyqtSignal
from PyQt5.QtGui import QIcon, QPixmap, QFont
from PyQt5.QtGui import QFont, QBrush, QColor
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QSplitter, QTreeWidget, QTreeWidgetItem, QTextEdit, QLabel, 
    QSpacerItem, QSizePolicy, QStackedWidget, QPushButton, QCheckBox, QSpinBox,
    QScrollArea
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
from mpl_toolkits.mplot3d import Axes3D

def bt_dang20_p4_b3_c5_ds8(self):
    # Dạng 20: Bài toán tổng hợp đa biểu đồ về cơ cấu sản xuất nông nghiệp và năng suất lúa
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        tong_dt = random.choice([140000, 160000, 180000])
        p_dx, p_ht, p_ngo = 45, 35, 20
        dt_dx = int(tong_dt * p_dx // 100)
        dt_ht = int(tong_dt * p_ht // 100)
        dt_ngo = int(tong_dt * p_ngo // 100)
        
        ns_dx = Decimal('6.8')
        ns_ht = Decimal('5.6')
        ns_ngo = Decimal('4.5')
        
        sl_dx = int(Decimal(dt_dx) * ns_dx)
        sl_ht = int(Decimal(dt_ht) * ns_ht)
        sl_ngo = int(Decimal(dt_ngo) * ns_ngo)
        tong_sl = sl_dx + sl_ht + sl_ngo
        
        def fmt_int(n):
            return f"{n:,}".replace(",", "\\,")
            
        tikz_code = (
            '\\begin{center}\n' +
            '\\begin{tikzpicture}[scale=0.9, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n' +
            '\\draw[line width=1pt, fill=black!15] (0,0) -- (0:1.6) arc (0:162:1.6) -- cycle;\n' +
            '\\draw[line width=1pt, fill=black!35] (0,0) -- (162:1.6) arc (162:288:1.6) -- cycle;\n' +
            '\\draw[line width=1pt, fill=white] (0,0) -- (288:1.6) arc (288:360:1.6) -- cycle;\n' +
            '\\node at (81:0.95) {$45\\%%$};\n' +
            '\\node at (225:0.95) {$35\\%%$};\n' +
            '\\node at (324:1.1) {$20\\%%$};\n' +
            '\\node[below] at (0,-1.8) {Cơ cấu diện tích};\n' +
            '\\begin{scope}[xshift=4.2cm, yshift=-1.4cm]\n' +
            '\\draw[line width=1pt, ->] (0,0) -- (4.6,0) node[below] {Cây trồng};\n' +
            '\\draw[line width=1pt, ->] (0,0) -- (0,3.2) node[left] {Năng suất (tấn/ha)};\n' +
            '\\draw[line width=1pt, fill=black!15] (0.5,0) rectangle (1.3,2.72); \\node[above] at (0.9,2.72) {$6,8$}; \\node[below] at (0.9,0) {Đông xuân};\n' +
            '\\draw[line width=1pt, fill=black!35] (1.8,0) rectangle (2.6,2.24); \\node[above] at (2.2,2.24) {$5,6$}; \\node[below] at (2.2,0) {Hè thu};\n' +
            '\\draw[line width=1pt, fill=white] (3.1,0) rectangle (3.9,1.80); \\node[above] at (3.5,1.80) {$4,5$}; \\node[below] at (3.5,0) {Ngô, khác};\n' +
            '\\end{scope}\n' +
            '\\end{tikzpicture}\n' +
            '\\end{center}'
        )
        
        noidungcauhoi = ('Tổng diện tích gieo trồng cây lương thực có hạt của một tỉnh năm $2025$ là $%s\\text{ ha}$. Biểu đồ hình quạt tròn cho biết cơ cấu diện tích và biểu đồ cột cho biết năng suất trung bình của từng loại cây trồng trong năm:\n' % fmt_int(tong_dt) +
                         tikz_code + '\n' +
                         'a) Tính diện tích gieo trồng (đơn vị: $\\text{ha}$) của từng loại cây trồng trong năm $2025$.\\\n' +
                         'b) Tính tổng sản lượng lương thực có hạt (đơn vị: tấn) mà tỉnh đó thu hoạch được trong năm $2025$.')
        
        loigiai = ('\\begin{enumEX}[a)]{1}\n' +
                   '\\item Diện tích gieo trồng của từng loại cây trồng năm $2025$ là:\\\\' +
                   '- Lúa đông xuân: $%s \\cdot 45\\%% = %s\\text{ (ha)}$.\\\\' +
                   '- Lúa hè thu: $%s \\cdot 35\\%% = %s\\text{ (ha)}$.\\\\' +
                   '- Ngô và cây lương thực khác: $%s \\cdot 20\\%% = %s\\text{ (ha)}$.\n' +
                   '\\item Sản lượng thu hoạch của từng loại cây trồng là:\\\\' +
                   '- Lúa đông xuân: $%s \\cdot 6,8 = %s$ (tấn).\\\\' +
                   '- Lúa hè thu: $%s \\cdot 5,6 = %s$ (tấn).\\\\' +
                   '- Ngô và cây lương thực khác: $%s \\cdot 4,5 = %s$ (tấn).\\\\' +
                   'Tổng sản lượng lương thực có hạt của tỉnh trong năm $2025$ là:\\\\' +
                   '$$%s + %s + %s = %s \\text{ (tấn)}.$$\n' +
                   '\\end{enumEX}'
                   ) % (fmt_int(tong_dt), fmt_int(dt_dx), fmt_int(tong_dt), fmt_int(dt_ht), fmt_int(tong_dt), fmt_int(dt_ngo),
                        fmt_int(dt_dx), fmt_int(sl_dx), fmt_int(dt_ht), fmt_int(sl_ht), fmt_int(dt_ngo), fmt_int(sl_ngo),
                        fmt_int(sl_dx), fmt_int(sl_ht), fmt_int(sl_ngo), fmt_int(tong_sl))

    # Xuất câu tự luận
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n' +
               '\\loigiai{ \n' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
