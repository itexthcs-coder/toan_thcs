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


def bt_dang1_p4_b3_c9_hh9(self):
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        gocA = randint(66, 86)
        gocB = randint(104, 124)
        gocBCD = 180 - gocA
        gocBCx = gocA
        gocDAy = 180 - gocA
        gocBCm = Rational(gocBCx, 2)
        gocDAn = Rational(gocDAy, 2)
        gocBCm_str = str(float(gocBCm)).replace('.0', '').replace('.', ',')
        gocDAn_str = str(float(gocDAn)).replace('.0', '').replace('.', ',')

        hinhve = ('''\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (O) at (0,0);
\\coordinate (A) at (145:1.5);
\\coordinate (B) at (220:1.5);
\\coordinate (C) at (-30:1.5);
\\coordinate (D) at (50:1.5);
\\coordinate (X) at ($(C)!-0.7!(D)$);
\\coordinate (Y) at ($(A)!-0.7!(B)$);
\\draw[line width=1pt] (O) circle (1.5);
\\draw[line width=1pt] (A)--(B)--(C)--(D)--cycle;
\\draw[line width=1pt] (C)--(X) (A)--(Y);
\\fill (O) circle (1pt) node[below] {$O$};
\\fill (A) circle (1pt) node[above left] {$A$};
\\fill (B) circle (1pt) node[below left] {$B$};
\\fill (C) circle (1pt) node[below] {$C$};
\\fill (D) circle (1pt) node[above right] {$D$};
\\node[below right] at (X) {$x$};
\\node[above left] at (Y) {$y$};
\\end{tikzpicture}
\\end{center}''')

        noidungcauhoi = ('''Cho tứ giác $ABCD$ nội tiếp đường tròn $(O)$ có $\\widehat{DAB} = %s^\\circ$ và $\\widehat{ABC} = %s^\\circ$. Gọi $Cx$ là tia đối của tia $CD$ và $Ay$ là tia đối của tia $AB$. Kẻ tia phân giác $Cm$ của góc $BCx$ và tia phân giác $An$ của góc $DAy$. \\\\
a) Tính số đo các góc $\\widehat{BCx}$ và $\\widehat{DAy}$. \\\\
b) Chứng minh rằng hai đường thẳng $Cm$ và $An$ song song với nhau.%s''' % (gocA, gocB, hinhve))

        loigiai = ('''\\begin{enumEX}[a)]{1}
\\item Vì tứ giác $ABCD$ nội tiếp đường tròn $(O)$ nên $\\widehat{DAB} + \\widehat{BCD} = 180^\\circ \\Rightarrow \\widehat{BCD} = 180^\\circ - %s^\\circ = %s^\\circ$.\\\\
Hai góc $\\widehat{BCD}$ và $\\widehat{BCx}$ kề bù nên $\\widehat{BCx} = 180^\\circ - \\widehat{BCD} = 180^\\circ - %s^\\circ = %s^\\circ$.\\\\
Hai góc $\\widehat{DAB}$ và $\\widehat{DAy}$ kề bù nên $\\widehat{DAy} = 180^\\circ - \\widehat{DAB} = 180^\\circ - %s^\\circ = %s^\\circ$.
\\item Vì $Cm$ là tia phân giác của $\\widehat{BCx}$ nên $\\widehat{BCm} = \\dfrac{\\widehat{BCx}}{2} = \\dfrac{%s^\\circ}{2} = %s^\\circ$.\\\\
Tương tự, $An$ là tia phân giác của $\\widehat{DAy}$ nên $\\widehat{nAB} = \\widehat{nAD} + \\widehat{DAB} = \\dfrac{%s^\\circ}{2} + %s^\\circ = %s^\\circ + %s^\\circ = %s^\\circ$.\\\\
Ta thấy $\\widehat{ABC} + \\widehat{BCm}$ và $\\widehat{nAB}$ tạo thành cặp góc trong cùng phía đối với hai đường thẳng $An, Cm$ cắt $AB$ có tổng bằng:\\\\
$\\widehat{nAB} + \\widehat{ABm} = %s^\\circ + (%s^\\circ - %s^\\circ)$ (xét góc $\\widehat{nAC}$ hoặc góc kề bù: $\\widehat{yAn} = %s^\\circ$, $\\widehat{mCx} = %s^\\circ$).\\\\
Cụ thể hơn: $\\widehat{mCD} = 180^\\circ - \\widehat{BCm} = 180^\\circ - %s^\\circ = %s^\\circ$. Trong tứ giác $ABCD$ có $\\widehat{ADC} = 180^\\circ - %s^\\circ = %s^\\circ$. Xét hai đường thẳng $An$ và $Cm$ bị cắt bởi cát tuyến $AD$, ta có $\\widehat{yAn} = %s^\\circ$ và $\\widehat{nAD} = %s^\\circ$, kết hợp tổng các góc trong tứ giác cho ta hai góc đồng vị bằng nhau, suy ra $Cm // An$.
\\end{enumEX}''' % (gocA, gocBCD, gocBCD, gocBCx, gocA, gocDAy, gocBCx, gocBCm_str, gocDAy, gocA, gocDAn_str, gocA, str(float(gocDAn + gocA)).replace('.0', '').replace('.', ','), str(float(gocDAn + gocA)).replace('.0', '').replace('.', ','), gocB, gocBCm_str, gocDAn_str, gocBCm_str, gocBCm_str, str(float(180 - gocBCm)).replace('.0', '').replace('.', ','), gocB, 180 - gocB, gocDAn_str, gocDAn_str))

    # Xuất câu hỏi và lời giải
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) +
               '\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
