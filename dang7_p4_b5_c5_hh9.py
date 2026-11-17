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



def bt_dang7_p4_b5_c5_hh9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        d = randint(5, 12)
        CD = 2 * d

        hinhve = '''
\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (O) at (0,0);
\\coordinate (O') at (3.2,0);
\\coordinate (A) at (1.8,1.2);
\\coordinate (B) at (1.8,-1.2);
\\coordinate (C) at (-1.8,1.2);
\\coordinate (D) at (4.6,1.2);
\\coordinate (E) at (-1.8,-1.2);
\\coordinate (F) at (4.6,-1.2);
\\coordinate (H) at (0,1.2);
\\coordinate (K) at (3.2,1.2);
\\draw[line width=1pt] (O) circle (2.16cm);
\\draw[line width=1pt] (O') circle (1.84cm);
\\draw[line width=1pt] (O)--(O') (C)--(D) (E)--(F) (C)--(E) (D)--(F);
\\draw[line width=1pt, dashed] (O)--(H) (O')--(K);
\\fill (O) circle (1pt) node[below] {$O$};
\\fill (O') circle (1pt) node[below] {$O'$};
\\fill (A) circle (1pt) node[above] {$A$};
\\fill (B) circle (1pt) node[below] {$B$};
\\fill (C) circle (1pt) node[above left] {$C$};
\\fill (D) circle (1pt) node[above right] {$D$};
\\fill (E) circle (1pt) node[below left] {$E$};
\\fill (F) circle (1pt) node[below right] {$F$};
\\fill (H) circle (1pt) node[above] {$H$};
\\fill (K) circle (1pt) node[above] {$K$};
\\end{tikzpicture}
\\end{center}
'''

        noidungcauhoi = ('''Cho hai đường tròn $(O)$ và $(O')$ cắt nhau tại $A$ và $B$ với khoảng cách hai tâm $OO' = %s\\text{ cm}$. Qua $A$ vẽ một đường thẳng $d$ song song với đường nối tâm $OO'$, đường thẳng $d$ cắt $(O)$ tại $C$ và cắt $(O')$ tại $D$ ($A$ nằm giữa $C$ và $D$).\\\\
        a) Tính độ dài đoạn thẳng $CD$.\\\\
        b) Đường thẳng qua $B$ và song song với $OO'$ cắt $(O)$ tại $E$ và cắt $(O')$ tại $F$ ($B$ nằm giữa $E$ và $F$). Chứng minh tứ giác $CDFE$ là hình bình hành. %s'''
                         % (latex(d), hinhve))

        loigiai = ('''\\begin{enumEX}[a)]{1}
        \\item Kẻ $OH \\perp CD$ tại $H$ và $O'K \\perp CD$ tại $K$.\\\\
        Xét đường tròn $(O)$ có $OH$ là một phần đường kính vuông góc với dây $AC$ nên $H$ là trung điểm của $AC$, suy ra $AC = 2AH$.\\\\
        Xét đường tròn $(O')$ có $O'K$ là một phần đường kính vuông góc với dây $AD$ nên $K$ là trung điểm của $AD$, suy ra $AD = 2AK$.\\\\
        Tứ giác $OO'KH$ có $\\widehat{OHK} = \\widehat{O'KH} = 90^\\circ$ và $HK // OO'$ (do $CD // OO'$) nên $OO'KH$ là hình chữ nhật, suy ra $HK = OO' = %s\\text{ cm}$.\\\\
        Vì $A$ nằm giữa $C$ và $D$ nên $CD = AC + AD = 2AH + 2AK = 2(AH + AK) = 2HK = 2OO' = 2 \\cdot %s = %s\\text{ (cm)}$.
        \\item Chứng minh tương tự câu a đối với đường thẳng qua $B$ song song với $OO'$, ta cũng có $EF // OO'$ và $EF = 2OO' = %s\\text{ cm}$.\\\\
        Xét tứ giác $CDFE$ có $CD // EF$ (cùng song song với $OO'$) và $CD = EF$ (cùng bằng $%s\\text{ cm}$).\\\\
        Vậy tứ giác $CDFE$ là hình bình hành.
        \\end{enumEX}'''
                   % (latex(d), latex(d), latex(CD), latex(CD), latex(CD)))

    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) +
               '\n\\loigiai{' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
