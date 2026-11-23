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


def bt_dang7_p4_b5_c3_hh8(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        bc = randint(6, 12)
        hieu = randint(3, 8)
        ab = bc + hieu
        cheo_mp = hieu
        dien_tich = Rational(hieu ** 2, 2)

        hinh_ve = ('''\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (A) at (0,2.4);
\\coordinate (B) at (4.2,2.4);
\\coordinate (C) at (4.2,0);
\\coordinate (D) at (0,0);
\\coordinate (M) at (1.2,1.2);
\\coordinate (N) at (2.1,2.1);
\\coordinate (P) at (3.0,1.2);
\\coordinate (Q) at (2.1,0.3);
\\draw[line width=1pt] (A)--(B)--(C)--(D)--cycle (A)--(N) (D)--(N) (B)--(Q) (C)--(Q) (M)--(P);
\\draw[line width=1pt] (0,0.2)--(0.2,0.2)--(0.2,0);
\\fill (A) circle (1pt) node[above left] {$A$};
\\fill (B) circle (1pt) node[above right] {$B$};
\\fill (C) circle (1pt) node[below right] {$C$};
\\fill (D) circle (1pt) node[below left] {$D$};
\\fill (M) circle (1pt) node[left] {$M$};
\\fill (N) circle (1pt) node[above] {$N$};
\\fill (P) circle (1pt) node[right] {$P$};
\\fill (Q) circle (1pt) node[below] {$Q$};
\\end{tikzpicture}
\\end{center}''')

        # Nội dung câu hỏi
        noidungcauhoi = ('''Cho hình chữ nhật $ABCD$ có $AB > BC$. Các tia phân giác của bốn góc trong $\\widehat{A}, \\widehat{B}, \\widehat{C}, \\widehat{D}$ cắt nhau tạo thành tứ giác $MNPQ$ (với $M$ là giao điểm tia phân giác góc $A$ và $D$, $P$ là giao điểm tia phân giác góc $B$ và $C$). \\\\
a) Chứng minh tứ giác $MNPQ$ là hình vuông. \\\\
b) Biết $AB = %s\\text{ cm}$ và $BC = %s\\text{ cm}$. Tính diện tích của hình vuông $MNPQ$.%s'''
                         % (ab, bc, hinh_ve))

        # Nội dung lời giải
        loigiai = ('''\\begin{enumEX}[a)]{1} 
\\item Vì $ABCD$ là hình chữ nhật nên $\\widehat{A} = \\widehat{B} = \\widehat{C} = \\widehat{D} = 90^\\circ$.\\\\
Các tia phân giác chia mỗi góc vuông thành hai góc bằng $45^\\circ$.\\\\
Xét $\\Delta AMD$ có $\\widehat{MAD} = \\widehat{MDA} = 45^\\circ$ nên $\\Delta AMD$ vuông cân tại $M$, suy ra $\\widehat{AMD} = 90^\\circ$ và $MA = MD$.\\\\
Tương tự, $\\Delta BPC$ vuông cân tại $P$ nên $\\widehat{BPC} = 90^\\circ$; $\\Delta AND$ vuông cân tại $N$ nên $\\widehat{AND} = 90^\\circ$ (suy ra $\\widehat{MNP} = 90^\\circ$) và $NA = ND$.\\\\
Tứ giác $MNPQ$ có $\\widehat{QMN} = \\widehat{MNP} = \\widehat{NPQ} = 90^\\circ$ nên là hình chữ nhật.\\\\
Mặt khác $\\Delta AND$ vuông cân tại $N$ có $AM$ là đường phân giác nên cũng là đường trung tuyến, suy ra $M$ là trung điểm của $AN$, do đó $MN = MA = MD$.\\\\
Tương tự $MQ = MD$, suy ra $MN = MQ$. Hình chữ nhật $MNPQ$ có hai cạnh kề bằng nhau nên là hình vuông.
\\item Kéo dài $AM$ cắt $CD$ tại $E$, $BP$ cắt $CD$ tại $F$. Vì $\\Delta ADE$ vuông cân tại $D$ nên $DE = AD = BC = %s\\text{ cm}$; tương tự $CF = BC = %s\\text{ cm}$.\\\\
Suy ra $EF = DE + CF - CD = 2BC - AB$ (hoặc $CD - DE - CF = AB - 2BC$).\\\\
Vì $M$ là trung điểm $AE$, $P$ là trung điểm $BF$ nên $MP$ là đường trung bình của hình thang $ABFE$ (hoặc hiệu hai đáy), ta luôn có độ dài đường chéo $MP = AB - BC = %s - %s = %s\\text{ (cm)}$.\\\\
Vậy diện tích hình vuông $MNPQ$ là:\\\\
$S_{MNPQ} = \\dfrac{1}{2}MP^2 = \\dfrac{%s^2}{2} = %s\\text{ (cm}^2)$.
\\end{enumEX} \n'''
                   % (bc, bc, ab, bc, cheo_mp, cheo_mp, latex(dien_tich)))

    # Xuất câu hỏi
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
