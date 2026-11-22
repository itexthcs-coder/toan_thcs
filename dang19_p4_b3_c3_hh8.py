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

def bt_dang19_p4_b3_c3_hh8(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        s_mab = randint(10, 20)
        s_mbc = randint(12, 24)
        s_mcd = randint(14, 26)
        s_mad = s_mab + s_mcd - s_mbc
        
        hinh_ve = '''\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (A) at (1.2,2.6);
\\coordinate (B) at (5.6,2.6);
\\coordinate (D) at (0,0);
\\coordinate (C) at (4.4,0);
\\coordinate (M) at (2.4,1.1);
\\coordinate (E) at (0.51,1.1);
\\coordinate (F) at (4.91,1.1);
\\draw[line width=1pt] (A)--(B)--(C)--(D)--cycle (M)--(A) (M)--(B) (M)--(C) (M)--(D);
\\draw[line width=1pt, dashed] (E)--(F);
\\fill (A) circle (1pt) node[above left] {$A$};
\\fill (B) circle (1pt) node[above right] {$B$};
\\fill (C) circle (1pt) node[below right] {$C$};
\\fill (D) circle (1pt) node[below left] {$D$};
\\fill (M) circle (1pt) node[below] {$M$};
\\fill (E) circle (1pt) node[left] {$E$};
\\fill (F) circle (1pt) node[right] {$F$};
\\end{tikzpicture}
\\end{center}'''
        
        noidungcauhoi = ('''Cho hình bình hành $ABCD$ có diện tích bằng $S$. Lấy một điểm $M$ bất kì nằm bên trong hình bình hành $ABCD$ (như hình vẽ). \\\\
a) Chứng minh rằng $S_{MAB} + S_{MCD} = \\frac{1}{2}S$. \\\\
b) Giả sử diện tích các tam giác $MAB$, $MBC$, $MCD$ lần lượt là $%s\\text{ cm}^2$, $%s\\text{ cm}^2$, $%s\\text{ cm}^2$. Tính diện tích tam giác $MAD$.
%s''' % (s_mab, s_mbc, s_mcd, hinh_ve))
        
        loigiai = ('''\\begin{enumEX}[a)]{1}
\\item Qua $M$ kẻ đường thẳng song song với $AB$ cắt $AD$ tại $E$ và cắt $BC$ tại $F$. \\\\
Tứ giác $ABFE$ có $AB // EF$ và $AE // BF$ (do $AD // BC$) nên $ABFE$ là hình bình hành. \\\\
Tam giác $MAB$ và hình bình hành $ABFE$ có chung cạnh đáy $AB$ và chiều cao hạ từ $M$ xuống $AB$ bằng chiều cao của hình bình hành $ABFE$, nên $S_{MAB} = \\frac{1}{2}S_{ABFE}$. \\\\
Tương tự, tứ giác $EFCD$ là hình bình hành và $S_{MCD} = \\frac{1}{2}S_{EFCD}$. \\\\
Cộng vế theo vế ta được: $S_{MAB} + S_{MCD} = \\frac{1}{2}(S_{ABFE} + S_{EFCD}) = \\frac{1}{2}S$.
\\item Hoàn toàn tương tự câu a, ta chứng minh được $S_{MAD} + S_{MBC} = \\frac{1}{2}S$. \\\\
Suy ra $S_{MAD} + S_{MBC} = S_{MAB} + S_{MCD} \\Rightarrow S_{MAD} + %s = %s + %s \\Rightarrow S_{MAD} = %s$ ($\\text{cm}^2$).
\\end{enumEX}''' % (s_mbc, s_mab, s_mcd, s_mad))
    
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) +
               '\\loigiai{ \n' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
