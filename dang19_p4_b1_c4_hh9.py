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


def bt_dang19_p4_b1_c4_hh9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        ad = randint(5, 10)
        ae = 2 * ad
        ab = randint(2, ad - 1)
        be = ae - ab
        bc = Rational(be, 3)
        ec = Rational(2 * be, 3)
        cd = ad - ec

        hinh_ve = ('''\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
    \\coordinate (D) at (0,0);
    \\coordinate (E) at (4.5,0);
    \\coordinate (A) at (0,2.6);
    \\coordinate (B) at (1.8,1.56);
    \\coordinate (C) at (1.2,0);
    \\draw[line width=1pt] (A)--(B)--(C)--(D)--cycle;
    \\draw[line width=1pt, dashed] (B)--(E)--(C);
    \\draw[line width=1pt] (0,0.3)--(0.3,0.3)--(0.3,0);
    \\fill (A) circle (1pt) node[above left] {$A$};
    \\fill (B) circle (1pt) node[above right] {$B$};
    \\fill (C) circle (1pt) node[below] {$C$};
    \\fill (D) circle (1pt) node[below left] {$D$};
    \\fill (E) circle (1pt) node[below right] {$E$};
\\end{tikzpicture}
\\end{center}''')

        # Nội dung câu hỏi
        noidungcauhoi = ('''Cho tứ giác $ABCD$ có $\\widehat{ABC} = \\widehat{ADC} = 90^\\circ$, $\\widehat{BAD} = 60^\\circ$, $AB = %s\\text{ cm}$ và $AD = %s\\text{ cm}$. Kéo dài $AB$ và $DC$ cắt nhau tại $E$. %s
a) Tính độ dài các đoạn thẳng $AE$, $BE$ và $DE$. \\\\
b) Tính độ dài các cạnh $BC$ và $CD$.'''
                         % (str(ab), str(ad), hinh_ve))

        # Nội dung lời giải
        loigiai = ('''\\begin{enumEX}[a)]{1} \n
\\item Xét tam giác $ADE$ vuông tại $D$ có $\\widehat{A} = 60^\\circ$ và $AD = %s\\text{ cm}$, ta có: \\\\
$AE = \\dfrac{AD}{\\cos 60^\\circ} = \\dfrac{%s}{\\dfrac{1}{2}} = %s\\text{ (cm)}$; \\\\
$DE = AD \\cdot \\tan 60^\\circ = %s\\sqrt{3}\\text{ (cm)}$. \\\\
Vì điểm $B$ nằm giữa $A$ và $E$ nên $BE = AE - AB = %s - %s = %s\\text{ (cm)}$. \n
\\item Trong tam giác $ADE$ vuông tại $D$ có $\\widehat{A} = 60^\\circ$, suy ra $\\widehat{E} = 90^\\circ - 60^\\circ = 30^\\circ$. \\\\
Xét tam giác $EBC$ vuông tại $B$ có $\\widehat{E} = 30^\\circ$ và $BE = %s\\text{ cm}$, ta có: \\\\
$BC = BE \\cdot \\tan 30^\\circ = %s \\cdot \\dfrac{\\sqrt{3}}{3} = %s\\sqrt{3}\\text{ (cm)}$; \\\\
$EC = \\dfrac{BE}{\\cos 30^\\circ} = \\dfrac{%s}{\\dfrac{\\sqrt{3}}{2}} = %s\\sqrt{3}\\text{ (cm)}$. \\\\
Vì điểm $C$ nằm giữa $D$ và $E$ nên $CD = DE - EC = %s\\sqrt{3} - %s\\sqrt{3} = %s\\sqrt{3}\\text{ (cm)}$. \n
\\end{enumEX} \n'''
                   % (str(ad), str(ad), str(ae), str(ad), str(ae), str(ab), str(be),
                      str(be), str(be), latex(bc), str(be), latex(ec),
                      str(ad), latex(ec), latex(cd)))

    # Xuất câu tự luận
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) +
               '\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
