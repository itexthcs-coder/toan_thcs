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


def bt_dang8_p3_b3_c5_hh9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        bo_so = [(6, 80, 120), (6, 90, 120), (4, 60, 120), (5, 60, 120), (4, 80, 120), (5, 80, 120), (4, 90, 180), (5, 90, 180)]
        R1, n1, n2 = random.choice(bo_so)
        R2 = Rational(n1 * R1, n2)
        l_coeff = Rational(n1 * R1, 180)
        S1_coeff = Rational(l_coeff * R1, 2)
        S2_coeff = Rational(l_coeff * R2, 2)
        diff_coeff = S2_coeff - S1_coeff
        val = float(diff_coeff) * 3.14
        number = Decimal(str(val))
        kq = number.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
        kq_str = str(kq).replace('.', ',')

        # Nội dung câu hỏi
        noidungcauhoi = ('''Trên đường tròn $(O_1; %d\\text{ cm})$ lấy cung $AB$ có số đo $%d^\\circ$, trên đường tròn $(O_2; R_2)$ lấy cung $CD$ có số đo $%d^\\circ$. Biết độ dài cung $AB$ bằng độ dài cung $CD$. Gọi $S_1, S_2$ lần lượt là diện tích của hình quạt tròn $O_1AB$ và hình quạt tròn $O_2CD$. Tính hiệu $S_2 - S_1$ theo đơn vị $\\text{cm}^2$ (lấy $\\pi \\approx 3,14$, làm tròn kết quả đến hàng phần mười).
\\begin{center}
\\begin{tikzpicture}[scale=0.8]
\\fill[blue!12] (0,0) -- (2.2,0) arc (0:75:2.2) -- cycle;
\\draw (0,0) -- (2.2,0) arc (0:75:2.2) -- cycle;
\\fill (0,0) circle (1.5pt) node[below left] {$O_1$};
\\node[right] at (2.2,0) {$A$};
\\node[above] at (75:2.2) {$B$};
\\node at (37:1.2) {$S_1$};
\\begin{scope}[xshift=4.2cm]
\\fill[red!12] (0,0) -- (1.4,0) arc (0:120:1.4) -- cycle;
\\draw (0,0) -- (1.4,0) arc (0:120:1.4) -- cycle;
\\fill (0,0) circle (1.5pt) node[below left] {$O_2$};
\\node[right] at (1.4,0) {$C$};
\\node[above left] at (120:1.4) {$D$};
\\node at (60:0.8) {$S_2$};
\\end{scope}
\\end{tikzpicture}
\\end{center}''' % (R1, n1, n2))

        # Nội dung lời giải
        loigiai = ('''Độ dài cung tròn $AB$ là $l_{AB} = \\dfrac{%d}{180}\\pi \\cdot %d = %s\\pi\\text{ (cm)}$. \\\\
Vì độ dài cung $CD$ bằng độ dài cung $AB$ nên:
$$\\dfrac{%d}{180}\\pi R_2 = %s\\pi \\Rightarrow R_2 = %s\\text{ (cm)}.$$
Áp dụng công thức $S_q = \\dfrac{l \\cdot R}{2}$, ta có:
$$S_1 = \\dfrac{%s\\pi \\cdot %d}{2} = %s\\pi\\text{ (cm}^2\\text{)}; \\quad S_2 = \\dfrac{%s\\pi \\cdot %s}{2} = %s\\pi\\text{ (cm}^2\\text{)}.$$
Suy ra hiệu diện tích là:
$$S_2 - S_1 = %s\\pi - %s\\pi = %s\\pi \\approx %s \\cdot 3,14 \\approx %s\\text{ (cm}^2\\text{)}.$$''' % (
            n1, R1, latex(l_coeff), n2, latex(l_coeff), latex(R2),
            latex(l_coeff), R1, latex(S1_coeff), latex(l_coeff), latex(R2), latex(S2_coeff),
            latex(S2_coeff), latex(S1_coeff), latex(diff_coeff), latex(diff_coeff), kq_str))

        # Đáp án
        dapan = '\\shortans[0]{$%s$}\n' % (str(kq_str))

    # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) +
               str(dapan) +
               '\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
