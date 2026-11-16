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


def bt_dang15_p4_b1_c4_hh9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        ab = 2 * randint(2, 6)
        ac = randint(4, 10)
        ah = ab // 2
        hc = ah + ac
        bc_sq = 3 * (ah**2) + hc**2
        bc_sym = sqrt(bc_sq)
        s_k = ah * ac // 2 if (ah * ac) % 2 == 0 else Rational(ah * ac, 2)

        hinh_ve = ('''\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
    \\coordinate (H) at (0,0);
    \\coordinate (A) at (1.5,0);
    \\coordinate (C) at (4.5,0);
    \\coordinate (B) at (0,2.6);
    \\draw[line width=1pt] (A)--(B)--(C)--cycle;
    \\draw[line width=1pt, dashed] (B)--(H)--(A);
    \\draw[line width=1pt] (0,0.3)--(0.3,0.3)--(0.3,0);
    \\fill (A) circle (1pt) node[below] {$A$};
    \\fill (B) circle (1pt) node[above left] {$B$};
    \\fill (C) circle (1pt) node[below right] {$C$};
    \\fill (H) circle (1pt) node[below left] {$H$};
    \\node[above right] at (0.75,1.3) {$%s\\text{ cm}$};
    \\node[below] at (3,0) {$%s\\text{ cm}$};
\\end{tikzpicture}
\\end{center}''' % (str(ab), str(ac)))

        # Nội dung câu hỏi
        noidungcauhoi = ('''Cho tam giác $ABC$ có $AB = %s\\text{ cm}$, $AC = %s\\text{ cm}$ và góc tù $\\widehat{BAC} = 120^\\circ$. Kẻ đường cao $BH$ ($H$ thuộc tia đối của tia $AC$). %s \\\\
a) Tính độ dài các đoạn thẳng $AH$ và $BH$. \\\\
b) Tính độ dài cạnh $BC$ và diện tích tam giác $ABC$.'''
                         % (str(ab), str(ac), hinh_ve))

        # Nội dung lời giải
        loigiai = ('''\\begin{enumEX}[a)]{1} \n
\\item Vì $\\widehat{BAC} = 120^\\circ$ nên góc kề bù với nó là $\\widehat{BAH} = 180^\\circ - 120^\\circ = 60^\\circ$. \\\\
Xét tam giác $AHB$ vuông tại $H$, ta có: \\\\
$AH = AB \\cdot \\cos 60^\\circ = %s \\cdot \\dfrac{1}{2} = %s\\text{ (cm)}$; \\\\
$BH = AB \\cdot \\sin 60^\\circ = %s \\cdot \\dfrac{\\sqrt{3}}{2} = %s\\sqrt{3}\\text{ (cm)}$. \n
\\item Vì điểm $A$ nằm giữa $H$ và $C$ nên $HC = HA + AC = %s + %s = %s\\text{ (cm)}$. \\\\
Áp dụng định lí Pythagore cho tam giác $BHC$ vuông tại $H$, ta có: \\\\
$BC^2 = BH^2 + HC^2 = (%s\\sqrt{3})^2 + %s^2 = %s + %s = %s \\Rightarrow BC = %s\\text{ (cm)}$. \\\\
Diện tích tam giác $ABC$ là: \\\\
$S_{ABC} = \\dfrac{1}{2} \\cdot BH \\cdot AC = \\dfrac{1}{2} \\cdot %s\\sqrt{3} \\cdot %s = %s\\sqrt{3}\\text{ (cm}^2\\text{)}$. \n
\\end{enumEX} \n'''
                   % (str(ab), str(ah), str(ab), str(ah),
                      str(ah), str(ac), str(hc),
                      str(ah), str(hc), str(3 * (ah**2)), str(hc**2), str(bc_sq), latex(bc_sym),
                      str(ah), str(ac), latex(s_k)))

    # Xuất câu tự luận
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) +
               '\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \end{minipage} \n\n')
    return content
