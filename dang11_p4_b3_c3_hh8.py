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

def bt_dang11_p4_b3_c3_hh8(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        hinh_ve = '''\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (A) at (1.5,2.6);
\\coordinate (B) at (5.9,2.6);
\\coordinate (D) at (0,0);
\\coordinate (C) at (4.4,0);
\\coordinate (E) at (2.06,1.18);
\\coordinate (F) at (3.24,1.94);
\\coordinate (G) at (3.84,1.42);
\\coordinate (H) at (2.66,0.66);
\\draw[line width=1pt] (A)--(B)--(C)--(D)--cycle (A)--(F) (D)--(H) (B)--(G) (C)--(E);
\\fill (A) circle (1pt) node[above left] {$A$};
\\fill (B) circle (1pt) node[above right] {$B$};
\\fill (C) circle (1pt) node[below right] {$C$};
\\fill (D) circle (1pt) node[below left] {$D$};
\\fill (E) circle (1pt) node[left] {$E$};
\\fill (F) circle (1pt) node[above] {$F$};
\\fill (G) circle (1pt) node[right] {$G$};
\\fill (H) circle (1pt) node[below] {$H$};
\\end{tikzpicture}
\\end{center}'''
        
        noidungcauhoi = ('''Cho hình bình hành $ABCD$ ($AB > BC$). Các tia phân giác của bốn góc $A, B, C, D$ cắt nhau tạo thành tứ giác $EFGH$, trong đó $E$ là giao điểm của phân giác góc $A$ và góc $D$, $F$ là giao điểm của phân giác góc $A$ và góc $B$, $G$ là giao điểm của phân giác góc $B$ và góc $C$, $H$ là giao điểm của phân giác góc $C$ và góc $D$ (như hình vẽ). \\\\
a) Chứng minh rằng $\\widehat{AED} = 90^\\circ$ và $\\widehat{BGC} = 90^\\circ$. \\\\
b) Chứng minh rằng tứ giác $EFGH$ là hình bình hành có bốn góc vuông.
%s''' % (hinh_ve))
        
        loigiai = ('''\\begin{enumEX}[a)]{1}
\\item Trong hình bình hành $ABCD$, hai góc kề cạnh $AD$ bù nhau nên $\\widehat{BAD} + \\widehat{ADC} = 180^\\circ$. \\\\
Vì $AE$ và $DE$ lần lượt là tia phân giác của $\\widehat{BAD}$ và $\\widehat{ADC}$ nên: \\\\
$\\widehat{EAD} + \\widehat{EDA} = \\frac{1}{2}(\\widehat{BAD} + \\widehat{ADC}) = \\frac{1}{2} \\cdot 180^\\circ = 90^\\circ$. \\\\
Xét $\\Delta AED$ có $\\widehat{AED} = 180^\\circ - (\\widehat{EAD} + \\widehat{EDA}) = 180^\\circ - 90^\\circ = 90^\\circ$. \\\\
Hoàn toàn tương tự, trong $\\Delta BGC$ ta có $\\widehat{GBC} + \\widehat{GCB} = \\frac{1}{2}(\\widehat{ABC} + \\widehat{BCD}) = 90^\\circ$, suy ra $\\widehat{BGC} = 90^\\circ$.
\\item Tương tự câu a, xét $\\Delta AFB$ và $\\Delta DHC$ ta chứng minh được $\\widehat{AFB} = 90^\\circ$ và $\\widehat{DHC} = 90^\\circ$. \\\\
Do hai góc đối đỉnh bằng nhau nên $\\widehat{EFG} = \\widehat{AFB} = 90^\\circ$ và $\\widehat{EHG} = \\widehat{DHC} = 90^\\circ$. \\\\
Tứ giác $EFGH$ có $\\widehat{FEH} = \\widehat{FGH} = 90^\\circ$ và $\\widehat{EFG} = \\widehat{EHG} = 90^\\circ$ (các góc đối bằng nhau) nên theo Định lí 3a, tứ giác $EFGH$ là hình bình hành và có bốn góc vuông.
\\end{enumEX}''')
    
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) +
               '\\loigiai{ \n' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
