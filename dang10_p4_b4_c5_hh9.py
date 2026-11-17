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


def bt_dang10_p4_b4_c5_hh9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        bo_so = [(3, 4, 5), (6, 8, 10), (5, 12, 13)]
        a0, b0, c0 = random.choice(bo_so)
        k = randint(1, 2)
        ab = a0 * k
        ac = b0 * k
        bc = c0 * k
        ah_val = Rational(ab * ac, bc)
        ah_dec = Decimal(str(float(ah_val))).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP).normalize()
        ah_str = str(ah_dec).replace('.', ',')

        # Nội dung câu hỏi
        noidungcauhoi = ('''Cho tam giác $ABC$ vuông tại $A$ có $AB = %s\\text{ cm}$, $AC = %s\\text{ cm}$. Gọi $H$ là chân đường cao kẻ từ $A$ xuống cạnh $BC$. Xét đường tròn $(A; R)$. Tìm điều kiện của bán kính $R$ để: \\\\
        a) Đường tròn $(A; R)$ và đường thẳng $BC$ cắt nhau tại hai điểm phân biệt. \\\\
        b) Đường tròn $(A; R)$ và đường thẳng $BC$ tiếp xúc với nhau. \\\\
        \\begin{center}
        \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
            \\coordinate (A) at (0,0);
            \\coordinate (B) at (0,2.4);
            \\coordinate (C) at (3.2,0);
            \\coordinate (H) at (1.152,1.536);
            \\draw[line width=1pt] (A)--(B)--(C)--cycle;
            \\draw[line width=1pt] (A) circle (1.92);
            \\draw[line width=1pt, dashed] (A)--(H);
            \\fill (A) circle (1pt) node[below left] {$A$};
            \\fill (B) circle (1pt) node[above] {$B$};
            \\fill (C) circle (1pt) node[right] {$C$};
            \\fill (H) circle (1pt) node[above right] {$H$};
        \\end{tikzpicture}
        \\end{center}'''
        %(latex(ab), latex(ac)))

        # Nội dung lời giải
        loigiai = ('''Xét tam giác $ABC$ vuông tại $A$, áp dụng định lí Pythagore ta có: \\\\
        $BC = \\sqrt{AB^2 + AC^2} = \\sqrt{%s^2 + %s^2} = %s\\text{ (cm)}$. \\\\
        Vì $AH \\perp BC$ tại $H$ nên khoảng cách từ tâm $A$ đến đường thẳng $BC$ là $d = AH$. \\\\
        Áp dụng hệ thức lượng trong tam giác vuông $ABC$ có đường cao $AH$, ta tính được: \\\\
        $AH \\cdot BC = AB \\cdot AC \\Rightarrow d = AH = \\dfrac{%s \\cdot %s}{%s} = %s\\text{ (cm)}$. \\\\
        \\begin{enumEX}[a)]{1} \n
        \\item Đường tròn $(A; R)$ và đường thẳng $BC$ cắt nhau tại hai điểm phân biệt khi và chỉ khi $R > d$, tức là $R > %s\\text{ cm}$. \n
        \\item Đường tròn $(A; R)$ và đường thẳng $BC$ tiếp xúc với nhau khi và chỉ khi $R = d$, tức là $R = %s\\text{ cm}$. \n
        \\end{enumEX} \n'''
        %(latex(ab), latex(ac), latex(bc), latex(ab), latex(ac), latex(bc), ah_str, ah_str, ah_str))

    # Xuất câu hỏi tự luận
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) +
               '\\loigiai{\n' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
