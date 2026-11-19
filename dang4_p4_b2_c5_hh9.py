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

def bt_dang4_p4_b2_c5_hh9(self):
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        R = randint(4, 15)
        CD = 2 * R

        noidungcauhoi = ('''Cho hình thang cân $ABCD$ ($AB // CD$) có đáy lớn $CD = %s\\text{ cm}$, cạnh bên $AD = BC = %s\\text{ cm}$ và góc ở đáy $\\widehat{ADC} = 60^\\circ$ (như hình vẽ).\\\\
                         a) Gọi $O$ là trung điểm của cạnh đáy $CD$. Chứng minh rằng bốn điểm $A, B, C, D$ cùng nằm trên đường tròn tâm $O$ và xác định bán kính của đường tròn đó.\\\\
                         b) Tính số đo của các cung nhỏ $\\overset\\frown{AD}$, $\\overset\\frown{AB}$ và $\\overset\\frown{BC}$ của đường tròn $(O)$.
                         \\begin{center}
                         \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
                         \\coordinate (O) at (0,0);
                         \\coordinate (D) at (-1.8,0);
                         \\coordinate (C) at (1.8,0);
                         \\coordinate (A) at (120:1.8);
                         \\coordinate (B) at (60:1.8);
                         \\draw[line width=1pt, dashed] (O) circle (1.8);
                         \\draw[line width=1pt] (D)--(A)--(B)--(C)--cycle (O)--(A) (O)--(B);
                         \\fill (O) circle (1pt) node[below] {$O$};
                         \\fill (D) circle (1pt) node[left] {$D$};
                         \\fill (C) circle (1pt) node[right] {$C$};
                         \\fill (A) circle (1pt) node[above left] {$A$};
                         \\fill (B) circle (1pt) node[above right] {$B$};
                         \\end{tikzpicture}
                         \\end{center}'''
                         % (CD, R))

        loigiai = ('''\\begin{enumEX}[a)]{1}
                        \\item Vì $O$ là trung điểm của $CD = %s\\text{ cm}$ nên $OD = OC = \\dfrac{CD}{2} = %s\\text{ cm}$.\\\\
                        Xét tam giác $OAD$ có $OD = AD = %s\\text{ cm}$ và $\\widehat{ADO} = 60^\\circ$ nên tam giác $OAD$ là tam giác đều, suy ra $OA = OD = %s\\text{ cm}$.\\\\
                        Vì $ABCD$ là hình thang cân nên $\\widehat{BCD} = \\widehat{ADC} = 60^\\circ$.\\\\
                        Xét tam giác $OBC$ có $OC = BC = %s\\text{ cm}$ và $\\widehat{BCO} = 60^\\circ$ nên tam giác $OBC$ là tam giác đều, suy ra $OB = OC = %s\\text{ cm}$.\\\\
                        Vậy $OA = OB = OC = OD = %s\\text{ cm}$, do đó bốn điểm $A, B, C, D$ cùng nằm trên đường tròn tâm $O$ bán kính $R = %s\\text{ cm}$.
                        \\item Vì các tam giác $OAD$ và $OBC$ đều nên $\\widehat{AOD} = 60^\\circ$ và $\\widehat{BOC} = 60^\\circ$.\\\\
                        Suy ra $\\text{sđ}\\overset\\frown{AD}_{\\text{nhỏ}} = \\widehat{AOD} = 60^\\circ$ và $\\text{sđ}\\overset\\frown{BC}_{\\text{nhỏ}} = \\widehat{BOC} = 60^\\circ$.\\\\
                        Vì $D, O, C$ thẳng hàng nên $\\widehat{AOB} = 180^\\circ - (\\widehat{AOD} + \\widehat{BOC}) = 180^\\circ - (60^\\circ + 60^\\circ) = 60^\\circ$.\\\\
                        Vậy $\\text{sđ}\\overset\\frown{AB}_{\\text{nhỏ}} = \\widehat{AOB} = 60^\\circ$.
                        \\end{enumEX}'''
                   % (CD, R, R, R, R, R, R, R))

    # Xuất câu hỏi tự luận
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) +
               '\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
