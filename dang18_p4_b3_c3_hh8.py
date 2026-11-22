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

def bt_dang18_p4_b3_c3_hh8(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        ac = randint(6, 15)
        
        hinh_ve = '''\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (A) at (1.2,2.6);
\\coordinate (B) at (0,0);
\\coordinate (C) at (3.6,0);
\\coordinate (D) at (2.4,-2.6);
\\coordinate (M) at ($(B)!0.5!(C)$);
\\coordinate (E) at ($(A)!0.38!(C)$);
\\coordinate (F) at (1.48,-1.61);
\\draw[line width=1pt] (A)--(B)--(C)--cycle (B)--(D)--(C) (A)--(D) (E)--(F);
\\fill (A) circle (1pt) node[above] {$A$};
\\fill (B) circle (1pt) node[left] {$B$};
\\fill (C) circle (1pt) node[right] {$C$};
\\fill (D) circle (1pt) node[below] {$D$};
\\fill (M) circle (1pt) node[above left] {$M$};
\\fill (E) circle (1pt) node[above right] {$E$};
\\fill (F) circle (1pt) node[below left] {$F$};
\\end{tikzpicture}
\\end{center}'''
        
        noidungcauhoi = ('''Cho tam giác $ABC$ có $AC = %s$ cm và đường trung tuyến $AM$. Qua đỉnh $B$ kẻ đường thẳng song song với $AC$, qua đỉnh $C$ kẻ đường thẳng song song với $AB$; hai đường thẳng này cắt nhau tại $D$ (như hình vẽ). \\\\
a) Chứng minh rằng tứ giác $ABDC$ là hình bình hành và ba điểm $A, M, D$ thẳng hàng. \\\\
b) Qua điểm $M$ kẻ đường thẳng cắt cạnh $AC$ tại $E$ và cắt đoạn thẳng $BD$ tại $F$. Chứng minh rằng $AE + BF = %s$ cm.
%s''' % (ac, ac, hinh_ve))
        
        loigiai = ('''\\begin{enumEX}[a)]{1}
\\item Tứ giác $ABDC$ có $AB // CD$ và $AC // BD$ (theo cách vẽ) nên theo định nghĩa, tứ giác $ABDC$ là hình bình hành. \\\\
Trong hình bình hành $ABDC$, hai đường chéo $AD$ và $BC$ cắt nhau tại trung điểm của mỗi đường. Mà $M$ là trung điểm của $BC$ (do $AM$ là đường trung tuyến của $\\Delta ABC$) nên $M$ cũng là trung điểm của $AD$. \\\\
Vậy ba điểm $A, M, D$ thẳng hàng.
\\item Xét $\\Delta MBF$ và $\\Delta MCE$ có: $\\widehat{MBF} = \\widehat{MCE}$ (hai góc so le trong do $BD // AC$), $MB = MC$ (giả thiết), $\\widehat{BMF} = \\widehat{CME}$ (hai góc đối đỉnh). \\\\
Do đó $\\Delta MBF = \\Delta MCE$ (g.c.g), suy ra $BF = CE$. \\\\
Vì điểm $E$ nằm trên cạnh $AC$ nên $AE + BF = AE + CE = AC = %s$ cm.
\\end{enumEX}''' % (ac))
    
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) +
               '\\loigiai{ \n' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
