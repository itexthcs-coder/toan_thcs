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



def bt_dang9_p4_b5_c5_hh9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        bo_so = [(9, 4, 12, Rational(36, 25)), (16, 4, 16, Rational(16, 9)), (16, 9, 24, Rational(144, 49)), (25, 4, 20, Rational(100, 49))]
        R1, R2, BC, r = random.choice(bo_so)

        hinhve = '''
\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (B) at (0,0);
\\coordinate (D) at (1.92,0);
\\coordinate (C) at (3.2,0);
\\coordinate (O1) at (0,2.4);
\\coordinate (O2) at (3.2,1.07);
\\coordinate (O3) at (1.92,0.384);
\\draw[line width=1pt] (-1,0)--(4.5,0);
\\draw[line width=1pt] (O1) circle (2.4cm);
\\draw[line width=1pt] (O2) circle (1.07cm);
\\draw[line width=1pt] (O3) circle (0.384cm);
\\draw[line width=1pt] (O1)--(B) (O2)--(C) (O3)--(D) (O1)--(O2);
\\fill (B) circle (1pt) node[below] {$B$};
\\fill (D) circle (1pt) node[below] {$D$};
\\fill (C) circle (1pt) node[below] {$C$};
\\fill (O1) circle (1pt) node[left] {$O_1$};
\\fill (O2) circle (1pt) node[right] {$O_2$};
\\fill (O3) circle (1pt) node[above] {$O_3$};
\\end{tikzpicture}
\\end{center}
'''

        noidungcauhoi = ('''Cho hai đường tròn $(O_1; %s\\text{ cm})$ và $(O_2; %s\\text{ cm})$ tiếp xúc ngoài với nhau tại $A$ và cùng tiếp xúc với một đường thẳng $d$ tại $B$ và $C$ ($O_1, O_2$ nằm cùng phía đối với $d$). Vẽ đường tròn $(O_3; r)$ tiếp xúc ngoài với cả $(O_1)$, $(O_2)$ và tiếp xúc với đường thẳng $d$ tại điểm $D$ nằm giữa $B$ và $C$.\\\\
        a) Tính độ dài đoạn thẳng $BC$.\\\\
        b) Tính bán kính $r$ của đường tròn $(O_3)$. %s'''
                         % (latex(R1), latex(R2), hinhve))

        loigiai = ('''\\begin{enumEX}[a)]{1}
        \\item Vì $(O_1)$ và $(O_2)$ tiếp xúc ngoài với nhau nên $O_1O_2 = R_1 + R_2 = %s + %s = %s\\text{ cm}$.\\\\
        Kẻ $O_2H \\perp O_1B$ tại $H$. Tứ giác $O_2HBC$ là hình chữ nhật nên $BC = O_2H$ và $BH = O_2C = %s\\text{ cm}$.\\\\
        Suy ra $O_1H = O_1B - BH = %s - %s = %s\\text{ cm}$.\\\\
        Áp dụng định lí Pythagore vào tam giác vuông $O_1HO_2$, ta có:\\\\
        $BC = O_2H = \\sqrt{O_1O_2^2 - O_1H^2} = \\sqrt{%s^2 - %s^2} = %s\\text{ (cm)}$.
        \\item Áp dụng công thức tính độ dài đoạn tiếp tuyến chung ngoài ở câu a cho cặp đường tròn $(O_1; %s\\text{ cm})$ và $(O_3; r)$, ta được:\\\\
        $BD = \\sqrt{(%s + r)^2 - (%s - r)^2} = \\sqrt{4 \\cdot %s r} = 2\\sqrt{%s r}$.\\\\
        Tương tự cho cặp đường tròn $(O_2; %s\\text{ cm})$ và $(O_3; r)$, ta được:\\\\
        $DC = \\sqrt{(%s + r)^2 - (%s - r)^2} = \\sqrt{4 \\cdot %s r} = 2\\sqrt{%s r}$.\\\\
        Vì $D$ nằm giữa $B$ và $C$ nên $BD + DC = BC \\Leftrightarrow 2\\sqrt{%s r} + 2\\sqrt{%s r} = %s$.\\\\
        Giải phương trình trên ta tìm được $\\sqrt{r} = \\frac{%s}{%s} \\Rightarrow r = %s\\text{ (cm)}$.
        \\end{enumEX}'''
                   % (latex(R1), latex(R2), latex(R1 + R2),
                      latex(R2), latex(R1), latex(R2), latex(R1 - R2),
                      latex(R1 + R2), latex(R1 - R2), latex(BC),
                      latex(R1), latex(R1), latex(R1), latex(R1), latex(R1),
                      latex(R2), latex(R2), latex(R2), latex(R2), latex(R2),
                      latex(R1), latex(R2), latex(BC),
                      latex(sqrt(r).as_numer_denom()[0]), latex(sqrt(r).as_numer_denom()[1]), latex(r)))

    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) +
               '\n\\loigiai{' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
