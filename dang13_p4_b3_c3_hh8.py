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

def bt_dang13_p4_b3_c3_hh8(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        bb1 = randint(2, 6)
        cc1 = randint(4, 9)
        aa1 = bb1 + cc1
        
        hinh_ve = '''\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\draw[line width=1pt] (-0.5,1.2)--(5.5,1.2) node[below] {$d$};
\\coordinate (A) at (2.2,3.6);
\\coordinate (B) at (0.4,0);
\\coordinate (C) at (4.6,0);
\\coordinate (I) at (2.5,0);
\\coordinate (G) at (2.4,1.2);
\\coordinate (A1) at (2.2,1.2);
\\coordinate (B1) at (0.4,1.2);
\\coordinate (C1) at (4.6,1.2);
\\draw[line width=1pt] (A)--(B)--(C)--cycle;
\\draw[line width=1pt, dashed] (A)--(I) (A)--(A1) (B)--(B1) (C)--(C1);
\\fill (A) circle (1pt) node[above] {$A$};
\\fill (B) circle (1pt) node[below left] {$B$};
\\fill (C) circle (1pt) node[below right] {$C$};
\\fill (I) circle (1pt) node[below] {$I$};
\\fill (G) circle (1pt) node[above right] {$G$};
\\fill (A1) circle (1pt) node[below] {$A'$};
\\fill (B1) circle (1pt) node[above] {$B'$};
\\fill (C1) circle (1pt) node[above] {$C'$};
\\end{tikzpicture}
\\end{center}'''
        
        noidungcauhoi = ('''Cho tam giác $ABC$ có trọng tâm $G$. Qua $G$ kẻ đường thẳng $d$ cắt cạnh $AB$ và cạnh $AC$. Gọi $A', B', C'$ lần lượt là hình chiếu vuông góc của $A, B, C$ trên đường thẳng $d$ (như hình vẽ). \\\\
a) Chứng minh rằng $AA' = BB' + CC'$. \\\\
b) Biết $BB' = %s$ cm và $CC' = %s$ cm. Tính độ dài đoạn thẳng $AA'$.
%s''' % (bb1, cc1, hinh_ve))
        
        loigiai = ('''\\begin{enumEX}[a)]{1}
\\item Gọi $I$ là trung điểm của $BC$, $I'$ là hình chiếu vuông góc của $I$ trên $d$. \\\\
Vì $BB' // II' // CC'$ (cùng vuông góc với $d$) và $IB = IC$ nên $II'$ là đường trung bình của hình thang $BB'C'C$, suy ra $BB' + CC' = 2II'$. \\\\
Lấy $K$ là trung điểm của $AG$, $K'$ là hình chiếu vuông góc của $K$ trên $d$. Vì $G$ là trọng tâm $\\Delta ABC$ nên $GA = 2GI$, suy ra $GK = GI$. \\\\
Hai tam giác vuông $GKK'$ và $GII'$ có $GK = GI$ và $\\widehat{KGK'} = \\widehat{IGI'}$ (đối đỉnh) nên $\\Delta GKK' = \\Delta GII'$ (cạnh huyền – góc nhọn), suy ra $KK' = II'$. \\\\
Mặt khác, $KK'$ là đường trung bình của $\\Delta AA'G$ nên $AA' = 2KK' = 2II' = BB' + CC'$.
\\item Thay $BB' = %s$ cm và $CC' = %s$ cm vào hệ thức trên, ta được: $AA' = %s + %s = %s$ (cm).
\\end{enumEX}''' % (bb1, cc1, bb1, cc1, aa1))
    
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) +
               '\\loigiai{ \n' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
