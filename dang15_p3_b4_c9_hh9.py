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
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QDialog, QLabel, QLineEdit, 
    QPushButton, QComboBox, QCheckBox, QTextEdit, QVBoxLayout, 
    QHBoxLayout, QGridLayout, QMessageBox, QColorDialog,
    QSplashScreen, QProgressBar
)
from PyQt5.QtCore import Qt, QSettings, QThread, pyqtSignal
from PyQt5.QtGui import QIcon, QPixmap, QFont
from PyQt5.QtGui import QFont, QBrush, QColor
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QSplitter, QTreeWidget, QTreeWidgetItem, QTextEdit, QLabel, 
    QSpacerItem, QSizePolicy, QStackedWidget, QPushButton, QCheckBox, QSpinBox,
    QScrollArea
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
from mpl_toolkits.mplot3d import Axes3D


def bt_dang15_p3_b4_c9_hh9(self):
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        duong_cheo = random.choice([6, 8, 10, 12, 14])
        r = duong_cheo // 2
        val = 16 * r * math.sin(math.radians(22.5))
        number = Decimal(str(val))
        kq = number.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
        kq_str = str(kq).replace('.', ',')

        hinh_tikz = '''\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (O) at (0,0);
\\coordinate (A) at (90:1.7);
\\coordinate (E) at (45:1.7);
\\coordinate (D) at (0:1.7);
\\coordinate (H) at (-45:1.7);
\\coordinate (C) at (-90:1.7);
\\coordinate (G) at (-135:1.7);
\\coordinate (B) at (180:1.7);
\\coordinate (F) at (135:1.7);
\\draw[line width=1pt] (O) circle (1.7);
\\draw[line width=1pt] (E)--(A)--(F)--(B)--(G)--(C)--(H)--(D)--cycle;
\\draw[line width=1pt, dashed] (A)--(C) (B)--(D);
\\fill (O) circle (1pt) node[below left] {$O$};
\\fill (A) circle (1pt) node[above] {$A$};
\\fill (E) circle (1pt) node[above right] {$E$};
\\fill (D) circle (1pt) node[right] {$D$};
\\fill (H) circle (1pt) node[below right] {$H$};
\\fill (C) circle (1pt) node[below] {$C$};
\\fill (G) circle (1pt) node[below left] {$G$};
\\fill (B) circle (1pt) node[left] {$B$};
\\fill (F) circle (1pt) node[above left] {$F$};
\\end{tikzpicture}
\\end{center}'''

        noidungcauhoi = ('''Cho hình vuông $ABCD$ có độ dài đường chéo bằng $%s\\text{ cm}$ nội tiếp đường tròn $(O)$. Phép quay thuận chiều $45^\\circ$ tâm $O$ biến các đỉnh $A, B, C, D$ lần lượt thành $E, F, G, H$, tạo thành bát giác đều $EAFBGCHD$ (như hình vẽ). Tính chu vi của bát giác đều $EAFBGCHD$ (đơn vị: $\\text{cm}$, làm tròn kết quả đến hàng phần mười). %s'''
                         % (duong_cheo, hinh_tikz))

        loigiai = ('''Bán kính đường tròn $(O)$ ngoại tiếp hình vuông $ABCD$ bằng nửa độ dài đường chéo: $R = \\frac{%s}{2} = %s\\text{ (cm)}$. \\
Bát giác đều $EAFBGCHD$ nội tiếp $(O; %s\\text{ cm})$ có mỗi cạnh bằng $2R\\sin 22,5^\\circ = %s\\sin 22,5^\\circ\\text{ (cm)}$. \\
Vậy chu vi của bát giác đều $EAFBGCHD$ là:
$$C = 8 \\cdot %s\\sin 22,5^\\circ = %s\\sin 22,5^\\circ \\approx %s\\text{ (cm)}.$$'''
                   % (duong_cheo, r, r, 2 * r, 2 * r, 16 * r, kq_str))

        dapan = '\\shortans[0]{$%s$}\n' % (str(kq_str))

    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' + str(noidungcauhoi) + '\n' + str(dapan) +
               '\\loigiai{ \n' + str(loigiai) + '}\n'
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
