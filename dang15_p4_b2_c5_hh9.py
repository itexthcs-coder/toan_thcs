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

def bt_dang15_p4_b2_c5_hh9(self):
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        R_nguyen = randint(11, 25)
        R = round(R_nguyen / 10, 1)
        tong_dai = round(6 * R, 1)
        R_str = str(R).replace('.', ',')
        tong_dai_str = str(tong_dai).replace('.', ',')

        noidungcauhoi = ('''Một ô cửa sổ kính màu hình tròn tâm $O$, bán kính $R = %s\\text{ m}$ được chia thành $6$ cánh hoa đối xứng đều nhau bởi $6$ bán kính $OA_1, OA_2, OA_3, OA_4, OA_5, OA_6$ (như hình vẽ).\\\\
                         a) Tính số đo của mỗi cung nhỏ $\\overset\\frown{A_1A_2}$ trên vành cửa sổ.\\\\
                         b) Người thợ uốn một khung thép lục giác đều $A_1A_2A_3A_4A_5A_6$ nội tiếp trong vành cửa sổ. Tính tổng chiều dài thanh thép cần dùng để làm khung lục giác đều này.
                         \\begin{center}
                         \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
                         \\coordinate (O) at (0,0);
                         \\draw[line width=1pt] (O) circle (1.8);
                         \\foreach \\k in {1,...,6} {
                             \\coordinate (A\\k) at (60*\\k-60:1.8);
                             \\draw[line width=1pt] (O)--(A\\k);
                         }
                         \\draw[line width=1pt] (A1)--(A2)--(A3)--(A4)--(A5)--(A6)--cycle;
                         \\fill (O) circle (1pt) node[below left] {$O$};
                         \\fill (A1) circle (1pt) node[right] {$A_1$};
                         \\fill (A2) circle (1pt) node[above right] {$A_2$};
                         \\fill (A3) circle (1pt) node[above left] {$A_3$};
                         \\fill (A4) circle (1pt) node[left] {$A_4$};
                         \\fill (A5) circle (1pt) node[below left] {$A_5$};
                         \\fill (A6) circle (1pt) node[below right] {$A_6$};
                         \\end{tikzpicture}
                         \\end{center}'''
                         % (R_str))

        loigiai = ('''\\begin{enumEX}[a)]{1}
                        \\item Vì vành cửa sổ hình tròn $360^\\circ$ được chia thành $6$ cung nhỏ bằng nhau nên số đo của mỗi cung nhỏ $\\overset\\frown{A_1A_2}$ bằng $\\dfrac{360^\\circ}{6} = 60^\\circ$.
                        \\item Với mỗi cạnh $A_iA_{i+1}$ của lục giác đều, tam giác $OA_iA_{i+1}$ có $OA_i = OA_{i+1} = R = %s\\text{ m}$ và góc ở tâm $\\widehat{A_iOA_{i+1}} = 60^\\circ$ nên là tam giác đều.\\\\
                        Suy ra độ dài mỗi cạnh của khung lục giác đều bằng $R = %s\\text{ m}$.\\\\
                        Vậy tổng chiều dài thanh thép cần dùng để làm khung lục giác đều gồm $6$ cạnh là $6 \\cdot %s = %s\\text{ m}$.
                        \\end{enumEX}'''
                   % (R_str, R_str, R_str, tong_dai_str))

    # Xuất câu hỏi tự luận
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) +
               '\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
