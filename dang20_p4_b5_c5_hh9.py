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



def bt_dang20_p4_b5_c5_hh9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        bo_so = [(60, 80, 100, 48), (50, 120, 130, Rational(600, 13)), (80, 150, 170, Rational(1200, 17)), (90, 120, 150, 72)]
        R_A, R_B, AB, h = random.choice(bo_so)

        hinhve = '''
\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (A) at (0,0);
\\coordinate (B) at (4,0);
\\coordinate (C) at (1.44,1.92);
\\coordinate (D) at (1.44,-1.92);
\\coordinate (H) at (1.44,0);
\\draw[line width=1pt] (A) circle (2.4cm);
\\draw[line width=1pt] (B) circle (3.2cm);
\\draw[line width=1pt] (A)--(B) (A)--(C)--(B);
\\draw[line width=1pt, dashed] (C)--(D);
\\fill (A) circle (1pt) node[left] {$A$};
\\fill (B) circle (1pt) node[right] {$B$};
\\fill (C) circle (1pt) node[above] {$C$};
\\fill (D) circle (1pt) node[below] {$D$};
\\fill (H) circle (1pt) node[below right] {$H$};
\\end{tikzpicture}
\\end{center}
'''

        noidungcauhoi = ('''Sau một trận động đất nhẹ, hai trạm quan trắc địa chấn đặt tại hai thành phố $A$ và $B$ cách nhau $%s\\text{ km}$ cùng ghi nhận được sóng địa chấn. Dựa vào độ trễ giữa sóng dọc và sóng ngang, trạm $A$ tính được tâm chấn cách $A$ một khoảng $%s\\text{ km}$, còn trạm $B$ tính được tâm chấn cách $B$ một khoảng $%s\\text{ km}$.\\\\
        a) Giải thích tại sao việc xét vị trí tương đối của hai đường tròn $(A; %s\\text{ km})$ và $(B; %s\\text{ km})$ giúp khoanh vùng được vị trí tâm chấn chỉ còn $2$ điểm nghi ngờ trên bản đồ.\\\\
        b) Tính khoảng cách ngắn nhất từ tâm chấn đến đường thẳng nối hai thành phố $A$ và $B$. %s'''
                         % (latex(AB), latex(R_A), latex(R_B), latex(R_A), latex(R_B), hinhve))

        loigiai = ('''\\begin{enumEX}[a)]{1}
        \\item Tập hợp các điểm cách trạm $A$ một khoảng $%s\\text{ km}$ là đường tròn $(A; %s\\text{ km})$. Tập hợp các điểm cách trạm $B$ một khoảng $%s\\text{ km}$ là đường tròn $(B; %s\\text{ km})$.\\\\
        Xét hai đường tròn $(A; %s\\text{ km})$ và $(B; %s\\text{ km})$ có khoảng cách hai tâm $AB = %s\\text{ km}$.\\\\
        Ta có $|%s - %s| = %s\\text{ km}$ và $%s + %s = %s\\text{ km}$.\\\\
        Vì $%s < %s < %s$ nên hai đường tròn $(A)$ và $(B)$ cắt nhau tại đúng hai giao điểm phân biệt $C$ và $D$.\\\\
        Do tâm chấn phải đồng thời thuộc cả hai đường tròn nên vị trí tâm chấn được khoanh vùng chính xác chỉ còn là một trong hai điểm $C$ hoặc $D$ trên bản đồ.
        \\item Xét tam giác $ABC$ có $AC = %s\\text{ km}$, $BC = %s\\text{ km}$ và $AB = %s\\text{ km}$.\\\\
        Ta thấy $AC^2 + BC^2 = %s^2 + %s^2 = %s = %s^2 = AB^2$.\\\\
        Theo định lí Pythagore đảo, tam giác $ABC$ vuông tại $C$.\\\\
        Kẻ đường cao $CH \\perp AB$ ($H \\in AB$). Khoảng cách ngắn nhất từ tâm chấn $C$ (hoặc $D$ đối xứng với $C$ qua $AB$) đến đường thẳng $AB$ chính là độ dài đoạn $CH$.\\\\
        Áp dụng hệ thức diện tích trong tam giác vuông $ABC$: $CH \\cdot AB = AC \\cdot BC$.\\\\
        Suy ra $CH = \\frac{AC \\cdot BC}{AB} = \\frac{%s \\cdot %s}{%s} = %s\\text{ (km)}$.\\\\
        Vậy khoảng cách ngắn nhất từ tâm chấn đến đường thẳng nối hai thành phố là $%s\\text{ km}$.
        \\end{enumEX}'''
                   % (latex(R_A), latex(R_A), latex(R_B), latex(R_B),
                      latex(R_A), latex(R_B), latex(AB),
                      latex(R_B), latex(R_A), latex(abs(R_B - R_A)), latex(R_A), latex(R_B), latex(R_A + R_B),
                      latex(abs(R_B - R_A)), latex(AB), latex(R_A + R_B),
                      latex(R_A), latex(R_B), latex(AB),
                      latex(R_A), latex(R_B), latex(AB**2), latex(AB),
                      latex(R_A), latex(R_B), latex(AB), latex(h), latex(h)))

    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) +
               '\n\\loigiai{' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
