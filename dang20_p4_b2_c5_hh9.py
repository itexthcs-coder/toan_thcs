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

def bt_dang20_p4_b2_c5_hh9(self):
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        R = random.choice([4, 6, 8, 10, 12])
        nua_R = R // 2

        noidungcauhoi = ('''Một chiếc bánh tét khi cắt khoanh tạo thành mặt cắt hình tròn tâm $O$, bán kính $R = %s\\text{ cm}$. Người ta dùng hai sợi lạt căng thẳng đặt song song nhau trên mặt khoanh bánh để chia bánh, tạo thành hai dây cung $AB$ và $CD$ sao cho $\\text{sđ}\\overset\\frown{AB}_{\\text{nhỏ}} = 60^\\circ$ và $\\text{sđ}\\overset\\frown{CD}_{\\text{nhỏ}} = 120^\\circ$ (như hình vẽ).\\\\
                         a) Tính độ dài của hai dây cung $AB$ và $CD$.\\\\
                         b) Tính khoảng cách giữa hai sợi lạt trong hai trường hợp: hai sợi lạt nằm cùng một phía đối với tâm $O$ và hai sợi lạt nằm về hai phía đối với tâm $O$.
                         \\begin{center}
                         \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
                         \\coordinate (O) at (0,0);
                         \\coordinate (A) at (120:1.8);
                         \\coordinate (B) at (60:1.8);
                         \\coordinate (C) at (150:1.8);
                         \\coordinate (D) at (30:1.8);
                         \\coordinate (H) at (0,1.56);
                         \\coordinate (K) at (0,0.9);
                         \\draw[line width=1pt] (O) circle (1.8);
                         \\draw[line width=1pt] (A)--(B) (C)--(D) (O)--(A) (O)--(C);
                         \\draw[line width=1pt, dashed] (O)--(H);
                         \\fill (O) circle (1pt) node[below] {$O$};
                         \\fill (A) circle (1pt) node[above left] {$A$};
                         \\fill (B) circle (1pt) node[above right] {$B$};
                         \\fill (C) circle (1pt) node[left] {$C$};
                         \\fill (D) circle (1pt) node[right] {$D$};
                         \\fill (H) circle (1pt) node[above] {$H$};
                         \\fill (K) circle (1pt) node[below right] {$K$};
                         \\end{tikzpicture}
                         \\end{center}'''
                         % (R))

        loigiai = ('''\\begin{enumEX}[a)]{1}
                        \\item Vì $\\text{sđ}\\overset\\frown{AB}_{\\text{nhỏ}} = 60^\\circ$ nên $\\widehat{AOB} = 60^\\circ$. Tam giác $OAB$ có $OA = OB = %s\\text{ cm}$ và $\\widehat{AOB} = 60^\\circ$ nên là tam giác đều, suy ra $AB = %s\\text{ cm}$.\\\\
                        Kẻ $OK \\perp CD$ tại $K$. Vì $\\text{sđ}\\overset\\frown{CD}_{\\text{nhỏ}} = 120^\\circ$ nên $\\widehat{COD} = 120^\\circ \\Rightarrow \\widehat{COK} = 60^\\circ$.\\\\
                        Trong tam giác $OKC$ vuông tại $K$, ta có $CK = OC \\cdot \\sin 60^\\circ = %s \\cdot \\dfrac{\\sqrt{3}}{2} = %s\\sqrt{3}\\text{ cm}$.\\\\
                        Vậy $CD = 2CK = %s\\sqrt{3}\\text{ cm}$.
                        \\item Kẻ $OH \\perp AB$ tại $H$. Trong tam giác đều $OAB$ cạnh $%s\\text{ cm}$, đường cao $OH = %s\\sqrt{3}\\text{ cm}$.\\\\
                        Trong tam giác $OKC$ vuông tại $K$, ta có $OK = OC \\cdot \\cos 60^\\circ = %s \\cdot \\dfrac{1}{2} = %s\\text{ cm}$.\\\\
                        - Trường hợp $1$: Hai sợi lạt $AB$ và $CD$ nằm cùng một phía đối với tâm $O$, khoảng cách giữa chúng bằng $OH - OK = (%s\\sqrt{3} - %s)\\text{ cm}$.\\\\
                        - Trường hợp $2$: Hai sợi lạt $AB$ và $CD$ nằm về hai phía đối với tâm $O$, khoảng cách giữa chúng bằng $OH + OK = (%s\\sqrt{3} + %s)\\text{ cm}$.
                        \\end{enumEX}'''
                   % (R, R, R, nua_R, R, R, nua_R, R, nua_R, nua_R, nua_R, nua_R, nua_R))

    # Xuất câu hỏi tự luận
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) +
               '\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
