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


def bt_dang4_p4_b3_c9_hh9(self):
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        ma, ab, mc, cd = random.choice([(5, 7, 4, 11), (4, 8, 3, 13), (6, 9, 5, 13), (4, 11, 5, 7)])
        mb = ma + ab
        md = mc + cd

        hinhve = ('''\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (O) at (0,0);
\\coordinate (M) at (-3.2,-0.7);
\\coordinate (A) at (150:1.5);
\\coordinate (B) at (35:1.5);
\\coordinate (C) at (-140:1.5);
\\coordinate (D) at (-25:1.5);
\\draw[line width=1pt] (O) circle (1.5);
\\draw[line width=1pt] (M)--(B) (M)--(D) (A)--(C) (B)--(D);
\\fill (O) circle (1pt) node[above] {$O$};
\\fill (M) circle (1pt) node[left] {$M$};
\\fill (A) circle (1pt) node[above left] {$A$};
\\fill (B) circle (1pt) node[above right] {$B$};
\\fill (C) circle (1pt) node[below] {$C$};
\\fill (D) circle (1pt) node[below right] {$D$};
\\end{tikzpicture}
\\end{center}''')

        noidungcauhoi = ('''Cho điểm $M$ nằm ngoài đường tròn $(O)$. Qua $M$ kẻ hai đường thẳng cắt $(O)$ lần lượt tại $A, B$ ($A$ nằm giữa $M$ và $B$) và $C, D$ ($C$ nằm giữa $M$ và $D$). \\\\
a) Chứng minh rằng $\\triangle MAC \\backsim \\triangle MDB$ và $MA \\cdot MB = MC \\cdot MD$. \\\\
b) Biết $MA = %s\\text{ cm}$, $AB = %s\\text{ cm}$, $MC = %s\\text{ cm}$. Tính độ dài đoạn thẳng $CD$.%s''' % (ma, ab, mc, hinhve))

        loigiai = ('''\\begin{enumEX}[a)]{1}
\\item Vì bốn đỉnh $A, B, D, C$ cùng nằm trên đường tròn $(O)$ nên tứ giác $ABDC$ nội tiếp đường tròn $(O)$.\\\\
Do đó tổng hai góc đối nhau bằng $180^\\circ$: $\\widehat{CAB} + \\widehat{CDB} = 180^\\circ$.\\\\
Mặt khác, hai góc $\\widehat{MAC}$ và $\\widehat{CAB}$ kề bù nên $\\widehat{MAC} + \\widehat{CAB} = 180^\\circ$.\\\\
Suy ra $\\widehat{MAC} = \\widehat{CDB} = \\widehat{MDB}$.\\\\
Xét $\\triangle MAC$ và $\\triangle MDB$ có $\\widehat{M}$ chung và $\\widehat{MAC} = \\widehat{MDB}$ nên $\\triangle MAC \\backsim \\triangle MDB$ (g.g).\\\\
Từ đó suy ra tỉ số đồng dạng $\\dfrac{MA}{MD} = \\dfrac{MC}{MB} \\Rightarrow MA \\cdot MB = MC \\cdot MD$.
\\item Ta có $MB = MA + AB = %s + %s = %s\\text{ (cm)}$.\\\\
Áp dụng đẳng thức $MA \\cdot MB = MC \\cdot MD$, ta được:\\\\
$%s \\cdot %s = %s \\cdot MD \\Rightarrow MD = \\dfrac{%s}{%s} = %s\\text{ (cm)}$.\\\\
Vì $C$ nằm giữa $M$ và $D$ nên độ dài đoạn thẳng $CD = MD - MC = %s - %s = %s\\text{ (cm)}$.
\\end{enumEX}''' % (ma, ab, mb, ma, mb, mc, ma * mb, mc, md, md, mc, cd))

    # Xuất câu hỏi và lời giải
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) +
               '\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
