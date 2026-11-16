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


def bt_dang20_p4_b1_c4_hh9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        ten_goc = random.choice(['\\alpha', '\\beta', 'x'])

        hinh_ve = ('''\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
    \\coordinate (A) at (0,0);
    \\coordinate (B) at (4,0);
    \\coordinate (C) at (0,2.8);
    \\draw[line width=1pt] (A)--(B)--(C)--cycle;
    \\draw[line width=1pt] (0,0.3)--(0.3,0.3)--(0.3,0);
    \\fill (A) circle (1pt) node[below left] {$A$};
    \\fill (B) circle (1pt) node[below right] {$B$};
    \\fill (C) circle (1pt) node[above left] {$C$};
    \\node[above left] at (3.6,0) {$%s$};
\\end{tikzpicture}
\\end{center}''' % (ten_goc))

        # Nội dung câu hỏi
        noidungcauhoi = ('''Cho góc nhọn $%s$. Chứng minh các bất đẳng thức sau: %s
a) $\\sin %s + \\cos %s > 1$. \\\\
b) $\\sin %s \\cdot \\cos %s \\le \\dfrac{1}{2}$. Dấu đẳng thức xảy ra khi nào?'''
                         % (ten_goc, hinh_ve, ten_goc, ten_goc, ten_goc, ten_goc))

        # Nội dung lời giải
        loigiai = ('''Xét tam giác $ABC$ vuông tại $A$ có góc nhọn $\\widehat{B} = %s$. Theo định nghĩa tỉ số lượng giác, ta có $\\sin %s = \\dfrac{AC}{BC}$ và $\\cos %s = \\dfrac{AB}{BC}$.
\\begin{enumEX}[a)]{1} \n
\\item Ta có: $\\sin %s + \\cos %s = \\dfrac{AC}{BC} + \\dfrac{AB}{BC} = \\dfrac{AC + AB}{BC}$. \\\\
Áp dụng bất đẳng thức tam giác cho $\\triangle ABC$, tổng độ dài hai cạnh luôn lớn hơn cạnh thứ ba nên $AC + AB > BC$. \\\\
Chia cả hai vế của bất đẳng thức trên cho $BC > 0$, ta được: \\\\
$\\dfrac{AC + AB}{BC} > 1 \\Leftrightarrow \\sin %s + \\cos %s > 1$. \n
\\item Với mọi số thực $AB, AC$, ta luôn có $(AB - AC)^2 \\ge 0 \\Leftrightarrow AB^2 + AC^2 \\ge 2AB \\cdot AC$. \\\\
Theo định lí Pythagore trong tam giác $ABC$ vuông tại $A$, ta có $AB^2 + AC^2 = BC^2$, suy ra: \\\\
$BC^2 \\ge 2AB \\cdot AC \\Leftrightarrow \\dfrac{AB \\cdot AC}{BC^2} \\le \\dfrac{1}{2}$. \\\\
Mặt khác, $\\sin %s \\cdot \\cos %s = \\dfrac{AC}{BC} \\cdot \\dfrac{AB}{BC} = \\dfrac{AB \\cdot AC}{BC^2}$, do đó $\\sin %s \\cdot \\cos %s \\le \\dfrac{1}{2}$. \\\\
Dấu đẳng thức xảy ra khi và chỉ khi $AB = AC$, tức là tam giác $ABC$ vuông cân tại $A$, hay góc nhọn $%s = 45^\\circ$. \n
\\end{enumEX} \n'''
                   % (ten_goc, ten_goc, ten_goc,
                      ten_goc, ten_goc, ten_goc, ten_goc,
                      ten_goc, ten_goc, ten_goc, ten_goc, ten_goc))

    # Xuất câu tự luận
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) +
               '\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
