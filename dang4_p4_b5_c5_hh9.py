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



def bt_dang4_p4_b5_c5_hh9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        bo_so = [(5, 3, 10, 6), (9, 6, 17, 8), (8, 4, 13, 5), (10, 5, 25, 20)]
        R, r, d, MN = random.choice(bo_so)
        OI = Rational(d * R, R + r)
        O1I = d - OI
        MI = sqrt(OI**2 - R**2)
        NI = MN - MI

        hinhve = '''
\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (O) at (0,0);
\\coordinate (O') at (5,0);
\\coordinate (I) at (3.125,0);
\\coordinate (M) at (1.28,1.6);
\\coordinate (N) at (4.23,-0.96);
\\draw[line width=1pt] (O) circle (2.05cm);
\\draw[line width=1pt] (O') circle (1.23cm);
\\draw[line width=1pt] (O)--(O') (O)--(M) (O')--(N);
\\draw[line width=1pt] (0.5,2.25)--(4.8,-1.44);
\\fill (O) circle (1pt) node[left] {$O$};
\\fill (O') circle (1pt) node[right] {$O'$};
\\fill (I) circle (1pt) node[above right] {$I$};
\\fill (M) circle (1pt) node[above] {$M$};
\\fill (N) circle (1pt) node[below] {$N$};
\\end{tikzpicture}
\\end{center}
'''

        noidungcauhoi = ('''Cho hai đường tròn ngoài nhau $(O; %s\\text{ cm})$ và $(O'; %s\\text{ cm})$ có khoảng cách hai tâm $OO' = %s\\text{ cm}$. Một đường thẳng $d$ tiếp xúc với $(O)$ tại $M$ và tiếp xúc với $(O')$ tại $N$ sao cho $O$ và $O'$ nằm khác phía đối với $d$. Gọi $I$ là giao điểm của $MN$ và $OO'$.\\\\
        a) Chứng minh $\\triangle OMI \\backsim \\triangle O'NI$ và tính độ dài các đoạn thẳng $OI, O'I$.\\\\
        b) Tính độ dài đoạn tiếp tuyến chung trong $MN$. %s'''
                         % (latex(R), latex(r), latex(d), hinhve))

        loigiai = ('''\\begin{enumEX}[a)]{1}
        \\item Vì đường thẳng $d$ tiếp xúc với $(O)$ tại $M$ và tiếp xúc với $(O')$ tại $N$ nên $OM \\perp MN$ và $O'N \\perp MN$, suy ra $\\widehat{OMI} = \\widehat{O'NI} = 90^\\circ$.\\\\
        Xét $\\triangle OMI$ và $\\triangle O'NI$ có:\\\\
        $\\widehat{OMI} = \\widehat{O'NI} = 90^\\circ$ và $\\widehat{OIM} = \\widehat{O'IN}$ (hai góc đối đỉnh).\\\\
        Do đó $\\triangle OMI \\backsim \\triangle O'NI$ (g.g).\\\\
        Suy ra $\\frac{OI}{O'I} = \\frac{OM}{O'N} = \\frac{%s}{%s}$.\\\\
        Vì $O$ và $O'$ nằm khác phía đối với $d$ nên $I$ nằm giữa $O$ và $O'$, do đó $OI + O'I = OO' = %s\\text{ cm}$.\\\\
        Từ $\\frac{OI}{%s} = \\frac{O'I}{%s} = \\frac{OI + O'I}{%s + %s} = \\frac{%s}{%s}$, ta tính được:\\\\
        $OI = %s\\text{ cm}$ và $O'I = %s\\text{ cm}$.
        \\item Áp dụng định lí Pythagore vào tam giác vuông $OMI$, ta có:\\\\
        $MI = \\sqrt{OI^2 - OM^2} = \\sqrt{\\left(%s\\right)^2 - %s^2} = %s\\text{ (cm)}$.\\\\
        Áp dụng định lí Pythagore vào tam giác vuông $O'NI$, ta có:\\\\
        $NI = \\sqrt{O'I^2 - O'N^2} = \\sqrt{\\left(%s\\right)^2 - %s^2} = %s\\text{ (cm)}$.\\\\
        Vì $I$ nằm giữa $M$ và $N$ nên độ dài đoạn tiếp tuyến chung trong là:\\\\
        $MN = MI + NI = %s + %s = %s\\text{ (cm)}$.
        \\end{enumEX}'''
                   % (latex(R), latex(r), latex(d),
                      latex(R), latex(r), latex(R), latex(r), latex(d), latex(R + r),
                      latex(OI), latex(O1I),
                      latex(OI), latex(R), latex(MI),
                      latex(O1I), latex(r), latex(NI),
                      latex(MI), latex(NI), latex(MN)))

    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) +
               '\n\\loigiai{' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
