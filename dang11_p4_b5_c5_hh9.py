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



def bt_dang11_p4_b5_c5_hh9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        R1 = 6 * randint(2, 3)
        R2 = 6 * randint(4, 5)
        tocdo = 30 * randint(4, 6)
        vong1 = 5 * randint(2, 4)
        kc = R1 + R2
        vong2 = Rational(vong1 * R1, R2)
        goc = vong2 * 360

        hinhve = '''
\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (O1) at (0,0);
\\coordinate (O2) at (3.6,0);
\\coordinate (A) at (1.44,0);
\\draw[line width=1pt] (O1) circle (1.44cm);
\\draw[line width=1pt] (O2) circle (2.16cm);
\\draw[line width=1pt] (O1)--(O2);
\\fill (O1) circle (1pt) node[left] {$O_1$};
\\fill (O2) circle (1pt) node[right] {$O_2$};
\\fill (A) circle (1pt) node[above right] {$A$};
\\end{tikzpicture}
\\end{center}
'''

        noidungcauhoi = ('''Trong một hộp số cơ khí, hai bánh răng hình tròn $(O_1)$ và $(O_2)$ ăn khớp ngoài với nhau (mô hình hóa là hai đường tròn tiếp xúc ngoài tại $A$). Bánh răng chủ động $(O_1)$ có bán kính $R_1 = %s\\text{ cm}$ quay với tốc độ $%s\\text{ vòng/phút}$, bánh răng bị động $(O_2)$ có bán kính $R_2 = %s\\text{ cm}$.\\\\
        a) Tính khoảng cách giữa hai trục quay $O_1$ và $O_2$.\\\\
        b) Khi bánh răng $(O_1)$ quay được $%s$ vòng thì bánh răng $(O_2)$ quay được bao nhiêu vòng và điểm tiếp xúc ban đầu trên vành bánh răng $(O_2)$ đã quay được một góc tổng cộng bằng bao nhiêu độ? %s'''
                         % (latex(R1), latex(tocdo), latex(R2), latex(vong1), hinhve))

        loigiai = ('''\\begin{enumEX}[a)]{1}
        \\item Vì hai bánh răng $(O_1)$ và $(O_2)$ ăn khớp ngoài với nhau nên hai đường tròn $(O_1; %s\\text{ cm})$ và $(O_2; %s\\text{ cm})$ tiếp xúc ngoài với nhau.\\\\
        Do đó khoảng cách giữa hai trục quay là: $O_1O_2 = R_1 + R_2 = %s + %s = %s\\text{ (cm)}$.
        \\item Chu vi của bánh răng $(O_1)$ là $C_1 = 2\\pi R_1 = 2\\pi \\cdot %s = %s\\pi\\text{ (cm)}$.\\\\
        Chu vi của bánh răng $(O_2)$ là $C_2 = 2\\pi R_2 = 2\\pi \\cdot %s = %s\\pi\\text{ (cm)}$.\\\\
        Khi bánh răng $(O_1)$ quay được $%s$ vòng thì quãng đường cung tròn mà một điểm trên vành bánh răng di chuyển được là: $S = %s \\cdot %s\\pi = %s\\pi\\text{ (cm)}$.\\\\
        Vì hai bánh răng ăn khớp không trượt nên vành bánh răng $(O_2)$ cũng di chuyển một độ dài cung tròn bằng $S$.\\\\
        Số vòng bánh răng $(O_2)$ quay được là: $n = \\frac{S}{C_2} = \\frac{%s\\pi}{%s\\pi} = %s\\text{ (vòng)}$.\\\\
        Mỗi vòng quay ứng với góc $360^\\circ$ nên tổng số đo góc quay của điểm đó trên vành bánh răng $(O_2)$ là: $\\alpha = %s \\cdot 360^\\circ = %s^\\circ$.
        \\end{enumEX}'''
                   % (latex(R1), latex(R2), latex(R1), latex(R2), latex(kc),
                      latex(R1), latex(2*R1), latex(R2), latex(2*R2),
                      latex(vong1), latex(vong1), latex(2*R1), latex(vong1*2*R1),
                      latex(vong1*2*R1), latex(2*R2), latex(vong2),
                      latex(vong2), latex(goc)))

    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) +
               '\n\\loigiai{' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
