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


def bt_dang11_p4_b2_c4_hh9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        v = random.choice([450, 500, 600])
        phut = 1.2 if v == 500 else (1.6 if v == 450 else 1.0)
        phut_str = str(phut).replace('.', ',')
        s_km = int(round(v * (phut / 60.0)))
        bh_sym = Rational(s_km, 2)
        ah_sym = Rational(s_km, 2) * sqrt(3)
        ah_str = str(Decimal(str(float(ah_sym))).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)).replace('.', ',')

        cao_muc_tieu = random.choice([6, 9, 12])
        qd_muc_tieu = 2 * cao_muc_tieu
        tg_phut = Rational(qd_muc_tieu * 60, v)
        tg_str = str(Decimal(str(float(tg_phut))).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)).replace('.', ',')

        hinhve = ('''\\begin{center}
    \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
    \\coordinate (A) at (0,0);
    \\coordinate (H) at (4.0,0);
    \\coordinate (B) at (4.0,2.31);
    \\draw[line width=1pt] (A)--(H)--(B)--cycle;
    \\draw[line width=1pt] (3.78,0)--(3.78,0.22)--(4.0,0.22);
    \\draw[line width=1pt] (0.65,0) arc (0:30:0.65);
    \\fill (A) circle (1pt) node[below left] {$A$};
    \\fill (H) circle (1pt) node[below right] {$H$};
    \\fill (B) circle (1pt) node[above right] {$B$};
    \\node at (0.95,0.22) {$30^\\circ$};
    \\end{tikzpicture}
    \\end{center}''')

        # Nội dung câu hỏi
        noidungcauhoi = ('''Một chiếc máy bay phản lực cất cánh từ đường băng tại $A$ và bay lên theo đường thẳng $AB$ tạo với phương nằm ngang $AH$ một góc $30^\\circ$ với vận tốc không đổi $%s\\text{ km/h}$ (như hình vẽ). \\\\
    a) Hỏi sau $%s\\text{ phút}$, máy bay lên cao được bao nhiêu kilômét theo phương thẳng đứng và bay xa được bao nhiêu kilômét theo phương nằm ngang (làm tròn đến chữ số thập phân thứ hai)? \\\\
    b) Để đạt được độ cao hành trình là $%s\\text{ km}$, máy bay cần duy trì góc cất cánh và vận tốc trên trong thời gian bao nhiêu phút?
    %s''' % (v, phut_str, cao_muc_tieu, hinhve))

        # Nội dung lời giải
        loigiai = ('''\\begin{enumEX}[a)]{1}
    \\item Đổi $%s\\text{ phút} = \\dfrac{%s}{60}\\text{ giờ}$. Quãng đường máy bay đi được theo đường bay là $AB = %s \\cdot \\dfrac{%s}{60} = %s\\text{ (km)}$.\\\\
    Xét tam giác $ABH$ vuông tại $H$, theo Định lí 1 ta có:\\\\
    Độ cao máy bay đạt được là $BH = AB \\cdot \\sin 30^\\circ = %s \\cdot \\dfrac{1}{2} = %s\\text{ (km)}$.\\\\
    Khoảng cách theo phương nằm ngang là $AH = AB \\cdot \\cos 30^\\circ = %s \\cdot \\dfrac{\\sqrt{3}}{2} = %s \\approx %s\\text{ (km)}$.
    \\item Để đạt được độ cao $BH' = %s\\text{ km}$, quãng đường máy bay cần bay là:\\\\
    $AB' = \\dfrac{BH'}{\\sin 30^\\circ} = \\dfrac{%s}{\\dfrac{1}{2}} = %s\\text{ (km)}$.\\\\
    Thời gian bay cần thiết là $t = \\dfrac{%s}{%s}\\text{ giờ} = \\dfrac{%s \\cdot 60}{%s} = %s\\text{ (phút)}$.
    \\end{enumEX}'''
                   % (phut_str, phut_str, v, phut_str, s_km,
                      s_km, latex(bh_sym),
                      s_km, latex(ah_sym), ah_str,
                      cao_muc_tieu, cao_muc_tieu, qd_muc_tieu,
                      qd_muc_tieu, v, qd_muc_tieu, v, tg_str))

    # Xuất câu hỏi
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) +
               '\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
