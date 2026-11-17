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


def bt_dang7_p3_b5_c5_hh9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        R2 = randint(4, 7)
        R1 = R2 + randint(4, 8)
        AB = randint(4, 2 * R2 - 1)
        BC_val = Rational(AB * (R1 - R2), R2)
        number = Decimal(float(BC_val))
        kq = number.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
        if kq == int(kq):
            kq_str = str(int(kq))
        else:
            kq_str = str(kq).replace('.', ',')

        hinhve = ('''\\begin{center}
\\begin{tikzpicture}[scale=0.8, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (O) at (0,0);
\\coordinate (Op) at (1.1,0);
\\coordinate (A) at (2.4,0);
\\coordinate (B) at (0.52, 1.16);
\\coordinate (C) at (-1.06, 2.15);
\\draw[line width=1pt] (O) circle (2.4cm);
\\draw[line width=1pt] (Op) circle (1.3cm);
\\draw[line width=1pt] (O)--(A) (A)--(C) (O)--(C) (Op)--(B);
\\fill (O) circle (1pt) node[below] {$O$};
\\fill (Op) circle (1pt) node[below] {$O'$};
\\fill (A) circle (1pt) node[right] {$A$};
\\fill (B) circle (1pt) node[above right] {$B$};
\\fill (C) circle (1pt) node[above left] {$C$};
\\end{tikzpicture}
\\end{center}''')

        noidungcauhoi = ('''Cho hai đường tròn $(O; %s\\text{ cm})$ và $(O'; %s\\text{ cm})$ tiếp xúc trong tại $A$. Một cát tuyến đi qua $A$ cắt $(O')$ tại $B$ và cắt $(O)$ tại $C$ (với $B$ nằm giữa $A$ và $C$). Biết $AB = %s\\text{ cm}$, tính độ dài đoạn thẳng $BC$ (đơn vị: $\\text{cm}$, làm tròn kết quả đến hàng phần mười nếu cần).\\\\
%s''' % (R1, R2, AB, hinhve))

        loigiai = ('''Vì hai đường tròn $(O)$ và $(O')$ tiếp xúc trong tại $A$ nên tiếp điểm $A$ thẳng hàng với hai tâm $O, O'$. \\\\
Xét tam giác $O'AB$ cân tại $O'$ ($O'A = O'B = %s\\text{ cm}$) nên $\\widehat{O'BA} = \\widehat{O'AB}$. \\\\
Xét tam giác $OAC$ cân tại $O$ ($OA = OC = %s\\text{ cm}$) nên $\\widehat{OCA} = \\widehat{OAC}$. \\\\
Do $O, O', A$ thẳng hàng nên $\\widehat{O'BA} = \\widehat{OCA}$, mà hai góc này ở vị trí đồng vị nên $O'B // OC$. \\\\
Áp dụng định lí Thalès vào tam giác $OAC$ với $O'B // OC$, ta có: \\\\
$\\dfrac{AB}{AC} = \\dfrac{O'A}{OA} = \\dfrac{%s}{%s} \\Rightarrow AC = \\dfrac{%s \\cdot %s}{%s} = %s\\text{ (cm)}$. \\\\
Vì $B$ nằm giữa $A$ và $C$ nên độ dài đoạn thẳng $BC$ là: \\\\
$BC = AC - AB = %s - %s = %s \\approx %s\\text{ (cm)}$.'''
                   % (R2, R1, R2, R1, AB, R1, R2, latex(Rational(AB * R1, R2)),
                      latex(Rational(AB * R1, R2)), AB, latex(BC_val), kq_str))

        dapan = '\\shortans[0]{$%s$}\n' % (kq_str)

    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) +
               str(dapan) +
               '\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
