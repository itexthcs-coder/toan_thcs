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

def bt_dang15_p4_b3_c3_hh8(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        r_val = random.choice([4, 6, 8, 10])
        r_nua = r_val // 2
        
        hinh_ve = '''\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (O) at (1.5,1.8);
\\coordinate (O1) at (4.5,1.8);
\\coordinate (A) at (0.8,0);
\\coordinate (B) at (3.8,0);
\\coordinate (M) at (2.2,2.7);
\\coordinate (C) at (5.2,2.7);
\\coordinate (I) at ($(A)!0.5!(M)$);
\\draw[line width=1pt] (O) circle (1.1);
\\draw[line width=1pt, dashed] (O1) circle (1.1);
\\draw[line width=1pt] (A)--(B)--(C)--(M)--cycle (A)--(M) (B)--(C);
\\draw[line width=1pt, dashed] (O)--(O1) (O)--(M) (O1)--(C) (A)--(O) (B)--(O1);
\\fill (O) circle (1pt) node[left] {$O$};
\\fill (O1) circle (1pt) node[right] {$O'$};
\\fill (A) circle (1pt) node[below left] {$A$};
\\fill (B) circle (1pt) node[below right] {$B$};
\\fill (M) circle (1pt) node[above] {$M$};
\\fill (C) circle (1pt) node[above] {$C$};
\\fill (I) circle (1pt) node[left] {$I$};
\\end{tikzpicture}
\\end{center}'''
        
        noidungcauhoi = ('''Cho đoạn thẳng $AB$ cố định và đường tròn $(O; %s\\text{ cm})$ cố định. Lấy điểm $M$ di động trên đường tròn $(O; %s\\text{ cm})$ (sao cho $M$ không nằm trên đường thẳng $AB$) và dựng hình bình hành $ABMC$ (như hình vẽ). \\\\
a) Chứng minh rằng điểm $C$ luôn di động trên một đường tròn cố định và tìm bán kính của đường tròn đó. \\\\
b) Gọi $I$ là giao điểm của hai đường chéo $AM$ và $BC$. Tìm quỹ tích điểm $I$ khi $M$ di động trên đường tròn $(O; %s\\text{ cm})$.
%s''' % (r_val, r_val, r_val, hinh_ve))
        
        loigiai = ('''\\begin{enumEX}[a)]{1}
\\item Dựng hình bình hành $ABOO'$. Vì $A, B, O$ cố định nên điểm $O'$ cố định. \\\\
Ta có $OO' // AB$ và $OO' = AB$. Mặt khác, $ABMC$ là hình bình hành nên $MC // AB$ và $MC = AB$. \\\\
Suy ra $MC // OO'$ và $MC = OO'$, do đó tứ giác $OO'CM$ là hình bình hành. \\\\
Vậy $O'C = OM = %s$ cm không đổi. Khi $M$ di động trên đường tròn $(O; %s\\text{ cm})$ (trừ giao điểm với đường thẳng $AB$) thì điểm $C$ di động trên đường tròn cố định tâm $O'$ có bán kính bằng $%s$ cm (trừ hai giao điểm với đường thẳng $AB$).
\\item Trong hình bình hành $ABMC$, hai đường chéo $AM$ và $BC$ cắt nhau tại trung điểm $I$ của mỗi đường. \\\\
Gọi $K$ là trung điểm của đoạn thẳng $BO'$ cố định thì $K$ cố định. Xét $\\Delta BCO'$ có $I$ là trung điểm $BC$ và $K$ là trung điểm $BO'$ nên $IK$ là đường trung bình của $\\Delta BCO'$. \\\\
Suy ra $IK = \\frac{1}{2}O'C = \\frac{%s}{2} = %s$ (cm) không đổi. \\\\
Vậy điểm $I$ luôn di động trên đường tròn cố định tâm $K$ bán kính bằng $%s$ cm (trừ hai giao điểm với đường thẳng $AB$).
\\end{enumEX}''' % (r_val, r_val, r_val, r_val, r_nua, r_nua))
    
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) +
               '\\loigiai{ \n' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
