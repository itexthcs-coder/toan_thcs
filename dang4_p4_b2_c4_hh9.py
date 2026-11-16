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


def bt_dang4_p4_b2_c4_hh9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        bc = random.choice([6, 12, 18, 24])
        ac_new = Rational(bc, 2) * sqrt(3)
        ab_new = Rational(bc, 2)
        ad_new = Rational(bc, 6) * sqrt(3)
        dc_new = ac_new - ad_new
        bd_new = Rational(bc, 3) * sqrt(3)

        hinhve = ('''\\begin{center}
    \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
    \\coordinate (A) at (0,0);
    \\coordinate (B) at (2.2,0);
    \\coordinate (C) at (0,3.81);
    \\coordinate (D) at (0,1.27);
    \\draw[line width=1pt] (A)--(B)--(C)--cycle (B)--(D);
    \\draw[line width=1pt] (0,0.22)--(0.22,0.22)--(0.22,0);
    \\fill (A) circle (1pt) node[below left] {$A$};
    \\fill (B) circle (1pt) node[below right] {$B$};
    \\fill (C) circle (1pt) node[above left] {$C$};
    \\fill (D) circle (1pt) node[left] {$D$};
    \\node[above right] at (1.1,1.9) {$%s\\text{ cm}$};
    \\end{tikzpicture}
    \\end{center}''' % (bc))

        # Nội dung câu hỏi
        noidungcauhoi = ('''Xét các tam giác vuông có một góc nhọn bằng hai lần góc nhọn còn lại. \\\\
    a) Chứng minh rằng tất cả các tam giác vuông như vậy đều đồng dạng với nhau. Tính giá trị chính xác của $\\sin$ và $\\cos$ của góc nhọn lớn hơn. \\\\
    b) Áp dụng: Cho tam giác $ABC$ vuông tại $A$ có $\\widehat{B} = 2\\widehat{C}$ và cạnh huyền $BC = %s\\text{ cm}$. Kẻ đường phân giác $BD$ của góc $B$ ($D \\in AC$) (như hình vẽ). Tính độ dài các đoạn thẳng $AD, DC$ và $BD$.
    %s''' % (bc, hinhve))

        # Nội dung lời giải
        loigiai = ('''\\begin{enumEX}[a)]{1}
    \\item Gọi hai góc nhọn của tam giác vuông đó là $\\alpha$ và $2\\alpha$. Vì tổng hai góc nhọn trong tam giác vuông bằng $90^\\circ$ nên $\\alpha + 2\\alpha = 90^\\circ \\Rightarrow 3\\alpha = 90^\\circ \\Rightarrow \\alpha = 30^\\circ$ và $2\\alpha = 60^\\circ$.\\\\
    Do đó mọi tam giác vuông có một góc nhọn bằng hai lần góc nhọn còn lại đều có các góc là $90^\\circ, 60^\\circ, 30^\\circ$ nên chúng luôn đồng dạng với nhau (trường hợp góc - góc).\\\\
    Góc nhọn lớn hơn có số đo bằng $60^\\circ$, ta có $\\sin 60^\\circ = \\dfrac{\\sqrt{3}}{2}$ và $\\cos 60^\\circ = \\dfrac{1}{2}$.
    \\item Theo câu a, ta có $\\widehat{C} = 30^\\circ$ và $\\widehat{ABC} = 60^\\circ$.\\\\
    Xét tam giác $ABC$ vuông tại $A$, theo Định lí 1 ta có:\\\\
    $AB = BC \\cdot \\cos 60^\\circ = %s \\cdot \\dfrac{1}{2} = %s\\text{ (cm)}$ và $AC = BC \\cdot \\sin 60^\\circ = %s \\cdot \\dfrac{\\sqrt{3}}{2} = %s\\text{ (cm)}$.\\\\
    Vì $BD$ là đường phân giác của $\\widehat{ABC}$ nên $\\widehat{ABD} = \\dfrac{60^\\circ}{2} = 30^\\circ$.\\\\
    Xét tam giác $ABD$ vuông tại $A$, ta có:\\\\
    $AD = AB \\cdot \\tan 30^\\circ = %s \\cdot \\dfrac{\\sqrt{3}}{3} = %s\\text{ (cm)}$ và $BD = \\dfrac{AB}{\\cos 30^\\circ} = \\dfrac{%s}{\\dfrac{\\sqrt{3}}{2}} = %s\\text{ (cm)}$.\\\\
    Suy ra $DC = AC - AD = %s - %s = %s\\text{ (cm)}$.
    \\end{enumEX}'''
                   % (bc, latex(ab_new), bc, latex(ac_new),
                      latex(ab_new), latex(ad_new), latex(ab_new), latex(bd_new),
                      latex(ac_new), latex(ad_new), latex(dc_new)))

    # Xuất câu hỏi
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) +
               '\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
