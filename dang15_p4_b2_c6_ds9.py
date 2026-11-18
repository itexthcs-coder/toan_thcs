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


def bt_dang15_p4_b2_c6_ds9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        R_val = randint(2, 6)
        h = randint(3, 9)
        S_coeff = 2 * (R_val**2 + h * R_val)
        c_pt = R_val**2 + h * R_val
        delta = h**2 + 4*c_pt
        R_neg = -(R_val + h)
        
        # Vẽ hình minh họa theo đúng chuẩn TikZ (không random tọa độ điểm)
        hinhve = ('''\\begin{center}
                   \\begin{tikzpicture}[scale=0.85, font=\\footnotesize, line join=round, line cap=round, >=stealth]
                   \\draw[line width=1pt] (0,0) ellipse (1.6cm and 0.45cm);
                   \\draw[line width=1pt] (-1.6,-3) arc (180:360:1.6cm and 0.45cm);
                   \\draw[line width=1pt, dashed] (-1.6,-3) arc (180:0:1.6cm and 0.45cm);
                   \\draw[line width=1pt] (-1.6,0) -- (-1.6,-3);
                   \\draw[line width=1pt] (1.6,0) -- (1.6,-3);
                   \\coordinate (O) at (0,0);
                   \\coordinate (O1) at (0,-3);
                   \\coordinate (A) at (1.6,-3);
                   \\draw[line width=1pt, dashed] (O) -- (O1) -- (A);
                   \\fill (O) circle (1pt) node[above] {$O$};
                   \\fill (O1) circle (1pt) node[below] {$O'$};
                   \\fill (A) circle (1pt) node[right] {$A$};
                   \\node[left] at (0,-1.5) {$h$};
                   \\node[below] at (0.8,-3) {$R$};
                   \\end{tikzpicture}
                   \\end{center}''')
        
        # Nội dung câu hỏi
        noidungcauhoi = ('''Một hình trụ có chiều cao $h = %s\\text{ cm}$ và diện tích toàn phần bằng $%s\\pi\\text{ cm}^2$ (như hình vẽ minh họa). Tính bán kính đáy $R$ của hình trụ đó (biết công thức tính diện tích toàn phần hình trụ là $S_{tp} = 2\\pi R^2 + 2\\pi Rh$). %s'''
                         %(latex(h), latex(S_coeff), hinhve
                         ))
        
        # Nội dung lời giải
        loigiai = ('''Điều kiện: bán kính đáy $R > 0$ ($\\text{cm}$). \\\\
                   Thay $h = %s\\text{ cm}$ và $S_{tp} = %s\\pi\\text{ cm}^2$ vào công thức tính diện tích toàn phần của hình trụ, ta được: \\\\
                   $2\\pi R^2 + 2\\pi R \\cdot %s = %s\\pi$ \\\\
                   Chia cả hai vế của phương trình cho $2\\pi$, ta được phương trình bậc hai ẩn $R$: \\\\
                   $R^2 + %sR = %s \\Leftrightarrow R^2 + %sR - %s = 0$. \\\\
                   Phương trình bậc hai trên có $a = 1$, $b = %s$, $c = -%s$. \\\\
                   Ta có biệt thức $\\Delta = %s^2 - 4 \\cdot 1 \\cdot (-%s) = %s > 0$. \\\\
                   Phương trình có hai nghiệm phân biệt: \\\\
                   $R_1 = \\dfrac{-%s + \\sqrt{%s}}{2 \\cdot 1} = %s$ (thỏa mãn điều kiện $R > 0$); \\\\
                   $R_2 = \\dfrac{-%s - \\sqrt{%s}}{2 \\cdot 1} = %s$ (không thỏa mãn điều kiện nên loại). \\\\
                   Vậy bán kính đáy của hình trụ là $R = %s\\text{ cm}$.'''
                   %(latex(h), latex(S_coeff),
                     latex(h), latex(S_coeff),
                     latex(h), latex(c_pt), latex(h), latex(c_pt),
                     latex(h), latex(c_pt),
                     latex(h), latex(c_pt), latex(delta),
                     latex(h), latex(delta), latex(R_val),
                     latex(h), latex(delta), latex(R_neg),
                     latex(R_val)
                   ))

    # Xuất câu hỏi tự luận
    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n' +
               '\\loigiai{ \n' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
