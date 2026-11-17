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



def bt_dang13_p4_b5_c5_hh9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        bo_so = [(15, 13, 14, 24), (20, 13, 21, 24), (17, 10, 21, 16), (25, 17, 28, 30)]
        R, r, d, CD = random.choice(bo_so)
        CH = Rational(CD, 2)
        AH = sqrt(R**2 - CH**2)

        hinhve = '''
\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (A) at (0,0);
\\coordinate (B) at (3.5,0);
\\coordinate (H) at (2.25,0);
\\coordinate (C) at (2.25,1.8);
\\coordinate (D) at (2.25,-1.8);
\\draw[line width=1pt] (A) circle (2.88cm);
\\draw[line width=1pt] (B) circle (2.19cm);
\\draw[line width=1pt] (A)--(B) (C)--(D) (A)--(C) (B)--(C);
\\fill (A) circle (1pt) node[left] {$A$};
\\fill (B) circle (1pt) node[right] {$B$};
\\fill (H) circle (1pt) node[below right] {$H$};
\\fill (C) circle (1pt) node[above] {$C$};
\\fill (D) circle (1pt) node[below] {$D$};
\\end{tikzpicture}
\\end{center}
'''

        noidungcauhoi = ('''Tại một tòa nhà văn phòng, người ta lắp đặt hai bộ phát Wi-Fi ở hai vị trí $A$ và $B$ cách nhau $%s\\text{ m}$ trên cùng một mặt sàn. Bộ phát tại $A$ có bán kính phủ sóng ổn định là $%s\\text{ m}$, bộ phát tại $B$ có bán kính phủ sóng ổn định là $%s\\text{ m}$.\\\\
        a) Hai vùng phủ sóng hình tròn của hai bộ phát này có giao nhau hay không? Giải thích.\\\\
        b) Để đảm bảo hành lang đi bộ nối thẳng hai giao điểm $C$ và $D$ của biên hai vùng phủ sóng được chiếu sáng bởi dải đèn LED, hãy tính chiều dài của dải đèn LED cần lắp đặt. %s'''
                         % (latex(d), latex(R), latex(r), hinhve))

        loigiai = ('''\\begin{enumEX}[a)]{1}
        \\item Đặt $R = %s\\text{ m}$ và $r = %s\\text{ m}$, khoảng cách hai tâm là $AB = %s\\text{ m}$.\\\\
        Ta có $R - r = %s - %s = %s\\text{ m}$ và $R + r = %s + %s = %s\\text{ m}$.\\\\
        Vì $%s < %s < %s$ nên $R - r < AB < R + r$.\\\\
        Vậy hai đường tròn biên của hai vùng phủ sóng cắt nhau tại hai điểm phân biệt $C$ và $D$, tức là hai vùng phủ sóng có giao nhau.
        \\item Vì $AB$ là đường nối tâm của hai đường tròn cắt nhau tại $C$ và $D$ nên $AB$ là đường trung trực của đoạn thẳng $CD$.\\\\
        Gọi $H$ là giao điểm của $AB$ và $CD$, suy ra $AB \\perp CD$ tại $H$ và $H$ là trung điểm của $CD$.\\\\
        Đặt $AH = x$ ($0 < x < %s$), suy ra $BH = %s - x$.\\\\
        Áp dụng định lí Pythagore vào hai tam giác vuông $ACH$ và $BCH$, ta có:\\\\
        $CH^2 = AC^2 - AH^2 = %s^2 - x^2$ và $CH^2 = BC^2 - BH^2 = %s^2 - (%s - x)^2$.\\\\
        Giải phương trình $%s - x^2 = %s - (%s - x)^2$ ta tìm được $x = %s\\text{ (m)}$.\\\\
        Khi đó $CH = \\sqrt{%s^2 - %s^2} = %s\\text{ (m)}$.\\\\
        Vậy chiều dài dải đèn LED cần lắp đặt là $CD = 2CH = 2 \\cdot %s = %s\\text{ (m)}$.
        \\end{enumEX}'''
                   % (latex(R), latex(r), latex(d),
                      latex(R), latex(r), latex(R - r), latex(R), latex(r), latex(R + r),
                      latex(R - r), latex(d), latex(R + r),
                      latex(d), latex(d),
                      latex(R), latex(r), latex(d),
                      latex(R**2), latex(r**2), latex(d), latex(AH),
                      latex(R), latex(AH), latex(CH),
                      latex(CH), latex(CD)))

    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) +
               '\n\\loigiai{' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
