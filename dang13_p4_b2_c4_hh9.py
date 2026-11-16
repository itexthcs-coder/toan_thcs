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


def bt_dang13_p4_b2_c4_hh9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        rong = 250
        cheo = 320
        deg_val = math.degrees(math.acos(rong / cheo))
        do_a = int(deg_val)
        phut_a = int(Decimal(str((deg_val - do_a) * 60)).quantize(Decimal('1'), rounding=ROUND_HALF_UP))

        v_kmh = random.choice([4, 5, 6])
        tg_phut = (cheo / 1000.0) / v_kmh * 60.0
        tg_str = str(Decimal(str(tg_phut)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)).replace('.', ',')

        hinhve = ('''\\begin{center}
    \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
    \\coordinate (A) at (0,0);
    \\coordinate (H) at (0,2.4);
    \\coordinate (B) at (1.9,2.4);
    \\draw[line width=1pt] (-0.6,0)--(3.0,0) (-0.6,2.4)--(3.0,2.4);
    \\draw[line width=1pt] (A)--(B);
    \\draw[line width=1pt, dashed] (A)--(H);
    \\draw[line width=1pt] (0,2.18)--(0.22,2.18)--(0.22,2.4);
    \\draw[line width=1pt] (0,0.65) arc (90:51.6:0.65);
    \\fill (A) circle (1pt) node[below] {$A$};
    \\fill (H) circle (1pt) node[above left] {$H$};
    \\fill (B) circle (1pt) node[above right] {$B$};
    \\node[left] at (0,1.2) {$%s\\text{ m}$};
    \\node[below right] at (0.95,1.2) {$%s\\text{ m}$};
    \\node at (0.25,0.92) {$\\alpha$};
    \\end{tikzpicture}
    \\end{center}''' % (rong, cheo))

        # Nội dung câu hỏi
        noidungcauhoi = ('''Một khúc sông có hai bờ song song cách nhau $AH = %s\\text{ m}$. Một người chèo đò xuất phát từ bến $A$ bên bờ này để sang bờ bên kia, nhưng do dòng nước chảy mạnh đẩy xiên nên con đò phải đi quãng đường thẳng $AB = %s\\text{ m}$ mới cập bến $B$ ở bờ bên kia (như hình vẽ). \\\\
    a) Hỏi dòng nước đã đẩy con đò đi lệch một góc $\\alpha = \\widehat{HAB}$ bằng bao nhiêu độ so với phương vuông góc với bờ sông (làm tròn kết quả đến phút)? \\\\
    b) Nếu người đó chèo đò với vận tốc thực tế dọc theo hướng đi $AB$ là $%s\\text{ km/h}$ thì mất bao nhiêu phút để sang tới bờ bên kia (làm tròn đến chữ số thập phân thứ nhất)?
    %s''' % (rong, cheo, v_kmh, hinhve))

        # Nội dung lời giải
        loigiai = ('''\\begin{enumEX}[a)]{1}
    \\item Xét tam giác $AHB$ vuông tại $H$, theo định nghĩa tỉ số lượng giác góc nhọn ta có:\\\\
    $\\cos \\alpha = \\dfrac{AH}{AB} = \\dfrac{%s}{%s} = \\dfrac{25}{32}$.\\\\
    Sử dụng máy tính cầm tay, ta tìm được $\\alpha \\approx %s^\\circ %s'$.
    \\item Đổi quãng đường $AB = %s\\text{ m} = 0,32\\text{ km}$.\\\\
    Thời gian người đó chèo đò sang tới bờ bên kia là:\\\\
    $t = \\dfrac{0,32}{%s}\\text{ giờ} = \\dfrac{0,32 \\cdot 60}{%s} = %s\\text{ (phút)}$.
    \\end{enumEX}'''
                   % (rong, cheo, do_a, phut_a,
                      cheo, v_kmh, v_kmh, tg_str))

    # Xuất câu hỏi
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) +
               '\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
