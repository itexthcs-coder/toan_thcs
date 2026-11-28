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


def bt_dang8_p4_b2_c8_ds8(self):
    # Dạng 8: Xác suất kết hợp kiến thức hàm số bậc nhất (chọn điểm thuộc đồ thị)
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        M = [-2, -1, 0, 1, 2, 3]
        a = random.choice([2, -2, 3])
        b = random.choice([-1, 0, 1])
        dau_b = '+' if b > 0 else ('-' if b < 0 else '')
        str_b = (' %s %s' % (dau_b, abs(b))) if b != 0 else ''
        pt_dt = 'y = %sx%s' % (a, str_b)

        pts = []
        for xv in M:
            yv = a * xv + b
            if yv in M:
                pts.append((xv, yv))

        tong_kq = len(M) * len(M)
        so_tl = len(pts)
        f = frac(so_tl, tong_kq)
        xs_str = '\\frac{%s}{%s}' % (f.numerator, f.denominator) if so_tl > 0 else '0'
        pts_str = '; '.join(['(%s; %s)' % (px, py) for px, py in pts])

        tikz_img = (
            '\\\\\n'
            '\\begin{center}\n'
            '\\begin{tikzpicture}[scale=0.65, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n'
            '\\draw[->, line width=1pt] (-2.8,0) -- (3.8,0) node[below] {$x$};\n'
            '\\draw[->, line width=1pt] (0,-2.5) -- (0,3.5) node[left] {$y$};\n'
            '\\fill (0,0) circle (1.2pt) node[below left] {$O$};\n'
            '\\foreach \\x in {-2,-1,1,2,3}{ \\draw[line width=1pt] (\\x,0.08)--(\\x,-0.08) node[below] {$\\x$}; }\n'
            '\\foreach \\y in {-2,-1,1,2,3}{ \\draw[line width=1pt] (0.08,\\y)--(-0.08,\\y) node[left] {$\\y$}; }\n'
            '\\end{tikzpicture}\n'
            '\\end{center}'
        )

        noidungcauhoi = (
            'Cho tập hợp $M = \\{-2; -1; 0; 1; 2; 3\\}$. Chọn ngẫu nhiên một số $x$ từ tập hợp $M$ làm hoành độ và một số $y$ cũng từ tập hợp $M$ làm tung độ để tạo thành điểm $A(x; y)$ trong mặt phẳng tọa độ $Oxy$. '
            'Tính xác suất để điểm $A$ nằm trên đường thẳng $%s$.%s'
        ) % (pt_dt, tikz_img)

        loigiai = (
            'Tập hợp $M$ có $6$ phần tử. Mỗi cách chọn cặp số $(x; y)$ với $x \\in M$ và $y \\in M$ cho ta một điểm $A(x; y)$.\\\\\n'
            'Tổng số kết quả có thể là $6 \\cdot 6 = 36$ điểm và các kết quả này là đồng khả năng.\\\\\n'
            'Điểm $A(x; y)$ nằm trên đường thẳng $%s$ khi và chỉ khi tọa độ $(x; y)$ thỏa mãn phương trình đường thẳng đó. Thay lần lượt các giá trị $x \\in M$ vào phương trình $%s$, ta tìm được các điểm thuộc tập hợp đã cho là:\\\\\n'
            '$%s$.\\\\\n'
            'Như vậy, có $%s$ kết quả thuận lợi cho biến cố điểm $A$ nằm trên đường thẳng $%s$.\\\\\n'
            'Vậy xác suất cần tìm là: $P = \\frac{%s}{36} = %s$.'
        ) % (pt_dt, pt_dt, pts_str, so_tl, pt_dt, so_tl, xs_str)

    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n' +
               '\\loigiai{\n' +
               str(loigiai) + '\n' +
               '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
