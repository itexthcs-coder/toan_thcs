# -*- coding: utf-8 -*-
"""
Created on Wed Dec 18 17:27:56 2024

@author: Pham Ngoc Chien
"""
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

def bt_dang19_p4_b2_c5_hh9(self):
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        goc_aob = random.choice([30, 40, 50, 60])
        nua_goc = goc_aob // 2
        nua_AB = random.choice([120, 150, 180, 200])
        AB = 2 * nua_AB
        R_val = nua_AB / math.sin(math.radians(nua_goc))
        OH_val = R_val * math.cos(math.radians(nua_goc))
        MH_val = R_val - OH_val

        R_round = str(Decimal(str(R_val)).quantize(Decimal('1'), rounding=ROUND_HALF_UP))
        OH_round = str(Decimal(str(OH_val)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)).replace('.', ',')
        R_1tp = str(Decimal(str(R_val)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)).replace('.', ',')
        MH_round = str(Decimal(str(MH_val)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)).replace('.', ',')

        noidungcauhoi = ('''Khi thiết kế một đoạn đường cao tốc uốn cong theo một cung tròn $\\overparen{AB}$ tâm $O$, các kĩ sư đo được góc ở tâm chắn cung $\\overparen{AB}$ bằng $%s^\\circ$ và chiều dài đường chim bay (dây cung $AB$) nối hai đầu đoạn cong bằng $%s\\text{ m}$ (như hình vẽ).\\\\
                         a) Tính bán kính $R$ của cung tròn đoạn đường cao tốc đó (làm tròn kết quả đến hàng đơn vị của mét).\\\\
                         b) Tính khoảng cách từ điểm chính giữa $M$ của cung nhỏ $\\overparen{AB}$ đến đường chim bay $AB$ (làm tròn kết quả đến hàng phần mười của mét).
                         \\begin{center}
                         \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
                         \\coordinate (O) at (0,0);
                         \\coordinate (A) at (110:2.2);
                         \\coordinate (B) at (70:2.2);
                         \\coordinate (H) at (0,2.07);
                         \\coordinate (M) at (0,2.2);
                         \\draw[line width=1pt] (B) arc (70:110:2.2);
                         \\draw[line width=1pt] (A)--(B);
                         \\draw[line width=1pt, dashed] (O)--(A) (O)--(B) (O)--(M);
                         \\fill (O) circle (1pt) node[below] {$O$};
                         \\fill (A) circle (1pt) node[left] {$A$};
                         \\fill (B) circle (1pt) node[right] {$B$};
                         \\fill (H) circle (1pt) node[below right] {$H$};
                         \\fill (M) circle (1pt) node[above] {$M$};
                         \\end{tikzpicture}
                         \\end{center}'''
                         % (goc_aob, AB))

        loigiai = ('''\\begin{enumEX}[a)]{1}
                        \\item Kẻ $OH \\perp AB$ tại $H$. Vì tam giác $OAB$ cân tại $O$ nên $H$ là trung điểm của $AB$ và $OH$ là tia phân giác của $\\widehat{AOB}$.\\\\
                        Suy ra $AH = \\dfrac{AB}{2} = \\dfrac{%s}{2} = %s\\text{ m}$ và $\\widehat{AOH} = \\dfrac{%s^\\circ}{2} = %s^\\circ$.\\\\
                        Xét tam giác $OHA$ vuông tại $H$, ta có:\\\\
                        $\\sin \\widehat{AOH} = \\dfrac{AH}{OA} \\Rightarrow R = OA = \\dfrac{AH}{\\sin %s^\\circ} = \\dfrac{%s}{\\sin %s^\\circ} \\approx %s\\text{ m}$.
                        \\item Trong tam giác $OHA$ vuông tại $H$, ta có $OH = OA \\cdot \\cos %s^\\circ = \\dfrac{%s}{\\sin %s^\\circ} \\cdot \\cos %s^\\circ \\approx %s\\text{ m}$.\\\\
                        Vì $M$ là điểm chính giữa cung nhỏ $\\overparen{AB}$ nên $O, H, M$ thẳng hàng và $OM = R \\approx %s\\text{ m}$.\\\\
                        Vậy khoảng cách từ điểm chính giữa $M$ đến đường chim bay $AB$ là $MH = OM - OH \\approx %s - %s = %s\\text{ m}$.
                        \\end{enumEX}'''
                   % (AB, nua_AB, goc_aob, nua_goc, nua_goc, nua_AB, nua_goc, R_round,
                      nua_goc, nua_AB, nua_goc, nua_goc, OH_round, R_1tp, R_1tp, OH_round, MH_round))

    # Xuất câu hỏi tự luận
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) +
               '\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
