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

def bt_dang6_p3_b2_c5_hh9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        bo_chon = random.choice([
            (10, 8, 6, 6, 8),
            (13, 12, 5, 5, 12),
            (20, 16, 12, 12, 16)
        ])
        R, AH, CK, OH, OK = bo_chon
        AB = 2 * AH
        CD = 2 * CK
        kc_2_day = OH + OK
        kq_str = str(R)

        # Nội dung câu hỏi
        noidungcauhoi = ('''Cho đường tròn $(O)$ có hai dây cung $AB = %s\\text{ cm}$ và $CD = %s\\text{ cm}$ song song với nhau và nằm về hai phía đối với tâm $O$ (như hình vẽ). Biết khoảng cách giữa hai dây $AB$ và $CD$ bằng $%s\\text{ cm}$. Tính bán kính của đường tròn $(O)$ (đơn vị: $\\text{cm}$).
        \\begin{center}
        \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
        \\coordinate (O) at (0,0);
        \\coordinate (A) at (143:1.8);
        \\coordinate (B) at (37:1.8);
        \\coordinate (C) at (-127:1.8);
        \\coordinate (D) at (-53:1.8);
        \\coordinate (H) at (0,1.08);
        \\coordinate (K) at (0,-1.44);
        \\draw[line width=1pt] (O) circle (1.8);
        \\draw[line width=1pt] (A)--(B) (C)--(D) (O)--(A) (O)--(C);
        \\draw[line width=1pt, dashed] (H)--(K);
        \\fill (O) circle (1pt) node[right] {$O$};
        \\fill (A) circle (1pt) node[above left] {$A$};
        \\fill (B) circle (1pt) node[above right] {$B$};
        \\fill (C) circle (1pt) node[below left] {$C$};
        \\fill (D) circle (1pt) node[below right] {$D$};
        \\fill (H) circle (1pt) node[above] {$H$};
        \\fill (K) circle (1pt) node[below] {$K$};
        \\end{tikzpicture}
        \\end{center}''' % (AB, CD, kc_2_day))

        # Nội dung lời giải
        loigiai = ('''Kẻ đường thẳng qua $O$ vuông góc với $AB$ và $CD$ lần lượt tại $H$ và $K$.\\\\
        Vì $AB // CD$ và $AB, CD$ nằm về hai phía đối với tâm $O$ nên $H, O, K$ thẳng hàng và $OH + OK = HK = %s\\text{ cm}$.\\\\
        Ta có $H$ là trung điểm $AB$ nên $AH = \\dfrac{%s}{2} = %s\\text{ cm}$; $K$ là trung điểm $CD$ nên $CK = \\dfrac{%s}{2} = %s\\text{ cm}$.\\\\
        Áp dụng định lí Pythagore trong hai tam giác vuông $OHA$ và $OKC$ có cùng cạnh huyền $OA = OC = R$:\\\\
        $OH^2 + %s^2 = OK^2 + %s^2 = R^2 \\Rightarrow OK^2 - OH^2 = %s^2 - %s^2 = %s$.\\\\
        Suy ra $(OK - OH)(OK + OH) = %s \\Rightarrow OK - OH = \\dfrac{%s}{%s} = %s\\text{ cm}$.\\\\
        Kết hợp với $OK + OH = %s\\text{ cm}$, giải ra ta được $OK = %s\\text{ cm}$ và $OH = %s\\text{ cm}$.\\\\
        Vậy bán kính của đường tròn $(O)$ là $R = \\sqrt{OH^2 + AH^2} = \\sqrt{%s^2 + %s^2} = %s\\text{ cm}$.'''
                   % (kc_2_day, AB, AH, CD, CK, AH, CK, AH, CK, AH*AH - CK*CK,
                      AH*AH - CK*CK, AH*AH - CK*CK, kc_2_day, OK - OH,
                      kc_2_day, OK, OH, OH, AH, R))

        #Đáp án
        dapan = '\\shortans[0]{$%s$}\n' % (str(kq_str))

    # Xuất câu hỏi với đáp án và lời giải
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + str(dapan) +
               '\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
