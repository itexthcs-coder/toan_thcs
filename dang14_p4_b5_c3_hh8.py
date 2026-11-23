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


def bt_dang14_p4_b5_c3_hh8(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        hinh_ve = ('''\\begin{center}
\\begin{tikzpicture}[scale=0.85, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (A) at (0,1.6);
\\coordinate (B) at (-1.2,0);
\\coordinate (C) at (1.5,0);
\\coordinate (H) at (0,0);
\\coordinate (E) at (-1.6,2.8);
\\coordinate (D) at (-2.8,1.2);
\\coordinate (G) at (1.6,3.1);
\\coordinate (F) at (3.1,1.5);
\\coordinate (M) at (0,2.95);
\\draw[line width=1pt] (A)--(B)--(C)--cycle (A)--(B)--(D)--(E)--cycle (A)--(C)--(F)--(G)--cycle (E)--(G) (M)--(H) (B)--(G) (C)--(E);
\\draw[line width=1pt, dashed] (E)--(-1.6,1.6)--(A) (G)--(1.6,1.6)--(A);
\\fill (A) circle (1pt) node[below left] {$A$};
\\fill (B) circle (1pt) node[below left] {$B$};
\\fill (C) circle (1pt) node[below right] {$C$};
\\fill (H) circle (1pt) node[below] {$H$};
\\fill (E) circle (1pt) node[above left] {$E$};
\\fill (D) circle (1pt) node[left] {$D$};
\\fill (G) circle (1pt) node[above right] {$G$};
\\fill (F) circle (1pt) node[right] {$F$};
\\fill (M) circle (1pt) node[above] {$M$};
\\end{tikzpicture}
\\end{center}''')

        # Nội dung câu hỏi
        noidungcauhoi = ('''Cho $\\Delta ABC$ nhọn. Vẽ ra phía ngoài tam giác đó các hình vuông $ABDE$ và $ACFG$. Gọi $H$ là chân đường cao kẻ từ $A$ xuống $BC$. Tia đối của tia $AH$ cắt đoạn thẳng $EG$ tại $M$. \\\\
a) Chứng minh $M$ là trung điểm của đoạn thẳng $EG$. \\\\
b) Chứng minh ba đường thẳng $AH, BG, CE$ đồng quy tại một điểm.%s'''
                         % (hinh_ve))

        # Nội dung lời giải
        loigiai = ('''\\begin{enumEX}[a)]{1} 
\\item Kẻ $EP \\perp AM$ tại $P$ và $GQ \\perp AM$ tại $Q$.\\\\
Ta có $\\widehat{EAP} + \\widehat{BAH} = 90^\\circ$ (do $\\widehat{EAB} = 90^\\circ$) và $\\widehat{ABH} + \\widehat{BAH} = 90^\\circ$ (do $\\Delta ABH$ vuông tại $H$), suy ra $\\widehat{EAP} = \\widehat{ABH}$.\\\\
Xét hai tam giác vuông $\\Delta EPA$ và $\\Delta AHB$ có: $\\widehat{EPA} = \\widehat{AHB} = 90^\\circ$, $EA = AB$ (cạnh hình vuông $ABDE$), $\\widehat{EAP} = \\widehat{ABH}$.\\\\
Suy ra $\\Delta EPA = \\Delta AHB$ (c.h - g.n), do đó $EP = AH$.\\\\
Chứng minh tương tự, $\\Delta GQA = \\Delta AHC$ (c.h - g.n), suy ra $GQ = AH$.\\\\
Do đó $EP = GQ$. Mặt khác $EP // GQ$ (cùng vuông góc với $AM$) nên $\\widehat{PEM} = \\widehat{QGM}$ (so le trong).\\\\
Xét hai tam giác vuông $\\Delta EPM$ và $\\Delta GQM$ có: $\\widehat{EPM} = \\widehat{GQM} = 90^\\circ$, $EP = GQ$, $\\widehat{PEM} = \\widehat{QGM}$.\\\\
Suy ra $\\Delta EPM = \\Delta GQM$ (g.c.g), do đó $EM = GM$, tức $M$ là trung điểm của đoạn thẳng $EG$.
\\item Xét $\\Delta EAC$ và $\\Delta BAG$ có: $AE = AB$, $\\widehat{EAC} = \\widehat{BAG} = 90^\\circ + \\widehat{BAC}$, $AC = AG$.\\\\
Suy ra $\\Delta EAC = \\Delta BAG$ (c.g.c), do đó $EC = BG$ và $EC \\perp BG$.\\\\
Trên tia $AH$ lấy điểm $K$ sao cho $AK = BC$. Ta chứng minh được $\\Delta KAC = \\Delta BCG$ (c.g.c) và $\\Delta KAB = \\Delta CBE$ (c.g.c).\\\\
Từ đó suy ra $AK \\perp BG$ và $AK \\perp CE$.\\\\
Xét $\\Delta KBC$ có $AH, BG, CE$ lần lượt vuông góc với $BC, CK, BK$ nên $AH, BG, CE$ là ba đường cao của $\\Delta KBC$.\\\\
Vậy ba đường thẳng $AH, BG, CE$ đồng quy tại trực tâm của $\\Delta KBC$.
\\end{enumEX} \n''')

    # Xuất câu hỏi
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
