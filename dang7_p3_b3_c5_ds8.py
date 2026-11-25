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

def bt_dang7_p3_b3_c5_ds8(self):
    # Dạng 7: Tính lượng nước tưới tiết kiệm được qua biểu đồ đoạn thẳng hai lưu vực sông
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        a10, a25 = Decimal('18.5'), Decimal('14.2')
        b10, b25 = Decimal('15.4'), Decimal('12.7')
        ha_a = random.choice([200, 250, 300])
        ha_b = random.choice([200, 300, 400])
        
        tk_a = int(Decimal(ha_a) * (a10 - a25))
        tk_b = int(Decimal(ha_b) * (b10 - b25))
        tong_tk = tk_a + tk_b
        kq_str = str(tong_tk)
        
        tikz_code = (
            '\\begin{center}\n' +
            '\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n' +
            '\\draw[line width=1pt, ->] (0,0) -- (4.8,0) node[below] {Năm};\n' +
            '\\draw[line width=1pt, ->] (0,0) -- (0,3.8) node[left] {Lượng nước ($\\text{m}^3/\\text{ha}$)};\n' +
            '\\node[below left] at (0,0) {$0$};\n' +
            '\\coordinate (A1) at (1.2,3.1); \\coordinate (A2) at (3.4,2.3);\n' +
            '\\draw[line width=1pt] (A1)--(A2);\n' +
            '\\fill (A1) circle (1pt) node[above] {$18,5$}; \\fill (A2) circle (1pt) node[above] {$14,2$};\n' +
            '\\coordinate (B1) at (1.2,2.5); \\coordinate (B2) at (3.4,1.9);\n' +
            '\\draw[line width=1pt, dashed] (B1)--(B2);\n' +
            '\\fill (B1) circle (1pt) node[below] {$15,4$}; \\fill (B2) circle (1pt) node[below] {$12,7$};\n' +
            '\\node[below] at (1.2,0) {$2010$}; \\node[below] at (3.4,0) {$2025$};\n' +
            '\\draw[line width=1pt] (4.9,2.8) -- (5.6,2.8) node[right] {Vùng $A$};\n' +
            '\\draw[line width=1pt, dashed] (4.9,2.1) -- (5.6,2.1) node[right] {Vùng $B$};\n' +
            '\\end{tikzpicture}\n' +
            '\\end{center}'
        )
        
        noidungcauhoi = ('Biểu đồ đoạn thẳng dưới đây cho biết nhu cầu về lượng nước tưới nông nghiệp (đơn vị: $\\text{m}^3/\\text{ha}$) tại hai vùng trồng lúa $A$ và $B$ trong năm $2010$ và năm $2025$:\n' +
                         tikz_code + '\n' +
                         'Nếu một hợp tác xã canh tác $%s\\text{ ha}$ lúa tại Vùng $A$ và $%s\\text{ ha}$ lúa tại Vùng $B$, thì trong năm $2025$ hợp tác xã đó tiết kiệm được tổng cộng bao nhiêu mét khối ($\\text{m}^3$) nước tưới so với năm $2010$?' % (ha_a, ha_b))
        
        loigiai = ('- Lượng nước tưới tiết kiệm được trên mỗi hecta tại Vùng $A$ là: $18,5 - 14,2 = 4,3\\text{ (m}^3/\\text{ha)}$.\\\\' +
                   'Lượng nước tiết kiệm được cho $%s\\text{ ha}$ tại Vùng $A$ là: $%s \\cdot 4,3 = %s\\text{ (m}^3\\text{)}$.\\\\' +
                   '- Lượng nước tưới tiết kiệm được trên mỗi hecta tại Vùng $B$ là: $15,4 - 12,7 = 2,7\\text{ (m}^3/\\text{ha)}$.\\\\' +
                   'Lượng nước tiết kiệm được cho $%s\\text{ ha}$ tại Vùng $B$ là: $%s \\cdot 2,7 = %s\\text{ (m}^3\\text{)}$.\\\\' +
                   'Tổng lượng nước tưới hợp tác xã tiết kiệm được là: $%s + %s = %s\\text{ (m}^3\\text{)}$.'
                   ) % (ha_a, ha_a, tk_a, ha_b, ha_b, tk_b, tk_a, tk_b, kq_str)

    # Đáp án
    dapan = '\\shortans[0]{$%s$}\n' % (str(kq_str))

    # Xuất câu hỏi
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n' + str(dapan) +
               '\\loigiai{ \n' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
