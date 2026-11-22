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

def bt_dang4_p4_b3_c3_hh8(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        hinh_ve = '''\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (A) at (1.2,2.4);
\\coordinate (B) at (5.4,2.4);
\\coordinate (D) at (0,0);
\\coordinate (C) at (4.2,0);
\\coordinate (O) at ($(A)!0.5!(C)$);
\\coordinate (M) at ($(A)!0.3!(B)$);
\\coordinate (N) at ($(C)!0.3!(D)$);
\\coordinate (P) at ($(A)!0.28!(D)$);
\\coordinate (Q) at ($(C)!0.28!(B)$);
\\draw[line width=1pt] (A)--(B)--(C)--(D)--cycle (M)--(P)--(N)--(Q)--cycle;
\\draw[line width=1pt, dashed] (A)--(C) (B)--(D) (M)--(N) (P)--(Q);
\\fill (A) circle (1pt) node[above left] {$A$};
\\fill (B) circle (1pt) node[above right] {$B$};
\\fill (C) circle (1pt) node[below right] {$C$};
\\fill (D) circle (1pt) node[below left] {$D$};
\\fill (O) circle (1pt) node[above right] {$O$};
\\fill (M) circle (1pt) node[above] {$M$};
\\fill (N) circle (1pt) node[below] {$N$};
\\fill (P) circle (1pt) node[left] {$P$};
\\fill (Q) circle (1pt) node[right] {$Q$};
\\end{tikzpicture}
\\end{center}'''
        
        noidungcauhoi = ('''Cho hình bình hành $ABCD$ có hai đường chéo $AC$ và $BD$ cắt nhau tại $O$. Qua $O$ kẻ hai đường thẳng phân biệt: đường thẳng thứ nhất cắt $AB$ tại $M$ và cắt $CD$ tại $N$; đường thẳng thứ hai cắt $AD$ tại $P$ và cắt $BC$ tại $Q$ (như hình vẽ). \\\\
a) Chứng minh rằng $OM = ON$ và $OP = OQ$. \\\\
b) Chứng minh rằng tứ giác $MPNQ$ là hình bình hành.
%s''' % (hinh_ve))
        
        loigiai = ('''\\begin{enumEX}[a)]{1}
\\item Vì $ABCD$ là hình bình hành có giao điểm hai đường chéo là $O$ nên $OA = OC$, $AB // CD$ và $AD // BC$. \\\\
Xét $\\Delta OAM$ và $\\Delta OCN$ có: $\\widehat{OAM} = \\widehat{OCN}$ (hai góc so le trong do $AB // CD$), $OA = OC$, $\\widehat{AOM} = \\widehat{CON}$ (hai góc đối đỉnh). \\\\
Do đó $\\Delta OAM = \\Delta OCN$ (g.c.g), suy ra $OM = ON$. \\\\
Tương tự, xét $\\Delta OAP$ và $\\Delta OCQ$ có: $\\widehat{OAP} = \\widehat{OCQ}$ (so le trong do $AD // BC$), $OA = OC$, $\\widehat{AOP} = \\widehat{COQ}$ (đối đỉnh). \\\\
Do đó $\\Delta OAP = \\Delta OCQ$ (g.c.g), suy ra $OP = OQ$.
\\item Tứ giác $MPNQ$ có hai đường chéo $MN$ và $PQ$ cắt nhau tại $O$, mà $OM = ON$ và $OP = OQ$ (chứng minh trên) nên $O$ là trung điểm của mỗi đường chéo. \\\\
Theo Định lí 3b, tứ giác $MPNQ$ là hình bình hành.
\\end{enumEX}''')
    
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) +
               '\\loigiai{ \n' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
